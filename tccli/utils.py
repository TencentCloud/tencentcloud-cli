# -*- coding: utf-8 -*-
import six
import json
import time
import os
import tccli.options_define as options_define


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
        if six.PY2:
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
        if six.PY2:
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
        if six.PY2:
            dst = dst.encode("utf-8")
        return dst

    @staticmethod
    def is_valid_version(version):
        try:
            time.strptime(version, "%Y-%m-%d")
            return True
        except Exception as err:
            return False

    @staticmethod
    def file_existed(path, file_name):
        file_path = os.path.join(path, file_name)
        if os.path.exists(file_path):
            return True, file_path
        return False, file_path

    @staticmethod
    def load_json_msg(filename):
        with open(filename, "r") as f:
            data = json.load(f)
            return data

    @staticmethod
    def dump_json_msg(filename, data):
        file_dir = os.path.split(filename)[0]
        if not os.path.isdir(file_dir):
            os.makedirs(file_dir)
        with open(filename, "w") as f:
            json.dump(data, f,
                      indent=2,
                      separators=(',', ': '),
                      ensure_ascii=False,
                      sort_keys=True)

    @staticmethod
    def get_call_mode():
        cli_line = os.environ.get('COMP_LINE') or os.environ.get('COMMAND_LINE') or ''
        cli_param = cli_line.split()
        size = len(cli_param)

        if size > 3:
            if cli_param[3] == "--" + options_define.GenerateCliSkeleton:
                mode = options_define.GenerateCliSkeleton
                return mode
            if cli_param[3] == "--" + options_define.CliInputJson:
                mode = options_define.CliInputJson
                return mode
            if cli_param[3] == "--" + options_define.CliUnfoldArgument:
                mode = options_define.CliUnfoldArgument
                return mode
        return None

