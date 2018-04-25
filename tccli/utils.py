# -*- coding: utf-8 -*-
import sys
import json


PY2 = sys.version_info[0] == 2


class Utils(object):

    @staticmethod
    def try_to_json(data, k):

        if k in data and data[k]:
            try:
                return json.loads(data[k])
            except Exception:
                return data[k]
        return None

    @staticmethod
    def split_str_bk(pre, src, step):
        if PY2:
            src = src.decode("utf-8")
        dst = ""
        strlist = src.split("\n")
        for s in strlist:
            start = 0
            size = len(s)
            while start < size:
                dst += (pre + s[start:start+step] + "\n")
                start += step
            dst += "\n"
        dst += "\n"
        return dst

    @staticmethod
    def split_str(pre, src, line_size):
        if PY2:
            src = src.decode("utf-8")
        dst = ""
        strlist = src.split("\n")
        for s in strlist:
            lsize = 0
            line = pre
            for c in s:
                line += c
                if ord(c) < 256:
                    lsize += 1
                else:
                    lsize += 2
                if lsize >= line_size:
                    dst += (line + "\n")
                    line = pre
                    lsize = 0
            dst += (line + "\n")
        dst += "\n"
        if PY2:
            dst = dst.encode("utf-8")
        return dst