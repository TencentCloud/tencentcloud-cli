# -*- coding: utf-8 -*-
import os
import sys
import json
from tccli.nice_command import NiceCommand
import tccli.services as Services
import tccli.help_template as HelpTmplate
import tccli.options_define as OptionsDefine
import tccli.error_msg as ErrorMsg
PY2 = sys.version_info[0] == 2


class Configure(object):

    def __init__(self, service_list=None):
        self.profile = "default"
        self.credential = "credential"
        self.configure = "configure"
        self.config_list = [OptionsDefine.Region, OptionsDefine.Output]
        self.cred_list = [OptionsDefine.SecretId, OptionsDefine.SecretKey]
        self.conf_service_list = [OptionsDefine.Version, OptionsDefine.Endpoint]
        self.service_list = service_list
        if not service_list:
            self.service_list = Services.service_get_list()
        self.cli_path = os.path.join(os.path.expanduser("~"), ".tccli")
        if not os.path.exists(self.cli_path):
            try:
                os.mkdir(self.cli_path)
            except Exception as err:
                pass

    def _load_json_msg(self, filename):
        with open(filename, "r") as f:
            data = json.load(f)
            return data

    def _dump_json_msg(self, filename, data):
        with open(filename, "w") as f:
            json.dump(data, f, indent=2, separators=(',', ': '), ensure_ascii=False, sort_keys=True)

    def _profile_existed(self, profile_name):
        file_path = os.path.join(self.cli_path, profile_name)
        if os.path.exists(file_path):
            return True, file_path
        return False, file_path

    def _modify_configure(self, name, data, extra={}):
        try:
            conf = {}
            if not data and not extra:
                return
            isexist, config_path = self._profile_existed(name)
            if isexist:
                conf = self._load_json_msg(config_path)

            for k in data.keys():
                conf[k] = data[k]
            if name.endswith(".configure"):
                for mod in self.service_list:
                    # we have to check autoscaling because we did it wrong in 3.0.30.1
                    # consider remove it in 3.1.x
                    if mod in conf and mod != 'autoscaling':
                        continue
                    conf[mod] = {}
                    conf[mod]["endpoint"] = "%s.tencentcloudapi.com" % mod
                    # we have to do this because as is a keyword in python
                    # as has been changed to autoscaling only in python sdk & cli
                    if mod == 'autoscaling':
                        conf[mod]["endpoint"] = "as.tencentcloudapi.com"
                    module = Services.dynamic_load_module(mod)
                    version = sorted(module.AVAILABLE_VERSION_LIST)[-1]
                    conf[mod]["version"] = version
            for k in extra.keys():
                try:
                    ks = k.split(".")
                    conf[ks[0]][ks[1]] = extra[k]
                except Exception:
                    pass
            self._dump_json_msg(config_path, conf)
        except Exception as err:
            raise Exception("modify file %s failed %s" % (config_path, str(err)))

    def _get_configure(self, argv, arglist):

        if OptionsDefine.Help in argv:
            print(HelpTmplate.GET_CONFIGURE)
            return
        name = "default"
        if ("--" + OptionsDefine.Profile) in argv:
            name = argv["--" + OptionsDefine.Profile]

        is_conexit, config_path = self._profile_existed(name + ".configure")
        is_creexit, cred_path = self._profile_existed(name + ".credential")
        conf = {}
        cred = {}
        if is_conexit:
            conf = self._load_json_msg(config_path)
        if is_creexit:
            cred = self._load_json_msg(cred_path)
        if not arglist:
             raise Exception(ErrorMsg.FEW_ARG)
        for arg in arglist:
            if arg in [OptionsDefine.Help, OptionsDefine.Profile]:
                continue
            if arg in conf.keys() and conf[arg]:
                if arg not in self.config_list:
                    continue
                print("%s = %s" % (arg, conf[arg]))
            elif arg in cred.keys() and cred[arg]:
                print("%s = %s" % (arg, cred[arg]))
            else:
                try:
                    ks = arg.split(".")
                    print("%s.%s = %s" % (ks[0], ks[1], conf[ks[0]][ks[1]]))
                except Exception:
                    pass

    def _set_configure(self, argv, arglist):
        if OptionsDefine.Help in argv:
            print(HelpTmplate.SET_CONFIGURE)
            return
        name = "default"
        if ("--" + OptionsDefine.Profile) in argv:
            name = argv["--" + OptionsDefine.Profile]
            del argv["--" + OptionsDefine.Profile]
        config = {}
        cred = {}
        extra = {}
        if not argv:
             raise Exception(ErrorMsg.FEW_ARG)
        for k in argv.keys():
            if k in self.cred_list:
                cred[k] = argv[k]
            elif k in self.config_list:
                config[k] = argv[k]
            else:
                extra[k] = argv[k]
        if config or extra:
            self._modify_configure(name + ".configure", config, extra)
        if cred:
            self._modify_configure(name + ".credential", cred)

    def _list_configure(self, argv, arglist):
        if OptionsDefine.Help in argv:
            print(HelpTmplate.LIST_CONFIGURE)
            return
        name = "default"
        if ("--" + OptionsDefine.Profile) in argv:
            name = argv["--" + OptionsDefine.Profile]

        # SecretId SecretKey in x.credential
        is_exit, cred_path = self._profile_existed(name + ".credential")
        print("credential:")
        if is_exit:
            cred = self._load_json_msg(cred_path)
            for config in self.cred_list:
                if config in cred and cred[config]:
                    print("%s =  %s" % (config, cred[config]))

        # other in x.configure
        is_exit, config_path = self._profile_existed(name + ".configure")
        print("configure:")
        if is_exit:
            config = self._load_json_msg(config_path)
            for c in self.config_list:
                if c in config and config[c]:
                    print("%s =  %s" % (c, config[c]))

            modlist = sorted(config.keys())
            for c in modlist:
                if not config[c]:
                    continue
                if c in self.config_list:
                    continue
                try:
                    print("%s.version =  %s" % (c, config[c]["version"]))
                    print("%s.endpoint =  %s" % (c, config[c]["endpoint"]))
                except Exception:
                    pass

    def _interactive_configure(self, profile):
        vinput = None
        if not PY2:
            vinput = input
        else:
            vinput = raw_input
        config = {
            OptionsDefine.Region: "ap-guangzhou",
            OptionsDefine.Output: "json"
        }

        cred = {
            OptionsDefine.SecretId: "None",
            OptionsDefine.SecretKey: "None"
        }

        is_conexist, config_path = self._profile_existed(profile + ".configure")
        is_creexist, cred_path = self._profile_existed(profile + ".credential")
        fileconf = {}
        filecred = {}
        if is_conexist:
            fileconf = self._load_json_msg(config_path)
            for c in config.keys():
                if c in fileconf and fileconf[c]:
                    config[c] = fileconf[c]
        if is_creexist:
            filecred = self._load_json_msg(cred_path)
            for c in cred.keys():
                if c in filecred and filecred[c]:
                    cred[c] = "*" + filecred[c][-4:]

        cmd = vinput("TencentCloud API secretId[%s]: " % cred[OptionsDefine.SecretId])
        if cmd:
            filecred["secretId"] = cmd

        cmd = vinput("TencentCloud API secretKey[%s]: " % cred[OptionsDefine.SecretKey])
        if cmd:
            filecred["secretKey"] = cmd

        cmd = vinput("region[%s]: " % config[OptionsDefine.Region])
        if cmd:
            fileconf["region"] = cmd

        cmd = vinput("output[%s]: " % config[OptionsDefine.Output])
        if cmd:
            fileconf["output"] = cmd

        self._modify_configure(config_path, fileconf)
        self._modify_configure(cred_path, filecred)

    def _configure(self, argv, arglist):
        if OptionsDefine.Help in argv:
            print(HelpTmplate.CONFIGURE_HELP)
            return
        name = "default"
        if ("--" + OptionsDefine.Profile) in argv:
            name = argv["--" + OptionsDefine.Profile]
        self._interactive_configure(name)

    def register_arg(self, command):
        # 增加cmd  profile
        config_cmd = NiceCommand("configure", self._configure)
        command.reg_cmd(config_cmd)
        config_cmd.reg_opt(OptionsDefine.Help, "bool")
        config_cmd.reg_opt("--" + OptionsDefine.Profile, "string")

        get_cmd = NiceCommand("get", self._get_configure)
        set_cmd = NiceCommand("set", self._set_configure)
        list_cmd = NiceCommand("list", self._list_configure)
        get_cmd.reg_opt("--" + OptionsDefine.Profile, "string")
        set_cmd.reg_opt("--" + OptionsDefine.Profile, "string")
        list_cmd.reg_opt("--" + OptionsDefine.Profile, "string")

        get_cmd.reg_opt(OptionsDefine.Help, "bool")
        set_cmd.reg_opt(OptionsDefine.Help, "bool")
        list_cmd.reg_opt(OptionsDefine.Help, "bool")

        for s in (self.config_list + self.cred_list):
            get_cmd.reg_opt(s, "bool")
            set_cmd.reg_opt(s, "string")

        for module in self.service_list:
            for opt in self.conf_service_list:
                get_cmd.reg_opt("%s.%s" % (module, opt), "bool")
                set_cmd.reg_opt("%s.%s" % (module, opt), "string")

        config_cmd.reg_cmd(get_cmd)
        config_cmd.reg_cmd(set_cmd)
        config_cmd.reg_cmd(list_cmd)

    def init_configures(self):
        if not self._profile_existed("default.configure")[0]:
            config = {
                "region": "ap-guangzhou",
                "output": "json",
            }
            self._modify_configure("default.configure", config)
