# -*- coding: utf-8 -*-

import os
import sys
import six
import tccli.options_define as OptionsDefine
from tccli.base_command import BasicCommand
from tccli.exceptions import ConfigurationError, ParamError
from tccli.help_command import BaseHelpCommand
from tccli.utils import Utils
from tccli.loaders import Loader


class BasicConfigure(BasicCommand):
    NAME = ''
    DESCRIPTION = ''
    USEAGE = ''
    OPTIONS = {
        "help": "show the tccli configure help info",
        "--profile": "specify a profile name"
    }
    EXAMPLES = ''

    def __init__(self):
        super(BasicConfigure, self).__init__()
        self.config_list = [
            OptionsDefine.Region, OptionsDefine.Output, OptionsDefine.ArrayCount, OptionsDefine.Warnings]
        self.cred_list = [OptionsDefine.SecretId, OptionsDefine.SecretKey, OptionsDefine.Token,
                          OptionsDefine.RoleArn, OptionsDefine.RoleSessionName]
        self.conf_service_list = [OptionsDefine.Version, OptionsDefine.Endpoint]
        self.cli_path = os.path.join(os.path.expanduser("~"), ".tccli")
        self._cli_data = Loader()

    def _run_main(self, parsed_args, parsed_globals):
        raise NotImplementedError("_run_main")

    def _init_configure(self, profile_name, input_data, extra={}):
        conf_data = {}
        is_exist, config_path = self._profile_existed(profile_name)
        if is_exist:
            conf_data = Utils.load_json_msg(config_path)

        for k in input_data.keys():
            conf_data[k] = input_data[k]
        if profile_name.endswith(".configure"):
            for mod in self._cli_data.get_available_services().keys():
                # we have to check autoscaling because we did it wrong in 3.0.30.1
                # consider remove it in 3.1.x
                if mod in conf_data and mod != 'autoscaling':
                    continue
                conf_data[mod] = {}
                conf_data[mod]["endpoint"] = "%s.tencentcloudapi.com" % mod
                # we have to do this because as is a keyword in python
                # as has been changed to autoscaling only in python sdk & cli
                if mod == 'autoscaling':
                    conf_data[mod]["endpoint"] = "as.tencentcloudapi.com"
                versions = self._cli_data.get_service_all_version_actions(mod).keys()
                version = sorted(versions)[-1]
                conf_data[mod]["version"] = version
        for k in extra.keys():
            try:
                ks = k.split(".")
                conf_data[ks[0]][ks[1]] = extra[k]
            except Exception as err:
                raise ConfigurationError("Unexpected format: %s\n "
                                         "Received input format: %s\n "
                                         "Valid input format eg. set cvm.version 2017-03-12"
                                         % (err, k))
        Utils.dump_json_msg(config_path, conf_data)

    def _checkout_config(self, profile_name):
        is_conexit, config_path = self._profile_existed(profile_name + ".configure")
        is_creexit, cred_path = self._profile_existed(profile_name + ".credential")
        if not is_conexit and not is_creexit:
            raise ConfigurationError(
                "not exist config file: %s or %s "
                % (profile_name + ".configure", profile_name + ".credential"))

        conf = Utils.load_json_msg(config_path)
        cred = Utils.load_json_msg(cred_path)
        if not (isinstance(conf, dict) and isinstance(cred, dict)):
            raise ConfigurationError(
                "not exist config file: %s or %s "
                % (profile_name + ".configure", profile_name + ".credential"))

    def _profile_existed(self, profile_name):
        return Utils.file_existed(self.cli_path, profile_name)

    def create_help_command(self):
        return ConfigureHelp(self.NAME, self)


class ConfigureListCommand(BasicConfigure):
    NAME = 'list'
    DESCRIPTION = 'list your profile(eg:secretId, secretKey, region, output).'
    USEAGE = 'tccli configure list [--profile profile-name]'
    EXAMPLES = "$ tccli configure list\n" \
               "credential:\n" \
               "secretId = ********************************\n" \
               "secretKey = ********************************\n" \
               "configure:\n" \
               "region = ap-guangzhou\n" \
               "output = json\n" \
               "cvm.version = 2017-03-12\n" \
               "cvm.endpoint = cvm.tencentcloudapi.com\n" \
               "...\n" \
               "..."

    def __init__(self, stream=sys.stdout):
        super(ConfigureListCommand, self).__init__()
        self._stream = stream

    def _run_main(self, args, parsed_globals):
        profile_name = parsed_globals.profile \
            if parsed_globals.profile else "default"

        is_exit, cred_path = self._profile_existed(profile_name + ".credential")
        self._stream.write("credential:\n")
        if is_exit:
            cred = Utils.load_json_msg(cred_path)
            for config in self.cred_list:
                if config in cred and cred[config]:
                    self._stream.write("%s = %s\n" % (config, cred[config]))

        # other in x.configure
        is_exit, config_path = self._profile_existed(profile_name + ".configure")
        self._stream.write("configure:\n")
        if is_exit:
            config = Utils.load_json_msg(config_path)
            for c in self.config_list:
                if c in config and config[c]:
                    self._stream.write("%s = %s\n" % (c, config[c]))

            modlist = sorted(config.keys())
            for c in modlist:
                if not config[c]:
                    continue
                if c in self.config_list:
                    continue
                try:
                    self._stream.write("%s.version = %s\n" % (c, config[c]["version"]))
                    self._stream.write("%s.endpoint = %s\n" % (c, config[c]["endpoint"]))
                except Exception:
                    pass


class ConfigureSetCommand(BasicConfigure):
    NAME = 'set'
    DESCRIPTION = 'set your profile(eg:secretId, secretKey, region, output).'
    USEAGE = 'tccli configure set [CONFIG] [--profile profile-name]'
    AVAILABLECONFIG = "secretId: TencentCloud API SecretId\n" \
                      "secretKey: TencentCloud API SecretKey\n" \
                      "region: which the region you want to work with belongs.\n" \
                      "output: TencentCloud API response format[json, text, table]\n" \
                      "[cvm, cbs ...].version: service [cvm cbs ...] version\n" \
                      "[cvm, cbs ...].endpoint: service [cvm cbs ...] access point domain name"
    EXAMPLES = "$ tccli configure set secretId ******\n" \
               "$ tccli configure set region ap-guangzhou\n" \
               "$ tccli configure set cvm.endpoint cvm.ap-guangzhou.tencentcloudapi.com"
    # 批量设置
    ARG_TABLE = [
        {'name': 'varname',
         'help_text': 'The name of the config value to set.',
         'action': 'store',
         'nargs': '+',
         'cli_type_name': 'string', 'positional_arg': True},
        # {'name': 'value',
        #  'help_text': 'The value to set.',
        #  'action': 'store',
        #  'no_paramfile': True,
        #  'cli_type_name': 'string', 'positional_arg': True},
    ]

    def __init__(self):
        super(ConfigureSetCommand, self).__init__()

    def _run_main(self, args, parsed_globals):
        varname_value = args.varname
        if len(varname_value) % 2 != 0:
            raise ParamError("Unexpected format\n"
                             "Expected input format：\n\n"
                             "   $tccli configure set region ap-guangzhou\n"
                             "   $tccli configure set region ap-guangzhou output json\n")
        varnames = varname_value[::2]
        values = varname_value[1::2]

        profile_name = parsed_globals.profile \
            if parsed_globals.profile else "default"

        config = {}
        cred = {}
        extra = {}

        for varname, value in zip(varnames, values):
            if varname in self.cred_list:
                cred[varname] = value
            elif varname in self.config_list:
                if varname == OptionsDefine.Output and value not in ['json', 'text', 'table']:
                    print('Output format must be json, text or table. Set as default: json')
                    config[varname] = 'json'
                else:
                    config[varname] = value
            else:
                extra[varname] = value

        if config or extra:
            self._init_configure(profile_name + '.configure', config, extra)
        if cred:
            self._init_configure(profile_name + '.credential', cred)


class ConfigureGetCommand(BasicConfigure):
    NAME = 'get'
    DESCRIPTION = "get your profile(eg:SecretId, SecretKey, Region)."
    USEAGE = "tccli configure get [CONFIG] [--profile profile-name]"
    AVAILABLECONFIG = "secretId: TencentCloud API SecretId\n" \
                      "secretKey: TencentCloud API SecretKey\n" \
                      "region: which the region you want to work with belongs.\n" \
                      "output: TencentCloud API response format[json, text, table]\n" \
                      "[cvm, cbs ...].version: service [cvm cbs ...] version\n" \
                      "[cvm, cbs ...].endpoint: service [cvm cbs ...] access point domain name"
    EXAMPLES = "$ tccli configure get region\n" \
               "region = ap-guangzhou\n" \
               "\n" \
               "$ tccli configure get cvm.version\n" \
               "cvm.version = 2017-03-12"

    ARG_TABLE = [
        {'name': 'varname',
         'help_text': 'The name of the config value to retrieve.',
         'action': 'store',
         'nargs': '+',
         'cli_type_name': 'string', 'positional_arg': True},
    ]

    def __init__(self, stream=sys.stdout, error_stream=sys.stderr):
        super(ConfigureGetCommand, self).__init__()
        self._stream = stream
        self._error_stream = error_stream

    def _run_main(self, args, parsed_globals):
        varname_list = args.varname
        profile_name = parsed_globals.profile \
            if parsed_globals.profile else "default"

        conf = {}
        cred = {}

        is_conf_exit, config_path = self._profile_existed(profile_name + ".configure")
        is_cred_exit, cred_path = self._profile_existed(profile_name + ".credential")

        if is_conf_exit:
            conf = Utils.load_json_msg(config_path)
        if is_cred_exit:
            cred = Utils.load_json_msg(cred_path)

        for varname in varname_list:
            if varname in conf.keys() and conf[varname]:
                value = conf[varname]
            elif varname in cred.keys() and cred[varname]:
                value = cred[varname]
            else:
                try:
                    kv = varname.split(".")
                    value = conf[kv[0]][kv[1]]
                except Exception as err:
                    raise ConfigurationError("%s in %s.configure not exist" % (varname, profile_name))
            self._stream.write("%s = %s" % (varname, value))
            self._stream.write('\n')


class ConfigureRemoveCommand(BasicConfigure):
    NAME = 'remove'
    DESCRIPTION = 'remove your profile: if you don\'t specify the file name, default file will be removed.'
    USEAGE = 'tccli configure remove [--profile profile-name]'
    EXAMPLES = "$ tccli configure remove\n" \
               "$ tccli configure remove --profile test\n"

    def __init__(self, error_stream=sys.stderr):
        super(ConfigureRemoveCommand, self).__init__()
        self._error_stream = error_stream

    def _run_main(self, args, parsed_globals):
        profile_name = parsed_globals.profile \
            if parsed_globals.profile else "default"

        configure_name = profile_name + '.configure'
        credential_name = profile_name + '.credential'

        configure_file = os.path.join(self.cli_path, configure_name)
        credential_file = os.path.join(self.cli_path, credential_name)

        if os.path.exists(configure_file):
            os.remove(configure_file)
        else:
            self._error_stream.write("profile `%s` is not exist\n" % configure_name)
        if os.path.exists(credential_file):
            os.remove(credential_file)
        else:
            self._error_stream.write("profile `%s` is not exist\n" % credential_name)


class ConfigureCommand(BasicConfigure):
    NAME = "configure"
    DESCRIPTION = "configure your profile(eg:secretId, secretKey, region, output)."
    USEAGE = "tccli configure [--profile profile-name]"
    AVAILABLESUBCOMMAND = ["set", 'get', 'list', 'remove']
    EXAMPLES = "To create a new configuration::\n" \
               "    $ tccli configure\n" \
               "    TencentCloud API secretId [None]: secretId\n" \
               "    TencentCloud API secretKey [None]: secretKey\n" \
               "    Default region name [ap-guangzhou]:\n" \
               "    Default output format [json]:\n" \
               "\n\n" \
               "To update just the region name::\n" \
               "    $ tccli configure\n" \
               "    TencentCloud API secretId [****]:\n" \
               "    TencentCloud API secretKey [****]:\n" \
               "    Default region name [ap-guangzhou]: ap-beijing\n" \
               "    Default output format [json]:\n"
    SUBCOMMANDS = [
        {'name': 'list', 'command_class': ConfigureListCommand},
        {'name': 'get', 'command_class': ConfigureGetCommand},
        {'name': 'set', 'command_class': ConfigureSetCommand},
        {'name': 'remove', 'command_class': ConfigureRemoveCommand}
    ]

    VALUES_TO_PROMPT = [
        ('secretId', "TencentCloud API secretId"),
        ('secretKey', "TencentCloud API secretKey"),
        ('region', "Default region name"),
        ('output', "Default output format"),
    ]

    def __init__(self):
        super(ConfigureCommand, self).__init__()
        self.init_configures()

    def _run_main(self, parsed_args, parsed_globals):
        # tccli configure
        profile_name = parsed_globals.profile \
            if parsed_globals.profile else "default"

        config = {
            OptionsDefine.Region: "ap-guangzhou",
            OptionsDefine.Output: "json"
        }

        cred = {
            OptionsDefine.SecretId: "None",
            OptionsDefine.SecretKey: "None"
        }

        is_conf_exist, config_path = self._profile_existed(profile_name + ".configure")
        is_cred_exist, cred_path = self._profile_existed(profile_name + ".credential")

        conf_data = {}
        cred_data = {}
        if is_conf_exist:
            conf_data = Utils.load_json_msg(config_path)
            for c in config:
                if c in conf_data and conf_data[c]:
                    config[c] = conf_data[c]
        if is_cred_exist:
            cred_data = Utils.load_json_msg(cred_path)
            for c in cred:
                if c in cred_data and cred_data[c]:
                    cred[c] = cred_data[c]

        for index, prompt_text in self.VALUES_TO_PROMPT:
            if index in config:
                response = self._compat_input("%s[%s]: " % (prompt_text, config[index]))
                if index == OptionsDefine.Output and response not in ['json', 'text', 'table']:
                    if config[index] not in ['json', 'text', 'table']:
                        print('Output format must be json, text or table. Set as default: json')
                        conf_data[index] = 'json'
                    else:
                        conf_data[index] = config[index]
                elif index == OptionsDefine.Region and not response:
                    if not config[index]:
                        print('Set region as default: %s' % config[index])
                    conf_data[index] = config[index]
                else:
                    conf_data[index] = response if response else config[index]
            else:
                response = self._compat_input(
                    "%s[%s]: " % (prompt_text, "*"+cred[index][-4:] if cred[index]!="None" else cred[index]))
                cred_data[index] = response if response else cred[index]

        self._init_configure(profile_name + ".configure", conf_data)
        self._init_configure(profile_name + ".credential", cred_data)

    def init_configures(self):
        config = {}
        if not self._profile_existed("default.configure")[0]:
            config = {
                "region": "ap-guangzhou",
                "output": "json",
                "array_count": 10,
                "warning": "off"
            }
        self._init_configure("default.configure", config)

    def _compat_input(self, prompt):
        sys.stdout.write(prompt)
        sys.stdout.flush()
        if six.PY2:
            return raw_input()
        else:
            return input()


class ConfigureHelp(BaseHelpCommand):

    def __init__(self, name, command_obj):
        self._name = name
        self.command_obj = command_obj
        super(ConfigureHelp, self).__init__()

    def _get_document_handler(self):
        return ConfigureDocumentHandler(self.doc, self.command_obj)


class ConfigureDocumentHandler(object):

    def __init__(self, doc, command_obj):
        self.doc = doc
        self.command_obj = command_obj

    def description(self):
        self.doc.style.h2('Description')
        self.doc.doc_description_indent(self.command_obj.DESCRIPTION)

    def useage(self):
        self.doc.style.h2('Useage')
        self.doc.doc_description_indent(self.command_obj.USEAGE)

    def options(self):
        self.doc.style.h2('Options')
        for option, content in self.command_obj.OPTIONS.items():
            self.doc.doc_title_indent('%s' % option)
            self.doc.doc_description_indent(content)

    def available_subcommand(self):
        if hasattr(self.command_obj, "AVAILABLESUBCOMMAND"):
            self.doc.style.h2('Available Subcommand')
            for sub_command in self.command_obj.AVAILABLESUBCOMMAND:
                self.doc.doc_title_indent(sub_command)

    def available_config(self):
        if hasattr(self.command_obj, "AVAILABLECONFIG"):
            self.doc.style.h2('Available config')
            self.doc.doc_description_indent(self.command_obj.AVAILABLECONFIG)

    def example(self):
        if hasattr(self.command_obj, "EXAMPLES"):
            self.doc.style.h2('Example')
            self.doc.doc_description_indent(self.command_obj.EXAMPLES)

    def doc_help(self):
        self.doc.style.h1(self.command_obj.NAME)
        self.description()
        self.useage()
        self.options()
        self.available_subcommand()
        self.available_config()
        self.example()




