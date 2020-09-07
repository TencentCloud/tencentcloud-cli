# -*- coding: utf-8 -*-
import os
import imp

def action_caller(service):
    cur_path = os.path.dirname(os.path.abspath(__file__))
    fp, pathname, desc = imp.find_module(service, [cur_path])
    mod = imp.load_module("tccli.services." + service, fp, pathname, desc)
    return mod.action_caller

