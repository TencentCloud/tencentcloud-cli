# -*- coding: utf-8 -*-
import tccli.error_msg as ErrorMsg


class NiceCommand(object):

    def __init__(self, name, action=None):
        self.name = name
        self.action = action

        self._opt_list = []
        self._subcmd_list = []
        self._opt_map = {}
        self._subcmd_map = {}

        self.runtime_opt_map = {}
        self.runtime_opt_list = []

    def reg_cmd(self, cmd):
        if not isinstance(cmd, NiceCommand):
            return

        if cmd.name is None:
            raise Exception("command name was invalid")
        if cmd.name in self._subcmd_map:
            raise Exception("command %s already exists" % cmd.name)

        self._subcmd_map[cmd.name] = cmd
        self._subcmd_list.append(cmd.name)

    def reg_opt(self, name, tp):
        if not isinstance(name, str):
            raise Exception("name expect a string argument")
        if not isinstance(tp, str):
            raise Exception("type expect a string argument")
        if tp not in ["bool", "string"]:
            raise Exception("%s type was invalid" % tp)

        if name in self._opt_map:
            raise Exception("option %s already exists" % name)
        opt = {
            "name": name,
            "type": tp,
            }
        self._opt_map[name] = opt
        self._opt_list.append(name)

    def parse(self, argv):
        if not isinstance(argv, list):
            return
        if argv and argv[0] in self._subcmd_list:
            self._subcmd_map[argv[0]].parse(argv[1:])
            return

        if self.action is None:
            raise Exception(ErrorMsg.INVALID_CMD % "too few arguments")

        argc = len(argv)
        cur = 0
        while cur < argc:
            if argv[cur] not in self._opt_list:
                raise Exception(ErrorMsg.INVALID_CMD % argv[cur])
            if self._opt_map[argv[cur]]["type"] == "bool":
                cur += self._bool_parse(argv, cur)
                continue
            else:
                cur += self._bool_string(argv, argc, cur)
                continue
        self.action(self.runtime_opt_map, self.runtime_opt_list)

    def _bool_parse(self, argv, ind):
        self.runtime_opt_map[argv[ind]] = True
        self.runtime_opt_list.append(argv[ind])
        return 1

    def _bool_string(self, argv, argc, ind):
        if ind <= (argc - 2):
            self.runtime_opt_map[argv[ind]] = argv[ind+1]
            self.runtime_opt_list.append(argv[ind])
            return 2
        else:
            raise Exception("%s expect a value" % argv[ind])












