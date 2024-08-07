# encoding: utf-8
from add import add_command

service_name = "test"
service_version = "2024-08-07"

_spec = {
    "metadata": {
        "serviceShortName": service_name,
        "apiVersion": service_version,
        "description": "this is a test module",
    },
    # list all the actions here
    "actions": {
        "add": {
            "name": "测试接口",
            "document": "this is an test action",
            "input": "addRequest",
            "output": "addResponse",
            "action_caller": add_command,  # the function to call
        },
    },
    "objects": {
        "addRequest": {
            "members": [
                {
                    "name": "number1",
                    # int64, uint64, string, float, bool, date, datetime, datetime_iso, binary
                    "member": "int64",
                    # same as member
                    "type": "int64",
                    "required": True,
                    "document": "doc about number1",
                },
                {
                    "name": "number2",
                    "member": "int64",
                    "type": "int64",
                    # 是否必传
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


# a function named register_service is required
def register_service(specs):
    specs[service_name] = {
        service_version: _spec,
    }
