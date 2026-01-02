# Imports

import curses
import os

from interface.add_path_bar import addPathBar
from interface.listFiles import listFiles, printFile

def main(stdscr):

    curses.curs_set(0)

    # Color init

    curses.start_color()
    curses.use_default_colors()

    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE) # Highlight
    curses.init_pair(2, curses.COLOR_BLUE, -1) # Directories 

     # Cleaning the screen

    stdscr.clear()

    # Get current path

    # path = os.getcwd()

    path = '/home/raskolnikov'

    # Adding path bar

    addPathBar(stdscr, path)

    # Printing files in the screen

    listFiles(stdscr, path)


    stdscr.refresh()
    
    stdscr.getch()




