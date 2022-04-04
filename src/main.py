from copy import deepcopy
import timeit
import ioHandler

from Board import Board
from PrioQueue import PriorityQueue

solutionBoard = None
pq = PriorityQueue()
boardCount = 0


def generateTable(table, moveBefore=None):
    tableUp = table.moveBlank(-1, 0)
    tableDown = table.moveBlank(1, 0)
    tableRight = table.moveBlank(0, 1)
    tableLeft = table.moveBlank(0, -1)

    global boardCount
    if(tableUp != None and moveBefore != "Down"):
        boardCount += 1
        pq.push(Board(tableUp, table.get_blankX() - 1, table.get_blankY(), table.get_depth() + 1, table, "Up"))
    if(tableDown != None and moveBefore != "Up"):
        boardCount += 1
        pq.push(Board(tableDown, table.get_blankX() + 1, table.get_blankY(), table.get_depth() + 1, table, "Down"))
    if(tableRight != None and moveBefore != "Left"):
        boardCount += 1
        pq.push(Board(tableRight, table.get_blankX(), table.get_blankY() + 1, table.get_depth() + 1, table, "Right"))
    if(tableLeft != None and moveBefore != "Right"):
        boardCount += 1
        pq.push(Board(tableLeft, table.get_blankX(), table.get_blankY() - 1, table.get_depth() + 1, table, "Left"))

def solve(table):
    copyTable = deepcopy(table)

    while(True):
        if(copyTable.is_target()):
            ioHandler.printRoute(copyTable)
            break
        else:
            if(pq.empty()):
                generateTable(copyTable)
                copyTable = pq.front()
            else:
                front = pq.pop()
                generateTable(front, front.get_move_before())
                copyTable = pq.front()            

def main():
    table = ioHandler.setup()

    if(table == None):
        print("Input tidak valid")
        return
        
    start = timeit.default_timer()

    indX, indY = -1, -1

    for i in range(4):
        for j in range(4):
            if(table[i][j] == 16):
                indX, indY = i, j
                break
        if(indX != -1):
            break
    
    root = Board(table, indX, indY, 0)

    varX = 0
    totalKurang = 0
    listKurangi = {}

    for i in range(4):
        for j in range(4):
            kurangi = root.find_Kurangi()
            listKurangi[table[i][j]] = kurangi
            totalKurang += kurangi


    ioHandler.printKurangi(listKurangi)

    if(indX % 2 == 0 and (indY == 1 or indY == 3)):
       varX = 1
    
    if(indX % 2 == 1 and (indY  == 0 or indY == 2)):
        varX = 1

    totalKurang += varX

    print("\u03A3Kurang(i) + X = ", (totalKurang))
    if(totalKurang % 2 == 1):
        stop = timeit.default_timer()
        
        
        print("Puzzle tidak dapat diselesaikan !!")
        print("Waktu yang dibutuhkan: ", stop - start)
        return

    print()
    print("Cara penyelesaian: ")
    print()


    solve(Board(table, indX, indY, 0))
    print("Puzzle diselesaikan !!")
    stop = timeit.default_timer()
    print("Waktu yang dibutuhkan: ", stop - start)
    print("Simpul yang dibangkitkan: ", boardCount)

if(__name__ == "__main__"):
    main()
