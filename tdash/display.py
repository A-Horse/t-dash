# -*- coding: utf-8 -*-

import unicodedata
import curses
import six
import rex

FG_COLORS = {
    "black": curses.COLOR_BLACK,
    "red": curses.COLOR_RED,
    "green": curses.COLOR_GREEN,
    "yellow": curses.COLOR_YELLOW,
    "blue": curses.COLOR_BLUE,
    "magenta": curses.COLOR_MAGENTA,
    "cyan": curses.COLOR_CYAN,
    "white": curses.COLOR_WHITE,
}

BG_COLORS = dict(("on_" + name, value)
                 for name, value in six.iteritems(FG_COLORS))

ATTRS = {
    "altcharset": curses.A_ALTCHARSET,
    "blink": curses.A_BLINK,
    "bold": curses.A_BOLD,
    "dim": curses.A_DIM,
    "normal": curses.A_NORMAL,
    "standout": curses.A_STANDOUT,
    "underline": curses.A_UNDERLINE,
    "reverse": curses.A_REVERSE,
}

COLOR_COUNT = len(FG_COLORS)


class Display(object):

    def __init__(self, screen, encoding):
        self.screen = screen
        self.encoding = encoding

    def addTitle(self, title):
        pass

    def addCenterText(self, text):
        pass




class Popup(object):

    def __init__(self, screen, encoding):
        pass

if __name__ == "__main__":
    import locale

    locale.setlocale(locale.LC_ALL, '')

    screen = curser.initscr()

    display = Display(screen, locale.getpreferredencoding())

    display.addTitle('Terminal Dash')

    display.addCenterText('Hello, there will be description text!')

    display.addPopup()
