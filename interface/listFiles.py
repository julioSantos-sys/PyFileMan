# Imports

import curses
from core.filesystem.getFilesList import getFiles

def printFile(screen, file, row, highlight=0):

    # Setting up color pairs

    dirAttr = curses.color_pair(2)
    binAttr = curses.color_pair(3)

    if highlight == 1:
        dirAttr = curses.color_pair(4)
        binAttr = curses.color_pair(5)
        textAttr = curses.color_pair(6)

    if file['type'] == 0:

        h, w = screen.getmaxyx()

        screen.attron(dirAttr)
        screen.addstr(row,0, " " * w)
        screen.addstr(row, 0, f"📁{file['name']}")
        screen.attroff(dirAttr)

    elif file['type'] == 1:

        h, w = screen.getmaxyx()

        screen.attron(binAttr)
        screen.addstr(row,0, " " * w)
        screen.addstr(row, 0, f"⚙ {file['name']}")
        screen.attroff(binAttr)

    elif file['type'] == 2:
            
        h, w = screen.getmaxyx() 
        if highlight == 1:
            screen.attron(curses.color_pair(6))

        screen.addstr(row,0, " " * w)
            
        screen.addstr(row, 0, f"📄{file['name']}")

        if highlight == 1:
            screen.attroff(curses.color_pair(6))


def listFiles(screen, path, startFrom=0, highlightFirstItem=0):
    

    h, w = screen.getmaxyx()

    currentRow = 1

    # Getting files list

    files = getFiles(path)

    if startFrom !=0:
        files = files[startFrom:]

    # Printing files on screen

    for file in files:
        if currentRow < h-1:
            printFile(screen, file, currentRow)
            currentRow = currentRow + 1
    if currentRow < h-1:
        for i in range(currentRow, h-1):
            screen.addstr(currentRow,0, " " * w)
            currentRow = currentRow + 1



    if highlightFirstItem == 1:
        printFile(screen, file=files[0], row=1, highlight=1)
            
    

        
    

    


