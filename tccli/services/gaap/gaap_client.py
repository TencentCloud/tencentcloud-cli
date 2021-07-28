# -*- coding: utf-8 -*-
import os
import json
import tccli.options_define as OptionsDefine
import tccli.format_output as FormatOutput
from tccli import __version__
from tccli.utils import Utils
from tccli.exceptions import ConfigurationError
from tencentcloud.common import credential
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.gaap.v20180529 import gaap_client as gaap_client_v20180529
from tencentcloud.gaap.v20180529 import models as models_v20180529


def doDescribeCertificates(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GaapClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeCertificatesRequest()
    model.from_json_string(json.dumps(args))
    rsp = client.DescribeCertificates(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateSecurityRules(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GaapClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateSecurityRulesRequest()
    model.from_json_string(json.dumps(args))
    rsp = client.CreateSecurityRules(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeHTTPSListeners(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GaapClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeHTTPSListenersRequest()
    model.from_json_string(json.dumps(args))
    rsp = client.DescribeHTTPSListeners(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteSecurityPolicy(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GaapClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteSecurityPolicyRequest()
    model.from_json_string(json.dumps(args))
    rsp = client.DeleteSecurityPolicy(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeBlackHeader(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GaapClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeBlackHeaderRequest()
    model.from_json_string(json.dumps(args))
    rsp = client.DescribeBlackHeader(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeCountryAreaMapping(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GaapClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeCountryAreaMappingRequest()
    model.from_json_string(json.dumps(args))
    rsp = client.DescribeCountryAreaMapping(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyHTTPListenerAttribute(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GaapClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyHTTPListenerAttributeRequest()
    model.from_json_string(json.dumps(args))
    rsp = client.ModifyHTTPListenerAttribute(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyCertificateAttributes(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GaapClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyCertificateAttributesRequest()
    model.from_json_string(json.dumps(args))
    rsp = client.ModifyCertificateAttributes(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateCustomHeader(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GaapClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateCustomHeaderRequest()
    model.from_json_string(json.dumps(args))
    rsp = client.CreateCustomHeader(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeGroupAndStatisticsProxy(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GaapClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeGroupAndStatisticsProxyRequest()
    model.from_json_string(json.dumps(args))
    rsp = client.DescribeGroupAndStatisticsProxy(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCloseSecurityPolicy(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GaapClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CloseSecurityPolicyRequest()
    model.from_json_string(json.dumps(args))
    rsp = client.CloseSecurityPolicy(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateProxyGroupDomain(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GaapClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateProxyGroupDomainRequest()
    model.from_json_string(json.dumps(args))
    rsp = client.CreateProxyGroupDomain(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeDestRegions(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GaapClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeDestRegionsRequest()
    model.from_json_string(json.dumps(args))
    rsp = client.DescribeDestRegions(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateUDPListeners(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GaapClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateUDPListenersRequest()
    model.from_json_string(json.dumps(args))
    rsp = client.CreateUDPListeners(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeProxyDetail(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GaapClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeProxyDetailRequest()
    model.from_json_string(json.dumps(args))
    rsp = client.DescribeProxyDetail(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeRuleRealServers(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GaapClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeRuleRealServersRequest()
    model.from_json_string(json.dumps(args))
    rsp = client.DescribeRuleRealServers(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeUDPListeners(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GaapClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeUDPListenersRequest()
    model.from_json_string(json.dumps(args))
    rsp = client.DescribeUDPListeners(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDestroyProxies(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GaapClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DestroyProxiesRequest()
    model.from_json_string(json.dumps(args))
    rsp = client.DestroyProxies(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeRulesByRuleIds(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GaapClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeRulesByRuleIdsRequest()
    model.from_json_string(json.dumps(args))
    rsp = client.DescribeRulesByRuleIds(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeProxyGroupList(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GaapClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeProxyGroupListRequest()
    model.from_json_string(json.dumps(args))
    rsp = client.DescribeProxyGroupList(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doOpenSecurityPolicy(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GaapClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.OpenSecurityPolicyRequest()
    model.from_json_string(json.dumps(args))
    rsp = client.OpenSecurityPolicy(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteDomainErrorPageInfo(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GaapClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteDomainErrorPageInfoRequest()
    model.from_json_string(json.dumps(args))
    rsp = client.DeleteDomainErrorPageInfo(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyCertificate(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GaapClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyCertificateRequest()
    model.from_json_string(json.dumps(args))
    rsp = client.ModifyCertificate(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateDomainErrorPageInfo(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GaapClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateDomainErrorPageInfoRequest()
    model.from_json_string(json.dumps(args))
    rsp = client.CreateDomainErrorPageInfo(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeProxyGroupStatistics(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GaapClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeProxyGroupStatisticsRequest()
    model.from_json_string(json.dumps(args))
    rsp = client.DescribeProxyGroupStatistics(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyRealServerName(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GaapClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyRealServerNameRequest()
    model.from_json_string(json.dumps(args))
    rsp = client.ModifyRealServerName(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doBindListenerRealServers(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GaapClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.BindListenerRealServersRequest()
    model.from_json_string(json.dumps(args))
    rsp = client.BindListenerRealServers(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeProxyGroupDetails(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GaapClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeProxyGroupDetailsRequest()
    model.from_json_string(json.dumps(args))
    rsp = client.DescribeProxyGroupDetails(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteSecurityRules(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GaapClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteSecurityRulesRequest()
    model.from_json_string(json.dumps(args))
    rsp = client.DeleteSecurityRules(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteCertificate(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GaapClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteCertificateRequest()
    model.from_json_string(json.dumps(args))
    rsp = client.DeleteCertificate(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeAccessRegionsByDestRegion(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GaapClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeAccessRegionsByDestRegionRequest()
    model.from_json_string(json.dumps(args))
    rsp = client.DescribeAccessRegionsByDestRegion(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyGroupDomainConfig(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GaapClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyGroupDomainConfigRequest()
    model.from_json_string(json.dumps(args))
    rsp = client.ModifyGroupDomainConfig(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeTCPListeners(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GaapClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeTCPListenersRequest()
    model.from_json_string(json.dumps(args))
    rsp = client.DescribeTCPListeners(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeRealServers(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GaapClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeRealServersRequest()
    model.from_json_string(json.dumps(args))
    rsp = client.DescribeRealServers(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeProxyAndStatisticsListeners(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GaapClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeProxyAndStatisticsListenersRequest()
    model.from_json_string(json.dumps(args))
    rsp = client.DescribeProxyAndStatisticsListeners(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateHTTPListener(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GaapClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateHTTPListenerRequest()
    model.from_json_string(json.dumps(args))
    rsp = client.CreateHTTPListener(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeSecurityRules(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GaapClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeSecurityRulesRequest()
    model.from_json_string(json.dumps(args))
    rsp = client.DescribeSecurityRules(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyProxyConfiguration(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GaapClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyProxyConfigurationRequest()
    model.from_json_string(json.dumps(args))
    rsp = client.ModifyProxyConfiguration(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCloseProxyGroup(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GaapClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CloseProxyGroupRequest()
    model.from_json_string(json.dumps(args))
    rsp = client.CloseProxyGroup(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyTCPListenerAttribute(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GaapClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyTCPListenerAttributeRequest()
    model.from_json_string(json.dumps(args))
    rsp = client.ModifyTCPListenerAttribute(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeRealServerStatistics(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GaapClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeRealServerStatisticsRequest()
    model.from_json_string(json.dumps(args))
    rsp = client.DescribeRealServerStatistics(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeHTTPListeners(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GaapClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeHTTPListenersRequest()
    model.from_json_string(json.dumps(args))
    rsp = client.DescribeHTTPListeners(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateProxyGroup(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GaapClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateProxyGroupRequest()
    model.from_json_string(json.dumps(args))
    rsp = client.CreateProxyGroup(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateCertificate(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GaapClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateCertificateRequest()
    model.from_json_string(json.dumps(args))
    rsp = client.CreateCertificate(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeCustomHeader(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GaapClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeCustomHeaderRequest()
    model.from_json_string(json.dumps(args))
    rsp = client.DescribeCustomHeader(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyProxiesAttribute(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GaapClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyProxiesAttributeRequest()
    model.from_json_string(json.dumps(args))
    rsp = client.ModifyProxiesAttribute(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateProxy(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GaapClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateProxyRequest()
    model.from_json_string(json.dumps(args))
    rsp = client.CreateProxy(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteDomain(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GaapClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteDomainRequest()
    model.from_json_string(json.dumps(args))
    rsp = client.DeleteDomain(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeSecurityPolicyDetail(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GaapClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeSecurityPolicyDetailRequest()
    model.from_json_string(json.dumps(args))
    rsp = client.DescribeSecurityPolicyDetail(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doRemoveRealServers(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GaapClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.RemoveRealServersRequest()
    model.from_json_string(json.dumps(args))
    rsp = client.RemoveRealServers(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateSecurityPolicy(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GaapClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateSecurityPolicyRequest()
    model.from_json_string(json.dumps(args))
    rsp = client.CreateSecurityPolicy(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteRule(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GaapClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteRuleRequest()
    model.from_json_string(json.dumps(args))
    rsp = client.DeleteRule(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateRule(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GaapClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateRuleRequest()
    model.from_json_string(json.dumps(args))
    rsp = client.CreateRule(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyDomain(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GaapClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyDomainRequest()
    model.from_json_string(json.dumps(args))
    rsp = client.ModifyDomain(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doOpenProxies(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GaapClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.OpenProxiesRequest()
    model.from_json_string(json.dumps(args))
    rsp = client.OpenProxies(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyUDPListenerAttribute(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GaapClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyUDPListenerAttributeRequest()
    model.from_json_string(json.dumps(args))
    rsp = client.ModifyUDPListenerAttribute(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doSetAuthentication(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GaapClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.SetAuthenticationRequest()
    model.from_json_string(json.dumps(args))
    rsp = client.SetAuthentication(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeProxies(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GaapClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeProxiesRequest()
    model.from_json_string(json.dumps(args))
    rsp = client.DescribeProxies(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteProxyGroup(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GaapClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteProxyGroupRequest()
    model.from_json_string(json.dumps(args))
    rsp = client.DeleteProxyGroup(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyProxiesProject(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GaapClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyProxiesProjectRequest()
    model.from_json_string(json.dumps(args))
    rsp = client.ModifyProxiesProject(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doAddRealServers(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GaapClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.AddRealServersRequest()
    model.from_json_string(json.dumps(args))
    rsp = client.AddRealServers(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateDomain(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GaapClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateDomainRequest()
    model.from_json_string(json.dumps(args))
    rsp = client.CreateDomain(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeCertificateDetail(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GaapClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeCertificateDetailRequest()
    model.from_json_string(json.dumps(args))
    rsp = client.DescribeCertificateDetail(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeRegionAndPrice(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GaapClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeRegionAndPriceRequest()
    model.from_json_string(json.dumps(args))
    rsp = client.DescribeRegionAndPrice(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeRealServersStatus(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GaapClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeRealServersStatusRequest()
    model.from_json_string(json.dumps(args))
    rsp = client.DescribeRealServersStatus(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeRules(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GaapClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeRulesRequest()
    model.from_json_string(json.dumps(args))
    rsp = client.DescribeRules(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeListenerRealServers(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GaapClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeListenerRealServersRequest()
    model.from_json_string(json.dumps(args))
    rsp = client.DescribeListenerRealServers(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateHTTPSListener(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GaapClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateHTTPSListenerRequest()
    model.from_json_string(json.dumps(args))
    rsp = client.CreateHTTPSListener(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCheckProxyCreate(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GaapClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CheckProxyCreateRequest()
    model.from_json_string(json.dumps(args))
    rsp = client.CheckProxyCreate(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doOpenProxyGroup(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GaapClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.OpenProxyGroupRequest()
    model.from_json_string(json.dumps(args))
    rsp = client.OpenProxyGroup(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeAccessRegions(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GaapClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeAccessRegionsRequest()
    model.from_json_string(json.dumps(args))
    rsp = client.DescribeAccessRegions(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyRuleAttribute(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GaapClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyRuleAttributeRequest()
    model.from_json_string(json.dumps(args))
    rsp = client.ModifyRuleAttribute(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeGroupDomainConfig(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GaapClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeGroupDomainConfigRequest()
    model.from_json_string(json.dumps(args))
    rsp = client.DescribeGroupDomainConfig(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyHTTPSListenerAttribute(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GaapClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyHTTPSListenerAttributeRequest()
    model.from_json_string(json.dumps(args))
    rsp = client.ModifyHTTPSListenerAttribute(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeListenerStatistics(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GaapClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeListenerStatisticsRequest()
    model.from_json_string(json.dumps(args))
    rsp = client.DescribeListenerStatistics(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteListeners(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GaapClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteListenersRequest()
    model.from_json_string(json.dumps(args))
    rsp = client.DeleteListeners(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeProxyStatistics(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GaapClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeProxyStatisticsRequest()
    model.from_json_string(json.dumps(args))
    rsp = client.DescribeProxyStatistics(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeDomainErrorPageInfo(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GaapClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeDomainErrorPageInfoRequest()
    model.from_json_string(json.dumps(args))
    rsp = client.DescribeDomainErrorPageInfo(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyProxyGroupAttribute(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GaapClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyProxyGroupAttributeRequest()
    model.from_json_string(json.dumps(args))
    rsp = client.ModifyProxyGroupAttribute(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doInquiryPriceCreateProxy(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GaapClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.InquiryPriceCreateProxyRequest()
    model.from_json_string(json.dumps(args))
    rsp = client.InquiryPriceCreateProxy(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifySecurityRule(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GaapClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifySecurityRuleRequest()
    model.from_json_string(json.dumps(args))
    rsp = client.ModifySecurityRule(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCloseProxies(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GaapClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CloseProxiesRequest()
    model.from_json_string(json.dumps(args))
    rsp = client.CloseProxies(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeDomainErrorPageInfoByIds(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GaapClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeDomainErrorPageInfoByIdsRequest()
    model.from_json_string(json.dumps(args))
    rsp = client.DescribeDomainErrorPageInfoByIds(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeProxiesStatus(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GaapClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeProxiesStatusRequest()
    model.from_json_string(json.dumps(args))
    rsp = client.DescribeProxiesStatus(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateTCPListeners(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GaapClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateTCPListenersRequest()
    model.from_json_string(json.dumps(args))
    rsp = client.CreateTCPListeners(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doBindRuleRealServers(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GaapClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.BindRuleRealServersRequest()
    model.from_json_string(json.dumps(args))
    rsp = client.BindRuleRealServers(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeResourcesByTag(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.GaapClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeResourcesByTagRequest()
    model.from_json_string(json.dumps(args))
    rsp = client.DescribeResourcesByTag(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


CLIENT_MAP = {
    "v20180529": gaap_client_v20180529,

}

MODELS_MAP = {
    "v20180529": models_v20180529,

}

ACTION_MAP = {
    "DescribeCertificates": doDescribeCertificates,
    "CreateSecurityRules": doCreateSecurityRules,
    "DescribeHTTPSListeners": doDescribeHTTPSListeners,
    "DeleteSecurityPolicy": doDeleteSecurityPolicy,
    "DescribeBlackHeader": doDescribeBlackHeader,
    "DescribeCountryAreaMapping": doDescribeCountryAreaMapping,
    "ModifyHTTPListenerAttribute": doModifyHTTPListenerAttribute,
    "ModifyCertificateAttributes": doModifyCertificateAttributes,
    "CreateCustomHeader": doCreateCustomHeader,
    "DescribeGroupAndStatisticsProxy": doDescribeGroupAndStatisticsProxy,
    "CloseSecurityPolicy": doCloseSecurityPolicy,
    "CreateProxyGroupDomain": doCreateProxyGroupDomain,
    "DescribeDestRegions": doDescribeDestRegions,
    "CreateUDPListeners": doCreateUDPListeners,
    "DescribeProxyDetail": doDescribeProxyDetail,
    "DescribeRuleRealServers": doDescribeRuleRealServers,
    "DescribeUDPListeners": doDescribeUDPListeners,
    "DestroyProxies": doDestroyProxies,
    "DescribeRulesByRuleIds": doDescribeRulesByRuleIds,
    "DescribeProxyGroupList": doDescribeProxyGroupList,
    "OpenSecurityPolicy": doOpenSecurityPolicy,
    "DeleteDomainErrorPageInfo": doDeleteDomainErrorPageInfo,
    "ModifyCertificate": doModifyCertificate,
    "CreateDomainErrorPageInfo": doCreateDomainErrorPageInfo,
    "DescribeProxyGroupStatistics": doDescribeProxyGroupStatistics,
    "ModifyRealServerName": doModifyRealServerName,
    "BindListenerRealServers": doBindListenerRealServers,
    "DescribeProxyGroupDetails": doDescribeProxyGroupDetails,
    "DeleteSecurityRules": doDeleteSecurityRules,
    "DeleteCertificate": doDeleteCertificate,
    "DescribeAccessRegionsByDestRegion": doDescribeAccessRegionsByDestRegion,
    "ModifyGroupDomainConfig": doModifyGroupDomainConfig,
    "DescribeTCPListeners": doDescribeTCPListeners,
    "DescribeRealServers": doDescribeRealServers,
    "DescribeProxyAndStatisticsListeners": doDescribeProxyAndStatisticsListeners,
    "CreateHTTPListener": doCreateHTTPListener,
    "DescribeSecurityRules": doDescribeSecurityRules,
    "ModifyProxyConfiguration": doModifyProxyConfiguration,
    "CloseProxyGroup": doCloseProxyGroup,
    "ModifyTCPListenerAttribute": doModifyTCPListenerAttribute,
    "DescribeRealServerStatistics": doDescribeRealServerStatistics,
    "DescribeHTTPListeners": doDescribeHTTPListeners,
    "CreateProxyGroup": doCreateProxyGroup,
    "CreateCertificate": doCreateCertificate,
    "DescribeCustomHeader": doDescribeCustomHeader,
    "ModifyProxiesAttribute": doModifyProxiesAttribute,
    "CreateProxy": doCreateProxy,
    "DeleteDomain": doDeleteDomain,
    "DescribeSecurityPolicyDetail": doDescribeSecurityPolicyDetail,
    "RemoveRealServers": doRemoveRealServers,
    "CreateSecurityPolicy": doCreateSecurityPolicy,
    "DeleteRule": doDeleteRule,
    "CreateRule": doCreateRule,
    "ModifyDomain": doModifyDomain,
    "OpenProxies": doOpenProxies,
    "ModifyUDPListenerAttribute": doModifyUDPListenerAttribute,
    "SetAuthentication": doSetAuthentication,
    "DescribeProxies": doDescribeProxies,
    "DeleteProxyGroup": doDeleteProxyGroup,
    "ModifyProxiesProject": doModifyProxiesProject,
    "AddRealServers": doAddRealServers,
    "CreateDomain": doCreateDomain,
    "DescribeCertificateDetail": doDescribeCertificateDetail,
    "DescribeRegionAndPrice": doDescribeRegionAndPrice,
    "DescribeRealServersStatus": doDescribeRealServersStatus,
    "DescribeRules": doDescribeRules,
    "DescribeListenerRealServers": doDescribeListenerRealServers,
    "CreateHTTPSListener": doCreateHTTPSListener,
    "CheckProxyCreate": doCheckProxyCreate,
    "OpenProxyGroup": doOpenProxyGroup,
    "DescribeAccessRegions": doDescribeAccessRegions,
    "ModifyRuleAttribute": doModifyRuleAttribute,
    "DescribeGroupDomainConfig": doDescribeGroupDomainConfig,
    "ModifyHTTPSListenerAttribute": doModifyHTTPSListenerAttribute,
    "DescribeListenerStatistics": doDescribeListenerStatistics,
    "DeleteListeners": doDeleteListeners,
    "DescribeProxyStatistics": doDescribeProxyStatistics,
    "DescribeDomainErrorPageInfo": doDescribeDomainErrorPageInfo,
    "ModifyProxyGroupAttribute": doModifyProxyGroupAttribute,
    "InquiryPriceCreateProxy": doInquiryPriceCreateProxy,
    "ModifySecurityRule": doModifySecurityRule,
    "CloseProxies": doCloseProxies,
    "DescribeDomainErrorPageInfoByIds": doDescribeDomainErrorPageInfoByIds,
    "DescribeProxiesStatus": doDescribeProxiesStatus,
    "CreateTCPListeners": doCreateTCPListeners,
    "BindRuleRealServers": doBindRuleRealServers,
    "DescribeResourcesByTag": doDescribeResourcesByTag,

}

AVAILABLE_VERSION_LIST = [
    "v20180529",

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

    for param in g_param.keys():
        if g_param[param] is None:
            if param in [OptionsDefine.SecretKey, OptionsDefine.SecretId, OptionsDefine.Token]:
                if param in cred:
                    g_param[param] = cred[param]
                else:
                    raise ConfigurationError("%s is invalid" % param)
            elif param in [OptionsDefine.Region, OptionsDefine.Output]:
                if param in conf:
                    g_param[param] = conf[param]
                else:
                    raise ConfigurationError("%s is invalid" % param)

    try:
        if g_param[OptionsDefine.ServiceVersion]:
            g_param[OptionsDefine.Version] = "v" + g_param[OptionsDefine.ServiceVersion].replace('-', '')
        else:
            version = conf["gaap"][OptionsDefine.Version]
            g_param[OptionsDefine.Version] = "v" + version.replace('-', '')

        if g_param[OptionsDefine.Endpoint] is None:
            g_param[OptionsDefine.Endpoint] = conf["gaap"][OptionsDefine.Endpoint]
    except Exception as err:
        raise ConfigurationError("config file:%s error, %s" % (conf_path, str(err)))

    if g_param[OptionsDefine.Version] not in AVAILABLE_VERSION_LIST:
        raise Exception("available versions: %s" % " ".join(AVAILABLE_VERSION_LIST))

    return g_param

