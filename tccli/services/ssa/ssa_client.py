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
from tencentcloud.ssa.v20180608 import ssa_client as ssa_client_v20180608
from tencentcloud.ssa.v20180608 import models as models_v20180608

from jmespath import search
import time

def doDescribeComplianceList(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')]
        )
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
    client = mod.SsaClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeComplianceListRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.DescribeComplianceList(model)
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


def doDescribeCheckConfigDetail(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')]
        )
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
    client = mod.SsaClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeCheckConfigDetailRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.DescribeCheckConfigDetail(model)
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


def doDescribeConfigList(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')]
        )
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
    client = mod.SsaClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeConfigListRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.DescribeConfigList(model)
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


def doDescribeAssetList(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')]
        )
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
    client = mod.SsaClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeAssetListRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.DescribeAssetList(model)
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


def doDescribeEventDetail(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')]
        )
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
    client = mod.SsaClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeEventDetailRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.DescribeEventDetail(model)
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


def doSaDivulgeDataQueryPub(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')]
        )
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
    client = mod.SsaClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.SaDivulgeDataQueryPubRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.SaDivulgeDataQueryPub(model)
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


def doDescribeSocCspmCompliance(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')]
        )
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
    client = mod.SsaClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeSocCspmComplianceRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.DescribeSocCspmCompliance(model)
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


def doDescribeCheckConfigAssetList(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')]
        )
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
    client = mod.SsaClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeCheckConfigAssetListRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.DescribeCheckConfigAssetList(model)
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


def doDescribeLeakDetectionList(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')]
        )
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
    client = mod.SsaClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeLeakDetectionListRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.DescribeLeakDetectionList(model)
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


def doDescribeAssetsMappingList(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')]
        )
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
    client = mod.SsaClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeAssetsMappingListRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.DescribeAssetsMappingList(model)
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


def doDescribeComplianceAssetList(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')]
        )
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
    client = mod.SsaClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeComplianceAssetListRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.DescribeComplianceAssetList(model)
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


def doDescribeVulList(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')]
        )
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
    client = mod.SsaClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeVulListRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.DescribeVulList(model)
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


def doDescribeComplianceDetail(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')]
        )
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
    client = mod.SsaClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeComplianceDetailRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.DescribeComplianceDetail(model)
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


def doDescribeSafetyEventList(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')]
        )
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
    client = mod.SsaClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeSafetyEventListRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.DescribeSafetyEventList(model)
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


def doDescribeSocAlertList(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')]
        )
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
    client = mod.SsaClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeSocAlertListRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.DescribeSocAlertList(model)
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


def doDescribeSocAlertDetails(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')]
        )
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
    client = mod.SsaClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeSocAlertDetailsRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.DescribeSocAlertDetails(model)
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


def doDescribeAssetDetail(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')]
        )
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
    client = mod.SsaClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeAssetDetailRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.DescribeAssetDetail(model)
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


def doDescribeVulDetail(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    if g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
        cred = credential.CVMRoleCredential()
    elif g_param[OptionsDefine.RoleArn.replace('-', '_')] and g_param[OptionsDefine.RoleSessionName.replace('-', '_')]:
        cred = credential.STSAssumeRoleCredential(
            g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.RoleArn.replace('-', '_')],
            g_param[OptionsDefine.RoleSessionName.replace('-', '_')]
        )
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
    client = mod.SsaClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeVulDetailRequest()
    model.from_json_string(json.dumps(args))
    start_time = time.time()
    while True:
        rsp = client.DescribeVulDetail(model)
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
    "v20180608": ssa_client_v20180608,

}

MODELS_MAP = {
    "v20180608": models_v20180608,

}

ACTION_MAP = {
    "DescribeComplianceList": doDescribeComplianceList,
    "DescribeCheckConfigDetail": doDescribeCheckConfigDetail,
    "DescribeConfigList": doDescribeConfigList,
    "DescribeAssetList": doDescribeAssetList,
    "DescribeEventDetail": doDescribeEventDetail,
    "SaDivulgeDataQueryPub": doSaDivulgeDataQueryPub,
    "DescribeSocCspmCompliance": doDescribeSocCspmCompliance,
    "DescribeCheckConfigAssetList": doDescribeCheckConfigAssetList,
    "DescribeLeakDetectionList": doDescribeLeakDetectionList,
    "DescribeAssetsMappingList": doDescribeAssetsMappingList,
    "DescribeComplianceAssetList": doDescribeComplianceAssetList,
    "DescribeVulList": doDescribeVulList,
    "DescribeComplianceDetail": doDescribeComplianceDetail,
    "DescribeSafetyEventList": doDescribeSafetyEventList,
    "DescribeSocAlertList": doDescribeSocAlertList,
    "DescribeSocAlertDetails": doDescribeSocAlertDetails,
    "DescribeAssetDetail": doDescribeAssetDetail,
    "DescribeVulDetail": doDescribeVulDetail,

}

AVAILABLE_VERSION_LIST = [
    "v20180608",

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
                elif not g_param[OptionsDefine.UseCVMRole.replace('-', '_')]:
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
            version = conf["ssa"][OptionsDefine.Version]
            g_param[OptionsDefine.Version] = "v" + version.replace('-', '')

        if g_param[OptionsDefine.Endpoint] is None:
            g_param[OptionsDefine.Endpoint] = conf["ssa"][OptionsDefine.Endpoint]
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
                param['timeout'] = 5
        param['interval'] = min(param['interval'], param['timeout'])
        g_param['OptionsDefine.WaiterInfo'] = param
    
    # 如果在配置文件中读取字段的值，python2中的json.load函数会读取unicode类型的值，因此这里要转化类型
    if six.PY2:
        for key, value in g_param.items():
            if isinstance(value, six.text_type):
                g_param[key] = value.encode('utf-8')
    return g_param

