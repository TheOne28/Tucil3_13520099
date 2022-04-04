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
    pq.push(table)

    while(not pq.empty()):
        if(copyTable.is_target()):
            step = ioHandler.printRoute(copyTable, 0)
            return step
        else:
            front = pq.pop()
            listKurangi, totalKurang, solveable = front.is_solveable()
            
            if(solveable):
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

    listKurangi, totalKurang, solveable = root.is_solveable()

    ioHandler.printKurangi(listKurangi)

    print("\u03A3Kurang(i) + X = ", (totalKurang))
    if(not solveable):
        stop = timeit.default_timer()

        print("Puzzle tidak dapat diselesaikan !!")
        print("Waktu yang dibutuhkan: ", stop - start, " sekon")
        return

    print()
    print("Cara penyelesaian: ")
    print()


    solve(root)
    print("Puzzle diselesaikan !!")

    stop = timeit.default_timer()
    print("Waktu yang dibutuhkan: ", stop - start, " second")
    print("Simpul yang dibangkitkan: ", boardCount)

if(__name__ == "__main__"):
    main()
