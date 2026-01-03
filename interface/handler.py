# Imports

import curses
import os

from interface.add_path_bar import addPathBar
from interface.add_label import addLabel
from interface.listFiles import listFiles, printFile
from interface.navigating import moveDown, moveUp
from core.filesystem.changeDirectory import goBack, goForward
from core.filesystem.getFilesList import getFiles

def main(stdscr):

    curses.curs_set(0)

    # Color init

    curses.start_color()
    curses.use_default_colors()

    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE) # Highlight blue
    curses.init_pair(2, curses.COLOR_BLUE, -1) # Directories 
    curses.init_pair(3, curses.COLOR_GREEN, -1) # binaries files
    curses.init_pair(7, curses.COLOR_WHITE, curses.COLOR_RED) # Highlight red

    curses.init_pair(4, curses.COLOR_BLUE, curses.COLOR_YELLOW) # Highlighted directories
    curses.init_pair(5, curses.COLOR_GREEN, curses.COLOR_YELLOW) # Highlighted binaries
    curses.init_pair(6, curses.COLOR_WHITE, curses.COLOR_YELLOW) # Highlighted text files

     # Cleaning the screen

    stdscr.clear()

    # Getting current path

    path = os.getcwd()
    filesCurrentDir = getFiles(path=path)

    # Adding path bar

    addPathBar(stdscr, path)

    # Adding label

    addLabel(stdscr)

    # Printing files in the screen

    listFiles(stdscr, path, highlightFirstItem=1, files=filesCurrentDir)

    stdscr.refresh()

    stdscr.keypad(True)

    h, w = stdscr.getmaxyx()

    max_visible_rows = h - 2

    currentListPos = 0
    row = 1
    firstFile = 0
    stdscr.refresh()

    while True:
        
        pressedKey = stdscr.getch()

        if pressedKey == curses.KEY_DOWN:
            currentListPos, row, firstFile = moveDown(stdscr, currentListPos, max_visible_rows, row, path, firstFile, filesCurrentDir)
        elif pressedKey == curses.KEY_UP:
            currentListPos, row, firstFile = moveUp(stdscr, currentListPos, max_visible_rows, row, path, firstFile, filesCurrentDir)
        elif pressedKey == curses.KEY_LEFT:
            path = goBack(path)
            currentListPos = 0
            row = 1
            firstFile = 0
            filesCurrentDir = getFiles(path=path)
            listFiles(stdscr, path, highlightFirstItem=1, files=filesCurrentDir)
            addPathBar(stdscr, path)
        elif pressedKey == curses.KEY_RIGHT:
            response = goForward(path, currentListPos, filesCurrentDir)
            if (response != 0):
                path = response
                currentListPos = 0
                row = 1
                firstFile = 0
                filesCurrentDir = getFiles(path=path)
                listFiles(stdscr, path, highlightFirstItem=1, files=filesCurrentDir)
                addPathBar(stdscr, path)
        
        stdscr.refresh()
    
    stdscr.getch()




