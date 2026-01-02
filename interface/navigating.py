import curses
from core.filesystem.getFilesList import getFiles, is_binary
from interface.listFiles import printFile, listFiles

def moveDown(screen, currentItemPos, maxRow, currentRow, path, firstItem=0):

    files = getFiles(path=path)

    if currentItemPos >= len(files) - 1:
        return currentItemPos, currentRow, firstItem

    previousFile = files[(currentItemPos)]
    file = files[currentItemPos+1]


    if currentRow != maxRow:
        printFile(screen=screen, file=previousFile, row=currentRow, highlight=0)      
        printFile(screen=screen, file=file, row=currentRow+1, highlight=1)

        return currentItemPos + 1, currentRow + 1, firstItem
    else:
        listFiles(screen=screen, path=path, startFrom=firstItem+1)
        printFile(screen=screen, file=file, row=currentRow, highlight=1)
        return currentItemPos + 1, currentRow, firstItem + 1

def moveUp(screen, currentItemPos, maxRow, currentRow, path, firstItem=0):

    files = getFiles(path=path)

    if currentItemPos <= 0:
        return currentItemPos, currentRow, firstItem

    previousFile = files[currentItemPos]
    file = files[currentItemPos - 1]

    if currentRow != 1:
        printFile(screen=screen, file=previousFile, row=currentRow, highlight=0)
        printFile(screen=screen, file=file, row=currentRow - 1, highlight=1)

        return currentItemPos - 1, currentRow - 1, firstItem
    else:
        listFiles(screen=screen, path=path, startFrom=firstItem - 1)
        printFile(screen=screen, file=file, row=currentRow, highlight=1)

        return currentItemPos - 1, currentRow, firstItem - 1
    

