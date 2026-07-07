# -*- coding: utf-8 -*-

import os
import six
import copy
import json
import sys
from tccli.utils import Utils
from tccli import __version__
from tccli.services import SERVICE_VERSIONS
from collections import OrderedDict
import tccli.plugin as plugin

BASE_TYPE = ["int64", "uint64", "string", "float", "bool", "date", "datetime", "datetime_iso", "binary"]
CLI_BASE_TYPE = ["Integer", "String", "Float", "Timestamp", "Boolean", "Binary"]

# --cli-unfold-argument 模式下扁平 key 的最大点号段数（含数字下标段），超过则报错。
MAX_INPUT_DEPTH = 30

# 自引用截断点 / 超限输入的统一替代写法提示文案。
RECURSIVE_HINT_FILE_OPTION = (
    "Use --cli-input-json file://<path/to/request.json> to provide the entire "
    "request as a JSON file (the value must begin with 'file://'; raw JSON "
    "strings are not accepted; run with --generate-cli-skeleton to get a JSON "
    "template)."
)

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

HELPER_MAP = {
    "--profile": "specify a profile name",
    "--secretId": "specify a SecretId",
    "--secretKey": "specify a SecretKey",
    "--token": "temporary certificate token",
    "--role-arn": "specify a RoleArn",
    "--role-session-name": "specify a RoleSessionName",
    "--use-cvm-role": "use CVM Role to obtain the secret id and secret key",
    "--region": "identify the region to which the instance you want to work with belongs.",
    "--endpoint": "specify an access point domain name",
    "--detail": "see detailed help information",
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
    "--https-proxy": "specify a https proxy",
    "--warning": "Open the warning log",
    "--waiter": "Set param `expr`, `to`, `timeout` and `interval` to get the polling result."
                "`expr` is the inquiry expresion, `to` is the ending status"
                ".`timeout` and `interval` are optional params.",
    "--language": "specify an output language, valid choices: [zh-CN, en-US], default value: zh-CN",
    "--request-client": "specify a custom request client identifier, used to mark the client name "
                        "(format: ^[0-9a-zA-Z-_,.]+$, max length 128).",
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

    def get_usage(self):
        return "tccli [options] <service> [options] <action> [options] [options and parameters]"

    def get_options(self):
        return {
            "help": "show the tccli help info",
            "--version": "show the version of tccli"
        }

    def get_cli_option(self):
        return {
            "filter": {
                "help": HELPER_MAP['--filter'],
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
                "help": HELPER_MAP['--secretId'],
            },
            "secretKey": {
                "help": HELPER_MAP['--secretKey'],
            },
            "token": {
                "help": HELPER_MAP['--token'],
            },
            "role-arn": {
                "help": HELPER_MAP['--role-arn'],
            },
            "role-session-name": {
                "help": HELPER_MAP['--role-session-name'],
            },
            "use-cvm-role": {
                "help": HELPER_MAP['--use-cvm-role'],
                'action': 'store_true'
            },
            "version": {
                "help": "specify a DescribeRegions api version",
                "metavar": "version_name"
            },
            "detail": {
                "help": HELPER_MAP['--detail'],
                'action': 'store_true'
            },
            "profile": {
                "help": HELPER_MAP['--profile'],
                "metavar": "profile_name"
            },
            "region": {
                "help": HELPER_MAP['--region'],
                "metavar": "region_name"
            },
            "endpoint": {
                "help": HELPER_MAP['--endpoint'],
                "metavar": "endpoint_url"
            },
            "timeout": {
                "type": "int",
                "help": HELPER_MAP['--timeout'],
            },
            "generate-cli-skeleton": {
                'help': HELPER_MAP['--generate-cli-skeleton'],
                'nargs': '?',
                'const': 'input',
                'choices': ['input'],
            },
            'cli-input-json': {
                'help': HELPER_MAP['--cli-input-json'],
            },
            'cli-unfold-argument': {
                'help': HELPER_MAP['--cli-unfold-argument'],
                'action': 'store_true'
            },
            'https-proxy': {
                'help': HELPER_MAP['--https-proxy'],
            },
            'warning': {
                'help': HELPER_MAP['--warning'],
                'action': 'store_true'
            },
            'waiter': {
                'help': HELPER_MAP['--waiter'],
            },
            "language": {
                'help': HELPER_MAP['--language'],
                "choices": [
                    "zh-CN",
                    "en-US"
                ],
            },
            "request-client": {
                "help": HELPER_MAP['--request-client'],
                "metavar": "request_client",
            },
        }

    def _version_transform(self, version):
        return version[1:5] + "-" + version[5:7] + "-" + version[7:9]

    def get_available_services(self):
        services = copy.deepcopy(SERVICE_VERSIONS)
        for name, vers in plugin.import_plugins().items():
            if name not in services:
                services[name] = []
            for ver, spec in vers.items():
                api_ver = spec["metadata"]["apiVersion"]
                if api_ver not in services[name]:
                    services[name].append(api_ver)
        return services

    def get_service_default_version(self, service):
        args = sys.argv[1:]
        profile = os.environ.get("TCCLI_PROFILE", "default")
        if "--profile" in args:
            location = args.index("--profile") + 1
            if location < len(args):
                profile = args[location]
        conf_path = os.path.join(os.path.expanduser("~"), ".tccli")
        conf = {}
        if Utils.file_existed(conf_path, profile+".configure")[0]:
            conf = Utils.load_json_msg(os.path.join(conf_path, profile+".configure"))
        return conf.get(service, {}).get("version", self.get_available_services()[service][0])

    def get_service_model(self, service, version):
        services_path = self.get_services_path()
        version = "v" + version.replace('-', '')
        apis_path = os.path.join(services_path, service, version, "api.json")
        model = {
            "metadata": {},
            "actions": {},
            "objects": {},
        }
        if os.path.exists(apis_path):
            if six.PY2:
                with open(apis_path, 'r') as f:
                    model = json.load(f)
            else:
                with open(apis_path, 'r', encoding='utf-8') as f:
                    model = json.load(f)

        # merge plugins
        for plugin_name, vers in plugin.import_plugins().items():

            if plugin_name != service:
                continue

            for ver, spec in vers.items():

                # 2017-03-12 -> v20170312
                compact_ver = 'v' + ver.replace('-', '')

                if compact_ver != version:
                    continue

                model["metadata"].update(spec["metadata"])
                model["actions"].update(spec["actions"])
                model["objects"].update(spec["objects"])

        if not model:
            raise Exception("Not find service:%s version:%s model" % (service, version))

        return model

    def get_service_description(self, service, version):
        service_model = self.get_service_model(service, version)
        description = service_model["metadata"].get("api_brief", '')
        return description

    def get_service_usage(self, service):
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
            actions_info[action]["status"] = service_model["actions"][action].get("status", "online")
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

    def get_action_online_status(self, service, version, action):
        return self.get_actions_info(service, version)[action].get('status', 'online')

    def get_action_usage(self, service, action):
        return "tccli %s %s [--param...]" % (service, action)

    def get_action_options(self, service, action):
        HELPER_MAP["help"] = "show the tccli %s %s help info" % (service, action)
        HELPER_MAP["--version"] = "specify a %s api version" % action
        return HELPER_MAP

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

    def _get_param_info(self, param_model, object_model, visited=None):
        # visited 沿当前 DFS 路径记录已展开的复合类型名，命中即截断
        if visited is None:
            visited = frozenset()
        param_info = {}
        for para in param_model:
            member = para["member"]
            recursive_hit = member not in BASE_TYPE and member in visited
            if para["type"] == "list":
                if member not in BASE_TYPE:
                    if recursive_hit:
                        self._filling_param_info(
                            param_info, para, "list", [member])
                    else:
                        self._filling_param_info(
                            param_info, para, "list",
                            [self._get_param_info(
                                object_model[member]["members"], object_model,
                                visited | {member})])
                else:
                    self._filling_param_info(
                        param_info, para, "list", [member])
            else:
                if member not in BASE_TYPE:
                    if recursive_hit:
                        param_info = self._filling_param_info(
                            param_info, para, member, member)
                    else:
                        param_info = self._filling_param_info(
                            param_info, para, member,
                            self._get_param_info(
                                object_model[member]["members"], object_model,
                                visited | {member}))
                else:
                    self._filling_param_info(param_info, para, member, member)
        return param_info

    def get_param_info(self, service, version, action):
        service_model = self.get_service_model(service, version)
        param_model = service_model["objects"]
        return self._get_param_info(param_model[action + "Request"]["members"], param_model)

    def get_output_param_info(self, service, version, action):
        service_model = self.get_service_model(service, version)
        param_model = service_model["objects"]
        return self._get_param_info(param_model[action + "Response"]["members"], param_model)

    def _generate_param_skeleton(self, param_model, name, visited=None):
        # visited 沿路径记录已展开的复合类型名，命中即以字符串占位表示自引用
        if visited is None:
            visited = frozenset()
        param_skeleton = {}
        for para in param_model:
            member = para["member"]
            recursive_hit = member not in BASE_TYPE and member in visited
            if para["type"] == "list":
                if member not in BASE_TYPE:
                    if recursive_hit:
                        param_skeleton[para["name"]] = [
                            "<recursive: fill '%s' with a JSON object of type %s (self-referenced)>"
                            % (para["name"], member)]
                    else:
                        param_skeleton[para["name"]] = \
                            [self._generate_param_skeleton(
                                name[member]["members"], name,
                                visited | {member})]
                else:
                    param_skeleton[para["name"]] = [PARAM_TYPE_MAP[member]]
            else:
                if member not in BASE_TYPE:
                    if recursive_hit:
                        param_skeleton[para["name"]] = \
                            "<recursive: fill '%s' with a JSON object of type %s (self-referenced)>" \
                            % (para["name"], member)
                    else:
                        param_skeleton[para["name"]] = \
                            self._generate_param_skeleton(
                                name[member]["members"], name,
                                visited | {member})
                else:
                    param_skeleton[para["name"]] = PARAM_TYPE_MAP[member]
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

        return self._filling_unfold_param_info(all_param_list, service, version, action, object_model)

    def _add_array_item(self, param_list, profile):
        is_conf_exist, conf_path = Utils.file_existed(os.path.join(os.path.expanduser("~"), ".tccli"),
                                                      profile + ".configure")
        if is_conf_exist:
            array_count = Utils.load_json_msg(conf_path).get("_sys_param", {}).get("arrayCount", 10)
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

    def _recur_get_unfold_param_info(self, param_model, object_model, return_param_list, param_list,
                                     visited=None):
        for para in param_model:
            self._get_unfold_param_info(object_model, return_param_list, param_list, para, visited)
        if param_list.pop().isdigit():
            param_list.pop()

    def _get_unfold_param_info(self, object_model, return_param_list, param_list, para, visited=None):
        # visited 沿路径维护，识别自引用类型（如 AllocationRuleExpression.Children）
        if visited is None:
            visited = frozenset()
        param_list.append(para["name"])
        if para["type"] == "list" and para["member"] not in BASE_TYPE:
            param_list.append('0')
        member = para["member"]
        if member not in BASE_TYPE:
            if member in visited:
                tmp = copy.deepcopy(param_list)
                return_param_list.append(tmp)
                if param_list.pop().isdigit():
                    param_list.pop()
                return
            self._recur_get_unfold_param_info(object_model[member]["members"],
                                              object_model, return_param_list, param_list,
                                              visited | {member})
        else:
            tmp = copy.deepcopy(param_list)
            return_param_list.append(tmp)

            if param_list.pop().isdigit():
                param_list.pop()

    def _filling_unfold_param_info(self, param_list, service, version, action, object_model=None):
        unfold_param = {}
        param_info = self.get_param_info(service, version, action)
        for param in param_list:
            unfold_param[".".join(param)] = {}

            tmp_param = [item for item in param if not item.isdigit()]
            res = param_info[tmp_param[0]]

            param_type = res["type"]
            type_name = res["type_name"]
            required = res.get("required")
            document = res["document"]
            recursive_truncated = False
            recursive_type = None

            for idx, item in enumerate(tmp_param[1:]):
                # 命中自引用截断：当前 res 的 members 是占位字符串（类型名）而非 dict
                if res["type"] == "Array":
                    members_container = res["members"][0]
                else:
                    members_container = res["members"]
                if not isinstance(members_container, dict) or item not in members_container:
                    # 该 leaf 是被环检测截断的占位项，不再向下钻取
                    recursive_truncated = True
                    recursive_type = members_container if isinstance(members_container, str) \
                        else (res.get("type_name") or "")
                    break
                res = members_container[item]

                # ?? seriously ??
                if required == "Required" and res["required"] == "Optional":
                    required = "Optional"

                if idx == len(tmp_param) - 2:
                    param_type = res["type"]
                    type_name = res["type_name"] if res["type"] == "Array" \
                        else res["type_name"]
                    document = res["document"]
                    break

            # 二次判定：路径走完后，若该 leaf 自身是被环检测截断的复合类型（members 为占位）
            if not recursive_truncated:
                final_members = res.get("members")
                if isinstance(final_members, list) and len(final_members) == 1 \
                        and isinstance(final_members[0], str) \
                        and final_members[0] not in BASE_TYPE \
                        and final_members[0] not in CLI_BASE_TYPE:
                    recursive_truncated = True
                    recursive_type = final_members[0]
                elif isinstance(final_members, str) \
                        and final_members not in BASE_TYPE \
                        and final_members not in CLI_BASE_TYPE:
                    recursive_truncated = True
                    recursive_type = final_members

            if len([item for item in param if item.isdigit() and int(item) > 0]) > 0:
                required = "Optional"

            if recursive_truncated:
                # 自引用截断点统一标记为 Object，提示用户用 JSON 整体传入
                param_type = "Object"
                type_name = recursive_type or "Object"
                required = "Optional"
                document = (document or "") + \
                    ("\nNote: this field is a self-referencing type %s. "
                     "--cli-unfold-argument only expands the first level. "
                     "For deeper nesting:\n  %s"
                     % (recursive_type or "", RECURSIVE_HINT_FILE_OPTION))

            unfold_param[".".join(param)]["type"] = param_type
            unfold_param[".".join(param)]["type_name"] = type_name
            unfold_param[".".join(param)]["required"] = required
            unfold_param[".".join(param)]["document"] = document
            # 稳定字段：供上层（如 command.py）在客户深入自引用路径报 Unknown options 时
            # 给出针对性提示，无需依赖 document 文案
            if recursive_truncated:
                unfold_param[".".join(param)]["recursive_truncated"] = True
                unfold_param[".".join(param)]["recursive_type"] = recursive_type or ""
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
