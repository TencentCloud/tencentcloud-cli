
from tccli.utils import Utils


class Document(object):

    def __init__(self):
        self.style = Style(self)
        self.content = []

    def _write(self, s):
        self.content.append(s)

    def write(self, content):
        self._write(content)

    def doc_title_indent(self, title):
        self.style.indent()
        self.write(self.style.spaces()+title)
        self.style.new_line()
        self.style.dedent()

    def doc_description_indent(self, description):
        self.style.indent()
        self.write(Utils.split_str(self.style.spaces(), description, 120-self.style.spaces_count))
        self.style.dedent()

    def doc_title(self, title):
        self.write(self.style.spaces() + title)
        self.style.new_line()
    
    def doc_description(self, description):
        self.write(Utils.split_str(self.style.spaces(), description, 120-self.style.spaces_count).rstrip())

    def getvalue(self):
        return ''.join(self.content)


class Style(object):

    def __init__(self, doc, indent_width=4):
        self.doc = doc
        self._indent_count = 0
        self.indent_width = indent_width

    def bold(self, text):
        self.doc.write('\033[1m' + text)

    def normal(self):
        self.doc.write('\033[0m')

    @property
    def indentation(self):
        return self._indent_count

    @indentation.setter
    def indentation(self, value):
        self._indent_count = value

    @property
    def spaces_count(self):
        return self._indent_count * self.indent_width

    def indent(self):
        self._indent_count += 1

    def dedent(self):
        if self._indent_count > 0:
            self._indent_count -= 1

    def spaces(self):
        return ' ' * (self._indent_count * self.indent_width)

    def new_line(self):
        self.doc.write('\n')

    def h1(self, text):
        self.doc.write("NAME")
        self.new_line()
        self.indent()
        self.doc.write(self.spaces()+text+'\n')
        self.dedent()

    def h2(self, text):
        self.new_line()
        self.doc.write(text.upper())
        self.new_line()

