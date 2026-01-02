import curses

def addLabel(screen):
    h, w = screen.getmaxyx()
    attr = curses.color_pair(7)

    label = " 📁: Directories  ⚙: Binaries  📄: Text Files | Use the arrrows to navigate"
    label = label[:w - 1]

    screen.attron(attr)

    # Preenche a linha inteira
    screen.addstr(h - 1, 0, " " * (w - 1))

    # Escreve o texto por cima
    screen.addstr(h - 1, 0, label)

    screen.attroff(attr)