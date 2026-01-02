import curses

def addPathBar(screen, path):
     
    h, w = screen.getmaxyx()


    attr = curses.color_pair(1)

    screen.move(0, 0)

    screen.attron(attr)

    screen.addstr(0,0, " " * w)

    screen.addstr(0, 0, path)

    screen.attroff(attr)


