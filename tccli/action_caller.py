# -*- coding:utf-8 -*-
import json
import os
import os.path as path
import sys
import time

import six
from jmespath import search
from tencentcloud.common import credential
from tencentcloud.common.common_client import CommonClient
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile

import tccli.format_output as format_output
import tccli.options_define as options_define
from tccli import __version__
from tccli.exceptions import ConfigurationError, ClientError, ParamError
from tccli.loaders import Loader, BASE_TYPE
from tccli.utils import Utils


class GenericActionCaller(object):
    _ACTION_TRAITS = {
        ("cls", "v20201016", "UploadLog"): {
            "request_mode": "octet-stream",
            "header_prefix": "X-CLS-",
            "header_fields": ("TopicId", "HashKey", "CompressType"),
        },
    }

    def __init__(self, module, action):
        self._module = module
        self._action = action
        self._avail_vers = []

    def __call__(self, args, parsed_globals):
        g_param = self.parse_global_arg(parsed_globals)
        traits = self._get_action_traits(g_param)
        client = self._create_client(g_param)
        if traits and traits["request_mode"] == "octet-stream":
            self._call_octet_stream(args, g_param, client, traits)
        else:
            self._call_json(args, g_param, client)

    def _get_action_traits(self, g_param):
        return self._ACTION_TRAITS.get((self._module.lower(), g_param[options_define.Version], self._action))

    def available_versions(self):
        if not self._avail_vers:
            svc_path = os.path.join(path.dirname(path.abspath(__file__)), 'services', self._module)
            try:
                dirs = os.listdir(svc_path)
            except OSError:
                raise ConfigurationError("service '%s' not found" % self._module)
            self._avail_vers = [d for d in dirs if d[0] == "v" and os.path.isdir(path.join(svc_path, d))]

        return self._avail_vers

    @staticmethod
    def convert_version_str(ver):
        return ver[1:5] + "-" + ver[5:7] + "-" + ver[7:9]

    def _create_client(self, g_param):
        if g_param[options_define.UseCVMRole.replace('-', '_')]:
            cred = credential.CVMRoleCredential()
        elif g_param[options_define.RoleArn.replace('-', '_')] and g_param[
            options_define.RoleSessionName.replace('-', '_')]:
            cred = credential.STSAssumeRoleCredential(
                g_param[options_define.SecretId], g_param[options_define.SecretKey],
                g_param[options_define.RoleArn.replace('-', '_')],
                g_param[options_define.RoleSessionName.replace('-', '_')], endpoint=g_param["sts_cred_endpoint"]
            )
        elif os.getenv(options_define.ENV_TKE_REGION) and os.getenv(options_define.ENV_TKE_PROVIDER_ID) and os.getenv(
                options_define.ENV_TKE_WEB_IDENTITY_TOKEN_FILE) and os.getenv(options_define.ENV_TKE_ROLE_ARN):
            cred = credential.DefaultTkeOIDCRoleArnProvider().get_credentials()
        else:
            cred = credential.Credential(
                g_param[options_define.SecretId], g_param[options_define.SecretKey], g_param[options_define.Token]
            )
        http_profile = HttpProfile(
            reqTimeout=60 if g_param[options_define.Timeout] is None else int(g_param[options_define.Timeout]),
            reqMethod="POST",
            endpoint=g_param[options_define.Endpoint],
            proxy=g_param[options_define.HttpsProxy.replace('-', '_')]
        )
        cpf = ClientProfile(httpProfile=http_profile, signMethod="TC3-HMAC-SHA256")
        cpf.request_client = "_CLI_" + __version__
        request_client = g_param[options_define.RequestClient.replace('-', '_')]
        if request_client:
            if "\r" in request_client or "\n" in request_client:
                raise ParamError("`--request-client` must not contain CR or LF characters.")
            cpf.request_client += "; " + request_client
        if g_param[options_define.Language]:
            cpf.language = g_param[options_define.Language]
        version = self.convert_version_str(g_param[options_define.Version])
        service_model = Loader().get_service_model(self._module, version)
        service = service_model["metadata"].get("serviceShortName") or self._module
        region = g_param[options_define.Region]
        client = CommonClient(service, version, cred, region, cpf)
        client._sdkVersion += ("_CLI_" + __version__)
        return client

    def _call_json(self, args, g_param, client):
        start_time = time.time()
        while True:
            raw = client.call_json(self._action, args)
            json_obj = raw.get("Response", raw) if isinstance(raw, dict) else raw
            json_obj = self._filter_response(json_obj, g_param[options_define.Version])

            if not g_param[options_define.Waiter] or search(g_param['OptionsDefine.WaiterInfo']['expr'], json_obj) == \
                    g_param['OptionsDefine.WaiterInfo']['to']:
                break

            cur_time = time.time()
            if cur_time - start_time >= g_param['OptionsDefine.WaiterInfo']['timeout']:
                raise ClientError('Request timeout, wait `%s` to `%s` timeout, last request is %s' %
                                  (g_param['OptionsDefine.WaiterInfo']['expr'],
                                   g_param['OptionsDefine.WaiterInfo']['to'],
                                   search(g_param['OptionsDefine.WaiterInfo']['expr'], json_obj)))
            else:
                print('Inquiry result is %s.' % search(g_param['OptionsDefine.WaiterInfo']['expr'], json_obj))
            time.sleep(g_param['OptionsDefine.WaiterInfo']['interval'])

        format_output.output("action", json_obj, g_param[options_define.Output], g_param[options_define.Filter])

    def _call_octet_stream(self, args, g_param, client, traits):
        if g_param[options_define.Waiter]:
            raise ParamError("`--waiter` is not supported for UploadLog to avoid duplicate log uploads.")

        headers = self._build_octet_stream_headers(args, traits)
        body = self._read_binary_stdin()
        raw = client.call_octet_stream(self._action, headers, body)
        json_obj = raw.get("Response", raw) if isinstance(raw, dict) else raw
        json_obj = self._filter_response(json_obj, g_param[options_define.Version])
        format_output.output("action", json_obj, g_param[options_define.Output], g_param[options_define.Filter])

    @staticmethod
    def _read_binary_stdin():
        if sys.stdin.isatty():
            raise ParamError("Missing required input, you can use `< /path/to/file` to input your binary file.")
        if six.PY2:
            return sys.stdin.read()
        return sys.stdin.buffer.read()

    @staticmethod
    def _build_octet_stream_headers(args, traits):
        if not isinstance(args, dict):
            raise ParamError("UploadLog request parameters must be a JSON object.")

        headers = {}
        for field in traits["header_fields"]:
            value = args.get(field)
            if value is None:
                continue
            if not isinstance(value, six.string_types):
                raise ParamError("UploadLog parameter `%s` must be a string." % field)
            if "\r" in value or "\n" in value:
                raise ParamError("UploadLog parameter `%s` must not contain CR or LF characters." % field)
            headers[traits["header_prefix"] + field] = value
        return headers

    def parse_global_arg(self, parsed_globals):
        g_param = parsed_globals
        cvm_role_flag = True
        for param in parsed_globals.keys():
            if param in [options_define.SecretKey, options_define.SecretId, options_define.RoleArn,
                         options_define.RoleSessionName]:
                if parsed_globals[param] is not None:
                    cvm_role_flag = False
                    break
        is_exist_profile = True
        if not parsed_globals["profile"]:
            is_exist_profile = False
            g_param["profile"] = os.environ.get("TCCLI_PROFILE", "default")

        configure_path = os.path.join(os.path.expanduser("~"), ".tccli")
        is_conf_exist, conf_path = Utils.file_existed(configure_path, g_param["profile"] + ".configure")
        is_cred_exist, cred_path = Utils.file_existed(configure_path, g_param["profile"] + ".credential")

        conf = {}
        cred = {}

        if is_conf_exist:
            conf = Utils.load_json_msg(conf_path)
        if is_cred_exist:
            cred = Utils.load_json_msg(cred_path)

        if not (isinstance(conf, dict) and isinstance(cred, dict)):
            raise ConfigurationError(
                "file: %s or %s is not json format"
                % (g_param["profile"] + ".configure", g_param["profile"] + ".credential"))

        if options_define.Token not in cred:
            cred[options_define.Token] = None

        if not is_exist_profile:
            if os.environ.get(options_define.ENV_SECRET_ID) and os.environ.get(options_define.ENV_SECRET_KEY):
                cred[options_define.SecretId] = os.environ.get(options_define.ENV_SECRET_ID)
                cred[options_define.SecretKey] = os.environ.get(options_define.ENV_SECRET_KEY)
                cred[options_define.Token] = os.environ.get(options_define.ENV_TOKEN)
                cvm_role_flag = False

            if os.environ.get(options_define.ENV_REGION):
                conf[options_define.SysParam][options_define.Region] = os.environ.get(options_define.ENV_REGION)

            if os.environ.get(options_define.ENV_ROLE_ARN) and os.environ.get(options_define.ENV_ROLE_SESSION_NAME):
                cred[options_define.RoleArn] = os.environ.get(options_define.ENV_ROLE_ARN)
                cred[options_define.RoleSessionName] = os.environ.get(options_define.ENV_ROLE_SESSION_NAME)
                cvm_role_flag = False

        if cvm_role_flag:
            if "type" in cred and cred["type"] == "cvm-role":
                g_param[options_define.UseCVMRole.replace('-', '_')] = True

        for param in g_param.keys():
            if g_param[param] is None:
                if param in [options_define.SecretKey, options_define.SecretId, options_define.Token]:
                    if param in cred:
                        g_param[param] = cred[param]
                    elif not (g_param[options_define.UseCVMRole.replace('-', '_')]
                              or os.getenv(options_define.ENV_TKE_ROLE_ARN)):
                        raise ConfigurationError("%s is invalid" % param)
                elif param in [options_define.Region, options_define.Output, options_define.Language]:
                    if param in conf[options_define.SysParam]:
                        g_param[param] = conf[options_define.SysParam][param]
                    elif param != options_define.Language:
                        raise ConfigurationError("%s is invalid" % param)
                elif param == options_define.RequestClient.replace('-', '_'):
                    if options_define.RequestClient in conf[options_define.SysParam]:
                        g_param[param] = conf[options_define.SysParam][options_define.RequestClient]
                elif param.replace('_', '-') in [options_define.RoleArn, options_define.RoleSessionName]:
                    if param.replace('_', '-') in cred:
                        g_param[param] = cred[param.replace('_', '-')]

        try:
            if g_param[options_define.ServiceVersion]:
                g_param[options_define.Version] = "v" + g_param[options_define.ServiceVersion].replace('-', '')
            else:
                version = conf[self._module][options_define.Version]
                g_param[options_define.Version] = "v" + version.replace('-', '')

            if g_param[options_define.Endpoint] is None:
                g_param[options_define.Endpoint] = conf[self._module][options_define.Endpoint]
            g_param["sts_cred_endpoint"] = conf.get("sts", {}).get("endpoint")
        except Exception as err:
            raise ConfigurationError("config file:%s error, %s" % (conf_path, str(err)))

        if g_param[options_define.Version] not in self.available_versions():
            raise Exception("available versions: %s" % " ".join(self.available_versions()))

        if g_param[options_define.Waiter]:
            try:
                param = json.loads(g_param[options_define.Waiter])
            except ValueError as e:
                raise Exception('`--waiter` must be a valid JSON string: %s' % str(e))
            if 'expr' not in param:
                raise Exception('`expr` in `--waiter` must be defined')
            if 'to' not in param:
                raise Exception('`to` in `--waiter` must be defined')
            if 'timeout' not in param:
                if 'waiter' in conf and 'timeout' in conf['waiter']:
                    param['timeout'] = conf['waiter']['timeout']
                else:
                    param['timeout'] = 180
            if 'interval' not in param:
                if 'waiter' in conf and 'interval' in conf['waiter']:
                    param['interval'] = conf['waiter']['interval']
                else:
                    param['interval'] = 5
            param['interval'] = min(param['interval'], param['timeout'])
            g_param['OptionsDefine.WaiterInfo'] = param

        if six.PY2:
            for key, value in g_param.items():
                if isinstance(value, six.text_type):
                    g_param[key] = value.encode('utf-8')
        return g_param

    def _filter_response(self, data, version):
        """加载 api.json 中 ActionResponse 的 schema，对响应 dict 做白名单字段投影"""
        try:
            loader = Loader()
            service_model = loader.get_service_model(self._module, self.convert_version_str(version))
            objects = service_model["objects"]
            resp_name = self._action + "Response"
            if resp_name not in objects:
                return data
            return self._filter_by_schema(data, objects[resp_name]["members"], objects)
        except Exception:
            return data

    def _filter_by_schema(self, data, members, objects):
        """按 schema members 递归投影 dict，丢弃未定义字段，复杂类型递归处理"""
        if not isinstance(data, dict):
            return data
        result = {}
        for para in members:
            name = para["name"]
            if name not in data:
                continue
            value = data[name]
            if para["type"] == "list":
                if para["member"] not in BASE_TYPE:
                    if isinstance(value, list):
                        sub_members = objects[para["member"]]["members"]
                        result[name] = [self._filter_by_schema(item, sub_members, objects) for item in value]
                    else:
                        result[name] = value
                else:
                    result[name] = value
            else:
                if para["member"] not in BASE_TYPE:
                    sub_members = objects[para["member"]]["members"]
                    result[name] = self._filter_by_schema(value, sub_members, objects)
                else:
                    result[name] = value
        return result
