# Imports

import curses
import os

from interface.add_path_bar import addPathBar

def main(stdscr):

    curses.curs_set(0)

    # Color init

    curses.start_color()
    curses.use_default_colors()

    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)

     # Cleaning the screen

    stdscr.clear()

    # Get current path

    path = os.getcwd()

    # Adding path bar

    addPathBar(stdscr, path)



    stdscr.refresh()
    
    stdscr.getch()




