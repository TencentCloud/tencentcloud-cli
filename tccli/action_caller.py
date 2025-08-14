# -*- coding:utf-8 -*-
import os
import os.path as path
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
from tccli.exceptions import ConfigurationError, ClientError
from tccli.utils import Utils


class GenericActionCaller(object):
    def __init__(self, module, action):
        self._module = module
        self._action = action
        self._avail_vers = []

    def __call__(self, args, parsed_globals):
        self._call_json(args, parsed_globals)

    def available_versions(self):
        if not self._avail_vers:
            svc_path = os.path.join(path.dirname(path.abspath(__file__)), 'services', self._module)
            dirs = os.listdir(svc_path)
            self._avail_vers = [d for d in dirs if d[0] == "v" and os.path.isdir(path.join(svc_path, d))]

        return self._avail_vers

    @staticmethod
    def convert_version_str(ver):
        return ver[1:5] + "-" + ver[5:7] + "-" + ver[7:9]

    def _call_json(self, args, parsed_globals):
        g_param = self.parse_global_arg(parsed_globals)

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
        cpf = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
        if g_param[options_define.Language]:
            cpf.language = g_param[options_define.Language]
        version = self.convert_version_str(g_param[options_define.Version])
        region = g_param[options_define.Region]
        client = CommonClient(self._module, version, cred, region, cpf)
        client._sdkVersion += ("_CLI_" + __version__)

        start_time = time.time()
        while True:
            json_obj = client.call_json(self._action, args)

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
            param = eval(g_param[options_define.Waiter])
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
