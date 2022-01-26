# -*- coding:utf8 -*-
from utils import TestCli


def test_help():
    cmd = 'tccli help'
    expect = 'tccli [options] <service> [options] <action> [options] [options and parameters]'
    test_cli = TestCli()
    test_cli.equal(cmd, expect)


def test_help_detail():
    cmd = 'tccli help --detail'
    expect = 'cvm\n    介绍如何使用API对云服务器进行操作，包括使用并管理实例、镜像、密钥等资源。'
    test_cli = TestCli()
    test_cli.equal(cmd, expect)


def test_cvm_help():
    cmd = 'tccli cvm help'
    expect = '<DescribeRegions>'
    test_cli = TestCli()
    test_cli.equal(cmd, expect)


def test_cvm_help_detail():
    cmd = 'tccli cvm help --detail'
    expect = 'AVAILABLE ACTIONS\n    AllocateHosts'
    test_cli = TestCli()
    test_cli.equal(cmd, expect)
