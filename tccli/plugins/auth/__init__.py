# encoding: utf-8
from tccli.plugins.auth.login import login_command_entrypoint
from tccli.plugins.auth.logout import logout_command_entrypoint

service_name = "auth"
service_version = "2024-08-20"

_spec = {
    "metadata": {
        "serviceShortName": service_name,
        "apiVersion": service_version,
        "description": "auth related commands",
    },
    "actions": {
        "login": {
            "name": "登陆",
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
                    "name": "browser",
                    "member": "string",
                    "type": "string",
                    "required": False,
                    "document": "use browser=no to indicate no browser login mode",
                },
            ],
        },
        "loginResponse": {
            "members": [],
        },
        "logoutRequest": {
            "members": [],
        },
        "logoutResponse": {
            "members": [],
        },
    },
    "version": "1.0",
}


def register_service(specs):
    specs[service_name] = {
        service_version: _spec,
    }
