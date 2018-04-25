#! /usr/bin/env python

"""
distutils/setuptools install script.
"""
import sys
import os
from setuptools import setup, find_packages
from tccli import __version__
ROOT = os.path.dirname(__file__)
PACKAGE = 'tccli'
VERSION = __import__(PACKAGE).__version__
SDK_VERSION = None
try:
     from tencentcloud import __version__ as sdk_version
     SDK_VERSION = sdk_version
except ImportError as err:
        SDK_VERSION = None

PY2 = sys.version_info[0] == 2


def main():
    vinput = None
    if not PY2:
        vinput = input
    else:
        vinput = raw_input
    cli_version = __version__.rsplit(".", 1)[0]
    dep_sdk = "tencentcloud-sdk-python >= %s" % cli_version
    if SDK_VERSION is not None:
        if SDK_VERSION < cli_version:
            answer = None
            prompt = ("The current python sdk version (%s) is "
                      "too low and we will update to %s(yes/no):") % (SDK_VERSION, cli_version)
            answer = vinput(prompt)
            if answer not in ["yes", "YES", "Yes"]:
                print("tccli install failed")
                return
    setup(
        name='tccli',
        install_requires=[dep_sdk],
        version=VERSION,
        description='Universal Command Line Environment for Tencent Cloud',
        long_description=open('README.rst').read(),
        author='Tencent Cloud',
        url='https://github.com/TencentCloud/tencentcloud-cli.git',
        maintainer_email="TencentCloudApi@tencent.com",
        packages=find_packages(),
        include_package_data=True,
        platforms=['unix', 'linux', 'win64'],
        scripts=[],
        py_modules=['tccli'],
        entry_points={
            'console_scripts': [
                'tccli = tccli.main:main',
                'tccli_completer  = tccli.completer:complete',
            ]
        },
        classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: Apache Software License',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.1',
            'Programming Language :: Python :: 3.2',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
        ],
    )


if __name__ == '__main__':
    main()
