# -*- coding: utf-8 -*-

import os
import copy
import json
from tccli.utils import Utils
from tccli import __version__
from tccli.services import SERVICE_VERSIONS
from collections import OrderedDict

BASE_TYPE = ["int64", "uint64", "string", "float", "bool", "date", "datetime", "datetime_iso", "binary"]
CLI_BASE_TYPE = ["Integer", "String", "Float", "Timestamp", "Boolean", "Binary"]

PARAM_TYPE_MAP = {
    'int64': 'Integer',
    'uint64': 'Integer',
    'int': 'Integer',
    'string': 'String',
    'float': 'Float',
    'bool': 'Boolean',
    'date': "Timestamp",
    'datetime': "Timestamp",
    'datetime_iso': "Timestamp",
    'binary': 'Binary',
    'object': 'Object',
    'list': 'Array'
}


class Loader(object):
    def get_services_path(self):
        base_path = os.path.dirname(os.path.abspath(__file__))
        services_path = os.path.join(base_path, 'services')
        return services_path

    def get_cli_version(self):
        return __version__

    def get_description(self):
        return "tccli (Tencent Cloud Command Line Interface) is a tool to manage your Tencent Cloud services."

    def get_configure(self):
        return "Before using tccli, you should use the command(tccli configure) to configure your profile " \
               "as the default For more information, please enter tccli configure help"

    def get_useage(self):
        return "tccli [options] <service> [options] <action> [options] [options and parameters]"

    def get_options(self):
        return {
            "help": "show the tccli help info",
            "--version": "show the version of tccli"
        }

    def get_cli_option(self):
        return {
            "filter": {
                "help": "specify a filter field"
            },
            "output": {
                "choices": [
                    "json",
                    "text",
                    "table"
                ],
                "metavar": "output_format"
            },
            "secretId": {
                "help": "specify a SecretId",
            },
            "secretKey": {
                "help": "specify a SecretKey",
            },
            "token": {
                "help": "temporary certificate token",
            },
            "version": {
                "help": "specify a DescribeRegions api version",
                "metavar": "version_name"
            },
            "profile": {
                "help": "specify a profile name",
                "metavar": "profile_name"
            },
            "region": {
                "help": "identify the region to which the instance you want to work with belongs.",
                "metavar": "region_name"
            },
            "endpoint": {
                "help": "specify an access point domain name",
                "metavar": "endpoint_url"
            },
            "timeout": {
                "type": "int",
                "help": "specify a request timeout"
            },
            "generate-cli-skeleton": {
                'help': 'Prints a JSON skeleton to standard output without sending '
                        'an API request. If provided with no value or the value '
                        '``input``, prints a sample input JSON that can be used as an '
                        'argument for ``--cli-input-json``.',
                'nargs': '?',
                'const': 'input',
                'choices': ['input'],
            },
            'cli-input-json': {
                'help': 'Reads arguments from the JSON string provided. The JSON string '
                        'follows the format provided by ``--generate-cli-skeleton``. '
            },
            'cli-unfold-argument': {
                'help': 'complex type parameters are expanded with dots',
                'action': 'store_true'
            },
            'warning': {
                'help': 'Open the warning log',
                'action': 'store_true'
            }

        }

    def _version_transform(self, version):
        return version[1:5] + "-" + version[5:7] + "-" + version[7:9]

    def get_available_services(self):
        return SERVICE_VERSIONS

    def get_service_default_version(self, service):
        return self.get_available_services()[service][0]

    def get_service_model(self, service, version):
        services_path = self.get_services_path()
        version = "v" + version.replace('-', '')
        apis_path = os.path.join(services_path, service, version, "api.json")
        if not os.path.exists(apis_path):
            raise Exception("Not find service:%s version:%s model" % (service, version))

        with open(apis_path, 'r') as f:
            return json.load(f)

    def get_service_description(self, service, version):
        service_model = self.get_service_model(service, version)
        description = service_model["metadata"].get("api_brief", '')
        return description

    def get_service_useage(self, service):
        return "tccli %s <action> [--param...]" % service

    def get_service_options(self, service):
        return {
            "help": "show the tccli %s help info" % service
        }

    def get_action_model(self, service, version, action):
        service_model = self.get_service_model(service, version)
        action_model = service_model["actions"][action]
        return action_model

    def get_actions_info(self, service, version):
        service_model = self.get_service_model(service, version)
        actions_info = OrderedDict()
        for action in sorted(service_model["actions"]):
            actions_info[action] = {}
            actions_info[action]["name"] = service_model["actions"][action]["name"]
            actions_info[action]["document"] = service_model["actions"][action]["document"]
        return actions_info

    def get_service_all_version_actions(self, service):
        services_path = self.get_services_path()
        module_path = os.path.join(services_path, service)
        if not os.path.exists(module_path):
            raise Exception("Not find service:%s " % service)
        version_actions = {}
        for version in os.listdir(module_path):
            if version.startswith("v") and os.path.isdir(os.path.join(module_path, version)):
                version = self._version_transform(version)
                actions = self.get_actions_info(service, version).keys()
                version_actions[version] = actions
        return version_actions

    def get_service_all_action_param(self, service, model=None):
        version_actions = self.get_service_all_version_actions(service)
        version_action_params = {}
        for version in version_actions:
            version_action_params[version] = {}
            for action in version_actions[version]:
                if model == "cli-unfold-argument":
                    params = self.get_unfold_param_info(service, version, action).keys()
                else:
                    params = self.get_param_info(service, version, action).keys()
                version_action_params[version][action] = params
        action_params = {}
        for version in version_action_params:
            for action in version_action_params[version]:
                if action in action_params:
                    action_params[action] = list(set(action_params[action] + version_action_params[version][action]))
                else:
                    action_params[action] = version_action_params[version][action]
        return action_params

    def get_action_description(self, service, version, action):
        return self.get_actions_info(service, version)[action]['document']

    def get_action_useage(self, service, action):
        return "tccli %s %s [--param...]" % (service, action)

    def get_action_options(self, service, action):
        return {
            "help": "show the tccli %s %s help info" % (service, action),
            "--profile": "specify a profile name",
            "--secretId": "specify a SecretId",
            "--secretKey": "specify a SecretKey",
            "--token": "temporary certificate token",
            "--region": "identify the region to which the instance you want to work with belongs.",
            "--endpoint": "specify an access point domain name",
            "--version": "specify a %s api version" % action,
            "--filter": "specify a filter field",
            "--timeout": "specify a request timeout",
            "--generate-cli-skeleton": "Prints a JSON skeleton to standard output without sending "
                                       "an API request. If provided with no value or the value "
                                       "input, prints a sample input JSON that can be used as an "
                                       "argument for --cli-input-json. If provided with the value "
                                       "output, it validates the command inputs and returns a "
                                       "sample output JSON for that command.",
            "--cli-input-json": "Reads arguments from the JSON string provided. The JSON string "
                                "follows the format provided by --generate-cli-skeleton. ",
            "--cli-unfold-argument": "complex type parameters are expanded with dots",
            "--warning": "Open the warning log",
        }

    def _filling_param_info(self, param_info, para, param_type, member):
        param_info[para["name"]] = {}
        param_info[para["name"]]["document"] = para["document"]
        if "required" in para:
            param_info[para["name"]]["required"] = "Required" if para["required"] else "Optional"
        if "value_allowed_null" in para:
            param_info[para["name"]]["value_allowed_null"] = \
                "AllowedNull" if para["value_allowed_null"] else "NotAllowedNull"
        param_info[para["name"]]["type_name"] = PARAM_TYPE_MAP.get(para["member"], para["member"])
        param_info[para["name"]]["type"] = PARAM_TYPE_MAP.get(param_type, param_type)
        param_info[para["name"]]["members"] = member
        return param_info

    def _get_param_info(self, param_model, object_model):
        param_info = {}
        for para in param_model:
            if para["type"] == "list":
                if para["member"] not in BASE_TYPE:
                    self._filling_param_info(
                        param_info, para, "list",
                        [self._get_param_info(object_model[para["member"]]["members"], object_model)])
                else:
                    self._filling_param_info(
                        param_info, para, "list", [para["member"]])
            else:
                if para["member"] not in BASE_TYPE:
                    param_info = self._filling_param_info(
                        param_info, para, para["member"],
                        self._get_param_info(object_model[para["member"]]["members"], object_model))
                else:
                    self._filling_param_info(param_info, para, para["member"], para["member"])
        return param_info

    def get_param_info(self, service, version, action):
        service_model = self.get_service_model(service, version)
        param_model = service_model["objects"]
        return self._get_param_info(param_model[action + "Request"]["members"], param_model)

    def get_output_param_info(self, service, version, action):
        service_model = self.get_service_model(service, version)
        param_model = service_model["objects"]
        return self._get_param_info(param_model[action + "Response"]["members"], param_model)

    def _generate_param_skeleton(self, param_model, name):
        param_skeleton = {}
        for para in param_model:
            if para["type"] == "list":
                if para["member"] not in BASE_TYPE:
                    param_skeleton[para["name"]] = \
                        [self._generate_param_skeleton(name[para["member"]]["members"], name)]
                else:
                    param_skeleton[para["name"]] = [PARAM_TYPE_MAP[para["member"]]]
            else:
                if para["member"] not in BASE_TYPE:
                    param_skeleton[para["name"]] = \
                        self._generate_param_skeleton(name[para["member"]]["members"], name)
                else:
                    param_skeleton[para["name"]] = PARAM_TYPE_MAP[para["member"]]
        return param_skeleton

    def generate_param_skeleton(self, service, version, action):
        service_model = self.get_service_model(service, version)
        param_model = service_model["objects"]
        return self._generate_param_skeleton(param_model[action + "Request"]["members"], param_model)

    def get_unfold_param_info(self, service, version, action, profile="default", param_array=False):
        service_model = self.get_service_model(service, version)
        object_model = service_model["objects"]
        all_param_list = []
        for para in object_model[action + "Request"]["members"]:
            param_list = []
            self._get_unfold_param_info(object_model, all_param_list, param_list, para)

        if param_array:
            all_param_list = self._add_array_item(all_param_list, profile)

        return self._filling_unfold_param_info(all_param_list, service, version, action)

    def _add_array_item(self, param_list, profile):
        is_conf_exist, conf_path = Utils.file_existed(os.path.join(os.path.expanduser("~"), ".tccli"),
                                                      profile + ".configure")
        if is_conf_exist:
            array_count = Utils.load_json_msg(conf_path).get("arrayCount", 10)
        else:
            array_count = 10
        all_param_list = param_list
        for para in param_list:
            for idx, item in enumerate(para):
                if item == '0':
                    for i in range(1, int(array_count)):
                        tmp = copy.deepcopy(para)
                        tmp[idx] = str(i)
                        all_param_list.append(tmp)
        return all_param_list

    def _recur_get_unfold_param_info(self, param_model, object_model, return_param_list, param_list):
        for para in param_model:
            self._get_unfold_param_info(object_model, return_param_list, param_list, para)
        if param_list.pop().isdigit():
            param_list.pop()

    def _get_unfold_param_info(self, object_model, return_param_list, param_list, para):
        param_list.append(para["name"])
        if para["type"] == "list" and para["member"] not in BASE_TYPE:
            param_list.append('0')
        if para["member"] not in BASE_TYPE:
            self._recur_get_unfold_param_info(object_model[para["member"]]["members"],
                                              object_model, return_param_list, param_list)
        else:
            tmp = copy.deepcopy(param_list)
            return_param_list.append(tmp)

            if param_list.pop().isdigit():
                param_list.pop()

    def _filling_unfold_param_info(self, param_list, service, version, action):
        unfold_param = {}
        param_info = self.get_param_info(service, version, action)
        for param in param_list:
            unfold_param[".".join(param)] = {}

            tmp_param = [item for item in param if not item.isdigit()]
            res = param_info[tmp_param[0]]

            param_type = res["type"]
            type_name = res["type_name"]
            required = res["required"]
            document = res["document"]

            for idx, item in enumerate(tmp_param[1:]):
                if res["type"] == "Array":
                    res = res["members"][0][item]
                else:
                    res = res["members"][item]

                if required == "Required" and res["required"] == "Optional":
                    required = "Optional"

                if idx == len(tmp_param) - 2:
                    param_type = res["type"]
                    type_name = res["type_name"] if res["type"] == "Array" \
                        else res["type_name"]
                    document = res["document"]
                    break

            if len([item for item in param if item.isdigit() and int(item) > 0]) > 0:
                required = "Optional"

            unfold_param[".".join(param)]["type"] = param_type
            unfold_param[".".join(param)]["type_name"] = type_name
            unfold_param[".".join(param)]["required"] = required
            unfold_param[".".join(param)]["document"] = document
        return unfold_param

    def get_action_example_model(self, service, version, action):
        services_path = self.get_services_path()
        version = "v" + version.replace('-', '')
        example_path = os.path.join(services_path, service, version, "examples.json")
        if not os.path.exists(example_path):
            raise Exception("Not find service:%s version:%s model" % (service, version))

        with open(example_path, 'r') as f:
            examples = json.load(f)
        return examples['actions'][action]

    def generate_cli_example(self, service, version, action):
        examples = self.get_action_example_model(service, version, action)
        for example in examples:
            example["input"] = self.translate_cli_example(service, action, example)
            try:
                example["output"] = json.dumps(json.loads(example["output"], object_pairs_hook=OrderedDict),
                                               indent=4, separators=(',', ': '), ensure_ascii=False)
            except Exception:
                pass
        return examples

    def translate_cli_example(self, module, action, example):
        if example["input"].startswith("https"):
            input_param_list = example["input"].replace(u"&<公共请求参数>", "").split("&")[1:]
            return self.translate_get_cli_param(input_param_list)
        elif example["input"].startswith("POST"):
            input_param = example["input"].split('\n\n')[-1]
            try:
                input_param = json.loads(input_param, object_pairs_hook=OrderedDict)
            except Exception as err:
                raise Exception("service: %s, action: %s, err: %s" % (module, action, err))
            return self.translate_post_cli_param(input_param)

    def translate_get_cli_param(self, input_param_list):
        param_list = [k.strip() for k in input_param_list]
        param_dict = OrderedDict()
        for item in param_list:
            try:
                key = item.split("=")[0]
                value = item.split("=")[1]
            except Exception:
                continue
            if key.split(".")[-1].isdigit():
                key = ".".join(key.split(".")[:-1])
                if key not in param_dict:
                    param_dict[key] = [value]
                else:
                    param_dict[key].append(value)
            else:
                param_dict[key] = value

        cli_param_list = []
        for key, value in param_dict.items():
            cli_param = "--" + key
            if isinstance(value, list):
                for item in value:
                    if " " in str(item):
                        cli_param += " " + "'" + str(item) + "'"
                    else:
                        cli_param += " " + str(item)
            else:
                if " " in str(value):
                    cli_param += " " + "'" + str(value) + "'"
                else:
                    cli_param += " " + str(value)
            cli_param_list.append(cli_param)
        return cli_param_list

    def translate_post_cli_param(self, input_param):
        all_param_list = []
        param_list = []
        self._translate_post_cli_param(input_param, param_list, all_param_list)
        cli_param_list = ["--" + ".".join(item[:-1]) + ' ' + item[-1] for item in all_param_list]
        return cli_param_list

    def _translate_post_cli_param(self, input_param, param_list, all_param_list):
        # basic type
        if not isinstance(input_param, list) and not isinstance(input_param, dict):
            if isinstance(input_param, str) and " " in input_param:
                input_param = "'" + input_param + "'"
            param_list.append(str(input_param))
            tmp = copy.deepcopy(param_list)
            all_param_list.append(tmp)
            param_list.pop()
        # basic type array
        elif isinstance(input_param, list) and len(input_param) > 0 and not isinstance(input_param[0], dict):
            value = " ".join(["'"+str(param)+"'" if " " in str(param) else str(param) for param in input_param])
            param_list.append(value)
            tmp = copy.deepcopy(param_list)
            all_param_list.append(tmp)
            param_list.pop()
        # complex object type array
        elif isinstance(input_param, list) and len(input_param) > 0 and isinstance(input_param[0], dict):
            for idx, param in enumerate(input_param):
                param_list.append(str(idx))
                self._translate_post_cli_param(param, param_list, all_param_list)
                param_list.pop()
        # complex object type
        elif isinstance(input_param, dict):
            for param in input_param:
                param_list.append(param)
                self._translate_post_cli_param(input_param[param], param_list, all_param_list)
                param_list.pop()
        # null array
        else:
            pass

