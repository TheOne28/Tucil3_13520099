from copy import deepcopy

target = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

class Board:
    '''
        table -> papan permainan
        indX -> index X yang kosong 
        indY -> index Y yang kosong
        depth -> kedalaman sekarang
        parent -> board yang menggenerate board sekarang
        moveBefore -> pergeseran yang dilakukan untuk mencapai target ini
    '''
    
    def __init__(self, table, indX, indY, depth, parent=None ,moveBefore=None) :
        self.table = table
        self.indX = indX
        self.indY = indY
        self.depth = depth
        self.parent = parent
        self.cost = depth + self.find_cost(table)
        self.moveBefore = moveBefore
    
    def find_cost(self, table):
        count = 0
        for i in range(4):
            for j in range(4):
                if(table[i][j] != 16 and target[i][j] != 16):
                    if(table[i][j] != target[i][j]):
                        count += 1
        return count

    
    def find_Kurangi(self, indX, indY):
        count = 0
        compare = self.table[indX][indY]

        for i in range(indY, 4):
            if(self.table[indX][i] < compare ):
                count += 1
    
        for i in range(indX + 1, 4):
            for j in range(4):
                if(self.table[i][j] < compare):
                    count += 1

        return count

    def is_solveable(self):
        varX = 0
        totalKurang = 0
        listKurangi = {}

        for i in range(4):
            for j in range(4):
                kurangi = self.find_Kurangi(i, j)
                listKurangi[self.table[i][j]] = kurangi
                totalKurang += kurangi

        if(self.indX % 2 == 0 and (self.indY == 1 or self.indY == 3)):
            varX = 1
    
        if(self.indX % 2 == 1 and (self.indY  == 0 or self.indY == 2)):
            varX = 1

        totalKurang += varX

        if(totalKurang % 2 == 1):
            return listKurangi, totalKurang, False
        else:
            return listKurangi, totalKurang, True

    def get_table(self):
        return self.table

    def get_cost(self):
        return self.cost

    def get_blankX(self):
        return self.indX
    
    def get_blankY(self):
        return self.indY

    def get_depth(self):
        return self.depth

    def get_move_before(self):
        return self.moveBefore

    def get_parent(self):
        return self.parent
    
    def is_target(self):
        for i in range(4):
            for j in range(4):
                if(self.table[i][j] != target[i][j]):
                    return False
        return True
    
    def moveBlank(self, deltaX, deltaY):
        newX = self.indX + deltaX
        newY = self.indY + deltaY
        
        if(newX >=0 and newX <= 3 and newY >= 0 and newY <= 3):
            newTable = deepcopy(self.table)

            newTable[newX][newY], newTable[self.indX][self.indY] = newTable[self.indX][self.indY], newTable[newX][newY]
            return newTable
        else:
            return None
    
    def printTable(self):
        if(self.moveBefore == None):
            print("Root")
        else:
            print("Move: ", self.moveBefore)

        for row in self.table:
            for cell in row:
                if(cell == 16):
                    print("-", end="\t")
                else:
                    print(cell, end = "\t")
            print()
    
    def __lt__(self, other):
        return self.cost < other.get_cost()