# -*- coding: utf-8 -*-
"""
Python版本兼容性模块
处理Python 3.14及更高版本的兼容性问题
"""

import sys
import six
import warnings


class PythonVersionChecker:
    """Python版本兼容性检查器"""
    
    @staticmethod
    def get_python_version():
        """获取Python版本信息"""
        return sys.version_info
    
    @staticmethod
    def is_python_314_or_later():
        """检查是否为Python 3.14或更高版本"""
        if six.PY2:
            return False
        return sys.version_info >= (3, 14)
    
    @staticmethod
    def is_python_3():
        """检查是否为Python 3.x版本"""
        return not six.PY2
    
    @staticmethod
    def check_compatibility():
        """检查并报告兼容性问题"""
        version = PythonVersionChecker.get_python_version()
        
        if version >= (3, 14):
            print("Info: Running on Python 3.14 or later")
            print("Applying compatibility adjustments for argparse and string handling")
            return False
        return True
    
    @staticmethod
    def apply_compatibility_fixes():
        """应用Python 3.14兼容性修复"""
        if PythonVersionChecker.is_python_314_or_later():
            # Python 3.14特定修复
            # 忽略argparse相关的弃用警告
            warnings.filterwarnings("ignore", category=DeprecationWarning, module="argparse")
            warnings.filterwarnings("ignore", category=FutureWarning, module="argparse")
            
            # 设置更安全的编码处理
            if hasattr(sys.stdout, 'encoding') and sys.stdout.encoding is None:
                import io
                sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
            
            if hasattr(sys.stderr, 'encoding') and sys.stderr.encoding is None:
                import io
                sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')
    
    @staticmethod
    def safe_string_format(text, *args, **kwargs):
        """安全的字符串格式化方法，处理Python 3.14兼容性问题"""
        if text is None:
            return ""
        
        try:
            # 确保文本是字符串
            if isinstance(text, bytes):
                text = text.decode('utf-8', errors='replace')
            
            # 安全的格式化
            if args or kwargs:
                return text.format(*args, **kwargs)
            else:
                return text
        except Exception as e:
            # 如果格式化失败，返回原始文本
            return str(text)
    
    @staticmethod
    def safe_help_string_generation(help_text):
        """安全的帮助字符串生成方法"""
        if help_text is None:
            return ""
        
        # 处理Python 3.14中的字符串编码问题
        if PythonVersionChecker.is_python_314_or_later():
            # 确保字符串是unicode
            if isinstance(help_text, bytes):
                help_text = help_text.decode('utf-8', errors='replace')
            
            # 清理可能的问题字符
            help_text = help_text.replace('\x00', '')  # 移除空字符
            help_text = help_text.strip()  # 移除首尾空白
            
            # 限制字符串长度，避免argparse处理过长的帮助字符串
            if len(help_text) > 1000:
                help_text = help_text[:1000] + "..."
        
        return help_text


def apply_python_314_compatibility():
    """应用Python 3.14兼容性修复（全局函数）"""
    PythonVersionChecker.apply_compatibility_fixes()


def check_python_version():
    """检查Python版本并返回兼容性状态"""
    return PythonVersionChecker.check_compatibility()