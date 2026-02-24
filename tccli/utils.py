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
        """改进的帮助字符串分割方法，增强Python 3.14兼容性"""
        if src is None:
            return ""
        
        # 处理Python 3.14的字符串编码要求
        if six.PY2:
            src = src.decode("utf-8")
        else:
            # Python 3.x: 确保字符串是unicode
            if isinstance(src, bytes):
                src = src.decode("utf-8")
        
        dst = ""
        strlist = src.split("\n")
        
        for s in strlist:
            if not s.strip():  # 跳过空行
                dst += pre + "\n"
                continue
                
            lsize = 0
            line = pre
            words = s.split()
            current_line_words = []
            
            for word in words:
                # 计算单词长度（考虑中英文字符）
                word_length = sum(2 if ord(c) > 127 else 1 for c in word)
                
                # 如果当前行加上新单词会超出限制
                if lsize + word_length + (len(current_line_words) > 0) >= line_size:
                    # 输出当前行
                    dst += line + " ".join(current_line_words) + "\n"
                    # 开始新行
                    line = pre
                    current_line_words = [word]
                    lsize = len(pre) + word_length
                else:
                    current_line_words.append(word)
                    lsize += word_length + 1  # +1 for space
            
            # 输出最后一行
            if current_line_words:
                dst += line + " ".join(current_line_words) + "\n"
        
        return dst

    @staticmethod
    def safe_help_string_generation(help_text):
        """安全的帮助字符串生成方法（兼容Python 3.14）"""
        if help_text is None:
            return ""
        
        # 处理Python 3.14中的字符串编码问题
        if not six.PY2:
            # 确保字符串是unicode
            if isinstance(help_text, bytes):
                help_text = help_text.decode("utf-8", errors="replace")
            
            # 清理可能的问题字符
            help_text = help_text.replace('\x00', '')  # 移除空字符
            help_text = help_text.strip()  # 移除首尾空白
            
            # 限制字符串长度，避免argparse处理过长的帮助字符串
            if len(help_text) > 1000:
                help_text = help_text[:1000] + "..."
        
        return help_text

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

    @staticmethod
    def is_bool(s):
        if s.lower() == 'true':
            return True, True
        elif s.lower() == 'false':
            return True, False
        else:
            return False, None