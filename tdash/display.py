# -*- coding: utf-8 -*-

import unicodedata
import curses
import six
import re


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


def get_fg_color(attrs):
    for attr in attrs:
        if attr in FG_COLORS:
            return FG_COLORS[attr]
    return FG_COLORS["default"]


def get_bg_color(attrs):
    for attr in attrs:
        if attr in BG_COLORS:
            return BG_COLORS[attr]
    return BG_COLORS["on_default"]


def get_attributes(attrs):
    for attr in attrs:
        if attr in ATTRS:
            yield ATTRS[attr]


# ============================================================ #
# Unicode
# ============================================================ #


def screen_len(s, beg=None, end=None):
    if beg is None:
        beg = 0
    if end is None:
        end = len(s)

    if "\t" in s:
        # consider tabstop (very naive approach)
        beg = len(s[0:beg].expandtabs())
        end = len(s[beg:end].expandtabs())
        s = s.expandtabs()

    if not isinstance(s, six.text_type):
        return end - beg

    dis_len = end - beg
    for i in six.moves.range(beg, end):
        if unicodedata.east_asian_width(s[i]) in ("W", "F"):
            dis_len += 1
    return dis_len


def screen_length_to_bytes_count(string, screen_length_limit, encoding):
    bytes_count = 0
    screen_length = 0
    for unicode_char in string:
        screen_length += screen_len(unicode_char)
        char_bytes_count = len(unicode_char.encode(encoding))
        bytes_count += char_bytes_count
        if screen_length > screen_length_limit:
            bytes_count -= char_bytes_count
            break
    return bytes_count


class Display(object):

    def __init__(self, screen, encoding):
        self.screen = screen
        self.encoding = encoding

        curses.start_color()

        self.has_default_colors = curses.COLORS > COLOR_COUNT
        self.update_screen_size()

    def update_screen_size(self):
        self.HEIGHT, self.WIDTH = self.screen.getmaxyx()

    @property
    def Y_BEGIN(self):
        return 0

    @property
    def Y_END(self):
        return self.HEIGHT - 1

    @property
    def X_BEGIN(self):
        return 0

    @property
    def X_END(self):
        return self.WIDTH - 1

    def get_pos_x(self, x_align, x_offset, whole_len):
        position = 0

        if x_align == "left":
            position = x_offset
        elif x_align == "right":
            position = self.WIDTH - whole_len - x_offset
        elif x_align == "center":
            position = x_offset + (int(self.WIDTH - whole_len) / 2)

        return position

    def get_pos_y(self, y_align, y_offset):
        position = 0

        if y_align == "top":
            position = y_offset
        elif y_align == "bottom":
            position = self.HEIGHT - y_offset
        elif y_align == "center":
            position = y_offset + int(self.HEIGHT / 2)

        return position

    def add_aligned_string(self, s, y_align="top", x_align="left",
                           y_offeset=0, x_offset=0, style=None,
                           fill=False, fill_char=" ", fill_style=None):
        pass

    # ============================================================ #
    # Fundamental
    # ============================================================ #
    def erase(self):
        self.screen.erase()

    def clear(self):
        self.screen.clear()

    def refresh(self):
        self.screen.refresh()

    def attrs_to_style(self, attrs):
        if attrs is None:
            return 0
        style = self.get_color_pair(get_fg_color(attrs), get_bg_color(attrs))
        for attr in get_attributes(attrs):
            style |= attr

        return style

    def get_raw_string(self, s):
        return s.encode(self.encoding) if isinstance(s, six.text_type) else s

    def addnstr(self, y, x, s, n, style):
        if not isinstance(style, six.integer_types):
            style = self.attrs_to_style(style)

        try:
            pass
        except curses.error:
            pass

    def addstr(self, y, x, s, style):
        if not isinstance(style, six.integer_types):
            style = self.attrs_to_style(style)

        try:
            sanitized_str = re.sub(r'[\x00-\x08\x0a-\x1f]', '?', s)
            raw_str = self.get_raw_string(sanitized_str)
            self.screen.addstr(y, x, raw_str, style)
            return True
        except curses.error:
            return False

    def add_string(self, s, pos_y=0, pos_x=0, style=None):
        self.addstr(pos_y, pos_x, s, style)

    def add_title(self, title):
        self.add_string(title)

    def add_center_text(self, text):
        pass




class Popup(object):

    def __init__(self, screen, encoding):
        pass

if __name__ == "__main__":
    import locale

    locale.setlocale(locale.LC_ALL, '')

    screen = curses.initscr()

    display = Display(screen, locale.getpreferredencoding())

    display.add_title('Terminal Dash')

    # display.addCenterText('Hello, there will be description text!')
    # display.addPopup()
    screen.getch()
