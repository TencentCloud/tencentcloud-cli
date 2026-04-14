# encoding: utf-8
"""
如何自定义插件
1. 定义一个 spec 对象，参考以下代码
2. export 一个函数，名字叫做 register_service，它负责向 cli 注册 spec

注册完成后，用户可以通过 tccli {服务名} {接口名} --{参数1}={参数值} ... 的方式调用

如下所示:
    定义了一个服务名叫 test, 包含一个接口 add, add 接口接受 2 个参数 number1, number2
    则用户可以以如下方式调用 tccli
    tccli test add --number1=3 --number2=5
"""
from tccli.plugins.test.add import add_command

service_name = "test"
service_version = "2024-08-07"

_spec = {
    "metadata": {
        # 产品名
        "serviceShortName": service_name,
        # 产品版本号
        "apiVersion": service_version,
        # 产品介绍
        "description": "this is a test module",
    },
    # 产品所有支持的接口
    "actions": {
        # 接口名推荐用小写，避免和云 API 的接口名冲突
        "add": {
            # 接口中文名
            "name": "测试接口",
            # 接口说明
            "document": "this is an test action",
            # 入参对象名，在 objects 中详细定义入参结构
            "input": "addRequest",
            # 出参对象名，在 objects 中详细定义出参结构
            "output": "addResponse",
            # 实际调用函数
            "action_caller": add_command,  # the function to call
        },
    },
    "objects": {
        "addRequest": {
            "members": [
                {
                    # 参数名
                    "name": "number1",
                    # int64, uint64, string, float, bool, date, datetime, datetime_iso, binary
                    "member": "int64",
                    # same as member
                    "type": "int64",
                    # 是否必传
                    "required": True,
                    # 参数说明
                    "document": "doc about number1",
                },
                {
                    "name": "number2",
                    "member": "int64",
                    "type": "int64",
                    "required": True,
                    "document": "doc about number2",
                },
            ],
        },
        "addResponse": {
            "members": [
                {
                    "name": "sum",
                    "member": "int64",
                    "type": "int64",
                    "required": True,
                    "document": "doc about arg1",
                },
            ],
        },
    },
    "version": "1.0",
}


def register_service(specs):
    specs[service_name] = {
        service_version: _spec,
    }
