import os.path
from random import randint

stepAll = None

'''
Setup table
Mengecek apakah akan membaca table dari input atau membuat random table
'''
def setup():
    print("Welcome to 15Puzzles")
    print("Silahkan pilih mode yang anda inginkan: ")
    print("1. Random table")
    print("2. Input table")

    choice = 0

    while(choice < 1 or choice > 2):
        choice = int(input("Mode mana yang anda inginkan? "))

        if(choice < 1 or choice > 3):
            print("Input tidak valid!")

    table = None

    if(choice == 1):
        done = []
        table = []

        for i in range(4):
            intable = []
            for j in range(4):
                while(True):
                    rand = randint(1, 16)
                    if(rand not in done):
                        intable.append(rand)
                        done.append(rand)
                        break
            table.append(intable)
    else:
        table = get_input()

    return table

'''
Membaca table dari input
Input dapat berupa file maupun terminal
'''
def get_input():
    print("Untuk cell kosong, silahkan masukkan 16")
    print("Silahkan pilih cara memasukkan input: ")
    print("1. File ")
    print("2. Terminal")

    choice = 0

    table = []

    while(choice < 1 or choice > 2):
        choice = int(input("Input mana yang anda inginkan? "))

        if(choice < 1 or choice > 3):
            print("Input tidak valid!")

    if(choice == 1):
        print("File input harus terletak di folder test !!")

        name = input("Silahkan masukkan nama file (lengkap dengan ekstensi): ")

        name = "../test/" + name
        myPath = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(myPath, name)

        if(os.path.exists(path)):
            with open(path, 'r') as f:
                line = f.readline()

                while line != "":
                    inTable = [int(a) for a in line.split(" ")]
                    table.append(inTable)
                    line = f.readline()
                
        else:
            print("File tidak ada!!")
            return None
    else:
        
        print("Silahkan masukkan table di terminal: \n")

        for i in range(4):
            intable = []
            for j in range(4):
                intable.append(int(input()))
            table.append(intable)

    if(check_table_valid(table)):
        return table
    else:
        return None
        
'''
Mengecek bahwa input table valid

Syarat valid:
    1. Tidak ada angka kembar
    2. Semua angka berada di range 1 - 16 (inclusive) -> 16 untuk cell kosong
'''
def check_table_valid(table):
    done = []

    for row in table:
        for cell in row:
            if((cell not in done ) and cell >= 1 and cell <= 16):
                done.append(cell)
            else:
                return False
    return True

def printKurangi(listKurangi):
    print ("   i            Kurang(i)")
    for numb in sorted(listKurangi):
        if(numb > 9):
            print("   {}              {}".format(numb, listKurangi[numb]))
        else:
            print("   {}               {}".format(numb, listKurangi[numb]))


def printRoute(solutionBoard, step):
    if(solutionBoard == None):
        global stepAll
        stepAll = step
        return
    printRoute(solutionBoard.get_parent(), step + 1)
    solutionBoard.printTable()
