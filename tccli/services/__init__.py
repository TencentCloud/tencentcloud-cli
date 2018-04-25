# -*- coding: utf-8 -*-
import os
import imp


def service_get_list():
    services = []
    srvpath = os.path.dirname(os.path.abspath(__file__))
    for f in os.listdir(srvpath):
        fpath = os.path.join(srvpath, f)
        if os.path.isdir(fpath) and not f.startswith("_"):
            services.append(f)
    return sorted(services)


def services_register_arg(command, service):
    cur_path = os.path.dirname(os.path.abspath(__file__))
    fp, pathname, desc = imp.find_module(service,[cur_path])
    mod = imp.load_module(service, fp, pathname, desc)
    mod.register_arg(command)


def services_get_module_info(service):
    cur_path = os.path.dirname(os.path.abspath(__file__))
    fp, pathname, desc = imp.find_module(service, [cur_path])
    mod = imp.load_module(service, fp, pathname, desc)
    return mod.get_actions_info()


def dynamic_load_module(service):
    cur_path = os.path.dirname(os.path.abspath(__file__))
    fp, pathname, desc = imp.find_module(service, [cur_path])
    mod = imp.load_module(service, fp, pathname, desc)
    return mod
