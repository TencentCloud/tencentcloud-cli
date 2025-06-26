# encoding: utf-8
from tccli.plugins.sso.login import login_command_entrypoint
from tccli.plugins.sso.logout import logout_command_entrypoint
from tccli.plugins.sso.configure import configure_command_entrypoint

service_name = "sso"
service_version = "2024-10-14"

_spec = {
    "metadata": {
        "serviceShortName": service_name,
        "apiVersion": service_version,
        "description": "sso related commands",
    },
    "actions": {
        "configure": {
            "name": "配置",
            "document": "configure login url",
            "input": "configureRequest",
            "output": "configureResponse",
            "action_caller": configure_command_entrypoint,
        },
        "login": {
            "name": "登录",
            "document": "login through sso",
            "input": "loginRequest",
            "output": "loginResponse",
            "action_caller": login_command_entrypoint,
        },
        "logout": {
            "name": "登出",
            "document": "remove local credential file",
            "input": "logoutRequest",
            "output": "logoutResponse",
            "action_caller": logout_command_entrypoint,
        },
    },
    "objects": {
        "loginRequest": {
            "members": [
                {
                    "name": "duration",
                    "member": "int64",
                    "type": "int64",
                    "required": False,
                    "document": "duration for credential",
                },
                {
                    "name": "uin",
                    "member": "string",
                    "type": "string",
                    "required": False,
                    "document": "Account uin to use",
                },
                {
                    "name": "rolename",
                    "member": "string",
                    "type": "string",
                    "required": False,
                    "document": "Role to use",
                },
            ],
        },
        "loginResponse": {"members": []},
        "logoutRequest": {"members": []},
        "logoutResponse": {"members": []},
        "configureRequest": {"members": [
            {
                "name": "url",
                "member": "string",
                "type": "string",
                "required": True,
                "document": "url for sso authentication",
            },
        ]},
        "configureResponse": {"members": []},
    },
    "version": "1.0",
}


def register_service(specs):
    specs[service_name] = {
        service_version: _spec,
    }
