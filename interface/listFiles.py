# Imports

import curses
from core.filesystem.getFilesList import getFiles

def printFile(screen, file, row):

    # Setting up color pairs

    dirAttr = curses.color_pair(2)
    binAttr = curses.color_pair(3)

    if file['type'] == 0:

        screen.attron(dirAttr)
        screen.addstr(row, 0, f"📁{file['name']}")
        screen.attroff(dirAttr)

    elif file['type'] == 1:

        screen.attron(binAttr)
        screen.addstr(row, 0, f"⚙ {file['name']}")
        screen.attroff(binAttr)

    elif file['type'] == 2:

        screen.addstr(row, 0, f"📄{file['name']}")


def listFiles(screen, path):
    h, w = h, w = screen.getmaxyx()

    currentRow = 1

    # Getting files list

    files = getFiles(path)

    # Printing files on screen

    for file in files:
        if currentRow < h-1:
            printFile(screen, file, currentRow)
            currentRow = currentRow + 1

    


