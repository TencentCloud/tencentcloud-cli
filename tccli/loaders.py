
import os
import json
from tccli import __version__
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
            }
        }

    def _version_transform(self, version):
        return version[1:5] + "-" + version[5:7] + "-" + version[7:9]

    def get_available_services(self):
        services = {}
        services_path = self.get_services_path()
        for module in sorted(os.listdir(services_path)):
            if module.startswith("_"):
                continue
            module_path = os.path.join(services_path, module)
            if not os.path.isdir(module_path):
                continue
            services[module] = []
            for version in sorted(os.listdir(module_path), reverse=True):
                version_path = os.path.join(module_path, version)
                if os.path.isdir(version_path) and version.startswith('v'):
                    version = self._version_transform(version)
                    services[module].append(version)
        return services

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

    def get_service_all_action_param(self, service):
        version_actions = self.get_service_all_version_actions(service)
        version_action_params = {}
        for version in version_actions:
            version_action_params[version] = {}
            for action in version_actions[version]:
                params = self.get_param_info(service, version, action).keys()
                version_action_params[version][action] = params
        action_params = {}
        for version in version_action_params:
            for action in version_action_params[version]:
                if action in action_params:
                    action_params[action] = list(set(action_params[action] +
                                                     version_action_params[version][action]))
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
                                "follows the format provided by --generate-cli-skeleton. "
        }

    def _filling_param_info(self, param_info, para, param_type, member):
        param_info[para["name"]] = {}
        param_info[para["name"]]["document"] = para["document"]
        param_info[para["name"]]["required"] = "Required" if para["required"] else "Optional"
        param_info[para["name"]]["type_name"] = para["member"]
        param_info[para["name"]]["type"] = PARAM_TYPE_MAP.get(param_type, param_type)
        param_info[para["name"]]["members"] = member
        return param_info

    def _get_param_info(self, param_model, object_model):
        param_info = {}
        for para in param_model:
            if para["type"] == "list":
                if para["member"] not in BASE_TYPE:
                    param_info = self._filling_param_info(
                        param_info, para, "list",
                        [self._recur_get_param_info(object_model, para["member"])])
                else:
                    param_info = self._filling_param_info(
                        param_info, para, "list",
                        [para["member"]])
            else:
                if para["member"] not in BASE_TYPE:
                    param_info = self._filling_param_info(
                        param_info, para, para["member"],
                        self._recur_get_param_info(object_model, para["member"]))
                else:
                    param_info = self._filling_param_info(param_info, para, para["member"], para["member"])
        return param_info

    def _recur_get_param_info(self, param_model, name):
        return self._get_param_info(param_model[name]["members"], param_model)

    def get_param_info(self, service, version, action):
        service_model = self.get_service_model(service, version)
        param_model = service_model["objects"]
        return self._get_param_info(param_model[action + "Request"]["members"], param_model)

    def _generate_param_skeleton(self, param_model, name):
        param_skeleton = {}
        for para in param_model:
            if para["type"] == "list":
                if para["member"] not in BASE_TYPE:
                    param_skeleton[para["name"]] = [self._recur_generate_param_skeleton(name, para["member"])]
                else:
                    param_skeleton[para["name"]] = [PARAM_TYPE_MAP[para["member"]]]
            else:
                if para["member"] not in BASE_TYPE:
                    param_skeleton[para["name"]] = self._recur_generate_param_skeleton(name, para["member"])
                else:
                    param_skeleton[para["name"]] = PARAM_TYPE_MAP[para["member"]]
        return param_skeleton

    def _recur_generate_param_skeleton(self, param_model, name):
        return self._generate_param_skeleton(param_model[name]["members"], param_model)

    def generate_param_skeleton(self, service, version, action):
        service_model = self.get_service_model(service, version)
        param_model = service_model["objects"]
        return self._generate_param_skeleton(param_model[action + "Request"]["members"], param_model)

