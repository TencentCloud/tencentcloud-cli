# encoding: utf-8
from add import add_command

service_name = "test"
service_version = "2024-08-07"
spec = {
    "metadata": {
        "apiVersion": service_version,
        "api_brief": "",
        "createdAt": "2023-05-18 01:01:13",
        "description": "this is a test module",
        "docurl": "",
        "intro": service_name,
        "regions": [
            "ap-shanghai"
        ],
        "serviceNameCN": "测试插件",
        "serviceShortName": "test",
    },
    "actions": {
        "add": {
            "name": "测试接口",
            "input": "addRequest",
            "output": "addResponse",
            "action_caller": add_command,
        },
    },
    "objects": {
        "addRequest": {
            "members": [
                {
                    "name": "number1",
                    "member": "int64",
                    "type": "int64",
                    "required": True,
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
            "members": {
                "name": "sum",
                "member": "int",
                "type": "int",
                "required": True,
                "document": "doc about arg1",
            },
        },
    },
    "version": "1.0",
}


class ServiceRegister(object):
    def register(self, specs):
        specs[service_name] = {
            service_version: spec,
        }
