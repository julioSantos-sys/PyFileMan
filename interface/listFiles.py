# Imports

import curses
from core.filesystem.getFilesList import getFiles

def printFile(screen, file, row):
    dirAttr = curses.color_pair(2)

    if file['is_dir'] == True:
        screen.attron(dirAttr)
        screen.addstr(row, 0, f"📁 {file['name']}")
        screen.attroff(dirAttr)
    else:
        screen.addstr(row, 0, f"📄 {file['name']}")

def listFiles(screen, path):
    h, w = h, w = screen.getmaxyx()

    currentRow = 1

    files = getFiles(path)

    for file in files:
        if currentRow < h-1:
            printFile(screen, file, currentRow)
            currentRow = currentRow + 1

    


