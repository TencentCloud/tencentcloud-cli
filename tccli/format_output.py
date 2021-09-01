# -*- coding:utf-8 -*-
import sys
import json
from tccli import text
from tccli.table import MultiTable
import jmespath
import io


PY2 = sys.version_info[0] == 2


class Response(object):

    def __call__(self, command, response, stream=None):
        if stream is None:
            if not PY2:
                sys.stdout = io.TextIOWrapper(sys.stdout.buffer,
                                              encoding='utf-8')
            stream = sys.stdout
        try:
            self._format_response(command, response, stream)
        except IOError as e:
            pass
        finally:
            self._flush_stream(stream)

    def _flush_stream(self, stream):
        try:
            stream.flush()
        except IOError:
            pass


class JSONResult(Response):
    def _format_response(self, command, response, stream=None):
        if stream is None:
            if not PY2:
                sys.stdout = io.TextIOWrapper(sys.stdout.buffer,
                                              encoding='utf-8')
            stream = sys.stdout
        if response is not None:
            ret = json.dumps(response, ensure_ascii=False, indent=4)
            if PY2:
                import platform
                if 'Windows' in platform.system():
                    print(ret.encode('GBK'))
                else:
                    print(ret.encode('utf8'))
            else:
                print(ret)
            #stream.write('\n')


class TextResult (Response):
    def __call__(self, command, response, stream=None):
        if stream is None:
            if not PY2:
                sys.stdout = io.TextIOWrapper(sys.stdout.buffer,
                                              encoding='utf-8')
            stream = sys.stdout
        try:
            self._format_response(response, stream)
        finally:
            self._flush_stream(stream)

    def _format_response(self, response, stream):
        text.format_text(response, stream)


class TableResult (Response):
    def __init__(self, table=None):
        self.table = MultiTable(initial_section=False,
                                column_separator='|')

    def _format_response(self, command, response, stream):
        if self._build_table(command, response):
            try:
                self.table.render(stream)
            except IOError:
                pass

    def _build_table(self, title, current, indent_level=0):
        if current is None:
            return False
        if title is not None:
            self.table.new_section(title, indent_level=indent_level)
        if isinstance(current, list) and len(current) > 0:
            if isinstance(current[0], dict):
                self._build_sub_table_from_list(current, indent_level, title)
            else:
                for item in current:
                    if self._scalar_type(item):
                        self.table.add_row([item])
                    elif all(self._scalar_type(el) for el in item):
                        self.table.add_row(item)
                    else:
                        self._build_table(title=None, current=item)
        elif isinstance(current, dict):
            self._build_sub_table_from_dict(current, indent_level)
        else:
            self.table.add_row([current])
        return True

    def _build_sub_table_from_dict(self, current, indent_level):
        headers, more = self._group_scalar_keys(current)
        if len(headers) == 1:
            self.table.add_row([headers[0], current[headers[0]]])
        elif headers:
            self.table.add_row_header(headers)
            self.table.add_row([current[k] for k in headers])
        for remaining in more:
            self._build_table(remaining, current[remaining],
                              indent_level=indent_level + 1)

    def _build_sub_table_from_list(self, current, indent_level, title):
        headers, more = self._group_scalar_keys_from_list(current)
        self.table.add_row_header(headers)
        first = True
        for element in current:
            if not first and more:
                self.table.new_section(title,
                                       indent_level=indent_level)
                self.table.add_row_header(headers)
            first = False

            self.table.add_row([element.get(header, '')
                                for header in headers])
            for remaining in more:

                if remaining in element:
                    self._build_table(remaining, element[remaining],
                                      indent_level=indent_level + 1)

    def _scalar_type(self, element):
        return not isinstance(element, (list, dict))

    def _group_scalar_keys_from_list(self, list_of_dicts):
        headers = set()
        more = set()
        for item in list_of_dicts:
            current_headers, current_more = self._group_scalar_keys(item)
            headers.update(current_headers)
            more.update(current_more)
        headers = list(sorted(headers))
        more = list(sorted(more))
        return headers, more

    def _group_scalar_keys(self, current):
        more = []
        headers = []
        for element in current:
            if self._scalar_type(current[element]):
                headers.append(element)
            else:
                more.append(element)
        headers.sort()
        more.sort()
        return headers, more


def _get_result(format):
    if format == 'json':
        return JSONResult()
    elif format == 'text':
        return TextResult()
    elif format == 'table':
        return TableResult()
    raise ValueError('Unknown output type: %s\nCurrently supported output '
                     'formats: "json", "text" and "table".' % format)


def output(cmd, response, format, filter=None):
    if not format:
        format = "json"
    if format not in ["json", "text", "table"]:
        raise Exception('Unknown output format: %s\nCurrently supported output '
                     'formats: "json", "text" and "table".' % format)

    if filter:
        expression = jmespath.compile(filter)
        response = expression.search(response)
    formatter = _get_result(format)
    formatter(cmd, response)

