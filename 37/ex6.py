import os

try:
    os.mkdir('os_exercises')
except FileExistsError:
    print('Folder already exists.')

os.chdir('os_exercises')

def standartFile():
    f = open('exercise.py', 'w+')
    print('Print to standart file:')
    f.write(input())
    f.close()

def newFile():
    print('New file name:')
    f = open(input(), 'w+')
    print('Content of file:')
    f.write(input())
    f.close()

def readFiles():
    l = os.listdir()
    for f in l:
        file = open(f, 'r')
        print(f + ' contents:')
        print(file.read())
        file.close()

standartFile()
newFile()
readFiles()
