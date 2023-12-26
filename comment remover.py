import re

def getFileName():
    return str(input("Input the name of the file: "))

def main():
    fileName = getFileName()
    fileArray = getFileData(fileName)
    newFileName = createNewFile(fileName)
    editFile(newFileName, fileArray)
    

def getFileData(fileName):
    f = open(fileName, "r")
    a = f.readlines()
    f.close()
    for i in range(0,len(a)):
        a[i] = re.sub("\{\[\%clk \d:\d\d:\d\d\]\}", '', a[i])
    return a

def createNewFile(fileName):
    newFileName = fileName.replace('.pgn', 'EDITED.pgn')
    g = open(newFileName, 'w')
    g.close()
    return newFileName

def editFile(fileName, array):
    h = open(fileName, 'a')
    for j in range(0,len(array)):
        h.write(array[j])
    h.close()

main()
