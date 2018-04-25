#! /usr/bin/env python

import os
import tccli.services as Services
import tccli.options_define as OptionsDefine
services = Services.service_get_list()
services.append("configure")
if os.environ.get('LC_CTYPE', '') == 'UTF-8':
    os.environ['LC_CTYPE'] = 'en_US.UTF-8'


def pre_print(result, cur):
    if cur:
        result = [x for x in result if x.startswith(cur)]
    print(' \n'.join(result))


def comp_one_arg():
        pre_print(services, None)


def comp_two_arg(arg):
    if arg not in services:
        pre_print(services, arg)
        return
    if arg == "configure":
        pre_print(["get", "list", "set"], None)
    else:
        action_list = []
        actions = Services.services_get_module_info(arg)
        action_list.extend([x for x in actions.keys()])
        pre_print(action_list, None)


def comp_three_arg(arg_service, arg_cur):
    if arg_service not in services:
        return
    if arg_service == "configure":
        if arg_cur in ["get", "list", "set"]:
            return
        pre_print(["get", "list", "set"], arg_cur)
    else:
        action_list = []
        actions = Services.services_get_module_info(arg_service)
        action_list.extend(actions.keys())

        if arg_cur in action_list:
            return
        else:
            pre_print(action_list, arg_cur)


def comp_more_arg(arg_service, arg_action, arg_parma):
    if arg_service not in services:
        return
    if arg_service == "configure":
        return

    actions = Services.services_get_module_info(arg_service)
    if arg_action in actions.keys():
        loc_params = ["--" + x["name"] for x in actions[arg_action]["params"]]
        glo_params = ["--" + x for x in OptionsDefine.ACTION_GLOBAL_OPT]
        params = loc_params + glo_params
        if arg_parma.startswith("-") and arg_parma not in params:
            pre_print(params, arg_parma)


def complete():
    try:
        cline = os.environ.get('COMP_LINE') or os.environ.get('COMMAND_LINE') or ''
        words = cline.split()
        size = len(words)

        if size == 1:
            comp_one_arg()
        elif size == 2:
            comp_two_arg(words[1])
        elif size == 3:
            comp_three_arg(words[1], words[2])
        else:
            comp_more_arg(words[1], words[2], words[size - 1])
    except Exception:
        pass


if __name__ == '__main__':
    complete()
