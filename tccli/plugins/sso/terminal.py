import sys

_LEFT_ARROW = "LEFT_ARROW"
_RIGHT_ARROW = "RIGHT_ARROW"
_UP_ARROW = "UP_ARROW"
_DOWN_ARROW = "DOWN_ARROW"
_CTRL_C = "\x03"
_BACKSPACE = "\x7f"
_ENTER = "\r"


class Printer(object):
    def __init__(self):
        self._n = 0

    def print_lines(self, lines):
        self.clear()
        lines = [line + '\n' for line in lines]
        sys.stdout.writelines(lines)
        self._n = len(lines)

    def clear(self):
        for _ in range(self._n):
            self.move_up()
            self.clear_cur_line()

    @staticmethod
    def clear_cur_line():
        sys.stdout.write("\033[K")

    @staticmethod
    def move_up():
        sys.stdout.write("\033[F")


def select_from_items(prompt, items, page_size):
    p = Printer()

    selection = 0
    search = ""

    while True:
        filtered_items = [item for item in items if search in item] if search else items

        page_total = len(filtered_items) / page_size
        page_num = selection / page_size
        page_start = page_size * page_num
        page_items = list(filtered_items[page_start: page_start + page_size])

        for i in range(len(page_items)):
            selection_i = selection % page_size
            selection_prompt = "*  " if i == selection_i else "   "
            page_items[i] = selection_prompt + page_items[i]

        page_lines = ["%s%s" % (prompt, search), ""] + page_items + ["", "page: %d/%d" % (page_num, page_total)]
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
            if selection + page_size < len(filtered_items):
                selection += page_size
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

        else:
            search += ch
            selection = 0


try:
    from msvcrt import getch
except ImportError:
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
