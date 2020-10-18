#! /usr/bin/env python

import os
import re
import tccli.options_define as OptionsDefine
from tccli.utils import Utils
from tccli.loaders import Loader
loader = Loader()
services = sorted(loader.get_available_services().keys())
services.append("configure")
if os.environ.get('LC_CTYPE', '') == 'UTF-8':
    os.environ['LC_CTYPE'] = 'en_US.UTF-8'


def pre_print(result, cur):
    if cur:
        mathch_list = [x for x in result if x.startswith(cur)]
        if not mathch_list:
            mathch_list = [x for x in result if re.match(cur, x, re.I)]
        print(' \n'.join(mathch_list))
        return
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
        actions = loader.get_service_all_action_param(arg)
        pre_print(actions.keys(), None)


def comp_three_arg(arg_service, arg_cur):
    if arg_service not in services:
        return
    if arg_service == "configure":
        if arg_cur in ["get", "list", "set"]:
            return
        pre_print(["get", "list", "set"], arg_cur)
    else:
        action_list = []
        actions = loader.get_service_all_action_param(arg_service)
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

    mode = Utils.get_call_mode()
    actions = loader.get_service_all_action_param(arg_service, mode)

    if arg_action in actions.keys():
        loc_params = ["--" + x for x in sorted(actions[arg_action])]
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
