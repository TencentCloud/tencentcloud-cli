#! /usr/bin/env python

from setuptools import setup, find_packages
from tccli import __version__


def main():
    dep_sdk = "tencentcloud-sdk-python >= %s" % __version__.rsplit(".", 1)[0]
    setup(
        name='tccli',
        install_requires=[dep_sdk, "jmespath==0.10.0", "six==1.16.0"],
        version=__version__,
        packages=find_packages(),
        include_package_data=True,
        entry_points={
            'console_scripts': [
                'tccli = tccli.main:main',
                'tccli_completer  = tccli.completer:complete',
            ]
        },
    )


if __name__ == '__main__':
    main()
