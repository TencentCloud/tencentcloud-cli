# -*- coding: utf-8 -*-
import os
import sys
import six
import json
import tccli.options_define as OptionsDefine
import tccli.format_output as FormatOutput
from tccli import __version__
from tccli.utils import Utils
from tccli.exceptions import ConfigurationError, ClientError, ParamError
from tencentcloud.common import credential
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.sms.v20210111 import sms_client as sms_client_v20210111
from tencentcloud.sms.v20210111 import models as models_v20210111
from tencentcloud.sms.v20190711 import sms_client as sms_client_v20190711
from tencentcloud.sms.v20190711 import models as models_v20190711

from jmespath import search
import time

def doModifySmsSign(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')], endpoint=g_param["sts_cred_endpoint"]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION)             and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID)             and os.getenv(OptionsDefine.ENV_TKE_WEB_IDENTITY_TOKEN_FILE)             and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
        cred = credential.DefaultTkeOIDCRoleArnProvider().get_credentials()
    else:
        cred = credential.Credential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
        )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint],
        proxy=g_param[OptionsDefine.HttpsProxy.replace('-', '_')]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    if g_param[OptionsDefine.Language]:
        profile.language = g_param[OptionsDefine.Language]
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.SmsClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifySmsSignRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.ModifySmsSign(model)
        result = rsp.to_json_string()
        try:
            json_obj = json.loads(result)
        except TypeError as e:
            json_obj = json.loads(result.decode('utf-8'))  # python3.3
        if not g_param[OptionsDefine.Waiter] or search(g_param['OptionsDefine.WaiterInfo']['expr'], json_obj) == g_param['OptionsDefine.WaiterInfo']['to']:
            break
        cur_time = time.time()
        if cur_time - start_time >= g_param['OptionsDefine.WaiterInfo']['timeout']:
            raise ClientError('Request timeout, wait `%s` to `%s` timeout, last request is %s' %
            (g_param['OptionsDefine.WaiterInfo']['expr'], g_param['OptionsDefine.WaiterInfo']['to'],
            search(g_param['OptionsDefine.WaiterInfo']['expr'], json_obj)))
        else:
            print('Inquiry result is %s.' % search(g_param['OptionsDefine.WaiterInfo']['expr'], json_obj))
        time.sleep(g_param['OptionsDefine.WaiterInfo']['interval'])
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doAddSmsSign(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')], endpoint=g_param["sts_cred_endpoint"]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION)             and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID)             and os.getenv(OptionsDefine.ENV_TKE_WEB_IDENTITY_TOKEN_FILE)             and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
        cred = credential.DefaultTkeOIDCRoleArnProvider().get_credentials()
    else:
        cred = credential.Credential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
        )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint],
        proxy=g_param[OptionsDefine.HttpsProxy.replace('-', '_')]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    if g_param[OptionsDefine.Language]:
        profile.language = g_param[OptionsDefine.Language]
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.SmsClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.AddSmsSignRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.AddSmsSign(model)
        result = rsp.to_json_string()
        try:
            json_obj = json.loads(result)
        except TypeError as e:
            json_obj = json.loads(result.decode('utf-8'))  # python3.3
        if not g_param[OptionsDefine.Waiter] or search(g_param['OptionsDefine.WaiterInfo']['expr'], json_obj) == g_param['OptionsDefine.WaiterInfo']['to']:
            break
        cur_time = time.time()
        if cur_time - start_time >= g_param['OptionsDefine.WaiterInfo']['timeout']:
            raise ClientError('Request timeout, wait `%s` to `%s` timeout, last request is %s' %
            (g_param['OptionsDefine.WaiterInfo']['expr'], g_param['OptionsDefine.WaiterInfo']['to'],
            search(g_param['OptionsDefine.WaiterInfo']['expr'], json_obj)))
        else:
            print('Inquiry result is %s.' % search(g_param['OptionsDefine.WaiterInfo']['expr'], json_obj))
        time.sleep(g_param['OptionsDefine.WaiterInfo']['interval'])
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doPullSmsSendStatus(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')], endpoint=g_param["sts_cred_endpoint"]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION)             and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID)             and os.getenv(OptionsDefine.ENV_TKE_WEB_IDENTITY_TOKEN_FILE)             and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
        cred = credential.DefaultTkeOIDCRoleArnProvider().get_credentials()
    else:
        cred = credential.Credential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
        )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint],
        proxy=g_param[OptionsDefine.HttpsProxy.replace('-', '_')]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    if g_param[OptionsDefine.Language]:
        profile.language = g_param[OptionsDefine.Language]
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.SmsClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.PullSmsSendStatusRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.PullSmsSendStatus(model)
        result = rsp.to_json_string()
        try:
            json_obj = json.loads(result)
        except TypeError as e:
            json_obj = json.loads(result.decode('utf-8'))  # python3.3
        if not g_param[OptionsDefine.Waiter] or search(g_param['OptionsDefine.WaiterInfo']['expr'], json_obj) == g_param['OptionsDefine.WaiterInfo']['to']:
            break
        cur_time = time.time()
        if cur_time - start_time >= g_param['OptionsDefine.WaiterInfo']['timeout']:
            raise ClientError('Request timeout, wait `%s` to `%s` timeout, last request is %s' %
            (g_param['OptionsDefine.WaiterInfo']['expr'], g_param['OptionsDefine.WaiterInfo']['to'],
            search(g_param['OptionsDefine.WaiterInfo']['expr'], json_obj)))
        else:
            print('Inquiry result is %s.' % search(g_param['OptionsDefine.WaiterInfo']['expr'], json_obj))
        time.sleep(g_param['OptionsDefine.WaiterInfo']['interval'])
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doSendSms(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')], endpoint=g_param["sts_cred_endpoint"]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION)             and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID)             and os.getenv(OptionsDefine.ENV_TKE_WEB_IDENTITY_TOKEN_FILE)             and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
        cred = credential.DefaultTkeOIDCRoleArnProvider().get_credentials()
    else:
        cred = credential.Credential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
        )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint],
        proxy=g_param[OptionsDefine.HttpsProxy.replace('-', '_')]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    if g_param[OptionsDefine.Language]:
        profile.language = g_param[OptionsDefine.Language]
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.SmsClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.SendSmsRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.SendSms(model)
        result = rsp.to_json_string()
        try:
            json_obj = json.loads(result)
        except TypeError as e:
            json_obj = json.loads(result.decode('utf-8'))  # python3.3
        if not g_param[OptionsDefine.Waiter] or search(g_param['OptionsDefine.WaiterInfo']['expr'], json_obj) == g_param['OptionsDefine.WaiterInfo']['to']:
            break
        cur_time = time.time()
        if cur_time - start_time >= g_param['OptionsDefine.WaiterInfo']['timeout']:
            raise ClientError('Request timeout, wait `%s` to `%s` timeout, last request is %s' %
            (g_param['OptionsDefine.WaiterInfo']['expr'], g_param['OptionsDefine.WaiterInfo']['to'],
            search(g_param['OptionsDefine.WaiterInfo']['expr'], json_obj)))
        else:
            print('Inquiry result is %s.' % search(g_param['OptionsDefine.WaiterInfo']['expr'], json_obj))
        time.sleep(g_param['OptionsDefine.WaiterInfo']['interval'])
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteSmsTemplate(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')], endpoint=g_param["sts_cred_endpoint"]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION)             and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID)             and os.getenv(OptionsDefine.ENV_TKE_WEB_IDENTITY_TOKEN_FILE)             and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
        cred = credential.DefaultTkeOIDCRoleArnProvider().get_credentials()
    else:
        cred = credential.Credential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
        )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint],
        proxy=g_param[OptionsDefine.HttpsProxy.replace('-', '_')]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    if g_param[OptionsDefine.Language]:
        profile.language = g_param[OptionsDefine.Language]
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.SmsClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteSmsTemplateRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.DeleteSmsTemplate(model)
        result = rsp.to_json_string()
        try:
            json_obj = json.loads(result)
        except TypeError as e:
            json_obj = json.loads(result.decode('utf-8'))  # python3.3
        if not g_param[OptionsDefine.Waiter] or search(g_param['OptionsDefine.WaiterInfo']['expr'], json_obj) == g_param['OptionsDefine.WaiterInfo']['to']:
            break
        cur_time = time.time()
        if cur_time - start_time >= g_param['OptionsDefine.WaiterInfo']['timeout']:
            raise ClientError('Request timeout, wait `%s` to `%s` timeout, last request is %s' %
            (g_param['OptionsDefine.WaiterInfo']['expr'], g_param['OptionsDefine.WaiterInfo']['to'],
            search(g_param['OptionsDefine.WaiterInfo']['expr'], json_obj)))
        else:
            print('Inquiry result is %s.' % search(g_param['OptionsDefine.WaiterInfo']['expr'], json_obj))
        time.sleep(g_param['OptionsDefine.WaiterInfo']['interval'])
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doSmsPackagesStatistics(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')], endpoint=g_param["sts_cred_endpoint"]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION)             and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID)             and os.getenv(OptionsDefine.ENV_TKE_WEB_IDENTITY_TOKEN_FILE)             and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
        cred = credential.DefaultTkeOIDCRoleArnProvider().get_credentials()
    else:
        cred = credential.Credential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
        )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint],
        proxy=g_param[OptionsDefine.HttpsProxy.replace('-', '_')]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    if g_param[OptionsDefine.Language]:
        profile.language = g_param[OptionsDefine.Language]
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.SmsClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.SmsPackagesStatisticsRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.SmsPackagesStatistics(model)
        result = rsp.to_json_string()
        try:
            json_obj = json.loads(result)
        except TypeError as e:
            json_obj = json.loads(result.decode('utf-8'))  # python3.3
        if not g_param[OptionsDefine.Waiter] or search(g_param['OptionsDefine.WaiterInfo']['expr'], json_obj) == g_param['OptionsDefine.WaiterInfo']['to']:
            break
        cur_time = time.time()
        if cur_time - start_time >= g_param['OptionsDefine.WaiterInfo']['timeout']:
            raise ClientError('Request timeout, wait `%s` to `%s` timeout, last request is %s' %
            (g_param['OptionsDefine.WaiterInfo']['expr'], g_param['OptionsDefine.WaiterInfo']['to'],
            search(g_param['OptionsDefine.WaiterInfo']['expr'], json_obj)))
        else:
            print('Inquiry result is %s.' % search(g_param['OptionsDefine.WaiterInfo']['expr'], json_obj))
        time.sleep(g_param['OptionsDefine.WaiterInfo']['interval'])
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doSendStatusStatistics(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')], endpoint=g_param["sts_cred_endpoint"]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION)             and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID)             and os.getenv(OptionsDefine.ENV_TKE_WEB_IDENTITY_TOKEN_FILE)             and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
        cred = credential.DefaultTkeOIDCRoleArnProvider().get_credentials()
    else:
        cred = credential.Credential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
        )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint],
        proxy=g_param[OptionsDefine.HttpsProxy.replace('-', '_')]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    if g_param[OptionsDefine.Language]:
        profile.language = g_param[OptionsDefine.Language]
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.SmsClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.SendStatusStatisticsRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.SendStatusStatistics(model)
        result = rsp.to_json_string()
        try:
            json_obj = json.loads(result)
        except TypeError as e:
            json_obj = json.loads(result.decode('utf-8'))  # python3.3
        if not g_param[OptionsDefine.Waiter] or search(g_param['OptionsDefine.WaiterInfo']['expr'], json_obj) == g_param['OptionsDefine.WaiterInfo']['to']:
            break
        cur_time = time.time()
        if cur_time - start_time >= g_param['OptionsDefine.WaiterInfo']['timeout']:
            raise ClientError('Request timeout, wait `%s` to `%s` timeout, last request is %s' %
            (g_param['OptionsDefine.WaiterInfo']['expr'], g_param['OptionsDefine.WaiterInfo']['to'],
            search(g_param['OptionsDefine.WaiterInfo']['expr'], json_obj)))
        else:
            print('Inquiry result is %s.' % search(g_param['OptionsDefine.WaiterInfo']['expr'], json_obj))
        time.sleep(g_param['OptionsDefine.WaiterInfo']['interval'])
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCallbackStatusStatistics(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')], endpoint=g_param["sts_cred_endpoint"]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION)             and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID)             and os.getenv(OptionsDefine.ENV_TKE_WEB_IDENTITY_TOKEN_FILE)             and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
        cred = credential.DefaultTkeOIDCRoleArnProvider().get_credentials()
    else:
        cred = credential.Credential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
        )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint],
        proxy=g_param[OptionsDefine.HttpsProxy.replace('-', '_')]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    if g_param[OptionsDefine.Language]:
        profile.language = g_param[OptionsDefine.Language]
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.SmsClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CallbackStatusStatisticsRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.CallbackStatusStatistics(model)
        result = rsp.to_json_string()
        try:
            json_obj = json.loads(result)
        except TypeError as e:
            json_obj = json.loads(result.decode('utf-8'))  # python3.3
        if not g_param[OptionsDefine.Waiter] or search(g_param['OptionsDefine.WaiterInfo']['expr'], json_obj) == g_param['OptionsDefine.WaiterInfo']['to']:
            break
        cur_time = time.time()
        if cur_time - start_time >= g_param['OptionsDefine.WaiterInfo']['timeout']:
            raise ClientError('Request timeout, wait `%s` to `%s` timeout, last request is %s' %
            (g_param['OptionsDefine.WaiterInfo']['expr'], g_param['OptionsDefine.WaiterInfo']['to'],
            search(g_param['OptionsDefine.WaiterInfo']['expr'], json_obj)))
        else:
            print('Inquiry result is %s.' % search(g_param['OptionsDefine.WaiterInfo']['expr'], json_obj))
        time.sleep(g_param['OptionsDefine.WaiterInfo']['interval'])
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeSmsTemplateList(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')], endpoint=g_param["sts_cred_endpoint"]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION)             and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID)             and os.getenv(OptionsDefine.ENV_TKE_WEB_IDENTITY_TOKEN_FILE)             and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
        cred = credential.DefaultTkeOIDCRoleArnProvider().get_credentials()
    else:
        cred = credential.Credential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
        )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint],
        proxy=g_param[OptionsDefine.HttpsProxy.replace('-', '_')]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    if g_param[OptionsDefine.Language]:
        profile.language = g_param[OptionsDefine.Language]
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.SmsClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeSmsTemplateListRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.DescribeSmsTemplateList(model)
        result = rsp.to_json_string()
        try:
            json_obj = json.loads(result)
        except TypeError as e:
            json_obj = json.loads(result.decode('utf-8'))  # python3.3
        if not g_param[OptionsDefine.Waiter] or search(g_param['OptionsDefine.WaiterInfo']['expr'], json_obj) == g_param['OptionsDefine.WaiterInfo']['to']:
            break
        cur_time = time.time()
        if cur_time - start_time >= g_param['OptionsDefine.WaiterInfo']['timeout']:
            raise ClientError('Request timeout, wait `%s` to `%s` timeout, last request is %s' %
            (g_param['OptionsDefine.WaiterInfo']['expr'], g_param['OptionsDefine.WaiterInfo']['to'],
            search(g_param['OptionsDefine.WaiterInfo']['expr'], json_obj)))
        else:
            print('Inquiry result is %s.' % search(g_param['OptionsDefine.WaiterInfo']['expr'], json_obj))
        time.sleep(g_param['OptionsDefine.WaiterInfo']['interval'])
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doPullSmsReplyStatus(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')], endpoint=g_param["sts_cred_endpoint"]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION)             and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID)             and os.getenv(OptionsDefine.ENV_TKE_WEB_IDENTITY_TOKEN_FILE)             and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
        cred = credential.DefaultTkeOIDCRoleArnProvider().get_credentials()
    else:
        cred = credential.Credential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
        )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint],
        proxy=g_param[OptionsDefine.HttpsProxy.replace('-', '_')]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    if g_param[OptionsDefine.Language]:
        profile.language = g_param[OptionsDefine.Language]
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.SmsClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.PullSmsReplyStatusRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.PullSmsReplyStatus(model)
        result = rsp.to_json_string()
        try:
            json_obj = json.loads(result)
        except TypeError as e:
            json_obj = json.loads(result.decode('utf-8'))  # python3.3
        if not g_param[OptionsDefine.Waiter] or search(g_param['OptionsDefine.WaiterInfo']['expr'], json_obj) == g_param['OptionsDefine.WaiterInfo']['to']:
            break
        cur_time = time.time()
        if cur_time - start_time >= g_param['OptionsDefine.WaiterInfo']['timeout']:
            raise ClientError('Request timeout, wait `%s` to `%s` timeout, last request is %s' %
            (g_param['OptionsDefine.WaiterInfo']['expr'], g_param['OptionsDefine.WaiterInfo']['to'],
            search(g_param['OptionsDefine.WaiterInfo']['expr'], json_obj)))
        else:
            print('Inquiry result is %s.' % search(g_param['OptionsDefine.WaiterInfo']['expr'], json_obj))
        time.sleep(g_param['OptionsDefine.WaiterInfo']['interval'])
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeSmsSignList(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')], endpoint=g_param["sts_cred_endpoint"]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION)             and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID)             and os.getenv(OptionsDefine.ENV_TKE_WEB_IDENTITY_TOKEN_FILE)             and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
        cred = credential.DefaultTkeOIDCRoleArnProvider().get_credentials()
    else:
        cred = credential.Credential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
        )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint],
        proxy=g_param[OptionsDefine.HttpsProxy.replace('-', '_')]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    if g_param[OptionsDefine.Language]:
        profile.language = g_param[OptionsDefine.Language]
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.SmsClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeSmsSignListRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.DescribeSmsSignList(model)
        result = rsp.to_json_string()
        try:
            json_obj = json.loads(result)
        except TypeError as e:
            json_obj = json.loads(result.decode('utf-8'))  # python3.3
        if not g_param[OptionsDefine.Waiter] or search(g_param['OptionsDefine.WaiterInfo']['expr'], json_obj) == g_param['OptionsDefine.WaiterInfo']['to']:
            break
        cur_time = time.time()
        if cur_time - start_time >= g_param['OptionsDefine.WaiterInfo']['timeout']:
            raise ClientError('Request timeout, wait `%s` to `%s` timeout, last request is %s' %
            (g_param['OptionsDefine.WaiterInfo']['expr'], g_param['OptionsDefine.WaiterInfo']['to'],
            search(g_param['OptionsDefine.WaiterInfo']['expr'], json_obj)))
        else:
            print('Inquiry result is %s.' % search(g_param['OptionsDefine.WaiterInfo']['expr'], json_obj))
        time.sleep(g_param['OptionsDefine.WaiterInfo']['interval'])
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doPullSmsSendStatusByPhoneNumber(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')], endpoint=g_param["sts_cred_endpoint"]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION)             and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID)             and os.getenv(OptionsDefine.ENV_TKE_WEB_IDENTITY_TOKEN_FILE)             and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
        cred = credential.DefaultTkeOIDCRoleArnProvider().get_credentials()
    else:
        cred = credential.Credential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
        )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint],
        proxy=g_param[OptionsDefine.HttpsProxy.replace('-', '_')]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    if g_param[OptionsDefine.Language]:
        profile.language = g_param[OptionsDefine.Language]
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.SmsClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.PullSmsSendStatusByPhoneNumberRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.PullSmsSendStatusByPhoneNumber(model)
        result = rsp.to_json_string()
        try:
            json_obj = json.loads(result)
        except TypeError as e:
            json_obj = json.loads(result.decode('utf-8'))  # python3.3
        if not g_param[OptionsDefine.Waiter] or search(g_param['OptionsDefine.WaiterInfo']['expr'], json_obj) == g_param['OptionsDefine.WaiterInfo']['to']:
            break
        cur_time = time.time()
        if cur_time - start_time >= g_param['OptionsDefine.WaiterInfo']['timeout']:
            raise ClientError('Request timeout, wait `%s` to `%s` timeout, last request is %s' %
            (g_param['OptionsDefine.WaiterInfo']['expr'], g_param['OptionsDefine.WaiterInfo']['to'],
            search(g_param['OptionsDefine.WaiterInfo']['expr'], json_obj)))
        else:
            print('Inquiry result is %s.' % search(g_param['OptionsDefine.WaiterInfo']['expr'], json_obj))
        time.sleep(g_param['OptionsDefine.WaiterInfo']['interval'])
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doReportConversion(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')], endpoint=g_param["sts_cred_endpoint"]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION)             and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID)             and os.getenv(OptionsDefine.ENV_TKE_WEB_IDENTITY_TOKEN_FILE)             and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
        cred = credential.DefaultTkeOIDCRoleArnProvider().get_credentials()
    else:
        cred = credential.Credential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
        )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint],
        proxy=g_param[OptionsDefine.HttpsProxy.replace('-', '_')]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    if g_param[OptionsDefine.Language]:
        profile.language = g_param[OptionsDefine.Language]
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.SmsClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ReportConversionRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.ReportConversion(model)
        result = rsp.to_json_string()
        try:
            json_obj = json.loads(result)
        except TypeError as e:
            json_obj = json.loads(result.decode('utf-8'))  # python3.3
        if not g_param[OptionsDefine.Waiter] or search(g_param['OptionsDefine.WaiterInfo']['expr'], json_obj) == g_param['OptionsDefine.WaiterInfo']['to']:
            break
        cur_time = time.time()
        if cur_time - start_time >= g_param['OptionsDefine.WaiterInfo']['timeout']:
            raise ClientError('Request timeout, wait `%s` to `%s` timeout, last request is %s' %
            (g_param['OptionsDefine.WaiterInfo']['expr'], g_param['OptionsDefine.WaiterInfo']['to'],
            search(g_param['OptionsDefine.WaiterInfo']['expr'], json_obj)))
        else:
            print('Inquiry result is %s.' % search(g_param['OptionsDefine.WaiterInfo']['expr'], json_obj))
        time.sleep(g_param['OptionsDefine.WaiterInfo']['interval'])
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifySmsTemplate(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')], endpoint=g_param["sts_cred_endpoint"]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION)             and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID)             and os.getenv(OptionsDefine.ENV_TKE_WEB_IDENTITY_TOKEN_FILE)             and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
        cred = credential.DefaultTkeOIDCRoleArnProvider().get_credentials()
    else:
        cred = credential.Credential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
        )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint],
        proxy=g_param[OptionsDefine.HttpsProxy.replace('-', '_')]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    if g_param[OptionsDefine.Language]:
        profile.language = g_param[OptionsDefine.Language]
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.SmsClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifySmsTemplateRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.ModifySmsTemplate(model)
        result = rsp.to_json_string()
        try:
            json_obj = json.loads(result)
        except TypeError as e:
            json_obj = json.loads(result.decode('utf-8'))  # python3.3
        if not g_param[OptionsDefine.Waiter] or search(g_param['OptionsDefine.WaiterInfo']['expr'], json_obj) == g_param['OptionsDefine.WaiterInfo']['to']:
            break
        cur_time = time.time()
        if cur_time - start_time >= g_param['OptionsDefine.WaiterInfo']['timeout']:
            raise ClientError('Request timeout, wait `%s` to `%s` timeout, last request is %s' %
            (g_param['OptionsDefine.WaiterInfo']['expr'], g_param['OptionsDefine.WaiterInfo']['to'],
            search(g_param['OptionsDefine.WaiterInfo']['expr'], json_obj)))
        else:
            print('Inquiry result is %s.' % search(g_param['OptionsDefine.WaiterInfo']['expr'], json_obj))
        time.sleep(g_param['OptionsDefine.WaiterInfo']['interval'])
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doPullSmsReplyStatusByPhoneNumber(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')], endpoint=g_param["sts_cred_endpoint"]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION)             and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID)             and os.getenv(OptionsDefine.ENV_TKE_WEB_IDENTITY_TOKEN_FILE)             and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
        cred = credential.DefaultTkeOIDCRoleArnProvider().get_credentials()
    else:
        cred = credential.Credential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
        )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint],
        proxy=g_param[OptionsDefine.HttpsProxy.replace('-', '_')]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    if g_param[OptionsDefine.Language]:
        profile.language = g_param[OptionsDefine.Language]
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.SmsClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.PullSmsReplyStatusByPhoneNumberRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.PullSmsReplyStatusByPhoneNumber(model)
        result = rsp.to_json_string()
        try:
            json_obj = json.loads(result)
        except TypeError as e:
            json_obj = json.loads(result.decode('utf-8'))  # python3.3
        if not g_param[OptionsDefine.Waiter] or search(g_param['OptionsDefine.WaiterInfo']['expr'], json_obj) == g_param['OptionsDefine.WaiterInfo']['to']:
            break
        cur_time = time.time()
        if cur_time - start_time >= g_param['OptionsDefine.WaiterInfo']['timeout']:
            raise ClientError('Request timeout, wait `%s` to `%s` timeout, last request is %s' %
            (g_param['OptionsDefine.WaiterInfo']['expr'], g_param['OptionsDefine.WaiterInfo']['to'],
            search(g_param['OptionsDefine.WaiterInfo']['expr'], json_obj)))
        else:
            print('Inquiry result is %s.' % search(g_param['OptionsDefine.WaiterInfo']['expr'], json_obj))
        time.sleep(g_param['OptionsDefine.WaiterInfo']['interval'])
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribePhoneNumberInfo(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')], endpoint=g_param["sts_cred_endpoint"]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION)             and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID)             and os.getenv(OptionsDefine.ENV_TKE_WEB_IDENTITY_TOKEN_FILE)             and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
        cred = credential.DefaultTkeOIDCRoleArnProvider().get_credentials()
    else:
        cred = credential.Credential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
        )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint],
        proxy=g_param[OptionsDefine.HttpsProxy.replace('-', '_')]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    if g_param[OptionsDefine.Language]:
        profile.language = g_param[OptionsDefine.Language]
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.SmsClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribePhoneNumberInfoRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.DescribePhoneNumberInfo(model)
        result = rsp.to_json_string()
        try:
            json_obj = json.loads(result)
        except TypeError as e:
            json_obj = json.loads(result.decode('utf-8'))  # python3.3
        if not g_param[OptionsDefine.Waiter] or search(g_param['OptionsDefine.WaiterInfo']['expr'], json_obj) == g_param['OptionsDefine.WaiterInfo']['to']:
            break
        cur_time = time.time()
        if cur_time - start_time >= g_param['OptionsDefine.WaiterInfo']['timeout']:
            raise ClientError('Request timeout, wait `%s` to `%s` timeout, last request is %s' %
            (g_param['OptionsDefine.WaiterInfo']['expr'], g_param['OptionsDefine.WaiterInfo']['to'],
            search(g_param['OptionsDefine.WaiterInfo']['expr'], json_obj)))
        else:
            print('Inquiry result is %s.' % search(g_param['OptionsDefine.WaiterInfo']['expr'], json_obj))
        time.sleep(g_param['OptionsDefine.WaiterInfo']['interval'])
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteSmsSign(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')], endpoint=g_param["sts_cred_endpoint"]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION)             and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID)             and os.getenv(OptionsDefine.ENV_TKE_WEB_IDENTITY_TOKEN_FILE)             and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
        cred = credential.DefaultTkeOIDCRoleArnProvider().get_credentials()
    else:
        cred = credential.Credential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
        )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint],
        proxy=g_param[OptionsDefine.HttpsProxy.replace('-', '_')]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    if g_param[OptionsDefine.Language]:
        profile.language = g_param[OptionsDefine.Language]
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.SmsClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteSmsSignRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.DeleteSmsSign(model)
        result = rsp.to_json_string()
        try:
            json_obj = json.loads(result)
        except TypeError as e:
            json_obj = json.loads(result.decode('utf-8'))  # python3.3
        if not g_param[OptionsDefine.Waiter] or search(g_param['OptionsDefine.WaiterInfo']['expr'], json_obj) == g_param['OptionsDefine.WaiterInfo']['to']:
            break
        cur_time = time.time()
        if cur_time - start_time >= g_param['OptionsDefine.WaiterInfo']['timeout']:
            raise ClientError('Request timeout, wait `%s` to `%s` timeout, last request is %s' %
            (g_param['OptionsDefine.WaiterInfo']['expr'], g_param['OptionsDefine.WaiterInfo']['to'],
            search(g_param['OptionsDefine.WaiterInfo']['expr'], json_obj)))
        else:
            print('Inquiry result is %s.' % search(g_param['OptionsDefine.WaiterInfo']['expr'], json_obj))
        time.sleep(g_param['OptionsDefine.WaiterInfo']['interval'])
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doAddSmsTemplate(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')], endpoint=g_param["sts_cred_endpoint"]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION)             and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID)             and os.getenv(OptionsDefine.ENV_TKE_WEB_IDENTITY_TOKEN_FILE)             and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
        cred = credential.DefaultTkeOIDCRoleArnProvider().get_credentials()
    else:
        cred = credential.Credential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
        )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint],
        proxy=g_param[OptionsDefine.HttpsProxy.replace('-', '_')]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    if g_param[OptionsDefine.Language]:
        profile.language = g_param[OptionsDefine.Language]
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.SmsClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.AddSmsTemplateRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.AddSmsTemplate(model)
        result = rsp.to_json_string()
        try:
            json_obj = json.loads(result)
        except TypeError as e:
            json_obj = json.loads(result.decode('utf-8'))  # python3.3
        if not g_param[OptionsDefine.Waiter] or search(g_param['OptionsDefine.WaiterInfo']['expr'], json_obj) == g_param['OptionsDefine.WaiterInfo']['to']:
            break
        cur_time = time.time()
        if cur_time - start_time >= g_param['OptionsDefine.WaiterInfo']['timeout']:
            raise ClientError('Request timeout, wait `%s` to `%s` timeout, last request is %s' %
            (g_param['OptionsDefine.WaiterInfo']['expr'], g_param['OptionsDefine.WaiterInfo']['to'],
            search(g_param['OptionsDefine.WaiterInfo']['expr'], json_obj)))
        else:
            print('Inquiry result is %s.' % search(g_param['OptionsDefine.WaiterInfo']['expr'], json_obj))
        time.sleep(g_param['OptionsDefine.WaiterInfo']['interval'])
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


CLIENT_MAP = {
    "v20210111": sms_client_v20210111,
    "v20190711": sms_client_v20190711,

}

MODELS_MAP = {
    "v20210111": models_v20210111,
    "v20190711": models_v20190711,

}

ACTION_MAP = {
    "ModifySmsSign": doModifySmsSign,
    "AddSmsSign": doAddSmsSign,
    "PullSmsSendStatus": doPullSmsSendStatus,
    "SendSms": doSendSms,
    "DeleteSmsTemplate": doDeleteSmsTemplate,
    "SmsPackagesStatistics": doSmsPackagesStatistics,
    "SendStatusStatistics": doSendStatusStatistics,
    "CallbackStatusStatistics": doCallbackStatusStatistics,
    "DescribeSmsTemplateList": doDescribeSmsTemplateList,
    "PullSmsReplyStatus": doPullSmsReplyStatus,
    "DescribeSmsSignList": doDescribeSmsSignList,
    "PullSmsSendStatusByPhoneNumber": doPullSmsSendStatusByPhoneNumber,
    "ReportConversion": doReportConversion,
    "ModifySmsTemplate": doModifySmsTemplate,
    "PullSmsReplyStatusByPhoneNumber": doPullSmsReplyStatusByPhoneNumber,
    "DescribePhoneNumberInfo": doDescribePhoneNumberInfo,
    "DeleteSmsSign": doDeleteSmsSign,
    "AddSmsTemplate": doAddSmsTemplate,

}

AVAILABLE_VERSION_LIST = [
    "v20210111",
    "v20190711",

]


def action_caller():
    return ACTION_MAP


def parse_global_arg(parsed_globals):
    g_param = parsed_globals
    cvm_role_flag = True
    for param in parsed_globals.keys():
        if param in [OptionsDefine.SecretKey, OptionsDefine.SecretId, OptionsDefine.RoleArn,
                     OptionsDefine.RoleSessionName]:
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

    if OptionsDefine.Token not in cred:
        cred[OptionsDefine.Token] = None

    if not is_exist_profile:
        if os.environ.get(OptionsDefine.ENV_SECRET_ID) and os.environ.get(OptionsDefine.ENV_SECRET_KEY):
            cred[OptionsDefine.SecretId] = os.environ.get(OptionsDefine.ENV_SECRET_ID)
            cred[OptionsDefine.SecretKey] = os.environ.get(OptionsDefine.ENV_SECRET_KEY)
            cred[OptionsDefine.Token] = os.environ.get(OptionsDefine.ENV_TOKEN)
            cvm_role_flag = False

        if os.environ.get(OptionsDefine.ENV_REGION):
            conf[OptionsDefine.SysParam][OptionsDefine.Region] = os.environ.get(OptionsDefine.ENV_REGION)

        if os.environ.get(OptionsDefine.ENV_ROLE_ARN) and os.environ.get(OptionsDefine.ENV_ROLE_SESSION_NAME):
            cred[OptionsDefine.RoleArn] = os.environ.get(OptionsDefine.ENV_ROLE_ARN)
            cred[OptionsDefine.RoleSessionName] = os.environ.get(OptionsDefine.ENV_ROLE_SESSION_NAME)
            cvm_role_flag = False
    
    if cvm_role_flag:
        if "type" in cred and cred["type"] == "cvm-role":
            g_param[OptionsDefine.UseCVMRole.replace('-', '_')] = True

    for param in g_param.keys():
        if g_param[param] is None:
            if param in [OptionsDefine.SecretKey, OptionsDefine.SecretId, OptionsDefine.Token]:
                if param in cred:
                    g_param[param] = cred[param]
                elif not (g_param[OptionsDefine.UseCVMRole.replace('-', '_')]
                          or os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN)):
                    raise ConfigurationError("%s is invalid" % param)
            elif param in [OptionsDefine.Region, OptionsDefine.Output, OptionsDefine.Language]:
                if param in conf[OptionsDefine.SysParam]:
                    g_param[param] = conf[OptionsDefine.SysParam][param]
                elif param != OptionsDefine.Language:
                    raise ConfigurationError("%s is invalid" % param)
            elif param.replace('_', '-') in [OptionsDefine.RoleArn, OptionsDefine.RoleSessionName]:
                if param.replace('_', '-') in cred:
                    g_param[param] = cred[param.replace('_', '-')]

    try:
        if g_param[OptionsDefine.ServiceVersion]:
            g_param[OptionsDefine.Version] = "v" + g_param[OptionsDefine.ServiceVersion].replace('-', '')
        else:
            version = conf["sms"][OptionsDefine.Version]
            g_param[OptionsDefine.Version] = "v" + version.replace('-', '')

        if g_param[OptionsDefine.Endpoint] is None:
            g_param[OptionsDefine.Endpoint] = conf["sms"][OptionsDefine.Endpoint]
        g_param["sts_cred_endpoint"] = conf.get("sts", {}).get("endpoint")
    except Exception as err:
        raise ConfigurationError("config file:%s error, %s" % (conf_path, str(err)))

    if g_param[OptionsDefine.Version] not in AVAILABLE_VERSION_LIST:
        raise Exception("available versions: %s" % " ".join(AVAILABLE_VERSION_LIST))

    if g_param[OptionsDefine.Waiter]:
        param = eval(g_param[OptionsDefine.Waiter])
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

