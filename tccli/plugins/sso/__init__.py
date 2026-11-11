# encoding: utf-8
from tccli.plugins.sso.login import login_command_entrypoint
from tccli.plugins.sso.logout import logout_command_entrypoint
from tccli.plugins.sso.configure import configure_command_entrypoint
from tccli.plugins.sso.list import list_uin_command_entrypoint, list_role_command_entrypoint

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
        "list-uin": {
            "name": "查询成员账号",
            "document": "list all member accounts (uin) available for the current login state. Output is one tab-separated record per line, fields: <uin>, <name>. Exits non-zero on failure.",
            "input": "list-uinRequest",
            "output": "list-uinResponse",
            "action_caller": list_uin_command_entrypoint,
        },
        "list-role": {
            "name": "查询角色",
            "document": "list role configurations of the specified uin. Output is one tab-separated record per line, fields: <uin>, <role name>, <role id>. Exits non-zero on failure.",
            "input": "list-roleRequest",
            "output": "list-roleResponse",
            "action_caller": list_role_command_entrypoint,
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
                {
                    "name": "role-id",
                    "member": "string",
                    "type": "string",
                    "required": False,
                    "document": "Role configuration id to use, takes precedence over rolename",
                },
            ],
        },
        "loginResponse": {"members": []},
        "logoutRequest": {"members": []},
        "list-uinRequest": {"members": []},
        "list-uinResponse": {"members": []},
        "list-roleRequest": {
            "members": [
                {
                    "name": "uin",
                    "member": "string",
                    "type": "string",
                    "required": False,
                    "document": "uin to list roles for; asked interactively when omitted and stdin is a terminal, required otherwise",
                },
            ],
        },
        "list-roleResponse": {"members": []},
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
