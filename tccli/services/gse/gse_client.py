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
from tencentcloud.gse.v20191112 import gse_client as gse_client_v20191112
from tencentcloud.gse.v20191112 import models as models_v20191112

from jmespath import search
import time

def doUpdateBucketCORSOpt(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION)             and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID)             and os.getenv(OptionsDefine.ENV_TKE_IDENTITY_TOKEN_FILE)             and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
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
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GseClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.UpdateBucketCORSOptRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.UpdateBucketCORSOpt(model)
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


def doDeleteFleet(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION)             and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID)             and os.getenv(OptionsDefine.ENV_TKE_IDENTITY_TOKEN_FILE)             and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
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
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GseClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteFleetRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.DeleteFleet(model)
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


def doUpdateFleetCapacity(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION)             and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID)             and os.getenv(OptionsDefine.ENV_TKE_IDENTITY_TOKEN_FILE)             and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
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
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GseClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.UpdateFleetCapacityRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.UpdateFleetCapacity(model)
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


def doDescribeFleetRelatedResources(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION)             and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID)             and os.getenv(OptionsDefine.ENV_TKE_IDENTITY_TOKEN_FILE)             and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
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
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GseClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeFleetRelatedResourcesRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.DescribeFleetRelatedResources(model)
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


def doDescribeRuntimeConfiguration(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION)             and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID)             and os.getenv(OptionsDefine.ENV_TKE_IDENTITY_TOKEN_FILE)             and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
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
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GseClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeRuntimeConfigurationRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.DescribeRuntimeConfiguration(model)
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


def doUpdateAlias(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION)             and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID)             and os.getenv(OptionsDefine.ENV_TKE_IDENTITY_TOKEN_FILE)             and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
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
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GseClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.UpdateAliasRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.UpdateAlias(model)
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


def doDescribeGameServerSessionPlacement(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION)             and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID)             and os.getenv(OptionsDefine.ENV_TKE_IDENTITY_TOKEN_FILE)             and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
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
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GseClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeGameServerSessionPlacementRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.DescribeGameServerSessionPlacement(model)
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


def doDescribeGameServerSessionDetails(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION)             and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID)             and os.getenv(OptionsDefine.ENV_TKE_IDENTITY_TOKEN_FILE)             and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
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
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GseClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeGameServerSessionDetailsRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.DescribeGameServerSessionDetails(model)
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


def doDescribeCcnInstances(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION)             and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID)             and os.getenv(OptionsDefine.ENV_TKE_IDENTITY_TOKEN_FILE)             and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
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
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GseClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeCcnInstancesRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.DescribeCcnInstances(model)
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


def doUpdateBucketAccelerateOpt(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION)             and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID)             and os.getenv(OptionsDefine.ENV_TKE_IDENTITY_TOKEN_FILE)             and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
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
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GseClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.UpdateBucketAccelerateOptRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.UpdateBucketAccelerateOpt(model)
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


def doCreateGameServerSessionQueue(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION)             and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID)             and os.getenv(OptionsDefine.ENV_TKE_IDENTITY_TOKEN_FILE)             and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
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
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GseClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateGameServerSessionQueueRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.CreateGameServerSessionQueue(model)
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


def doDescribeFleetPortSettings(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION)             and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID)             and os.getenv(OptionsDefine.ENV_TKE_IDENTITY_TOKEN_FILE)             and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
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
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GseClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeFleetPortSettingsRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.DescribeFleetPortSettings(model)
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


def doDeleteAsset(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION)             and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID)             and os.getenv(OptionsDefine.ENV_TKE_IDENTITY_TOKEN_FILE)             and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
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
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GseClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteAssetRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.DeleteAsset(model)
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


def doListFleets(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION)             and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID)             and os.getenv(OptionsDefine.ENV_TKE_IDENTITY_TOKEN_FILE)             and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
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
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GseClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ListFleetsRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.ListFleets(model)
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


def doGetGameServerSessionLogUrl(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION)             and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID)             and os.getenv(OptionsDefine.ENV_TKE_IDENTITY_TOKEN_FILE)             and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
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
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GseClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.GetGameServerSessionLogUrlRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.GetGameServerSessionLogUrl(model)
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


def doUpdateRuntimeConfiguration(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION)             and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID)             and os.getenv(OptionsDefine.ENV_TKE_IDENTITY_TOKEN_FILE)             and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
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
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GseClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.UpdateRuntimeConfigurationRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.UpdateRuntimeConfiguration(model)
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


def doDescribeFleetCapacity(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION)             and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID)             and os.getenv(OptionsDefine.ENV_TKE_IDENTITY_TOKEN_FILE)             and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
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
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GseClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeFleetCapacityRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.DescribeFleetCapacity(model)
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


def doDeleteGameServerSessionQueue(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION)             and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID)             and os.getenv(OptionsDefine.ENV_TKE_IDENTITY_TOKEN_FILE)             and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
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
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GseClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteGameServerSessionQueueRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.DeleteGameServerSessionQueue(model)
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


def doCreateAssetWithImage(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION)             and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID)             and os.getenv(OptionsDefine.ENV_TKE_IDENTITY_TOKEN_FILE)             and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
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
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GseClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateAssetWithImageRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.CreateAssetWithImage(model)
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


def doStartFleetActions(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION)             and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID)             and os.getenv(OptionsDefine.ENV_TKE_IDENTITY_TOKEN_FILE)             and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
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
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GseClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.StartFleetActionsRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.StartFleetActions(model)
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


def doDescribeGameServerSessionQueues(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION)             and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID)             and os.getenv(OptionsDefine.ENV_TKE_IDENTITY_TOKEN_FILE)             and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
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
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GseClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeGameServerSessionQueuesRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.DescribeGameServerSessionQueues(model)
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


def doDescribeInstanceTypes(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION)             and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID)             and os.getenv(OptionsDefine.ENV_TKE_IDENTITY_TOKEN_FILE)             and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
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
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GseClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeInstanceTypesRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.DescribeInstanceTypes(model)
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


def doDescribeScalingPolicies(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION)             and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID)             and os.getenv(OptionsDefine.ENV_TKE_IDENTITY_TOKEN_FILE)             and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
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
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GseClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeScalingPoliciesRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.DescribeScalingPolicies(model)
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


def doCopyFleet(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION)             and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID)             and os.getenv(OptionsDefine.ENV_TKE_IDENTITY_TOKEN_FILE)             and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
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
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GseClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CopyFleetRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.CopyFleet(model)
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


def doDescribeGameServerSessions(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION)             and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID)             and os.getenv(OptionsDefine.ENV_TKE_IDENTITY_TOKEN_FILE)             and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
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
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GseClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeGameServerSessionsRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.DescribeGameServerSessions(model)
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


def doDescribeFleetEvents(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION)             and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID)             and os.getenv(OptionsDefine.ENV_TKE_IDENTITY_TOKEN_FILE)             and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
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
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GseClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeFleetEventsRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.DescribeFleetEvents(model)
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


def doJoinGameServerSession(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION)             and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID)             and os.getenv(OptionsDefine.ENV_TKE_IDENTITY_TOKEN_FILE)             and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
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
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GseClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.JoinGameServerSessionRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.JoinGameServerSession(model)
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


def doJoinGameServerSessionBatch(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION)             and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID)             and os.getenv(OptionsDefine.ENV_TKE_IDENTITY_TOKEN_FILE)             and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
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
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GseClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.JoinGameServerSessionBatchRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.JoinGameServerSessionBatch(model)
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


def doDescribeFleetStatisticSummary(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION)             and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID)             and os.getenv(OptionsDefine.ENV_TKE_IDENTITY_TOKEN_FILE)             and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
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
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GseClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeFleetStatisticSummaryRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.DescribeFleetStatisticSummary(model)
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


def doDeleteAlias(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION)             and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID)             and os.getenv(OptionsDefine.ENV_TKE_IDENTITY_TOKEN_FILE)             and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
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
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GseClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteAliasRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.DeleteAlias(model)
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


def doDeleteTimerScalingPolicy(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION)             and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID)             and os.getenv(OptionsDefine.ENV_TKE_IDENTITY_TOKEN_FILE)             and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
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
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GseClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteTimerScalingPolicyRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.DeleteTimerScalingPolicy(model)
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


def doUpdateAsset(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION)             and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID)             and os.getenv(OptionsDefine.ENV_TKE_IDENTITY_TOKEN_FILE)             and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
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
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GseClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.UpdateAssetRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.UpdateAsset(model)
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


def doStartGameServerSessionPlacement(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION)             and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID)             and os.getenv(OptionsDefine.ENV_TKE_IDENTITY_TOKEN_FILE)             and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
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
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GseClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.StartGameServerSessionPlacementRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.StartGameServerSessionPlacement(model)
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


def doDescribeInstanceLimit(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION)             and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID)             and os.getenv(OptionsDefine.ENV_TKE_IDENTITY_TOKEN_FILE)             and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
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
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GseClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeInstanceLimitRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.DescribeInstanceLimit(model)
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


def doAttachCcnInstances(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION)             and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID)             and os.getenv(OptionsDefine.ENV_TKE_IDENTITY_TOKEN_FILE)             and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
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
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GseClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.AttachCcnInstancesRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.AttachCcnInstances(model)
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


def doGetUploadCredentials(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION)             and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID)             and os.getenv(OptionsDefine.ENV_TKE_IDENTITY_TOKEN_FILE)             and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
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
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GseClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.GetUploadCredentialsRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.GetUploadCredentials(model)
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


def doSearchGameServerSessions(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION)             and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID)             and os.getenv(OptionsDefine.ENV_TKE_IDENTITY_TOKEN_FILE)             and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
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
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GseClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.SearchGameServerSessionsRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.SearchGameServerSessions(model)
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


def doDeleteScalingPolicy(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION)             and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID)             and os.getenv(OptionsDefine.ENV_TKE_IDENTITY_TOKEN_FILE)             and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
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
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GseClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteScalingPolicyRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.DeleteScalingPolicy(model)
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


def doCreateAlias(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION)             and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID)             and os.getenv(OptionsDefine.ENV_TKE_IDENTITY_TOKEN_FILE)             and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
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
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GseClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateAliasRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.CreateAlias(model)
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


def doDescribeFleetStatisticFlows(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION)             and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID)             and os.getenv(OptionsDefine.ENV_TKE_IDENTITY_TOKEN_FILE)             and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
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
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GseClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeFleetStatisticFlowsRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.DescribeFleetStatisticFlows(model)
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


def doCreateGameServerSession(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION)             and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID)             and os.getenv(OptionsDefine.ENV_TKE_IDENTITY_TOKEN_FILE)             and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
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
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GseClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateGameServerSessionRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.CreateGameServerSession(model)
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


def doDescribePlayerSessions(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION)             and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID)             and os.getenv(OptionsDefine.ENV_TKE_IDENTITY_TOKEN_FILE)             and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
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
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GseClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribePlayerSessionsRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.DescribePlayerSessions(model)
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


def doDescribeAsset(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION)             and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID)             and os.getenv(OptionsDefine.ENV_TKE_IDENTITY_TOKEN_FILE)             and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
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
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GseClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeAssetRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.DescribeAsset(model)
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


def doDescribeAssetSystems(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION)             and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID)             and os.getenv(OptionsDefine.ENV_TKE_IDENTITY_TOKEN_FILE)             and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
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
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GseClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeAssetSystemsRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.DescribeAssetSystems(model)
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


def doCreateFleet(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION)             and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID)             and os.getenv(OptionsDefine.ENV_TKE_IDENTITY_TOKEN_FILE)             and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
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
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GseClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateFleetRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.CreateFleet(model)
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


def doStopGameServerSessionPlacement(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION)             and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID)             and os.getenv(OptionsDefine.ENV_TKE_IDENTITY_TOKEN_FILE)             and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
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
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GseClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.StopGameServerSessionPlacementRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.StopGameServerSessionPlacement(model)
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


def doUpdateGameServerSessionQueue(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION)             and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID)             and os.getenv(OptionsDefine.ENV_TKE_IDENTITY_TOKEN_FILE)             and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
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
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GseClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.UpdateGameServerSessionQueueRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.UpdateGameServerSessionQueue(model)
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


def doGetInstanceAccess(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION)             and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID)             and os.getenv(OptionsDefine.ENV_TKE_IDENTITY_TOKEN_FILE)             and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
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
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GseClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.GetInstanceAccessRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.GetInstanceAccess(model)
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


def doUpdateFleetAttributes(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION)             and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID)             and os.getenv(OptionsDefine.ENV_TKE_IDENTITY_TOKEN_FILE)             and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
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
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GseClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.UpdateFleetAttributesRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.UpdateFleetAttributes(model)
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


def doSetServerWeight(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION)             and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID)             and os.getenv(OptionsDefine.ENV_TKE_IDENTITY_TOKEN_FILE)             and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
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
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GseClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.SetServerWeightRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.SetServerWeight(model)
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


def doDetachCcnInstances(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION)             and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID)             and os.getenv(OptionsDefine.ENV_TKE_IDENTITY_TOKEN_FILE)             and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
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
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GseClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DetachCcnInstancesRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.DetachCcnInstances(model)
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


def doDescribeFleetAttributes(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION)             and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID)             and os.getenv(OptionsDefine.ENV_TKE_IDENTITY_TOKEN_FILE)             and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
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
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GseClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeFleetAttributesRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.DescribeFleetAttributes(model)
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


def doDescribeInstances(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION)             and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID)             and os.getenv(OptionsDefine.ENV_TKE_IDENTITY_TOKEN_FILE)             and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
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
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GseClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeInstancesRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.DescribeInstances(model)
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


def doEndGameServerSessionAndProcess(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION)             and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID)             and os.getenv(OptionsDefine.ENV_TKE_IDENTITY_TOKEN_FILE)             and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
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
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GseClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.EndGameServerSessionAndProcessRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.EndGameServerSessionAndProcess(model)
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


def doGetUploadFederationToken(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION)             and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID)             and os.getenv(OptionsDefine.ENV_TKE_IDENTITY_TOKEN_FILE)             and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
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
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GseClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.GetUploadFederationTokenRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.GetUploadFederationToken(model)
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


def doResolveAlias(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION)             and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID)             and os.getenv(OptionsDefine.ENV_TKE_IDENTITY_TOKEN_FILE)             and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
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
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GseClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ResolveAliasRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.ResolveAlias(model)
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


def doSetServerReserved(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION)             and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID)             and os.getenv(OptionsDefine.ENV_TKE_IDENTITY_TOKEN_FILE)             and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
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
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GseClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.SetServerReservedRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.SetServerReserved(model)
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


def doDescribeFleetStatisticDetails(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION)             and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID)             and os.getenv(OptionsDefine.ENV_TKE_IDENTITY_TOKEN_FILE)             and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
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
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GseClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeFleetStatisticDetailsRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.DescribeFleetStatisticDetails(model)
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


def doDescribeAssets(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION)             and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID)             and os.getenv(OptionsDefine.ENV_TKE_IDENTITY_TOKEN_FILE)             and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
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
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GseClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeAssetsRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.DescribeAssets(model)
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


def doCreateAsset(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION)             and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID)             and os.getenv(OptionsDefine.ENV_TKE_IDENTITY_TOKEN_FILE)             and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
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
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GseClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateAssetRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.CreateAsset(model)
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


def doStopFleetActions(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION)             and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID)             and os.getenv(OptionsDefine.ENV_TKE_IDENTITY_TOKEN_FILE)             and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
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
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GseClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.StopFleetActionsRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.StopFleetActions(model)
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


def doDescribeTimerScalingPolicies(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION)             and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID)             and os.getenv(OptionsDefine.ENV_TKE_IDENTITY_TOKEN_FILE)             and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
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
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GseClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeTimerScalingPoliciesRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.DescribeTimerScalingPolicies(model)
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


def doDescribeInstancesExtend(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION)             and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID)             and os.getenv(OptionsDefine.ENV_TKE_IDENTITY_TOKEN_FILE)             and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
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
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GseClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeInstancesExtendRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.DescribeInstancesExtend(model)
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


def doDescribeAlias(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION)             and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID)             and os.getenv(OptionsDefine.ENV_TKE_IDENTITY_TOKEN_FILE)             and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
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
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GseClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeAliasRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.DescribeAlias(model)
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


def doDescribeUserQuota(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION)             and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID)             and os.getenv(OptionsDefine.ENV_TKE_IDENTITY_TOKEN_FILE)             and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
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
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GseClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeUserQuotaRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.DescribeUserQuota(model)
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


def doDescribeUserQuotas(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION)             and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID)             and os.getenv(OptionsDefine.ENV_TKE_IDENTITY_TOKEN_FILE)             and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
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
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GseClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeUserQuotasRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.DescribeUserQuotas(model)
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


def doPutScalingPolicy(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION)             and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID)             and os.getenv(OptionsDefine.ENV_TKE_IDENTITY_TOKEN_FILE)             and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
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
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GseClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.PutScalingPolicyRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.PutScalingPolicy(model)
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


def doListAliases(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION)             and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID)             and os.getenv(OptionsDefine.ENV_TKE_IDENTITY_TOKEN_FILE)             and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
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
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GseClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ListAliasesRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.ListAliases(model)
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


def doUpdateFleetPortSettings(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION)             and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID)             and os.getenv(OptionsDefine.ENV_TKE_IDENTITY_TOKEN_FILE)             and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
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
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GseClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.UpdateFleetPortSettingsRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.UpdateFleetPortSettings(model)
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


def doUpdateFleetName(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION)             and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID)             and os.getenv(OptionsDefine.ENV_TKE_IDENTITY_TOKEN_FILE)             and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
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
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GseClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.UpdateFleetNameRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.UpdateFleetName(model)
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


def doDescribeFleetUtilization(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION)             and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID)             and os.getenv(OptionsDefine.ENV_TKE_IDENTITY_TOKEN_FILE)             and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
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
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GseClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeFleetUtilizationRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.DescribeFleetUtilization(model)
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


def doUpdateGameServerSession(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION)             and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID)             and os.getenv(OptionsDefine.ENV_TKE_IDENTITY_TOKEN_FILE)             and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
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
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GseClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.UpdateGameServerSessionRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.UpdateGameServerSession(model)
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


def doGetGameServerInstanceLogUrl(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION)             and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID)             and os.getenv(OptionsDefine.ENV_TKE_IDENTITY_TOKEN_FILE)             and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
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
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GseClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.GetGameServerInstanceLogUrlRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.GetGameServerInstanceLogUrl(model)
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


def doPutTimerScalingPolicy(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')]
        )
    elif os.getenv(OptionsDefine.ENV_TKE_REGION)             and os.getenv(OptionsDefine.ENV_TKE_PROVIDER_ID)             and os.getenv(OptionsDefine.ENV_TKE_IDENTITY_TOKEN_FILE)             and os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN):
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
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GseClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.PutTimerScalingPolicyRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.PutTimerScalingPolicy(model)
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
    "v20191112": gse_client_v20191112,

}

MODELS_MAP = {
    "v20191112": models_v20191112,

}

ACTION_MAP = {
    "UpdateBucketCORSOpt": doUpdateBucketCORSOpt,
    "DeleteFleet": doDeleteFleet,
    "UpdateFleetCapacity": doUpdateFleetCapacity,
    "DescribeFleetRelatedResources": doDescribeFleetRelatedResources,
    "DescribeRuntimeConfiguration": doDescribeRuntimeConfiguration,
    "UpdateAlias": doUpdateAlias,
    "DescribeGameServerSessionPlacement": doDescribeGameServerSessionPlacement,
    "DescribeGameServerSessionDetails": doDescribeGameServerSessionDetails,
    "DescribeCcnInstances": doDescribeCcnInstances,
    "UpdateBucketAccelerateOpt": doUpdateBucketAccelerateOpt,
    "CreateGameServerSessionQueue": doCreateGameServerSessionQueue,
    "DescribeFleetPortSettings": doDescribeFleetPortSettings,
    "DeleteAsset": doDeleteAsset,
    "ListFleets": doListFleets,
    "GetGameServerSessionLogUrl": doGetGameServerSessionLogUrl,
    "UpdateRuntimeConfiguration": doUpdateRuntimeConfiguration,
    "DescribeFleetCapacity": doDescribeFleetCapacity,
    "DeleteGameServerSessionQueue": doDeleteGameServerSessionQueue,
    "CreateAssetWithImage": doCreateAssetWithImage,
    "StartFleetActions": doStartFleetActions,
    "DescribeGameServerSessionQueues": doDescribeGameServerSessionQueues,
    "DescribeInstanceTypes": doDescribeInstanceTypes,
    "DescribeScalingPolicies": doDescribeScalingPolicies,
    "CopyFleet": doCopyFleet,
    "DescribeGameServerSessions": doDescribeGameServerSessions,
    "DescribeFleetEvents": doDescribeFleetEvents,
    "JoinGameServerSession": doJoinGameServerSession,
    "JoinGameServerSessionBatch": doJoinGameServerSessionBatch,
    "DescribeFleetStatisticSummary": doDescribeFleetStatisticSummary,
    "DeleteAlias": doDeleteAlias,
    "DeleteTimerScalingPolicy": doDeleteTimerScalingPolicy,
    "UpdateAsset": doUpdateAsset,
    "StartGameServerSessionPlacement": doStartGameServerSessionPlacement,
    "DescribeInstanceLimit": doDescribeInstanceLimit,
    "AttachCcnInstances": doAttachCcnInstances,
    "GetUploadCredentials": doGetUploadCredentials,
    "SearchGameServerSessions": doSearchGameServerSessions,
    "DeleteScalingPolicy": doDeleteScalingPolicy,
    "CreateAlias": doCreateAlias,
    "DescribeFleetStatisticFlows": doDescribeFleetStatisticFlows,
    "CreateGameServerSession": doCreateGameServerSession,
    "DescribePlayerSessions": doDescribePlayerSessions,
    "DescribeAsset": doDescribeAsset,
    "DescribeAssetSystems": doDescribeAssetSystems,
    "CreateFleet": doCreateFleet,
    "StopGameServerSessionPlacement": doStopGameServerSessionPlacement,
    "UpdateGameServerSessionQueue": doUpdateGameServerSessionQueue,
    "GetInstanceAccess": doGetInstanceAccess,
    "UpdateFleetAttributes": doUpdateFleetAttributes,
    "SetServerWeight": doSetServerWeight,
    "DetachCcnInstances": doDetachCcnInstances,
    "DescribeFleetAttributes": doDescribeFleetAttributes,
    "DescribeInstances": doDescribeInstances,
    "EndGameServerSessionAndProcess": doEndGameServerSessionAndProcess,
    "GetUploadFederationToken": doGetUploadFederationToken,
    "ResolveAlias": doResolveAlias,
    "SetServerReserved": doSetServerReserved,
    "DescribeFleetStatisticDetails": doDescribeFleetStatisticDetails,
    "DescribeAssets": doDescribeAssets,
    "CreateAsset": doCreateAsset,
    "StopFleetActions": doStopFleetActions,
    "DescribeTimerScalingPolicies": doDescribeTimerScalingPolicies,
    "DescribeInstancesExtend": doDescribeInstancesExtend,
    "DescribeAlias": doDescribeAlias,
    "DescribeUserQuota": doDescribeUserQuota,
    "DescribeUserQuotas": doDescribeUserQuotas,
    "PutScalingPolicy": doPutScalingPolicy,
    "ListAliases": doListAliases,
    "UpdateFleetPortSettings": doUpdateFleetPortSettings,
    "UpdateFleetName": doUpdateFleetName,
    "DescribeFleetUtilization": doDescribeFleetUtilization,
    "UpdateGameServerSession": doUpdateGameServerSession,
    "GetGameServerInstanceLogUrl": doGetGameServerInstanceLogUrl,
    "PutTimerScalingPolicy": doPutTimerScalingPolicy,

}

AVAILABLE_VERSION_LIST = [
    "v20191112",

]


def action_caller():
    return ACTION_MAP


def parse_global_arg(parsed_globals):
    g_param = parsed_globals

    is_exist_profile = True
    if not parsed_globals["profile"]:
        is_exist_profile = False
        g_param["profile"] = "default"

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

        if os.environ.get(OptionsDefine.ENV_REGION):
            conf[OptionsDefine.Region] = os.environ.get(OptionsDefine.ENV_REGION)

        if os.environ.get(OptionsDefine.ENV_ROLE_ARN) and os.environ.get(OptionsDefine.ENV_ROLE_SESSION_NAME):
            cred[OptionsDefine.RoleArn] = os.environ.get(OptionsDefine.ENV_ROLE_ARN)
            cred[OptionsDefine.RoleSessionName] = os.environ.get(OptionsDefine.ENV_ROLE_SESSION_NAME)

    for param in g_param.keys():
        if g_param[param] is None:
            if param in [OptionsDefine.SecretKey, OptionsDefine.SecretId, OptionsDefine.Token]:
                if param in cred:
                    g_param[param] = cred[param]
                elif not (g_param[OptionsDefine.UseCVMRole.replace('-', '_')]
                          or os.getenv(OptionsDefine.ENV_TKE_ROLE_ARN)):
                    raise ConfigurationError("%s is invalid" % param)
            elif param in [OptionsDefine.Region, OptionsDefine.Output]:
                if param in conf:
                    g_param[param] = conf[param]
                else:
                    raise ConfigurationError("%s is invalid" % param)
            elif param.replace('_', '-') in [OptionsDefine.RoleArn, OptionsDefine.RoleSessionName]:
                if param.replace('_', '-') in cred:
                    g_param[param] = cred[param.replace('_', '-')]

    try:
        if g_param[OptionsDefine.ServiceVersion]:
            g_param[OptionsDefine.Version] = "v" + g_param[OptionsDefine.ServiceVersion].replace('-', '')
        else:
            version = conf["gse"][OptionsDefine.Version]
            g_param[OptionsDefine.Version] = "v" + version.replace('-', '')

        if g_param[OptionsDefine.Endpoint] is None:
            g_param[OptionsDefine.Endpoint] = conf["gse"][OptionsDefine.Endpoint]
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

