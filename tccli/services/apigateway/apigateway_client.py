# -*- coding: utf-8 -*-
import os
import json
import tccli.options_define as OptionsDefine
import tccli.format_output as FormatOutput
from tccli.nice_command import NiceCommand
import tccli.error_msg as ErrorMsg
import tccli.help_template as HelpTemplate
from tccli import __version__
from tccli.utils import Utils
from tccli.configure import Configure
from tencentcloud.common import credential
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.apigateway.v20180808 import apigateway_client as apigateway_client_v20180808
from tencentcloud.apigateway.v20180808 import models as models_v20180808
from tccli.services.apigateway import v20180808
from tccli.services.apigateway.v20180808 import help as v20180808_help


def doCreateService(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateService", g_param[OptionsDefine.Version])
        return

    param = {
        "ServiceName": argv.get("--ServiceName"),
        "Protocol": argv.get("--Protocol"),
        "ServiceDesc": argv.get("--ServiceDesc"),
        "ExclusiveSetName": argv.get("--ExclusiveSetName"),
        "NetTypes": Utils.try_to_json(argv, "--NetTypes"),
        "IpVersion": argv.get("--IpVersion"),
        "SetServerName": argv.get("--SetServerName"),
        "AppIdType": argv.get("--AppIdType"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.ApigatewayClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateServiceRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateService(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeUsagePlansStatus(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeUsagePlansStatus", g_param[OptionsDefine.Version])
        return

    param = {
        "Limit": Utils.try_to_json(argv, "--Limit"),
        "Offset": Utils.try_to_json(argv, "--Offset"),
        "Filters": Utils.try_to_json(argv, "--Filters"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.ApigatewayClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeUsagePlansStatusRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeUsagePlansStatus(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteUsagePlan(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteUsagePlan", g_param[OptionsDefine.Version])
        return

    param = {
        "UsagePlanId": argv.get("--UsagePlanId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.ApigatewayClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteUsagePlanRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeleteUsagePlan(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyApi(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyApi", g_param[OptionsDefine.Version])
        return

    param = {
        "ServiceId": argv.get("--ServiceId"),
        "ServiceType": argv.get("--ServiceType"),
        "RequestConfig": Utils.try_to_json(argv, "--RequestConfig"),
        "ApiId": argv.get("--ApiId"),
        "ApiName": argv.get("--ApiName"),
        "ApiDesc": argv.get("--ApiDesc"),
        "ApiType": argv.get("--ApiType"),
        "AuthType": argv.get("--AuthType"),
        "AuthRequired": Utils.try_to_json(argv, "--AuthRequired"),
        "ServiceTimeout": Utils.try_to_json(argv, "--ServiceTimeout"),
        "Protocol": argv.get("--Protocol"),
        "EnableCORS": Utils.try_to_json(argv, "--EnableCORS"),
        "ConstantParameters": Utils.try_to_json(argv, "--ConstantParameters"),
        "RequestParameters": Utils.try_to_json(argv, "--RequestParameters"),
        "ApiBusinessType": argv.get("--ApiBusinessType"),
        "ServiceMockReturnMessage": argv.get("--ServiceMockReturnMessage"),
        "MicroServices": Utils.try_to_json(argv, "--MicroServices"),
        "ServiceTsfLoadBalanceConf": Utils.try_to_json(argv, "--ServiceTsfLoadBalanceConf"),
        "ServiceTsfHealthCheckConf": Utils.try_to_json(argv, "--ServiceTsfHealthCheckConf"),
        "TargetServicesLoadBalanceConf": Utils.try_to_json(argv, "--TargetServicesLoadBalanceConf"),
        "TargetServicesHealthCheckConf": Utils.try_to_json(argv, "--TargetServicesHealthCheckConf"),
        "ServiceScfFunctionName": argv.get("--ServiceScfFunctionName"),
        "ServiceWebsocketRegisterFunctionName": argv.get("--ServiceWebsocketRegisterFunctionName"),
        "ServiceWebsocketCleanupFunctionName": argv.get("--ServiceWebsocketCleanupFunctionName"),
        "ServiceWebsocketTransportFunctionName": argv.get("--ServiceWebsocketTransportFunctionName"),
        "ServiceScfFunctionNamespace": argv.get("--ServiceScfFunctionNamespace"),
        "ServiceScfFunctionQualifier": argv.get("--ServiceScfFunctionQualifier"),
        "ServiceWebsocketRegisterFunctionNamespace": argv.get("--ServiceWebsocketRegisterFunctionNamespace"),
        "ServiceWebsocketRegisterFunctionQualifier": argv.get("--ServiceWebsocketRegisterFunctionQualifier"),
        "ServiceWebsocketTransportFunctionNamespace": argv.get("--ServiceWebsocketTransportFunctionNamespace"),
        "ServiceWebsocketTransportFunctionQualifier": argv.get("--ServiceWebsocketTransportFunctionQualifier"),
        "ServiceWebsocketCleanupFunctionNamespace": argv.get("--ServiceWebsocketCleanupFunctionNamespace"),
        "ServiceWebsocketCleanupFunctionQualifier": argv.get("--ServiceWebsocketCleanupFunctionQualifier"),
        "ServiceScfIsIntegratedResponse": Utils.try_to_json(argv, "--ServiceScfIsIntegratedResponse"),
        "IsDebugAfterCharge": Utils.try_to_json(argv, "--IsDebugAfterCharge"),
        "TagSpecifications": Utils.try_to_json(argv, "--TagSpecifications"),
        "IsDeleteResponseErrorCodes": Utils.try_to_json(argv, "--IsDeleteResponseErrorCodes"),
        "ResponseType": argv.get("--ResponseType"),
        "ResponseSuccessExample": argv.get("--ResponseSuccessExample"),
        "ResponseFailExample": argv.get("--ResponseFailExample"),
        "ServiceConfig": Utils.try_to_json(argv, "--ServiceConfig"),
        "AuthRelationApiId": argv.get("--AuthRelationApiId"),
        "ServiceParameters": Utils.try_to_json(argv, "--ServiceParameters"),
        "OauthConfig": Utils.try_to_json(argv, "--OauthConfig"),
        "ResponseErrorCodes": Utils.try_to_json(argv, "--ResponseErrorCodes"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.ApigatewayClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyApiRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyApi(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDemoteServiceUsagePlan(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DemoteServiceUsagePlan", g_param[OptionsDefine.Version])
        return

    param = {
        "UsagePlanId": argv.get("--UsagePlanId"),
        "ServiceId": argv.get("--ServiceId"),
        "Environment": argv.get("--Environment"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.ApigatewayClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DemoteServiceUsagePlanRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DemoteServiceUsagePlan(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeApiKeysStatus(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeApiKeysStatus", g_param[OptionsDefine.Version])
        return

    param = {
        "Limit": Utils.try_to_json(argv, "--Limit"),
        "Offset": Utils.try_to_json(argv, "--Offset"),
        "Filters": Utils.try_to_json(argv, "--Filters"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.ApigatewayClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeApiKeysStatusRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeApiKeysStatus(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyApiEnvironmentStrategy(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyApiEnvironmentStrategy", g_param[OptionsDefine.Version])
        return

    param = {
        "ServiceId": argv.get("--ServiceId"),
        "Strategy": Utils.try_to_json(argv, "--Strategy"),
        "EnvironmentName": argv.get("--EnvironmentName"),
        "ApiIds": Utils.try_to_json(argv, "--ApiIds"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.ApigatewayClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyApiEnvironmentStrategyRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyApiEnvironmentStrategy(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyUsagePlan(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyUsagePlan", g_param[OptionsDefine.Version])
        return

    param = {
        "UsagePlanId": argv.get("--UsagePlanId"),
        "UsagePlanName": argv.get("--UsagePlanName"),
        "UsagePlanDesc": argv.get("--UsagePlanDesc"),
        "MaxRequestNum": Utils.try_to_json(argv, "--MaxRequestNum"),
        "MaxRequestNumPreSec": Utils.try_to_json(argv, "--MaxRequestNumPreSec"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.ApigatewayClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyUsagePlanRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyUsagePlan(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeLogSearch(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeLogSearch", g_param[OptionsDefine.Version])
        return

    param = {
        "StartTime": argv.get("--StartTime"),
        "EndTime": argv.get("--EndTime"),
        "ServiceId": argv.get("--ServiceId"),
        "Filters": Utils.try_to_json(argv, "--Filters"),
        "Limit": Utils.try_to_json(argv, "--Limit"),
        "ConText": argv.get("--ConText"),
        "Sort": argv.get("--Sort"),
        "Query": argv.get("--Query"),
        "LogQuerys": Utils.try_to_json(argv, "--LogQuerys"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.ApigatewayClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeLogSearchRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeLogSearch(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeUsagePlanSecretIds(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeUsagePlanSecretIds", g_param[OptionsDefine.Version])
        return

    param = {
        "UsagePlanId": argv.get("--UsagePlanId"),
        "Limit": Utils.try_to_json(argv, "--Limit"),
        "Offset": Utils.try_to_json(argv, "--Offset"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.ApigatewayClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeUsagePlanSecretIdsRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeUsagePlanSecretIds(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeServiceSubDomains(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeServiceSubDomains", g_param[OptionsDefine.Version])
        return

    param = {
        "ServiceId": argv.get("--ServiceId"),
        "Limit": Utils.try_to_json(argv, "--Limit"),
        "Offset": Utils.try_to_json(argv, "--Offset"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.ApigatewayClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeServiceSubDomainsRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeServiceSubDomains(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyIPStrategy(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyIPStrategy", g_param[OptionsDefine.Version])
        return

    param = {
        "ServiceId": argv.get("--ServiceId"),
        "StrategyId": argv.get("--StrategyId"),
        "StrategyData": argv.get("--StrategyData"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.ApigatewayClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyIPStrategyRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyIPStrategy(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteService(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteService", g_param[OptionsDefine.Version])
        return

    param = {
        "ServiceId": argv.get("--ServiceId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.ApigatewayClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteServiceRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeleteService(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doUnBindIPStrategy(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("UnBindIPStrategy", g_param[OptionsDefine.Version])
        return

    param = {
        "ServiceId": argv.get("--ServiceId"),
        "StrategyId": argv.get("--StrategyId"),
        "EnvironmentName": argv.get("--EnvironmentName"),
        "UnBindApiIds": Utils.try_to_json(argv, "--UnBindApiIds"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.ApigatewayClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.UnBindIPStrategyRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.UnBindIPStrategy(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doUpdateService(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("UpdateService", g_param[OptionsDefine.Version])
        return

    param = {
        "ServiceId": argv.get("--ServiceId"),
        "EnvironmentName": argv.get("--EnvironmentName"),
        "VersionName": argv.get("--VersionName"),
        "UpdateDesc": argv.get("--UpdateDesc"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.ApigatewayClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.UpdateServiceRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.UpdateService(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeIPStrategyApisStatus(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeIPStrategyApisStatus", g_param[OptionsDefine.Version])
        return

    param = {
        "ServiceId": argv.get("--ServiceId"),
        "StrategyId": argv.get("--StrategyId"),
        "EnvironmentName": argv.get("--EnvironmentName"),
        "Limit": Utils.try_to_json(argv, "--Limit"),
        "Offset": Utils.try_to_json(argv, "--Offset"),
        "Filters": Utils.try_to_json(argv, "--Filters"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.ApigatewayClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeIPStrategyApisStatusRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeIPStrategyApisStatus(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doUnReleaseService(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("UnReleaseService", g_param[OptionsDefine.Version])
        return

    param = {
        "ServiceId": argv.get("--ServiceId"),
        "EnvironmentName": argv.get("--EnvironmentName"),
        "ApiIds": Utils.try_to_json(argv, "--ApiIds"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.ApigatewayClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.UnReleaseServiceRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.UnReleaseService(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyApiIncrement(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyApiIncrement", g_param[OptionsDefine.Version])
        return

    param = {
        "ServiceId": argv.get("--ServiceId"),
        "ApiId": argv.get("--ApiId"),
        "BusinessType": argv.get("--BusinessType"),
        "PublicKey": argv.get("--PublicKey"),
        "LoginRedirectUrl": argv.get("--LoginRedirectUrl"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.ApigatewayClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyApiIncrementRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyApiIncrement(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeServiceEnvironmentReleaseHistory(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeServiceEnvironmentReleaseHistory", g_param[OptionsDefine.Version])
        return

    param = {
        "ServiceId": argv.get("--ServiceId"),
        "EnvironmentName": argv.get("--EnvironmentName"),
        "Limit": Utils.try_to_json(argv, "--Limit"),
        "Offset": Utils.try_to_json(argv, "--Offset"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.ApigatewayClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeServiceEnvironmentReleaseHistoryRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeServiceEnvironmentReleaseHistory(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeApiUsagePlan(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeApiUsagePlan", g_param[OptionsDefine.Version])
        return

    param = {
        "ServiceId": argv.get("--ServiceId"),
        "Limit": Utils.try_to_json(argv, "--Limit"),
        "Offset": Utils.try_to_json(argv, "--Offset"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.ApigatewayClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeApiUsagePlanRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeApiUsagePlan(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteApi(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteApi", g_param[OptionsDefine.Version])
        return

    param = {
        "ServiceId": argv.get("--ServiceId"),
        "ApiId": argv.get("--ApiId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.ApigatewayClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteApiRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeleteApi(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeIPStrategysStatus(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeIPStrategysStatus", g_param[OptionsDefine.Version])
        return

    param = {
        "ServiceId": argv.get("--ServiceId"),
        "Filters": Utils.try_to_json(argv, "--Filters"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.ApigatewayClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeIPStrategysStatusRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeIPStrategysStatus(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeServiceEnvironmentList(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeServiceEnvironmentList", g_param[OptionsDefine.Version])
        return

    param = {
        "ServiceId": argv.get("--ServiceId"),
        "Limit": Utils.try_to_json(argv, "--Limit"),
        "Offset": Utils.try_to_json(argv, "--Offset"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.ApigatewayClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeServiceEnvironmentListRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeServiceEnvironmentList(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeServiceUsagePlan(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeServiceUsagePlan", g_param[OptionsDefine.Version])
        return

    param = {
        "ServiceId": argv.get("--ServiceId"),
        "Limit": Utils.try_to_json(argv, "--Limit"),
        "Offset": Utils.try_to_json(argv, "--Offset"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.ApigatewayClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeServiceUsagePlanRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeServiceUsagePlan(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyServiceEnvironmentStrategy(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyServiceEnvironmentStrategy", g_param[OptionsDefine.Version])
        return

    param = {
        "ServiceId": argv.get("--ServiceId"),
        "Strategy": Utils.try_to_json(argv, "--Strategy"),
        "EnvironmentNames": Utils.try_to_json(argv, "--EnvironmentNames"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.ApigatewayClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyServiceEnvironmentStrategyRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyServiceEnvironmentStrategy(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateUsagePlan(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateUsagePlan", g_param[OptionsDefine.Version])
        return

    param = {
        "UsagePlanName": argv.get("--UsagePlanName"),
        "UsagePlanDesc": argv.get("--UsagePlanDesc"),
        "MaxRequestNum": Utils.try_to_json(argv, "--MaxRequestNum"),
        "MaxRequestNumPreSec": Utils.try_to_json(argv, "--MaxRequestNumPreSec"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.ApigatewayClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateUsagePlanRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateUsagePlan(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doUpdateApiKey(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("UpdateApiKey", g_param[OptionsDefine.Version])
        return

    param = {
        "AccessKeyId": argv.get("--AccessKeyId"),
        "AccessKeySecret": argv.get("--AccessKeySecret"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.ApigatewayClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.UpdateApiKeyRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.UpdateApiKey(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeServiceSubDomainMappings(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeServiceSubDomainMappings", g_param[OptionsDefine.Version])
        return

    param = {
        "ServiceId": argv.get("--ServiceId"),
        "SubDomain": argv.get("--SubDomain"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.ApigatewayClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeServiceSubDomainMappingsRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeServiceSubDomainMappings(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doBindEnvironment(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("BindEnvironment", g_param[OptionsDefine.Version])
        return

    param = {
        "UsagePlanIds": Utils.try_to_json(argv, "--UsagePlanIds"),
        "BindType": argv.get("--BindType"),
        "Environment": argv.get("--Environment"),
        "ServiceId": argv.get("--ServiceId"),
        "ApiIds": Utils.try_to_json(argv, "--ApiIds"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.ApigatewayClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.BindEnvironmentRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.BindEnvironment(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doUnBindSecretIds(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("UnBindSecretIds", g_param[OptionsDefine.Version])
        return

    param = {
        "UsagePlanId": argv.get("--UsagePlanId"),
        "AccessKeyIds": Utils.try_to_json(argv, "--AccessKeyIds"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.ApigatewayClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.UnBindSecretIdsRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.UnBindSecretIds(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doBindIPStrategy(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("BindIPStrategy", g_param[OptionsDefine.Version])
        return

    param = {
        "ServiceId": argv.get("--ServiceId"),
        "StrategyId": argv.get("--StrategyId"),
        "EnvironmentName": argv.get("--EnvironmentName"),
        "BindApiIds": Utils.try_to_json(argv, "--BindApiIds"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.ApigatewayClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.BindIPStrategyRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.BindIPStrategy(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeServicesStatus(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeServicesStatus", g_param[OptionsDefine.Version])
        return

    param = {
        "Limit": Utils.try_to_json(argv, "--Limit"),
        "Offset": Utils.try_to_json(argv, "--Offset"),
        "Filters": Utils.try_to_json(argv, "--Filters"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.ApigatewayClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeServicesStatusRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeServicesStatus(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeIPStrategy(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeIPStrategy", g_param[OptionsDefine.Version])
        return

    param = {
        "ServiceId": argv.get("--ServiceId"),
        "StrategyId": argv.get("--StrategyId"),
        "EnvironmentName": argv.get("--EnvironmentName"),
        "Limit": Utils.try_to_json(argv, "--Limit"),
        "Offset": Utils.try_to_json(argv, "--Offset"),
        "Filters": Utils.try_to_json(argv, "--Filters"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.ApigatewayClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeIPStrategyRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeIPStrategy(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeUsagePlanEnvironments(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeUsagePlanEnvironments", g_param[OptionsDefine.Version])
        return

    param = {
        "UsagePlanId": argv.get("--UsagePlanId"),
        "BindType": argv.get("--BindType"),
        "Limit": Utils.try_to_json(argv, "--Limit"),
        "Offset": Utils.try_to_json(argv, "--Offset"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.ApigatewayClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeUsagePlanEnvironmentsRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeUsagePlanEnvironments(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doEnableApiKey(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("EnableApiKey", g_param[OptionsDefine.Version])
        return

    param = {
        "AccessKeyId": argv.get("--AccessKeyId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.ApigatewayClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.EnableApiKeyRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.EnableApiKey(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateIPStrategy(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateIPStrategy", g_param[OptionsDefine.Version])
        return

    param = {
        "ServiceId": argv.get("--ServiceId"),
        "StrategyName": argv.get("--StrategyName"),
        "StrategyType": argv.get("--StrategyType"),
        "StrategyData": argv.get("--StrategyData"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.ApigatewayClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateIPStrategyRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateIPStrategy(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeServiceReleaseVersion(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeServiceReleaseVersion", g_param[OptionsDefine.Version])
        return

    param = {
        "ServiceId": argv.get("--ServiceId"),
        "Limit": Utils.try_to_json(argv, "--Limit"),
        "Offset": Utils.try_to_json(argv, "--Offset"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.ApigatewayClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeServiceReleaseVersionRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeServiceReleaseVersion(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeApisStatus(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeApisStatus", g_param[OptionsDefine.Version])
        return

    param = {
        "ServiceId": argv.get("--ServiceId"),
        "Offset": Utils.try_to_json(argv, "--Offset"),
        "Limit": Utils.try_to_json(argv, "--Limit"),
        "Filters": Utils.try_to_json(argv, "--Filters"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.ApigatewayClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeApisStatusRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeApisStatus(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateApiKey(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateApiKey", g_param[OptionsDefine.Version])
        return

    param = {
        "SecretName": argv.get("--SecretName"),
        "AccessKeyType": argv.get("--AccessKeyType"),
        "AccessKeyId": argv.get("--AccessKeyId"),
        "AccessKeySecret": argv.get("--AccessKeySecret"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.ApigatewayClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateApiKeyRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateApiKey(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifySubDomain(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifySubDomain", g_param[OptionsDefine.Version])
        return

    param = {
        "ServiceId": argv.get("--ServiceId"),
        "SubDomain": argv.get("--SubDomain"),
        "IsDefaultMapping": Utils.try_to_json(argv, "--IsDefaultMapping"),
        "CertificateId": argv.get("--CertificateId"),
        "Protocol": argv.get("--Protocol"),
        "PathMappingSet": Utils.try_to_json(argv, "--PathMappingSet"),
        "NetType": argv.get("--NetType"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.ApigatewayClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifySubDomainRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifySubDomain(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteIPStrategy(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteIPStrategy", g_param[OptionsDefine.Version])
        return

    param = {
        "ServiceId": argv.get("--ServiceId"),
        "StrategyId": argv.get("--StrategyId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.ApigatewayClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteIPStrategyRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeleteIPStrategy(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doReleaseService(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ReleaseService", g_param[OptionsDefine.Version])
        return

    param = {
        "ServiceId": argv.get("--ServiceId"),
        "EnvironmentName": argv.get("--EnvironmentName"),
        "ReleaseDesc": argv.get("--ReleaseDesc"),
        "ApiIds": Utils.try_to_json(argv, "--ApiIds"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.ApigatewayClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ReleaseServiceRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ReleaseService(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDisableApiKey(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DisableApiKey", g_param[OptionsDefine.Version])
        return

    param = {
        "AccessKeyId": argv.get("--AccessKeyId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.ApigatewayClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DisableApiKeyRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DisableApiKey(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyService(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyService", g_param[OptionsDefine.Version])
        return

    param = {
        "ServiceId": argv.get("--ServiceId"),
        "ServiceName": argv.get("--ServiceName"),
        "ServiceDesc": argv.get("--ServiceDesc"),
        "Protocol": argv.get("--Protocol"),
        "NetTypes": Utils.try_to_json(argv, "--NetTypes"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.ApigatewayClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyServiceRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyService(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doUnBindEnvironment(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("UnBindEnvironment", g_param[OptionsDefine.Version])
        return

    param = {
        "BindType": argv.get("--BindType"),
        "UsagePlanIds": Utils.try_to_json(argv, "--UsagePlanIds"),
        "Environment": argv.get("--Environment"),
        "ServiceId": argv.get("--ServiceId"),
        "ApiIds": Utils.try_to_json(argv, "--ApiIds"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.ApigatewayClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.UnBindEnvironmentRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.UnBindEnvironment(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeApiEnvironmentStrategy(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeApiEnvironmentStrategy", g_param[OptionsDefine.Version])
        return

    param = {
        "ServiceId": argv.get("--ServiceId"),
        "EnvironmentNames": Utils.try_to_json(argv, "--EnvironmentNames"),
        "ApiId": argv.get("--ApiId"),
        "Limit": Utils.try_to_json(argv, "--Limit"),
        "Offset": Utils.try_to_json(argv, "--Offset"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.ApigatewayClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeApiEnvironmentStrategyRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeApiEnvironmentStrategy(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doBindSecretIds(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("BindSecretIds", g_param[OptionsDefine.Version])
        return

    param = {
        "UsagePlanId": argv.get("--UsagePlanId"),
        "AccessKeyIds": Utils.try_to_json(argv, "--AccessKeyIds"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.ApigatewayClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.BindSecretIdsRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.BindSecretIds(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeServiceEnvironmentStrategy(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeServiceEnvironmentStrategy", g_param[OptionsDefine.Version])
        return

    param = {
        "ServiceId": argv.get("--ServiceId"),
        "Limit": Utils.try_to_json(argv, "--Limit"),
        "Offset": Utils.try_to_json(argv, "--Offset"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.ApigatewayClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeServiceEnvironmentStrategyRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeServiceEnvironmentStrategy(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeService(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeService", g_param[OptionsDefine.Version])
        return

    param = {
        "ServiceId": argv.get("--ServiceId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.ApigatewayClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeServiceRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeService(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteServiceSubDomainMapping(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteServiceSubDomainMapping", g_param[OptionsDefine.Version])
        return

    param = {
        "ServiceId": argv.get("--ServiceId"),
        "SubDomain": argv.get("--SubDomain"),
        "Environment": argv.get("--Environment"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.ApigatewayClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteServiceSubDomainMappingRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeleteServiceSubDomainMapping(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeApiKey(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeApiKey", g_param[OptionsDefine.Version])
        return

    param = {
        "AccessKeyId": argv.get("--AccessKeyId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.ApigatewayClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeApiKeyRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeApiKey(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeUsagePlan(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeUsagePlan", g_param[OptionsDefine.Version])
        return

    param = {
        "UsagePlanId": argv.get("--UsagePlanId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.ApigatewayClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeUsagePlanRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeUsagePlan(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doUnBindSubDomain(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("UnBindSubDomain", g_param[OptionsDefine.Version])
        return

    param = {
        "ServiceId": argv.get("--ServiceId"),
        "SubDomain": argv.get("--SubDomain"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.ApigatewayClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.UnBindSubDomainRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.UnBindSubDomain(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doBindSubDomain(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("BindSubDomain", g_param[OptionsDefine.Version])
        return

    param = {
        "ServiceId": argv.get("--ServiceId"),
        "SubDomain": argv.get("--SubDomain"),
        "Protocol": argv.get("--Protocol"),
        "NetType": argv.get("--NetType"),
        "IsDefaultMapping": Utils.try_to_json(argv, "--IsDefaultMapping"),
        "NetSubDomain": argv.get("--NetSubDomain"),
        "CertificateId": argv.get("--CertificateId"),
        "PathMappingSet": Utils.try_to_json(argv, "--PathMappingSet"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.ApigatewayClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.BindSubDomainRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.BindSubDomain(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeApi(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeApi", g_param[OptionsDefine.Version])
        return

    param = {
        "ServiceId": argv.get("--ServiceId"),
        "ApiId": argv.get("--ApiId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.ApigatewayClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeApiRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeApi(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteApiKey(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteApiKey", g_param[OptionsDefine.Version])
        return

    param = {
        "AccessKeyId": argv.get("--AccessKeyId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.ApigatewayClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteApiKeyRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeleteApiKey(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateApi(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateApi", g_param[OptionsDefine.Version])
        return

    param = {
        "ServiceId": argv.get("--ServiceId"),
        "ServiceType": argv.get("--ServiceType"),
        "ServiceTimeout": Utils.try_to_json(argv, "--ServiceTimeout"),
        "Protocol": argv.get("--Protocol"),
        "RequestConfig": Utils.try_to_json(argv, "--RequestConfig"),
        "ApiName": argv.get("--ApiName"),
        "ApiDesc": argv.get("--ApiDesc"),
        "ApiType": argv.get("--ApiType"),
        "AuthType": argv.get("--AuthType"),
        "EnableCORS": Utils.try_to_json(argv, "--EnableCORS"),
        "ConstantParameters": Utils.try_to_json(argv, "--ConstantParameters"),
        "RequestParameters": Utils.try_to_json(argv, "--RequestParameters"),
        "ApiBusinessType": argv.get("--ApiBusinessType"),
        "ServiceMockReturnMessage": argv.get("--ServiceMockReturnMessage"),
        "MicroServices": Utils.try_to_json(argv, "--MicroServices"),
        "ServiceTsfLoadBalanceConf": Utils.try_to_json(argv, "--ServiceTsfLoadBalanceConf"),
        "ServiceTsfHealthCheckConf": Utils.try_to_json(argv, "--ServiceTsfHealthCheckConf"),
        "TargetServices": Utils.try_to_json(argv, "--TargetServices"),
        "TargetServicesLoadBalanceConf": Utils.try_to_json(argv, "--TargetServicesLoadBalanceConf"),
        "TargetServicesHealthCheckConf": Utils.try_to_json(argv, "--TargetServicesHealthCheckConf"),
        "ServiceScfFunctionName": argv.get("--ServiceScfFunctionName"),
        "ServiceWebsocketRegisterFunctionName": argv.get("--ServiceWebsocketRegisterFunctionName"),
        "ServiceWebsocketCleanupFunctionName": argv.get("--ServiceWebsocketCleanupFunctionName"),
        "ServiceWebsocketTransportFunctionName": argv.get("--ServiceWebsocketTransportFunctionName"),
        "ServiceScfFunctionNamespace": argv.get("--ServiceScfFunctionNamespace"),
        "ServiceScfFunctionQualifier": argv.get("--ServiceScfFunctionQualifier"),
        "ServiceWebsocketRegisterFunctionNamespace": argv.get("--ServiceWebsocketRegisterFunctionNamespace"),
        "ServiceWebsocketRegisterFunctionQualifier": argv.get("--ServiceWebsocketRegisterFunctionQualifier"),
        "ServiceWebsocketTransportFunctionNamespace": argv.get("--ServiceWebsocketTransportFunctionNamespace"),
        "ServiceWebsocketTransportFunctionQualifier": argv.get("--ServiceWebsocketTransportFunctionQualifier"),
        "ServiceWebsocketCleanupFunctionNamespace": argv.get("--ServiceWebsocketCleanupFunctionNamespace"),
        "ServiceWebsocketCleanupFunctionQualifier": argv.get("--ServiceWebsocketCleanupFunctionQualifier"),
        "ServiceScfIsIntegratedResponse": Utils.try_to_json(argv, "--ServiceScfIsIntegratedResponse"),
        "IsDebugAfterCharge": Utils.try_to_json(argv, "--IsDebugAfterCharge"),
        "IsDeleteResponseErrorCodes": Utils.try_to_json(argv, "--IsDeleteResponseErrorCodes"),
        "ResponseType": argv.get("--ResponseType"),
        "ResponseSuccessExample": argv.get("--ResponseSuccessExample"),
        "ResponseFailExample": argv.get("--ResponseFailExample"),
        "ServiceConfig": Utils.try_to_json(argv, "--ServiceConfig"),
        "AuthRelationApiId": argv.get("--AuthRelationApiId"),
        "ServiceParameters": Utils.try_to_json(argv, "--ServiceParameters"),
        "OauthConfig": Utils.try_to_json(argv, "--OauthConfig"),
        "ResponseErrorCodes": Utils.try_to_json(argv, "--ResponseErrorCodes"),
        "TargetNamespaceId": argv.get("--TargetNamespaceId"),
        "UserType": argv.get("--UserType"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.ApigatewayClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateApiRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateApi(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doGenerateApiDocument(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("GenerateApiDocument", g_param[OptionsDefine.Version])
        return

    param = {
        "ServiceId": argv.get("--ServiceId"),
        "GenEnvironment": argv.get("--GenEnvironment"),
        "GenLanguage": argv.get("--GenLanguage"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.ApigatewayClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.GenerateApiDocumentRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.GenerateApiDocument(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


CLIENT_MAP = {
    "v20180808": apigateway_client_v20180808,

}

MODELS_MAP = {
    "v20180808": models_v20180808,

}

ACTION_MAP = {
    "CreateService": doCreateService,
    "DescribeUsagePlansStatus": doDescribeUsagePlansStatus,
    "DeleteUsagePlan": doDeleteUsagePlan,
    "ModifyApi": doModifyApi,
    "DemoteServiceUsagePlan": doDemoteServiceUsagePlan,
    "DescribeApiKeysStatus": doDescribeApiKeysStatus,
    "ModifyApiEnvironmentStrategy": doModifyApiEnvironmentStrategy,
    "ModifyUsagePlan": doModifyUsagePlan,
    "DescribeLogSearch": doDescribeLogSearch,
    "DescribeUsagePlanSecretIds": doDescribeUsagePlanSecretIds,
    "DescribeServiceSubDomains": doDescribeServiceSubDomains,
    "ModifyIPStrategy": doModifyIPStrategy,
    "DeleteService": doDeleteService,
    "UnBindIPStrategy": doUnBindIPStrategy,
    "UpdateService": doUpdateService,
    "DescribeIPStrategyApisStatus": doDescribeIPStrategyApisStatus,
    "UnReleaseService": doUnReleaseService,
    "ModifyApiIncrement": doModifyApiIncrement,
    "DescribeServiceEnvironmentReleaseHistory": doDescribeServiceEnvironmentReleaseHistory,
    "DescribeApiUsagePlan": doDescribeApiUsagePlan,
    "DeleteApi": doDeleteApi,
    "DescribeIPStrategysStatus": doDescribeIPStrategysStatus,
    "DescribeServiceEnvironmentList": doDescribeServiceEnvironmentList,
    "DescribeServiceUsagePlan": doDescribeServiceUsagePlan,
    "ModifyServiceEnvironmentStrategy": doModifyServiceEnvironmentStrategy,
    "CreateUsagePlan": doCreateUsagePlan,
    "UpdateApiKey": doUpdateApiKey,
    "DescribeServiceSubDomainMappings": doDescribeServiceSubDomainMappings,
    "BindEnvironment": doBindEnvironment,
    "UnBindSecretIds": doUnBindSecretIds,
    "BindIPStrategy": doBindIPStrategy,
    "DescribeServicesStatus": doDescribeServicesStatus,
    "DescribeIPStrategy": doDescribeIPStrategy,
    "DescribeUsagePlanEnvironments": doDescribeUsagePlanEnvironments,
    "EnableApiKey": doEnableApiKey,
    "CreateIPStrategy": doCreateIPStrategy,
    "DescribeServiceReleaseVersion": doDescribeServiceReleaseVersion,
    "DescribeApisStatus": doDescribeApisStatus,
    "CreateApiKey": doCreateApiKey,
    "ModifySubDomain": doModifySubDomain,
    "DeleteIPStrategy": doDeleteIPStrategy,
    "ReleaseService": doReleaseService,
    "DisableApiKey": doDisableApiKey,
    "ModifyService": doModifyService,
    "UnBindEnvironment": doUnBindEnvironment,
    "DescribeApiEnvironmentStrategy": doDescribeApiEnvironmentStrategy,
    "BindSecretIds": doBindSecretIds,
    "DescribeServiceEnvironmentStrategy": doDescribeServiceEnvironmentStrategy,
    "DescribeService": doDescribeService,
    "DeleteServiceSubDomainMapping": doDeleteServiceSubDomainMapping,
    "DescribeApiKey": doDescribeApiKey,
    "DescribeUsagePlan": doDescribeUsagePlan,
    "UnBindSubDomain": doUnBindSubDomain,
    "BindSubDomain": doBindSubDomain,
    "DescribeApi": doDescribeApi,
    "DeleteApiKey": doDeleteApiKey,
    "CreateApi": doCreateApi,
    "GenerateApiDocument": doGenerateApiDocument,

}

AVAILABLE_VERSION_LIST = [
    v20180808.version,

]
AVAILABLE_VERSIONS = {
     'v' + v20180808.version.replace('-', ''): {"help": v20180808_help.INFO,"desc": v20180808_help.DESC},

}


def apigateway_action(argv, arglist):
    if "help" in argv:
        versions = sorted(AVAILABLE_VERSIONS.keys())
        opt_v = "--" + OptionsDefine.Version
        version = versions[-1]
        if opt_v in argv:
            version = 'v' + argv[opt_v].replace('-', '')
        if version not in versions:
            print("available versions: %s" % " ".join(AVAILABLE_VERSION_LIST))
            return
        action_str = ""
        docs = AVAILABLE_VERSIONS[version]["help"]
        desc = AVAILABLE_VERSIONS[version]["desc"]
        for action, info in docs.items():
            action_str += "        %s\n" % action
            action_str += Utils.split_str("        ", info["desc"], 120)
        helpstr = HelpTemplate.SERVICE % {"name": "apigateway", "desc": desc, "actions": action_str}
        print(helpstr)
    else:
        print(ErrorMsg.FEW_ARG)


def version_merge():
    help_merge = {}
    for v in AVAILABLE_VERSIONS:
        for action in AVAILABLE_VERSIONS[v]["help"]:
            if action not in help_merge:
                help_merge[action] = {}
            help_merge[action]["cb"] = ACTION_MAP[action]
            help_merge[action]["params"] = []
            for param in AVAILABLE_VERSIONS[v]["help"][action]["params"]:
                if param["name"] not in help_merge[action]["params"]:
                    help_merge[action]["params"].append(param["name"])
    return help_merge


def register_arg(command):
    cmd = NiceCommand("apigateway", apigateway_action)
    command.reg_cmd(cmd)
    cmd.reg_opt("help", "bool")
    cmd.reg_opt(OptionsDefine.Version, "string")
    help_merge = version_merge()

    for actionName, action in help_merge.items():
        c = NiceCommand(actionName, action["cb"])
        cmd.reg_cmd(c)
        c.reg_opt("help", "bool")
        for param in action["params"]:
            c.reg_opt("--" + param, "string")

        for opt in OptionsDefine.ACTION_GLOBAL_OPT:
            stropt = "--" + opt
            c.reg_opt(stropt, "string")


def parse_global_arg(argv):
    params = {}
    for opt in OptionsDefine.ACTION_GLOBAL_OPT:
        stropt = "--" + opt
        if stropt in argv:
            params[opt] = argv[stropt]
        else:
            params[opt] = None
    if params[OptionsDefine.Version]:
        params[OptionsDefine.Version] = "v" + params[OptionsDefine.Version].replace('-', '')

    config_handle = Configure()
    profile = config_handle.profile
    if ("--" + OptionsDefine.Profile) in argv:
        profile = argv[("--" + OptionsDefine.Profile)]

    is_conexist, conf_path = config_handle._profile_existed(profile + "." + config_handle.configure)
    is_creexist, cred_path = config_handle._profile_existed(profile + "." + config_handle.credential)
    config = {}
    cred = {}
    if is_conexist:
        config = config_handle._load_json_msg(conf_path)
    if is_creexist:
        cred = config_handle._load_json_msg(cred_path)
    if os.environ.get(OptionsDefine.ENV_SECRET_ID):
        cred[OptionsDefine.SecretId] = os.environ.get(OptionsDefine.ENV_SECRET_ID)
    if os.environ.get(OptionsDefine.ENV_SECRET_KEY):
        cred[OptionsDefine.SecretKey] = os.environ.get(OptionsDefine.ENV_SECRET_KEY)
    if os.environ.get(OptionsDefine.ENV_REGION):
        config[OptionsDefine.Region] = os.environ.get(OptionsDefine.ENV_REGION)

    for param in params.keys():
        if param == OptionsDefine.Version:
            continue
        if params[param] is None:
            if param in [OptionsDefine.SecretKey, OptionsDefine.SecretId]:
                if param in cred:
                    params[param] = cred[param]
                else:
                    raise Exception("%s is invalid" % param)
            else:
                if param in config:
                    params[param] = config[param]
                elif param == OptionsDefine.Region:
                    raise Exception("%s is invalid" % OptionsDefine.Region)
    try:
        if params[OptionsDefine.Version] is None:
            version = config["apigateway"][OptionsDefine.Version]
            params[OptionsDefine.Version] = "v" + version.replace('-', '')

        if params[OptionsDefine.Endpoint] is None:
            params[OptionsDefine.Endpoint] = config["apigateway"][OptionsDefine.Endpoint]
    except Exception as err:
        raise Exception("config file:%s error, %s" % (conf_path, str(err)))
    versions = sorted(AVAILABLE_VERSIONS.keys())
    if params[OptionsDefine.Version] not in versions:
        raise Exception("available versions: %s" % " ".join(AVAILABLE_VERSION_LIST))
    return params


def show_help(action, version):
    docs = AVAILABLE_VERSIONS[version]["help"][action]
    desc = AVAILABLE_VERSIONS[version]["desc"]
    docstr = ""
    for param in docs["params"]:
        docstr += "        %s\n" % ("--" + param["name"])
        docstr += Utils.split_str("        ", param["desc"], 120)

    helpmsg = HelpTemplate.ACTION % {"name": action, "service": "apigateway", "desc": desc, "params": docstr}
    print(helpmsg)


def get_actions_info():
    config = Configure()
    new_version = max(AVAILABLE_VERSIONS.keys())
    version = new_version
    try:
        profile = config._load_json_msg(os.path.join(config.cli_path, "default.configure"))
        version = profile["apigateway"]["version"]
        version = "v" + version.replace('-', '')
    except Exception:
        pass
    if version not in AVAILABLE_VERSIONS.keys():
        version = new_version
    return AVAILABLE_VERSIONS[version]["help"]
