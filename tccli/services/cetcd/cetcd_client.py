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
from tencentcloud.cetcd.v20220325 import cetcd_client as cetcd_client_v20220325
from tencentcloud.cetcd.v20220325 import models as models_v20220325

from jmespath import search
import time

def doModifyEtcdConfiguration(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')], endpoint=g_param["sts_cred_endpoint"]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION) \
            and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID) \
            and os.getenv(OptionsDefine.ENV_TKE_WEB_IDENTITY_TOKEN_FILE) \
            and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
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
    profile = ClientProfile(httpProfile=http_profile, signMethod="TC3-HMAC-SHA256")
    if g_param[OptionsDefine.Language]:
        profile.language = g_param[OptionsDefine.Language]
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CetcdClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyEtcdConfigurationRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.ModifyEtcdConfiguration(model)
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


def doDescribeEtcdSnapshotPolicies(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')], endpoint=g_param["sts_cred_endpoint"]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION) \
            and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID) \
            and os.getenv(OptionsDefine.ENV_TKE_WEB_IDENTITY_TOKEN_FILE) \
            and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
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
    profile = ClientProfile(httpProfile=http_profile, signMethod="TC3-HMAC-SHA256")
    if g_param[OptionsDefine.Language]:
        profile.language = g_param[OptionsDefine.Language]
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CetcdClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeEtcdSnapshotPoliciesRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.DescribeEtcdSnapshotPolicies(model)
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


def doUpgradeEtcdInstance(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')], endpoint=g_param["sts_cred_endpoint"]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION) \
            and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID) \
            and os.getenv(OptionsDefine.ENV_TKE_WEB_IDENTITY_TOKEN_FILE) \
            and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
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
    profile = ClientProfile(httpProfile=http_profile, signMethod="TC3-HMAC-SHA256")
    if g_param[OptionsDefine.Language]:
        profile.language = g_param[OptionsDefine.Language]
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CetcdClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.UpgradeEtcdInstanceRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.UpgradeEtcdInstance(model)
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


def doResizeEtcdInstance(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')], endpoint=g_param["sts_cred_endpoint"]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION) \
            and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID) \
            and os.getenv(OptionsDefine.ENV_TKE_WEB_IDENTITY_TOKEN_FILE) \
            and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
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
    profile = ClientProfile(httpProfile=http_profile, signMethod="TC3-HMAC-SHA256")
    if g_param[OptionsDefine.Language]:
        profile.language = g_param[OptionsDefine.Language]
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CetcdClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ResizeEtcdInstanceRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.ResizeEtcdInstance(model)
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


def doCreateEtcdSnapshot(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')], endpoint=g_param["sts_cred_endpoint"]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION) \
            and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID) \
            and os.getenv(OptionsDefine.ENV_TKE_WEB_IDENTITY_TOKEN_FILE) \
            and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
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
    profile = ClientProfile(httpProfile=http_profile, signMethod="TC3-HMAC-SHA256")
    if g_param[OptionsDefine.Language]:
        profile.language = g_param[OptionsDefine.Language]
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CetcdClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateEtcdSnapshotRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.CreateEtcdSnapshot(model)
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


def doDescribeEtcdSnapshots(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')], endpoint=g_param["sts_cred_endpoint"]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION) \
            and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID) \
            and os.getenv(OptionsDefine.ENV_TKE_WEB_IDENTITY_TOKEN_FILE) \
            and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
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
    profile = ClientProfile(httpProfile=http_profile, signMethod="TC3-HMAC-SHA256")
    if g_param[OptionsDefine.Language]:
        profile.language = g_param[OptionsDefine.Language]
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CetcdClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeEtcdSnapshotsRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.DescribeEtcdSnapshots(model)
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


def doDescribeEtcdCredentials(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')], endpoint=g_param["sts_cred_endpoint"]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION) \
            and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID) \
            and os.getenv(OptionsDefine.ENV_TKE_WEB_IDENTITY_TOKEN_FILE) \
            and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
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
    profile = ClientProfile(httpProfile=http_profile, signMethod="TC3-HMAC-SHA256")
    if g_param[OptionsDefine.Language]:
        profile.language = g_param[OptionsDefine.Language]
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CetcdClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeEtcdCredentialsRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.DescribeEtcdCredentials(model)
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


def doDescribeEtcdInstances(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')], endpoint=g_param["sts_cred_endpoint"]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION) \
            and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID) \
            and os.getenv(OptionsDefine.ENV_TKE_WEB_IDENTITY_TOKEN_FILE) \
            and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
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
    profile = ClientProfile(httpProfile=http_profile, signMethod="TC3-HMAC-SHA256")
    if g_param[OptionsDefine.Language]:
        profile.language = g_param[OptionsDefine.Language]
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CetcdClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeEtcdInstancesRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.DescribeEtcdInstances(model)
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


def doCreateEtcdInstance(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')], endpoint=g_param["sts_cred_endpoint"]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION) \
            and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID) \
            and os.getenv(OptionsDefine.ENV_TKE_WEB_IDENTITY_TOKEN_FILE) \
            and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
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
    profile = ClientProfile(httpProfile=http_profile, signMethod="TC3-HMAC-SHA256")
    if g_param[OptionsDefine.Language]:
        profile.language = g_param[OptionsDefine.Language]
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CetcdClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateEtcdInstanceRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.CreateEtcdInstance(model)
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


def doModifyEtcdSnapshotPolicy(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')], endpoint=g_param["sts_cred_endpoint"]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION) \
            and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID) \
            and os.getenv(OptionsDefine.ENV_TKE_WEB_IDENTITY_TOKEN_FILE) \
            and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
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
    profile = ClientProfile(httpProfile=http_profile, signMethod="TC3-HMAC-SHA256")
    if g_param[OptionsDefine.Language]:
        profile.language = g_param[OptionsDefine.Language]
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CetcdClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyEtcdSnapshotPolicyRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.ModifyEtcdSnapshotPolicy(model)
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


def doModifyEtcdAttribute(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')], endpoint=g_param["sts_cred_endpoint"]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION) \
            and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID) \
            and os.getenv(OptionsDefine.ENV_TKE_WEB_IDENTITY_TOKEN_FILE) \
            and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
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
    profile = ClientProfile(httpProfile=http_profile, signMethod="TC3-HMAC-SHA256")
    if g_param[OptionsDefine.Language]:
        profile.language = g_param[OptionsDefine.Language]
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CetcdClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyEtcdAttributeRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.ModifyEtcdAttribute(model)
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


def doDescribeEtcdAvailableVersions(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')], endpoint=g_param["sts_cred_endpoint"]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION) \
            and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID) \
            and os.getenv(OptionsDefine.ENV_TKE_WEB_IDENTITY_TOKEN_FILE) \
            and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
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
    profile = ClientProfile(httpProfile=http_profile, signMethod="TC3-HMAC-SHA256")
    if g_param[OptionsDefine.Language]:
        profile.language = g_param[OptionsDefine.Language]
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CetcdClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeEtcdAvailableVersionsRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.DescribeEtcdAvailableVersions(model)
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


def doDescribeEtcdCreatingProgress(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')], endpoint=g_param["sts_cred_endpoint"]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION) \
            and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID) \
            and os.getenv(OptionsDefine.ENV_TKE_WEB_IDENTITY_TOKEN_FILE) \
            and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
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
    profile = ClientProfile(httpProfile=http_profile, signMethod="TC3-HMAC-SHA256")
    if g_param[OptionsDefine.Language]:
        profile.language = g_param[OptionsDefine.Language]
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CetcdClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeEtcdCreatingProgressRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.DescribeEtcdCreatingProgress(model)
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


def doCreateEtcdSnapshotPolicy(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')], endpoint=g_param["sts_cred_endpoint"]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION) \
            and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID) \
            and os.getenv(OptionsDefine.ENV_TKE_WEB_IDENTITY_TOKEN_FILE) \
            and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
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
    profile = ClientProfile(httpProfile=http_profile, signMethod="TC3-HMAC-SHA256")
    if g_param[OptionsDefine.Language]:
        profile.language = g_param[OptionsDefine.Language]
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CetcdClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateEtcdSnapshotPolicyRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.CreateEtcdSnapshotPolicy(model)
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


def doDescribeRPCMethodList(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')], endpoint=g_param["sts_cred_endpoint"]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION) \
            and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID) \
            and os.getenv(OptionsDefine.ENV_TKE_WEB_IDENTITY_TOKEN_FILE) \
            and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
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
    profile = ClientProfile(httpProfile=http_profile, signMethod="TC3-HMAC-SHA256")
    if g_param[OptionsDefine.Language]:
        profile.language = g_param[OptionsDefine.Language]
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CetcdClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeRPCMethodListRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.DescribeRPCMethodList(model)
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


def doDescribeEtcdRegions(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')], endpoint=g_param["sts_cred_endpoint"]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION) \
            and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID) \
            and os.getenv(OptionsDefine.ENV_TKE_WEB_IDENTITY_TOKEN_FILE) \
            and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
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
    profile = ClientProfile(httpProfile=http_profile, signMethod="TC3-HMAC-SHA256")
    if g_param[OptionsDefine.Language]:
        profile.language = g_param[OptionsDefine.Language]
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CetcdClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeEtcdRegionsRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.DescribeEtcdRegions(model)
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


def doDescribeEtcdTasks(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')], endpoint=g_param["sts_cred_endpoint"]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION) \
            and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID) \
            and os.getenv(OptionsDefine.ENV_TKE_WEB_IDENTITY_TOKEN_FILE) \
            and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
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
    profile = ClientProfile(httpProfile=http_profile, signMethod="TC3-HMAC-SHA256")
    if g_param[OptionsDefine.Language]:
        profile.language = g_param[OptionsDefine.Language]
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CetcdClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeEtcdTasksRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.DescribeEtcdTasks(model)
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


def doEnableEtcdInstanceDeletionProtection(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')], endpoint=g_param["sts_cred_endpoint"]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION) \
            and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID) \
            and os.getenv(OptionsDefine.ENV_TKE_WEB_IDENTITY_TOKEN_FILE) \
            and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
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
    profile = ClientProfile(httpProfile=http_profile, signMethod="TC3-HMAC-SHA256")
    if g_param[OptionsDefine.Language]:
        profile.language = g_param[OptionsDefine.Language]
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CetcdClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.EnableEtcdInstanceDeletionProtectionRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.EnableEtcdInstanceDeletionProtection(model)
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


def doDescribeEtcdQuota(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')], endpoint=g_param["sts_cred_endpoint"]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION) \
            and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID) \
            and os.getenv(OptionsDefine.ENV_TKE_WEB_IDENTITY_TOKEN_FILE) \
            and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
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
    profile = ClientProfile(httpProfile=http_profile, signMethod="TC3-HMAC-SHA256")
    if g_param[OptionsDefine.Language]:
        profile.language = g_param[OptionsDefine.Language]
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CetcdClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeEtcdQuotaRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.DescribeEtcdQuota(model)
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


def doDisableEtcdInstanceDeletionProtection(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')], endpoint=g_param["sts_cred_endpoint"]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION) \
            and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID) \
            and os.getenv(OptionsDefine.ENV_TKE_WEB_IDENTITY_TOKEN_FILE) \
            and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
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
    profile = ClientProfile(httpProfile=http_profile, signMethod="TC3-HMAC-SHA256")
    if g_param[OptionsDefine.Language]:
        profile.language = g_param[OptionsDefine.Language]
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CetcdClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DisableEtcdInstanceDeletionProtectionRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.DisableEtcdInstanceDeletionProtection(model)
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
    "v20220325": cetcd_client_v20220325,

}

MODELS_MAP = {
    "v20220325": models_v20220325,

}

ACTION_MAP = {
    "ModifyEtcdConfiguration": doModifyEtcdConfiguration,
    "DescribeEtcdSnapshotPolicies": doDescribeEtcdSnapshotPolicies,
    "UpgradeEtcdInstance": doUpgradeEtcdInstance,
    "ResizeEtcdInstance": doResizeEtcdInstance,
    "CreateEtcdSnapshot": doCreateEtcdSnapshot,
    "DescribeEtcdSnapshots": doDescribeEtcdSnapshots,
    "DescribeEtcdCredentials": doDescribeEtcdCredentials,
    "DescribeEtcdInstances": doDescribeEtcdInstances,
    "CreateEtcdInstance": doCreateEtcdInstance,
    "ModifyEtcdSnapshotPolicy": doModifyEtcdSnapshotPolicy,
    "ModifyEtcdAttribute": doModifyEtcdAttribute,
    "DescribeEtcdAvailableVersions": doDescribeEtcdAvailableVersions,
    "DescribeEtcdCreatingProgress": doDescribeEtcdCreatingProgress,
    "CreateEtcdSnapshotPolicy": doCreateEtcdSnapshotPolicy,
    "DescribeRPCMethodList": doDescribeRPCMethodList,
    "DescribeEtcdRegions": doDescribeEtcdRegions,
    "DescribeEtcdTasks": doDescribeEtcdTasks,
    "EnableEtcdInstanceDeletionProtection": doEnableEtcdInstanceDeletionProtection,
    "DescribeEtcdQuota": doDescribeEtcdQuota,
    "DisableEtcdInstanceDeletionProtection": doDisableEtcdInstanceDeletionProtection,

}

AVAILABLE_VERSION_LIST = [
    "v20220325",

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
            version = conf["cetcd"][OptionsDefine.Version]
            g_param[OptionsDefine.Version] = "v" + version.replace('-', '')

        if g_param[OptionsDefine.Endpoint] is None:
            g_param[OptionsDefine.Endpoint] = conf["cetcd"][OptionsDefine.Endpoint]
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

