# encoding: utf-8
import math
import sys
import os
from string import ascii_letters, digits, punctuation

_LEFT_ARROW = "LEFT_ARROW"
_RIGHT_ARROW = "RIGHT_ARROW"
_UP_ARROW = "UP_ARROW"
_DOWN_ARROW = "DOWN_ARROW"
_CTRL_C = "\x03"
_ENTER = "\r"
_BACKSPACE = "\x7f"
_EL = "\033[K"
_CPL = "\033[F"
_LIGHTBLUE = "\033[94m"
_LIGHTBLUE_END = "\033[0m"

_win = os.name == "nt"


class Printer(object):
    def __init__(self):
        self._n = 0

    def print_lines(self, lines):
        self.clear()
        lines = [line + '\n' for line in lines]
        sys.stdout.writelines(lines)
        sys.stdout.flush()
        self._n = len(lines)

    def clear(self):
        for _ in range(self._n):
            self.move_up()
            self.clear_cur_line()

    @staticmethod
    def clear_cur_line():
        sys.stdout.write(_EL)

    @staticmethod
    def move_up():
        sys.stdout.write(_CPL)


def _select_from_items_unix(prompt, items, page_size):
    p = Printer()

    selection = 0
    search = ""

    while True:
        filtered_items = [item for item in items if search in item] if search else items

        page_total = math.ceil(len(filtered_items) / float(page_size))
        page_num = selection // page_size + 1
        page_start = page_size * (page_num - 1)
        page_items = list(filtered_items[page_start: page_start + page_size])

        for i in range(len(page_items)):
            selection_i = selection % page_size
            selection_prompt = "*  " if i == selection_i else "   "
            page_items[i] = selection_prompt + _LIGHTBLUE + page_items[i] + _LIGHTBLUE_END

        page_lines = ["", "%s%s" % (prompt, search), ""] + page_items + ["", "page: %d/%d" % (page_num, page_total)]
        p.print_lines(page_lines)

        ch = _getch_wrap()

        if ch == _CTRL_C:
            raise KeyboardInterrupt()

        if ch == _UP_ARROW:
            selection = max(0, selection - 1)
        elif ch == _DOWN_ARROW:
            selection = min(len(filtered_items) - 1, selection + 1)
        elif ch == _LEFT_ARROW:
            if selection - page_size >= 0:
                selection -= page_size
        elif ch == _RIGHT_ARROW:
            selection = min(len(filtered_items) - 1, selection + page_size)
        elif ch == _BACKSPACE:
            search = search[:len(search) - 1] if search else ""
            selection = 0
        elif ch == _ENTER:
            idx = 0
            matched = -1

            for item in items:
                if search in item:
                    matched += 1
                if matched == selection:
                    p.print_lines([])
                    return idx
                idx += 1

        elif ch in (ascii_letters + digits + punctuation):
            search += ch
            selection = 0


def _select_from_items_win(prompt, items, page_size):
    print("")
    print("--------------------------------")
    for i in range(len(items)):
        print("%d. %s" % (i, items[i]))

    print("--------------------------------")
    sys.stdout.flush()

    try:
        input_func = raw_input
    except NameError:
        input_func = input

    while True:
        try:
            sys.stdout.write(prompt)
            idx = int(input_func())
            if 0 <= idx < len(items):
                return idx
        except ValueError:
            pass


select_from_items = _select_from_items_win if _win else _select_from_items_unix

if not _win:
    def getch():
        import sys
        import tty
        import termios
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            return sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)


    def _getch_wrap():
        ch = getch()
        if ch == "\x1b":
            ch1 = getch()
            if ch1 != "[":
                raise KeyError(ch1)
            ch2 = getch()
            if ch2 == "A":
                return _UP_ARROW
            if ch2 == "B":
                return _DOWN_ARROW
            if ch2 == "C":
                return _RIGHT_ARROW
            if ch2 == "D":
                return _LEFT_ARROW

            raise KeyError(ch + ch1 + ch2)
        else:
            return ch
