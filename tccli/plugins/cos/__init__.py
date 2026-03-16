# encoding: utf-8
"""
COS命令行工具插件
将coscmd的所有命令集成到tencentcloud-cli中
"""
from .list_object import list_object

service_name = "cos"
service_version = "2021-02-24"

_spec = {
    "metadata": {
        "serviceShortName": service_name,
        "apiVersion": service_version,
        "description": "COS (Cloud Object Storage) command line tool",
    },
    "actions": {
        "list": {
            "name": "列出文件",
            "document": "List files on COS",
            "input": "ListRequest",
            "output": "ListResponse",
            "action_caller": list_object,
        }
    },
    "objects": {
        "listRequest": {
            "members": [
                {"name": "bucket", "member": "string", "type": "string", "required": False, "document": "bucket id"},
            ],
        },
        "listResponse": {
            "members": [],
        },
    },
    "version": "1.0",
}


def register_service(specs):
    specs[service_name] = {
        service_version: _spec,
    }
