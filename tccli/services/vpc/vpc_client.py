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
from tencentcloud.vpc.v20170312 import vpc_client as vpc_client_v20170312
from tencentcloud.vpc.v20170312 import models as models_v20170312
from tccli.services.vpc import v20170312
from tccli.services.vpc.v20170312 import help as v20170312_help


def doDescribeVpcResourceDashboard(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeVpcResourceDashboard", g_param[OptionsDefine.Version])
        return

    param = {
        "VpcIds": Utils.try_to_json(argv, "--VpcIds"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeVpcResourceDashboardRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeVpcResourceDashboard(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeCcnRegionBandwidthLimits(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeCcnRegionBandwidthLimits", g_param[OptionsDefine.Version])
        return

    param = {
        "CcnId": argv.get("--CcnId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeCcnRegionBandwidthLimitsRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeCcnRegionBandwidthLimits(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeCustomerGateways(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeCustomerGateways", g_param[OptionsDefine.Version])
        return

    param = {
        "CustomerGatewayIds": Utils.try_to_json(argv, "--CustomerGatewayIds"),
        "Filters": Utils.try_to_json(argv, "--Filters"),
        "Offset": Utils.try_to_json(argv, "--Offset"),
        "Limit": Utils.try_to_json(argv, "--Limit"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeCustomerGatewaysRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeCustomerGateways(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doReplaceSecurityGroupPolicy(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ReplaceSecurityGroupPolicy", g_param[OptionsDefine.Version])
        return

    param = {
        "SecurityGroupId": argv.get("--SecurityGroupId"),
        "SecurityGroupPolicySet": Utils.try_to_json(argv, "--SecurityGroupPolicySet"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ReplaceSecurityGroupPolicyRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ReplaceSecurityGroupPolicy(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateFlowLog(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateFlowLog", g_param[OptionsDefine.Version])
        return

    param = {
        "VpcId": argv.get("--VpcId"),
        "FlowLogName": argv.get("--FlowLogName"),
        "ResourceType": argv.get("--ResourceType"),
        "ResourceId": argv.get("--ResourceId"),
        "TrafficType": argv.get("--TrafficType"),
        "CloudLogId": argv.get("--CloudLogId"),
        "FlowLogDescription": argv.get("--FlowLogDescription"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateFlowLogRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateFlowLog(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyNatGatewayAttribute(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyNatGatewayAttribute", g_param[OptionsDefine.Version])
        return

    param = {
        "NatGatewayId": argv.get("--NatGatewayId"),
        "NatGatewayName": argv.get("--NatGatewayName"),
        "InternetMaxBandwidthOut": Utils.try_to_json(argv, "--InternetMaxBandwidthOut"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyNatGatewayAttributeRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyNatGatewayAttribute(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeTaskResult(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeTaskResult", g_param[OptionsDefine.Version])
        return

    param = {
        "TaskId": Utils.try_to_json(argv, "--TaskId"),
        "DealName": argv.get("--DealName"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeTaskResultRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeTaskResult(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateNetworkAcl(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateNetworkAcl", g_param[OptionsDefine.Version])
        return

    param = {
        "VpcId": argv.get("--VpcId"),
        "NetworkAclName": argv.get("--NetworkAclName"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateNetworkAclRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateNetworkAcl(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeServiceTemplateGroups(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeServiceTemplateGroups", g_param[OptionsDefine.Version])
        return

    param = {
        "Filters": Utils.try_to_json(argv, "--Filters"),
        "Offset": argv.get("--Offset"),
        "Limit": argv.get("--Limit"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeServiceTemplateGroupsRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeServiceTemplateGroups(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeRouteTables(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeRouteTables", g_param[OptionsDefine.Version])
        return

    param = {
        "RouteTableIds": Utils.try_to_json(argv, "--RouteTableIds"),
        "Filters": Utils.try_to_json(argv, "--Filters"),
        "Offset": argv.get("--Offset"),
        "Limit": argv.get("--Limit"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeRouteTablesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeRouteTables(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateBandwidthPackage(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateBandwidthPackage", g_param[OptionsDefine.Version])
        return

    param = {
        "NetworkType": argv.get("--NetworkType"),
        "ChargeType": argv.get("--ChargeType"),
        "BandwidthPackageName": argv.get("--BandwidthPackageName"),
        "BandwidthPackageCount": Utils.try_to_json(argv, "--BandwidthPackageCount"),
        "InternetMaxBandwidth": Utils.try_to_json(argv, "--InternetMaxBandwidth"),
        "Tags": Utils.try_to_json(argv, "--Tags"),
        "Protocol": argv.get("--Protocol"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateBandwidthPackageRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateBandwidthPackage(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteFlowLog(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteFlowLog", g_param[OptionsDefine.Version])
        return

    param = {
        "VpcId": argv.get("--VpcId"),
        "FlowLogId": argv.get("--FlowLogId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteFlowLogRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeleteFlowLog(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateRouteTable(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateRouteTable", g_param[OptionsDefine.Version])
        return

    param = {
        "VpcId": argv.get("--VpcId"),
        "RouteTableName": argv.get("--RouteTableName"),
        "Tags": Utils.try_to_json(argv, "--Tags"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateRouteTableRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateRouteTable(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doAssignIpv6CidrBlock(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("AssignIpv6CidrBlock", g_param[OptionsDefine.Version])
        return

    param = {
        "VpcId": argv.get("--VpcId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.AssignIpv6CidrBlockRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.AssignIpv6CidrBlock(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteNetworkAcl(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteNetworkAcl", g_param[OptionsDefine.Version])
        return

    param = {
        "NetworkAclId": argv.get("--NetworkAclId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteNetworkAclRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeleteNetworkAcl(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeNatGatewayDestinationIpPortTranslationNatRules(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeNatGatewayDestinationIpPortTranslationNatRules", g_param[OptionsDefine.Version])
        return

    param = {
        "NatGatewayIds": Utils.try_to_json(argv, "--NatGatewayIds"),
        "Filters": Utils.try_to_json(argv, "--Filters"),
        "Offset": Utils.try_to_json(argv, "--Offset"),
        "Limit": Utils.try_to_json(argv, "--Limit"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeNatGatewayDestinationIpPortTranslationNatRulesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeNatGatewayDestinationIpPortTranslationNatRules(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyFlowLogAttribute(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyFlowLogAttribute", g_param[OptionsDefine.Version])
        return

    param = {
        "VpcId": argv.get("--VpcId"),
        "FlowLogId": argv.get("--FlowLogId"),
        "FlowLogName": argv.get("--FlowLogName"),
        "FlowLogDescription": argv.get("--FlowLogDescription"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyFlowLogAttributeRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyFlowLogAttribute(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDisassociateNetworkInterfaceSecurityGroups(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DisassociateNetworkInterfaceSecurityGroups", g_param[OptionsDefine.Version])
        return

    param = {
        "NetworkInterfaceIds": Utils.try_to_json(argv, "--NetworkInterfaceIds"),
        "SecurityGroupIds": Utils.try_to_json(argv, "--SecurityGroupIds"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DisassociateNetworkInterfaceSecurityGroupsRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DisassociateNetworkInterfaceSecurityGroups(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyAddressInternetChargeType(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyAddressInternetChargeType", g_param[OptionsDefine.Version])
        return

    param = {
        "AddressId": argv.get("--AddressId"),
        "InternetChargeType": argv.get("--InternetChargeType"),
        "InternetMaxBandwidthOut": Utils.try_to_json(argv, "--InternetMaxBandwidthOut"),
        "AddressChargePrepaid": Utils.try_to_json(argv, "--AddressChargePrepaid"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyAddressInternetChargeTypeRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyAddressInternetChargeType(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeCcnAttachedInstances(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeCcnAttachedInstances", g_param[OptionsDefine.Version])
        return

    param = {
        "Offset": Utils.try_to_json(argv, "--Offset"),
        "Limit": Utils.try_to_json(argv, "--Limit"),
        "Filters": Utils.try_to_json(argv, "--Filters"),
        "CcnId": argv.get("--CcnId"),
        "OrderField": argv.get("--OrderField"),
        "OrderDirection": argv.get("--OrderDirection"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeCcnAttachedInstancesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeCcnAttachedInstances(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doResetRoutes(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ResetRoutes", g_param[OptionsDefine.Version])
        return

    param = {
        "RouteTableId": argv.get("--RouteTableId"),
        "RouteTableName": argv.get("--RouteTableName"),
        "Routes": Utils.try_to_json(argv, "--Routes"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ResetRoutesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ResetRoutes(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeNetworkInterfaceLimit(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeNetworkInterfaceLimit", g_param[OptionsDefine.Version])
        return

    param = {
        "InstanceId": argv.get("--InstanceId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeNetworkInterfaceLimitRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeNetworkInterfaceLimit(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeNetDetects(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeNetDetects", g_param[OptionsDefine.Version])
        return

    param = {
        "NetDetectIds": Utils.try_to_json(argv, "--NetDetectIds"),
        "Filters": Utils.try_to_json(argv, "--Filters"),
        "Offset": Utils.try_to_json(argv, "--Offset"),
        "Limit": Utils.try_to_json(argv, "--Limit"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeNetDetectsRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeNetDetects(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyCcnRegionBandwidthLimitsType(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyCcnRegionBandwidthLimitsType", g_param[OptionsDefine.Version])
        return

    param = {
        "CcnId": argv.get("--CcnId"),
        "BandwidthLimitType": argv.get("--BandwidthLimitType"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyCcnRegionBandwidthLimitsTypeRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyCcnRegionBandwidthLimitsType(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeGatewayFlowMonitorDetail(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeGatewayFlowMonitorDetail", g_param[OptionsDefine.Version])
        return

    param = {
        "TimePoint": argv.get("--TimePoint"),
        "VpnId": argv.get("--VpnId"),
        "DirectConnectGatewayId": argv.get("--DirectConnectGatewayId"),
        "PeeringConnectionId": argv.get("--PeeringConnectionId"),
        "NatId": argv.get("--NatId"),
        "Offset": Utils.try_to_json(argv, "--Offset"),
        "Limit": Utils.try_to_json(argv, "--Limit"),
        "OrderField": argv.get("--OrderField"),
        "OrderDirection": argv.get("--OrderDirection"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeGatewayFlowMonitorDetailRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeGatewayFlowMonitorDetail(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doEnableGatewayFlowMonitor(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("EnableGatewayFlowMonitor", g_param[OptionsDefine.Version])
        return

    param = {
        "GatewayId": argv.get("--GatewayId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.EnableGatewayFlowMonitorRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.EnableGatewayFlowMonitor(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doUnassignIpv6Addresses(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("UnassignIpv6Addresses", g_param[OptionsDefine.Version])
        return

    param = {
        "NetworkInterfaceId": argv.get("--NetworkInterfaceId"),
        "Ipv6Addresses": Utils.try_to_json(argv, "--Ipv6Addresses"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.UnassignIpv6AddressesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.UnassignIpv6Addresses(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeNetworkAcls(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeNetworkAcls", g_param[OptionsDefine.Version])
        return

    param = {
        "NetworkAclIds": Utils.try_to_json(argv, "--NetworkAclIds"),
        "Filters": Utils.try_to_json(argv, "--Filters"),
        "Offset": Utils.try_to_json(argv, "--Offset"),
        "Limit": Utils.try_to_json(argv, "--Limit"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeNetworkAclsRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeNetworkAcls(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteVpnConnection(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteVpnConnection", g_param[OptionsDefine.Version])
        return

    param = {
        "VpnGatewayId": argv.get("--VpnGatewayId"),
        "VpnConnectionId": argv.get("--VpnConnectionId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteVpnConnectionRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeleteVpnConnection(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyAddressTemplateGroupAttribute(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyAddressTemplateGroupAttribute", g_param[OptionsDefine.Version])
        return

    param = {
        "AddressTemplateGroupId": argv.get("--AddressTemplateGroupId"),
        "AddressTemplateGroupName": argv.get("--AddressTemplateGroupName"),
        "AddressTemplateIds": Utils.try_to_json(argv, "--AddressTemplateIds"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyAddressTemplateGroupAttributeRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyAddressTemplateGroupAttribute(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeCustomerGatewayVendors(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeCustomerGatewayVendors", g_param[OptionsDefine.Version])
        return

    param = {

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeCustomerGatewayVendorsRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeCustomerGatewayVendors(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeAddresses(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeAddresses", g_param[OptionsDefine.Version])
        return

    param = {
        "AddressIds": Utils.try_to_json(argv, "--AddressIds"),
        "Filters": Utils.try_to_json(argv, "--Filters"),
        "Offset": Utils.try_to_json(argv, "--Offset"),
        "Limit": Utils.try_to_json(argv, "--Limit"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeAddressesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeAddresses(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDetachCcnInstances(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DetachCcnInstances", g_param[OptionsDefine.Version])
        return

    param = {
        "CcnId": argv.get("--CcnId"),
        "Instances": Utils.try_to_json(argv, "--Instances"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DetachCcnInstancesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DetachCcnInstances(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doAssociateNatGatewayAddress(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("AssociateNatGatewayAddress", g_param[OptionsDefine.Version])
        return

    param = {
        "NatGatewayId": argv.get("--NatGatewayId"),
        "AddressCount": Utils.try_to_json(argv, "--AddressCount"),
        "PublicIpAddresses": Utils.try_to_json(argv, "--PublicIpAddresses"),
        "Zone": argv.get("--Zone"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.AssociateNatGatewayAddressRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.AssociateNatGatewayAddress(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyPrivateIpAddressesAttribute(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyPrivateIpAddressesAttribute", g_param[OptionsDefine.Version])
        return

    param = {
        "NetworkInterfaceId": argv.get("--NetworkInterfaceId"),
        "PrivateIpAddresses": Utils.try_to_json(argv, "--PrivateIpAddresses"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyPrivateIpAddressesAttributeRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyPrivateIpAddressesAttribute(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateDirectConnectGatewayCcnRoutes(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateDirectConnectGatewayCcnRoutes", g_param[OptionsDefine.Version])
        return

    param = {
        "DirectConnectGatewayId": argv.get("--DirectConnectGatewayId"),
        "Routes": Utils.try_to_json(argv, "--Routes"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateDirectConnectGatewayCcnRoutesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateDirectConnectGatewayCcnRoutes(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doRemoveBandwidthPackageResources(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("RemoveBandwidthPackageResources", g_param[OptionsDefine.Version])
        return

    param = {
        "BandwidthPackageId": argv.get("--BandwidthPackageId"),
        "ResourceType": argv.get("--ResourceType"),
        "ResourceIds": Utils.try_to_json(argv, "--ResourceIds"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.RemoveBandwidthPackageResourcesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.RemoveBandwidthPackageResources(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doInquiryPriceRenewVpnGateway(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("InquiryPriceRenewVpnGateway", g_param[OptionsDefine.Version])
        return

    param = {
        "VpnGatewayId": argv.get("--VpnGatewayId"),
        "InstanceChargePrepaid": Utils.try_to_json(argv, "--InstanceChargePrepaid"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.InquiryPriceRenewVpnGatewayRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.InquiryPriceRenewVpnGateway(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doAssignPrivateIpAddresses(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("AssignPrivateIpAddresses", g_param[OptionsDefine.Version])
        return

    param = {
        "NetworkInterfaceId": argv.get("--NetworkInterfaceId"),
        "PrivateIpAddresses": Utils.try_to_json(argv, "--PrivateIpAddresses"),
        "SecondaryPrivateIpAddressCount": Utils.try_to_json(argv, "--SecondaryPrivateIpAddressCount"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.AssignPrivateIpAddressesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.AssignPrivateIpAddresses(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateAndAttachNetworkInterface(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateAndAttachNetworkInterface", g_param[OptionsDefine.Version])
        return

    param = {
        "VpcId": argv.get("--VpcId"),
        "NetworkInterfaceName": argv.get("--NetworkInterfaceName"),
        "SubnetId": argv.get("--SubnetId"),
        "InstanceId": argv.get("--InstanceId"),
        "PrivateIpAddresses": Utils.try_to_json(argv, "--PrivateIpAddresses"),
        "SecondaryPrivateIpAddressCount": Utils.try_to_json(argv, "--SecondaryPrivateIpAddressCount"),
        "SecurityGroupIds": Utils.try_to_json(argv, "--SecurityGroupIds"),
        "NetworkInterfaceDescription": argv.get("--NetworkInterfaceDescription"),
        "Tags": Utils.try_to_json(argv, "--Tags"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateAndAttachNetworkInterfaceRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateAndAttachNetworkInterface(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeNatGateways(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeNatGateways", g_param[OptionsDefine.Version])
        return

    param = {
        "NatGatewayIds": Utils.try_to_json(argv, "--NatGatewayIds"),
        "Filters": Utils.try_to_json(argv, "--Filters"),
        "Offset": Utils.try_to_json(argv, "--Offset"),
        "Limit": Utils.try_to_json(argv, "--Limit"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeNatGatewaysRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeNatGateways(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateSubnets(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateSubnets", g_param[OptionsDefine.Version])
        return

    param = {
        "VpcId": argv.get("--VpcId"),
        "Subnets": Utils.try_to_json(argv, "--Subnets"),
        "Tags": Utils.try_to_json(argv, "--Tags"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateSubnetsRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateSubnets(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doSetCcnRegionBandwidthLimits(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("SetCcnRegionBandwidthLimits", g_param[OptionsDefine.Version])
        return

    param = {
        "CcnId": argv.get("--CcnId"),
        "CcnRegionBandwidthLimits": Utils.try_to_json(argv, "--CcnRegionBandwidthLimits"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.SetCcnRegionBandwidthLimitsRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.SetCcnRegionBandwidthLimits(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doReplaceRouteTableAssociation(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ReplaceRouteTableAssociation", g_param[OptionsDefine.Version])
        return

    param = {
        "SubnetId": argv.get("--SubnetId"),
        "RouteTableId": argv.get("--RouteTableId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ReplaceRouteTableAssociationRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ReplaceRouteTableAssociation(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeTemplateLimits(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeTemplateLimits", g_param[OptionsDefine.Version])
        return

    param = {

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeTemplateLimitsRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeTemplateLimits(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCheckNetDetectState(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CheckNetDetectState", g_param[OptionsDefine.Version])
        return

    param = {
        "DetectDestinationIp": Utils.try_to_json(argv, "--DetectDestinationIp"),
        "NextHopType": argv.get("--NextHopType"),
        "NextHopDestination": argv.get("--NextHopDestination"),
        "NetDetectId": argv.get("--NetDetectId"),
        "VpcId": argv.get("--VpcId"),
        "SubnetId": argv.get("--SubnetId"),
        "NetDetectName": argv.get("--NetDetectName"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CheckNetDetectStateRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CheckNetDetectState(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeDhcpIps(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeDhcpIps", g_param[OptionsDefine.Version])
        return

    param = {
        "DhcpIpIds": Utils.try_to_json(argv, "--DhcpIpIds"),
        "Filters": Utils.try_to_json(argv, "--Filters"),
        "Offset": Utils.try_to_json(argv, "--Offset"),
        "Limit": Utils.try_to_json(argv, "--Limit"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeDhcpIpsRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeDhcpIps(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doInquiryPriceResetVpnGatewayInternetMaxBandwidth(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("InquiryPriceResetVpnGatewayInternetMaxBandwidth", g_param[OptionsDefine.Version])
        return

    param = {
        "VpnGatewayId": argv.get("--VpnGatewayId"),
        "InternetMaxBandwidthOut": Utils.try_to_json(argv, "--InternetMaxBandwidthOut"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.InquiryPriceResetVpnGatewayInternetMaxBandwidthRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.InquiryPriceResetVpnGatewayInternetMaxBandwidth(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteDirectConnectGatewayCcnRoutes(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteDirectConnectGatewayCcnRoutes", g_param[OptionsDefine.Version])
        return

    param = {
        "DirectConnectGatewayId": argv.get("--DirectConnectGatewayId"),
        "RouteIds": Utils.try_to_json(argv, "--RouteIds"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteDirectConnectGatewayCcnRoutesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeleteDirectConnectGatewayCcnRoutes(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doRejectAttachCcnInstances(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("RejectAttachCcnInstances", g_param[OptionsDefine.Version])
        return

    param = {
        "CcnId": argv.get("--CcnId"),
        "Instances": Utils.try_to_json(argv, "--Instances"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.RejectAttachCcnInstancesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.RejectAttachCcnInstances(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doMigrateNetworkInterface(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("MigrateNetworkInterface", g_param[OptionsDefine.Version])
        return

    param = {
        "NetworkInterfaceId": argv.get("--NetworkInterfaceId"),
        "SourceInstanceId": argv.get("--SourceInstanceId"),
        "DestinationInstanceId": argv.get("--DestinationInstanceId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.MigrateNetworkInterfaceRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.MigrateNetworkInterface(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyAddressesBandwidth(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyAddressesBandwidth", g_param[OptionsDefine.Version])
        return

    param = {
        "AddressIds": Utils.try_to_json(argv, "--AddressIds"),
        "InternetMaxBandwidthOut": Utils.try_to_json(argv, "--InternetMaxBandwidthOut"),
        "StartTime": argv.get("--StartTime"),
        "EndTime": argv.get("--EndTime"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyAddressesBandwidthRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyAddressesBandwidth(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateNatGatewayDestinationIpPortTranslationNatRule(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateNatGatewayDestinationIpPortTranslationNatRule", g_param[OptionsDefine.Version])
        return

    param = {
        "NatGatewayId": argv.get("--NatGatewayId"),
        "DestinationIpPortTranslationNatRules": Utils.try_to_json(argv, "--DestinationIpPortTranslationNatRules"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateNatGatewayDestinationIpPortTranslationNatRuleRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateNatGatewayDestinationIpPortTranslationNatRule(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateSubnet(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateSubnet", g_param[OptionsDefine.Version])
        return

    param = {
        "VpcId": argv.get("--VpcId"),
        "SubnetName": argv.get("--SubnetName"),
        "CidrBlock": argv.get("--CidrBlock"),
        "Zone": argv.get("--Zone"),
        "Tags": Utils.try_to_json(argv, "--Tags"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateSubnetRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateSubnet(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doAllocateIp6AddressesBandwidth(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("AllocateIp6AddressesBandwidth", g_param[OptionsDefine.Version])
        return

    param = {
        "Ip6Addresses": Utils.try_to_json(argv, "--Ip6Addresses"),
        "InternetMaxBandwidthOut": Utils.try_to_json(argv, "--InternetMaxBandwidthOut"),
        "InternetChargeType": argv.get("--InternetChargeType"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.AllocateIp6AddressesBandwidthRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.AllocateIp6AddressesBandwidth(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteDhcpIp(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteDhcpIp", g_param[OptionsDefine.Version])
        return

    param = {
        "DhcpIpId": argv.get("--DhcpIpId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteDhcpIpRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeleteDhcpIp(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyAddressTemplateAttribute(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyAddressTemplateAttribute", g_param[OptionsDefine.Version])
        return

    param = {
        "AddressTemplateId": argv.get("--AddressTemplateId"),
        "AddressTemplateName": argv.get("--AddressTemplateName"),
        "Addresses": Utils.try_to_json(argv, "--Addresses"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyAddressTemplateAttributeRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyAddressTemplateAttribute(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doAcceptAttachCcnInstances(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("AcceptAttachCcnInstances", g_param[OptionsDefine.Version])
        return

    param = {
        "CcnId": argv.get("--CcnId"),
        "Instances": Utils.try_to_json(argv, "--Instances"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.AcceptAttachCcnInstancesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.AcceptAttachCcnInstances(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteServiceTemplateGroup(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteServiceTemplateGroup", g_param[OptionsDefine.Version])
        return

    param = {
        "ServiceTemplateGroupId": argv.get("--ServiceTemplateGroupId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteServiceTemplateGroupRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeleteServiceTemplateGroup(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeGatewayFlowQos(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeGatewayFlowQos", g_param[OptionsDefine.Version])
        return

    param = {
        "GatewayId": argv.get("--GatewayId"),
        "IpAddresses": Utils.try_to_json(argv, "--IpAddresses"),
        "Offset": Utils.try_to_json(argv, "--Offset"),
        "Limit": Utils.try_to_json(argv, "--Limit"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeGatewayFlowQosRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeGatewayFlowQos(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeIp6Translators(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeIp6Translators", g_param[OptionsDefine.Version])
        return

    param = {
        "Ip6TranslatorIds": Utils.try_to_json(argv, "--Ip6TranslatorIds"),
        "Filters": Utils.try_to_json(argv, "--Filters"),
        "Offset": Utils.try_to_json(argv, "--Offset"),
        "Limit": Utils.try_to_json(argv, "--Limit"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeIp6TranslatorsRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeIp6Translators(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doResetAttachCcnInstances(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ResetAttachCcnInstances", g_param[OptionsDefine.Version])
        return

    param = {
        "CcnId": argv.get("--CcnId"),
        "CcnUin": argv.get("--CcnUin"),
        "Instances": Utils.try_to_json(argv, "--Instances"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ResetAttachCcnInstancesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ResetAttachCcnInstances(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteSecurityGroupPolicies(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteSecurityGroupPolicies", g_param[OptionsDefine.Version])
        return

    param = {
        "SecurityGroupId": argv.get("--SecurityGroupId"),
        "SecurityGroupPolicySet": Utils.try_to_json(argv, "--SecurityGroupPolicySet"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteSecurityGroupPoliciesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeleteSecurityGroupPolicies(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateVpc(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateVpc", g_param[OptionsDefine.Version])
        return

    param = {
        "VpcName": argv.get("--VpcName"),
        "CidrBlock": argv.get("--CidrBlock"),
        "EnableMulticast": argv.get("--EnableMulticast"),
        "DnsServers": Utils.try_to_json(argv, "--DnsServers"),
        "DomainName": argv.get("--DomainName"),
        "Tags": Utils.try_to_json(argv, "--Tags"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateVpcRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateVpc(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyIp6Rule(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyIp6Rule", g_param[OptionsDefine.Version])
        return

    param = {
        "Ip6TranslatorId": argv.get("--Ip6TranslatorId"),
        "Ip6RuleId": argv.get("--Ip6RuleId"),
        "Ip6RuleName": argv.get("--Ip6RuleName"),
        "Vip": argv.get("--Vip"),
        "Vport": Utils.try_to_json(argv, "--Vport"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyIp6RuleRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyIp6Rule(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doAddBandwidthPackageResources(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("AddBandwidthPackageResources", g_param[OptionsDefine.Version])
        return

    param = {
        "ResourceIds": Utils.try_to_json(argv, "--ResourceIds"),
        "BandwidthPackageId": argv.get("--BandwidthPackageId"),
        "NetworkType": argv.get("--NetworkType"),
        "ResourceType": argv.get("--ResourceType"),
        "Protocol": argv.get("--Protocol"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.AddBandwidthPackageResourcesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.AddBandwidthPackageResources(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doAssignIpv6SubnetCidrBlock(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("AssignIpv6SubnetCidrBlock", g_param[OptionsDefine.Version])
        return

    param = {
        "VpcId": argv.get("--VpcId"),
        "Ipv6SubnetCidrBlocks": Utils.try_to_json(argv, "--Ipv6SubnetCidrBlocks"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.AssignIpv6SubnetCidrBlockRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.AssignIpv6SubnetCidrBlock(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeVpnGatewayCcnRoutes(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeVpnGatewayCcnRoutes", g_param[OptionsDefine.Version])
        return

    param = {
        "VpnGatewayId": argv.get("--VpnGatewayId"),
        "Offset": Utils.try_to_json(argv, "--Offset"),
        "Limit": Utils.try_to_json(argv, "--Limit"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeVpnGatewayCcnRoutesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeVpnGatewayCcnRoutes(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doAllocateAddresses(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("AllocateAddresses", g_param[OptionsDefine.Version])
        return

    param = {
        "AddressCount": Utils.try_to_json(argv, "--AddressCount"),
        "InternetServiceProvider": argv.get("--InternetServiceProvider"),
        "InternetChargeType": argv.get("--InternetChargeType"),
        "InternetMaxBandwidthOut": Utils.try_to_json(argv, "--InternetMaxBandwidthOut"),
        "AddressType": argv.get("--AddressType"),
        "AnycastZone": argv.get("--AnycastZone"),
        "ApplicableForCLB": Utils.try_to_json(argv, "--ApplicableForCLB"),
        "Tags": Utils.try_to_json(argv, "--Tags"),
        "BandwidthPackageId": argv.get("--BandwidthPackageId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.AllocateAddressesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.AllocateAddresses(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCheckAssistantCidr(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CheckAssistantCidr", g_param[OptionsDefine.Version])
        return

    param = {
        "VpcId": argv.get("--VpcId"),
        "NewCidrBlocks": Utils.try_to_json(argv, "--NewCidrBlocks"),
        "OldCidrBlocks": Utils.try_to_json(argv, "--OldCidrBlocks"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CheckAssistantCidrRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CheckAssistantCidr(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeVpcIpv6Addresses(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeVpcIpv6Addresses", g_param[OptionsDefine.Version])
        return

    param = {
        "VpcId": argv.get("--VpcId"),
        "Ipv6Addresses": Utils.try_to_json(argv, "--Ipv6Addresses"),
        "Offset": Utils.try_to_json(argv, "--Offset"),
        "Limit": Utils.try_to_json(argv, "--Limit"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeVpcIpv6AddressesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeVpcIpv6Addresses(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeIp6Addresses(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeIp6Addresses", g_param[OptionsDefine.Version])
        return

    param = {
        "Ip6AddressIds": Utils.try_to_json(argv, "--Ip6AddressIds"),
        "Filters": Utils.try_to_json(argv, "--Filters"),
        "Offset": Utils.try_to_json(argv, "--Offset"),
        "Limit": Utils.try_to_json(argv, "--Limit"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeIp6AddressesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeIp6Addresses(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doRenewVpnGateway(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("RenewVpnGateway", g_param[OptionsDefine.Version])
        return

    param = {
        "VpnGatewayId": argv.get("--VpnGatewayId"),
        "InstanceChargePrepaid": Utils.try_to_json(argv, "--InstanceChargePrepaid"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.RenewVpnGatewayRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.RenewVpnGateway(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeVpcs(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeVpcs", g_param[OptionsDefine.Version])
        return

    param = {
        "VpcIds": Utils.try_to_json(argv, "--VpcIds"),
        "Filters": Utils.try_to_json(argv, "--Filters"),
        "Offset": argv.get("--Offset"),
        "Limit": argv.get("--Limit"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeVpcsRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeVpcs(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doAttachCcnInstances(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("AttachCcnInstances", g_param[OptionsDefine.Version])
        return

    param = {
        "CcnId": argv.get("--CcnId"),
        "Instances": Utils.try_to_json(argv, "--Instances"),
        "CcnUin": argv.get("--CcnUin"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.AttachCcnInstancesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.AttachCcnInstances(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doAssociateAddress(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("AssociateAddress", g_param[OptionsDefine.Version])
        return

    param = {
        "AddressId": argv.get("--AddressId"),
        "InstanceId": argv.get("--InstanceId"),
        "NetworkInterfaceId": argv.get("--NetworkInterfaceId"),
        "PrivateIpAddress": argv.get("--PrivateIpAddress"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.AssociateAddressRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.AssociateAddress(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteCustomerGateway(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteCustomerGateway", g_param[OptionsDefine.Version])
        return

    param = {
        "CustomerGatewayId": argv.get("--CustomerGatewayId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteCustomerGatewayRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeleteCustomerGateway(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteSubnet(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteSubnet", g_param[OptionsDefine.Version])
        return

    param = {
        "SubnetId": argv.get("--SubnetId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteSubnetRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeleteSubnet(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doAttachClassicLinkVpc(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("AttachClassicLinkVpc", g_param[OptionsDefine.Version])
        return

    param = {
        "VpcId": argv.get("--VpcId"),
        "InstanceIds": Utils.try_to_json(argv, "--InstanceIds"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.AttachClassicLinkVpcRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.AttachClassicLinkVpc(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDisassociateNatGatewayAddress(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DisassociateNatGatewayAddress", g_param[OptionsDefine.Version])
        return

    param = {
        "NatGatewayId": argv.get("--NatGatewayId"),
        "PublicIpAddresses": Utils.try_to_json(argv, "--PublicIpAddresses"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DisassociateNatGatewayAddressRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DisassociateNatGatewayAddress(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeFlowLogs(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeFlowLogs", g_param[OptionsDefine.Version])
        return

    param = {
        "VpcId": argv.get("--VpcId"),
        "FlowLogId": argv.get("--FlowLogId"),
        "FlowLogName": argv.get("--FlowLogName"),
        "ResourceType": argv.get("--ResourceType"),
        "ResourceId": argv.get("--ResourceId"),
        "TrafficType": argv.get("--TrafficType"),
        "CloudLogId": argv.get("--CloudLogId"),
        "CloudLogState": argv.get("--CloudLogState"),
        "OrderField": argv.get("--OrderField"),
        "OrderDirection": argv.get("--OrderDirection"),
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
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeFlowLogsRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeFlowLogs(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteDirectConnectGateway(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteDirectConnectGateway", g_param[OptionsDefine.Version])
        return

    param = {
        "DirectConnectGatewayId": argv.get("--DirectConnectGatewayId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteDirectConnectGatewayRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeleteDirectConnectGateway(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeDirectConnectGatewayCcnRoutes(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeDirectConnectGatewayCcnRoutes", g_param[OptionsDefine.Version])
        return

    param = {
        "DirectConnectGatewayId": argv.get("--DirectConnectGatewayId"),
        "CcnRouteType": argv.get("--CcnRouteType"),
        "Offset": Utils.try_to_json(argv, "--Offset"),
        "Limit": Utils.try_to_json(argv, "--Limit"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeDirectConnectGatewayCcnRoutesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeDirectConnectGatewayCcnRoutes(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateNetworkInterface(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateNetworkInterface", g_param[OptionsDefine.Version])
        return

    param = {
        "VpcId": argv.get("--VpcId"),
        "NetworkInterfaceName": argv.get("--NetworkInterfaceName"),
        "SubnetId": argv.get("--SubnetId"),
        "NetworkInterfaceDescription": argv.get("--NetworkInterfaceDescription"),
        "SecondaryPrivateIpAddressCount": Utils.try_to_json(argv, "--SecondaryPrivateIpAddressCount"),
        "SecurityGroupIds": Utils.try_to_json(argv, "--SecurityGroupIds"),
        "PrivateIpAddresses": Utils.try_to_json(argv, "--PrivateIpAddresses"),
        "Tags": Utils.try_to_json(argv, "--Tags"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateNetworkInterfaceRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateNetworkInterface(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteBandwidthPackage(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteBandwidthPackage", g_param[OptionsDefine.Version])
        return

    param = {
        "BandwidthPackageId": argv.get("--BandwidthPackageId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteBandwidthPackageRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeleteBandwidthPackage(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifySecurityGroupPolicies(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifySecurityGroupPolicies", g_param[OptionsDefine.Version])
        return

    param = {
        "SecurityGroupId": argv.get("--SecurityGroupId"),
        "SecurityGroupPolicySet": Utils.try_to_json(argv, "--SecurityGroupPolicySet"),
        "SortPolicys": Utils.try_to_json(argv, "--SortPolicys"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifySecurityGroupPoliciesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifySecurityGroupPolicies(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeNetDetectStates(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeNetDetectStates", g_param[OptionsDefine.Version])
        return

    param = {
        "NetDetectIds": Utils.try_to_json(argv, "--NetDetectIds"),
        "Filters": Utils.try_to_json(argv, "--Filters"),
        "Offset": Utils.try_to_json(argv, "--Offset"),
        "Limit": Utils.try_to_json(argv, "--Limit"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeNetDetectStatesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeNetDetectStates(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeCcns(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeCcns", g_param[OptionsDefine.Version])
        return

    param = {
        "CcnIds": Utils.try_to_json(argv, "--CcnIds"),
        "Filters": Utils.try_to_json(argv, "--Filters"),
        "Offset": Utils.try_to_json(argv, "--Offset"),
        "Limit": Utils.try_to_json(argv, "--Limit"),
        "OrderField": argv.get("--OrderField"),
        "OrderDirection": argv.get("--OrderDirection"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeCcnsRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeCcns(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteIp6Translators(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteIp6Translators", g_param[OptionsDefine.Version])
        return

    param = {
        "Ip6TranslatorIds": Utils.try_to_json(argv, "--Ip6TranslatorIds"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteIp6TranslatorsRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeleteIp6Translators(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteCcn(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteCcn", g_param[OptionsDefine.Version])
        return

    param = {
        "CcnId": argv.get("--CcnId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteCcnRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeleteCcn(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyNetworkAclEntries(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyNetworkAclEntries", g_param[OptionsDefine.Version])
        return

    param = {
        "NetworkAclId": argv.get("--NetworkAclId"),
        "NetworkAclEntrySet": Utils.try_to_json(argv, "--NetworkAclEntrySet"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyNetworkAclEntriesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyNetworkAclEntries(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doHaVipDisassociateAddressIp(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("HaVipDisassociateAddressIp", g_param[OptionsDefine.Version])
        return

    param = {
        "HaVipId": argv.get("--HaVipId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.HaVipDisassociateAddressIpRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.HaVipDisassociateAddressIp(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyVpnGatewayCcnRoutes(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyVpnGatewayCcnRoutes", g_param[OptionsDefine.Version])
        return

    param = {
        "VpnGatewayId": argv.get("--VpnGatewayId"),
        "Routes": Utils.try_to_json(argv, "--Routes"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyVpnGatewayCcnRoutesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyVpnGatewayCcnRoutes(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDetachNetworkInterface(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DetachNetworkInterface", g_param[OptionsDefine.Version])
        return

    param = {
        "NetworkInterfaceId": argv.get("--NetworkInterfaceId"),
        "InstanceId": argv.get("--InstanceId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DetachNetworkInterfaceRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DetachNetworkInterface(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyServiceTemplateGroupAttribute(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyServiceTemplateGroupAttribute", g_param[OptionsDefine.Version])
        return

    param = {
        "ServiceTemplateGroupId": argv.get("--ServiceTemplateGroupId"),
        "ServiceTemplateGroupName": argv.get("--ServiceTemplateGroupName"),
        "ServiceTemplateIds": Utils.try_to_json(argv, "--ServiceTemplateIds"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyServiceTemplateGroupAttributeRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyServiceTemplateGroupAttribute(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteAssistantCidr(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteAssistantCidr", g_param[OptionsDefine.Version])
        return

    param = {
        "VpcId": argv.get("--VpcId"),
        "CidrBlocks": Utils.try_to_json(argv, "--CidrBlocks"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteAssistantCidrRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeleteAssistantCidr(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyDhcpIpAttribute(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyDhcpIpAttribute", g_param[OptionsDefine.Version])
        return

    param = {
        "DhcpIpId": argv.get("--DhcpIpId"),
        "DhcpIpName": argv.get("--DhcpIpName"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyDhcpIpAttributeRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyDhcpIpAttribute(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteNetworkInterface(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteNetworkInterface", g_param[OptionsDefine.Version])
        return

    param = {
        "NetworkInterfaceId": argv.get("--NetworkInterfaceId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteNetworkInterfaceRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeleteNetworkInterface(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeVpnConnections(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeVpnConnections", g_param[OptionsDefine.Version])
        return

    param = {
        "VpnConnectionIds": Utils.try_to_json(argv, "--VpnConnectionIds"),
        "Filters": Utils.try_to_json(argv, "--Filters"),
        "Offset": Utils.try_to_json(argv, "--Offset"),
        "Limit": Utils.try_to_json(argv, "--Limit"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeVpnConnectionsRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeVpnConnections(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeFlowLog(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeFlowLog", g_param[OptionsDefine.Version])
        return

    param = {
        "VpcId": argv.get("--VpcId"),
        "FlowLogId": argv.get("--FlowLogId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeFlowLogRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeFlowLog(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyGatewayFlowQos(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyGatewayFlowQos", g_param[OptionsDefine.Version])
        return

    param = {
        "GatewayId": argv.get("--GatewayId"),
        "Bandwidth": Utils.try_to_json(argv, "--Bandwidth"),
        "IpAddresses": Utils.try_to_json(argv, "--IpAddresses"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyGatewayFlowQosRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyGatewayFlowQos(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteNatGateway(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteNatGateway", g_param[OptionsDefine.Version])
        return

    param = {
        "NatGatewayId": argv.get("--NatGatewayId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteNatGatewayRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeleteNatGateway(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeRouteConflicts(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeRouteConflicts", g_param[OptionsDefine.Version])
        return

    param = {
        "RouteTableId": argv.get("--RouteTableId"),
        "DestinationCidrBlocks": Utils.try_to_json(argv, "--DestinationCidrBlocks"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeRouteConflictsRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeRouteConflicts(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDisableRoutes(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DisableRoutes", g_param[OptionsDefine.Version])
        return

    param = {
        "RouteTableId": argv.get("--RouteTableId"),
        "RouteIds": Utils.try_to_json(argv, "--RouteIds"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DisableRoutesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DisableRoutes(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateDefaultSecurityGroup(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateDefaultSecurityGroup", g_param[OptionsDefine.Version])
        return

    param = {
        "ProjectId": argv.get("--ProjectId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateDefaultSecurityGroupRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateDefaultSecurityGroup(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doAddIp6Rules(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("AddIp6Rules", g_param[OptionsDefine.Version])
        return

    param = {
        "Ip6TranslatorId": argv.get("--Ip6TranslatorId"),
        "Ip6RuleInfos": Utils.try_to_json(argv, "--Ip6RuleInfos"),
        "Ip6RuleName": argv.get("--Ip6RuleName"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.AddIp6RulesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.AddIp6Rules(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doAssociateDhcpIpWithAddressIp(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("AssociateDhcpIpWithAddressIp", g_param[OptionsDefine.Version])
        return

    param = {
        "DhcpIpId": argv.get("--DhcpIpId"),
        "AddressIp": argv.get("--AddressIp"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.AssociateDhcpIpWithAddressIpRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.AssociateDhcpIpWithAddressIp(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteServiceTemplate(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteServiceTemplate", g_param[OptionsDefine.Version])
        return

    param = {
        "ServiceTemplateId": argv.get("--ServiceTemplateId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteServiceTemplateRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeleteServiceTemplate(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doUnassignPrivateIpAddresses(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("UnassignPrivateIpAddresses", g_param[OptionsDefine.Version])
        return

    param = {
        "NetworkInterfaceId": argv.get("--NetworkInterfaceId"),
        "PrivateIpAddresses": Utils.try_to_json(argv, "--PrivateIpAddresses"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.UnassignPrivateIpAddressesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.UnassignPrivateIpAddresses(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteAddressTemplateGroup(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteAddressTemplateGroup", g_param[OptionsDefine.Version])
        return

    param = {
        "AddressTemplateGroupId": argv.get("--AddressTemplateGroupId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteAddressTemplateGroupRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeleteAddressTemplateGroup(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeCcnRoutes(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeCcnRoutes", g_param[OptionsDefine.Version])
        return

    param = {
        "CcnId": argv.get("--CcnId"),
        "RouteIds": Utils.try_to_json(argv, "--RouteIds"),
        "Filters": Utils.try_to_json(argv, "--Filters"),
        "Offset": Utils.try_to_json(argv, "--Offset"),
        "Limit": Utils.try_to_json(argv, "--Limit"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeCcnRoutesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeCcnRoutes(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateNetDetect(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateNetDetect", g_param[OptionsDefine.Version])
        return

    param = {
        "VpcId": argv.get("--VpcId"),
        "SubnetId": argv.get("--SubnetId"),
        "NetDetectName": argv.get("--NetDetectName"),
        "DetectDestinationIp": Utils.try_to_json(argv, "--DetectDestinationIp"),
        "NextHopType": argv.get("--NextHopType"),
        "NextHopDestination": argv.get("--NextHopDestination"),
        "NetDetectDescription": argv.get("--NetDetectDescription"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateNetDetectRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateNetDetect(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateIp6Translators(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateIp6Translators", g_param[OptionsDefine.Version])
        return

    param = {
        "Ip6TranslatorName": argv.get("--Ip6TranslatorName"),
        "Ip6TranslatorCount": Utils.try_to_json(argv, "--Ip6TranslatorCount"),
        "Ip6InternetServiceProvider": argv.get("--Ip6InternetServiceProvider"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateIp6TranslatorsRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateIp6Translators(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateAssistantCidr(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateAssistantCidr", g_param[OptionsDefine.Version])
        return

    param = {
        "VpcId": argv.get("--VpcId"),
        "CidrBlocks": Utils.try_to_json(argv, "--CidrBlocks"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateAssistantCidrRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateAssistantCidr(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateDefaultVpc(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateDefaultVpc", g_param[OptionsDefine.Version])
        return

    param = {
        "Zone": argv.get("--Zone"),
        "Force": Utils.try_to_json(argv, "--Force"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateDefaultVpcRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateDefaultVpc(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doAttachNetworkInterface(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("AttachNetworkInterface", g_param[OptionsDefine.Version])
        return

    param = {
        "NetworkInterfaceId": argv.get("--NetworkInterfaceId"),
        "InstanceId": argv.get("--InstanceId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.AttachNetworkInterfaceRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.AttachNetworkInterface(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doReplaceDirectConnectGatewayCcnRoutes(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ReplaceDirectConnectGatewayCcnRoutes", g_param[OptionsDefine.Version])
        return

    param = {
        "DirectConnectGatewayId": argv.get("--DirectConnectGatewayId"),
        "Routes": Utils.try_to_json(argv, "--Routes"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ReplaceDirectConnectGatewayCcnRoutesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ReplaceDirectConnectGatewayCcnRoutes(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doGetCcnRegionBandwidthLimits(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("GetCcnRegionBandwidthLimits", g_param[OptionsDefine.Version])
        return

    param = {
        "CcnId": argv.get("--CcnId"),
        "Filters": Utils.try_to_json(argv, "--Filters"),
        "SortedBy": argv.get("--SortedBy"),
        "Offset": Utils.try_to_json(argv, "--Offset"),
        "Limit": Utils.try_to_json(argv, "--Limit"),
        "OrderBy": argv.get("--OrderBy"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.GetCcnRegionBandwidthLimitsRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.GetCcnRegionBandwidthLimits(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateNatGateway(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateNatGateway", g_param[OptionsDefine.Version])
        return

    param = {
        "NatGatewayName": argv.get("--NatGatewayName"),
        "VpcId": argv.get("--VpcId"),
        "InternetMaxBandwidthOut": Utils.try_to_json(argv, "--InternetMaxBandwidthOut"),
        "MaxConcurrentConnection": Utils.try_to_json(argv, "--MaxConcurrentConnection"),
        "AddressCount": Utils.try_to_json(argv, "--AddressCount"),
        "PublicIpAddresses": Utils.try_to_json(argv, "--PublicIpAddresses"),
        "Zone": argv.get("--Zone"),
        "Tags": Utils.try_to_json(argv, "--Tags"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateNatGatewayRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateNatGateway(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteNetDetect(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteNetDetect", g_param[OptionsDefine.Version])
        return

    param = {
        "NetDetectId": argv.get("--NetDetectId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteNetDetectRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeleteNetDetect(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifySecurityGroupAttribute(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifySecurityGroupAttribute", g_param[OptionsDefine.Version])
        return

    param = {
        "SecurityGroupId": argv.get("--SecurityGroupId"),
        "GroupName": argv.get("--GroupName"),
        "GroupDescription": argv.get("--GroupDescription"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifySecurityGroupAttributeRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifySecurityGroupAttribute(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteAddressTemplate(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteAddressTemplate", g_param[OptionsDefine.Version])
        return

    param = {
        "AddressTemplateId": argv.get("--AddressTemplateId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteAddressTemplateRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeleteAddressTemplate(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyAssistantCidr(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyAssistantCidr", g_param[OptionsDefine.Version])
        return

    param = {
        "VpcId": argv.get("--VpcId"),
        "NewCidrBlocks": Utils.try_to_json(argv, "--NewCidrBlocks"),
        "OldCidrBlocks": Utils.try_to_json(argv, "--OldCidrBlocks"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyAssistantCidrRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyAssistantCidr(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteVpnGateway(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteVpnGateway", g_param[OptionsDefine.Version])
        return

    param = {
        "VpnGatewayId": argv.get("--VpnGatewayId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteVpnGatewayRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeleteVpnGateway(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateServiceTemplate(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateServiceTemplate", g_param[OptionsDefine.Version])
        return

    param = {
        "ServiceTemplateName": argv.get("--ServiceTemplateName"),
        "Services": Utils.try_to_json(argv, "--Services"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateServiceTemplateRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateServiceTemplate(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteRoutes(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteRoutes", g_param[OptionsDefine.Version])
        return

    param = {
        "RouteTableId": argv.get("--RouteTableId"),
        "Routes": Utils.try_to_json(argv, "--Routes"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteRoutesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeleteRoutes(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyDirectConnectGatewayAttribute(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyDirectConnectGatewayAttribute", g_param[OptionsDefine.Version])
        return

    param = {
        "DirectConnectGatewayId": argv.get("--DirectConnectGatewayId"),
        "DirectConnectGatewayName": argv.get("--DirectConnectGatewayName"),
        "CcnRouteType": argv.get("--CcnRouteType"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyDirectConnectGatewayAttributeRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyDirectConnectGatewayAttribute(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyNetworkInterfaceAttribute(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyNetworkInterfaceAttribute", g_param[OptionsDefine.Version])
        return

    param = {
        "NetworkInterfaceId": argv.get("--NetworkInterfaceId"),
        "NetworkInterfaceName": argv.get("--NetworkInterfaceName"),
        "NetworkInterfaceDescription": argv.get("--NetworkInterfaceDescription"),
        "SecurityGroupIds": Utils.try_to_json(argv, "--SecurityGroupIds"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyNetworkInterfaceAttributeRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyNetworkInterfaceAttribute(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifySubnetAttribute(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifySubnetAttribute", g_param[OptionsDefine.Version])
        return

    param = {
        "SubnetId": argv.get("--SubnetId"),
        "SubnetName": argv.get("--SubnetName"),
        "EnableBroadcast": argv.get("--EnableBroadcast"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifySubnetAttributeRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifySubnetAttribute(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeNetworkInterfaces(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeNetworkInterfaces", g_param[OptionsDefine.Version])
        return

    param = {
        "NetworkInterfaceIds": Utils.try_to_json(argv, "--NetworkInterfaceIds"),
        "Filters": Utils.try_to_json(argv, "--Filters"),
        "Offset": Utils.try_to_json(argv, "--Offset"),
        "Limit": Utils.try_to_json(argv, "--Limit"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeNetworkInterfacesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeNetworkInterfaces(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDisableCcnRoutes(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DisableCcnRoutes", g_param[OptionsDefine.Version])
        return

    param = {
        "CcnId": argv.get("--CcnId"),
        "RouteIds": Utils.try_to_json(argv, "--RouteIds"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DisableCcnRoutesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DisableCcnRoutes(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doInquiryPriceCreateVpnGateway(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("InquiryPriceCreateVpnGateway", g_param[OptionsDefine.Version])
        return

    param = {
        "InternetMaxBandwidthOut": Utils.try_to_json(argv, "--InternetMaxBandwidthOut"),
        "InstanceChargeType": argv.get("--InstanceChargeType"),
        "InstanceChargePrepaid": Utils.try_to_json(argv, "--InstanceChargePrepaid"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.InquiryPriceCreateVpnGatewayRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.InquiryPriceCreateVpnGateway(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doResetVpnConnection(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ResetVpnConnection", g_param[OptionsDefine.Version])
        return

    param = {
        "VpnGatewayId": argv.get("--VpnGatewayId"),
        "VpnConnectionId": argv.get("--VpnConnectionId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ResetVpnConnectionRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ResetVpnConnection(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateCustomerGateway(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateCustomerGateway", g_param[OptionsDefine.Version])
        return

    param = {
        "CustomerGatewayName": argv.get("--CustomerGatewayName"),
        "IpAddress": argv.get("--IpAddress"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateCustomerGatewayRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateCustomerGateway(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateAddressTemplateGroup(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateAddressTemplateGroup", g_param[OptionsDefine.Version])
        return

    param = {
        "AddressTemplateGroupName": argv.get("--AddressTemplateGroupName"),
        "AddressTemplateIds": Utils.try_to_json(argv, "--AddressTemplateIds"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateAddressTemplateGroupRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateAddressTemplateGroup(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateAddressTemplate(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateAddressTemplate", g_param[OptionsDefine.Version])
        return

    param = {
        "AddressTemplateName": argv.get("--AddressTemplateName"),
        "Addresses": Utils.try_to_json(argv, "--Addresses"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateAddressTemplateRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateAddressTemplate(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateSecurityGroup(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateSecurityGroup", g_param[OptionsDefine.Version])
        return

    param = {
        "GroupName": argv.get("--GroupName"),
        "GroupDescription": argv.get("--GroupDescription"),
        "ProjectId": argv.get("--ProjectId"),
        "Tags": Utils.try_to_json(argv, "--Tags"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateSecurityGroupRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateSecurityGroup(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doAssociateNetworkAclSubnets(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("AssociateNetworkAclSubnets", g_param[OptionsDefine.Version])
        return

    param = {
        "NetworkAclId": argv.get("--NetworkAclId"),
        "SubnetIds": Utils.try_to_json(argv, "--SubnetIds"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.AssociateNetworkAclSubnetsRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.AssociateNetworkAclSubnets(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeVpnGateways(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeVpnGateways", g_param[OptionsDefine.Version])
        return

    param = {
        "VpnGatewayIds": Utils.try_to_json(argv, "--VpnGatewayIds"),
        "Filters": Utils.try_to_json(argv, "--Filters"),
        "Offset": Utils.try_to_json(argv, "--Offset"),
        "Limit": Utils.try_to_json(argv, "--Limit"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeVpnGatewaysRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeVpnGateways(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDownloadCustomerGatewayConfiguration(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DownloadCustomerGatewayConfiguration", g_param[OptionsDefine.Version])
        return

    param = {
        "VpnGatewayId": argv.get("--VpnGatewayId"),
        "VpnConnectionId": argv.get("--VpnConnectionId"),
        "CustomerGatewayVendor": Utils.try_to_json(argv, "--CustomerGatewayVendor"),
        "InterfaceName": argv.get("--InterfaceName"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DownloadCustomerGatewayConfigurationRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DownloadCustomerGatewayConfiguration(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeVpcInstances(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeVpcInstances", g_param[OptionsDefine.Version])
        return

    param = {
        "Filters": Utils.try_to_json(argv, "--Filters"),
        "Offset": Utils.try_to_json(argv, "--Offset"),
        "Limit": Utils.try_to_json(argv, "--Limit"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeVpcInstancesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeVpcInstances(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteRouteTable(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteRouteTable", g_param[OptionsDefine.Version])
        return

    param = {
        "RouteTableId": argv.get("--RouteTableId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteRouteTableRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeleteRouteTable(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeSecurityGroupLimits(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeSecurityGroupLimits", g_param[OptionsDefine.Version])
        return

    param = {

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeSecurityGroupLimitsRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeSecurityGroupLimits(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDisassociateAddress(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DisassociateAddress", g_param[OptionsDefine.Version])
        return

    param = {
        "AddressId": argv.get("--AddressId"),
        "ReallocateNormalPublicIp": Utils.try_to_json(argv, "--ReallocateNormalPublicIp"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DisassociateAddressRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DisassociateAddress(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeVpcPrivateIpAddresses(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeVpcPrivateIpAddresses", g_param[OptionsDefine.Version])
        return

    param = {
        "VpcId": argv.get("--VpcId"),
        "PrivateIpAddresses": Utils.try_to_json(argv, "--PrivateIpAddresses"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeVpcPrivateIpAddressesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeVpcPrivateIpAddresses(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyIpv6AddressesAttribute(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyIpv6AddressesAttribute", g_param[OptionsDefine.Version])
        return

    param = {
        "NetworkInterfaceId": argv.get("--NetworkInterfaceId"),
        "Ipv6Addresses": Utils.try_to_json(argv, "--Ipv6Addresses"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyIpv6AddressesAttributeRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyIpv6AddressesAttribute(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeDirectConnectGateways(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeDirectConnectGateways", g_param[OptionsDefine.Version])
        return

    param = {
        "DirectConnectGatewayIds": Utils.try_to_json(argv, "--DirectConnectGatewayIds"),
        "Filters": Utils.try_to_json(argv, "--Filters"),
        "Offset": Utils.try_to_json(argv, "--Offset"),
        "Limit": Utils.try_to_json(argv, "--Limit"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeDirectConnectGatewaysRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeDirectConnectGateways(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyIp6Translator(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyIp6Translator", g_param[OptionsDefine.Version])
        return

    param = {
        "Ip6TranslatorId": argv.get("--Ip6TranslatorId"),
        "Ip6TranslatorName": argv.get("--Ip6TranslatorName"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyIp6TranslatorRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyIp6Translator(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeAccountAttributes(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeAccountAttributes", g_param[OptionsDefine.Version])
        return

    param = {

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeAccountAttributesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeAccountAttributes(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doAssignIpv6Addresses(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("AssignIpv6Addresses", g_param[OptionsDefine.Version])
        return

    param = {
        "NetworkInterfaceId": argv.get("--NetworkInterfaceId"),
        "Ipv6Addresses": Utils.try_to_json(argv, "--Ipv6Addresses"),
        "Ipv6AddressCount": Utils.try_to_json(argv, "--Ipv6AddressCount"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.AssignIpv6AddressesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.AssignIpv6Addresses(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doMigratePrivateIpAddress(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("MigratePrivateIpAddress", g_param[OptionsDefine.Version])
        return

    param = {
        "SourceNetworkInterfaceId": argv.get("--SourceNetworkInterfaceId"),
        "DestinationNetworkInterfaceId": argv.get("--DestinationNetworkInterfaceId"),
        "PrivateIpAddress": argv.get("--PrivateIpAddress"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.MigratePrivateIpAddressRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.MigratePrivateIpAddress(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeServiceTemplates(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeServiceTemplates", g_param[OptionsDefine.Version])
        return

    param = {
        "Filters": Utils.try_to_json(argv, "--Filters"),
        "Offset": argv.get("--Offset"),
        "Limit": argv.get("--Limit"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeServiceTemplatesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeServiceTemplates(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doUnassignIpv6CidrBlock(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("UnassignIpv6CidrBlock", g_param[OptionsDefine.Version])
        return

    param = {
        "VpcId": argv.get("--VpcId"),
        "Ipv6CidrBlock": argv.get("--Ipv6CidrBlock"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.UnassignIpv6CidrBlockRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.UnassignIpv6CidrBlock(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyNatGatewayDestinationIpPortTranslationNatRule(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyNatGatewayDestinationIpPortTranslationNatRule", g_param[OptionsDefine.Version])
        return

    param = {
        "NatGatewayId": argv.get("--NatGatewayId"),
        "SourceNatRule": Utils.try_to_json(argv, "--SourceNatRule"),
        "DestinationNatRule": Utils.try_to_json(argv, "--DestinationNatRule"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyNatGatewayDestinationIpPortTranslationNatRuleRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyNatGatewayDestinationIpPortTranslationNatRule(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeVpcLimits(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeVpcLimits", g_param[OptionsDefine.Version])
        return

    param = {
        "LimitTypes": Utils.try_to_json(argv, "--LimitTypes"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeVpcLimitsRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeVpcLimits(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doHaVipAssociateAddressIp(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("HaVipAssociateAddressIp", g_param[OptionsDefine.Version])
        return

    param = {
        "HaVipId": argv.get("--HaVipId"),
        "AddressIp": argv.get("--AddressIp"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.HaVipAssociateAddressIpRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.HaVipAssociateAddressIp(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doRemoveIp6Rules(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("RemoveIp6Rules", g_param[OptionsDefine.Version])
        return

    param = {
        "Ip6TranslatorId": argv.get("--Ip6TranslatorId"),
        "Ip6RuleIds": Utils.try_to_json(argv, "--Ip6RuleIds"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.RemoveIp6RulesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.RemoveIp6Rules(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCheckDefaultSubnet(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CheckDefaultSubnet", g_param[OptionsDefine.Version])
        return

    param = {
        "Zone": argv.get("--Zone"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CheckDefaultSubnetRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CheckDefaultSubnet(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeHaVips(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeHaVips", g_param[OptionsDefine.Version])
        return

    param = {
        "HaVipIds": Utils.try_to_json(argv, "--HaVipIds"),
        "Filters": Utils.try_to_json(argv, "--Filters"),
        "Offset": Utils.try_to_json(argv, "--Offset"),
        "Limit": Utils.try_to_json(argv, "--Limit"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeHaVipsRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeHaVips(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doAssociateNetworkInterfaceSecurityGroups(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("AssociateNetworkInterfaceSecurityGroups", g_param[OptionsDefine.Version])
        return

    param = {
        "NetworkInterfaceIds": Utils.try_to_json(argv, "--NetworkInterfaceIds"),
        "SecurityGroupIds": Utils.try_to_json(argv, "--SecurityGroupIds"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.AssociateNetworkInterfaceSecurityGroupsRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.AssociateNetworkInterfaceSecurityGroups(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteHaVip(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteHaVip", g_param[OptionsDefine.Version])
        return

    param = {
        "HaVipId": argv.get("--HaVipId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteHaVipRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeleteHaVip(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyBandwidthPackageAttribute(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyBandwidthPackageAttribute", g_param[OptionsDefine.Version])
        return

    param = {
        "BandwidthPackageId": argv.get("--BandwidthPackageId"),
        "BandwidthPackageName": argv.get("--BandwidthPackageName"),
        "ChargeType": argv.get("--ChargeType"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyBandwidthPackageAttributeRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyBandwidthPackageAttribute(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeAddressQuota(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeAddressQuota", g_param[OptionsDefine.Version])
        return

    param = {

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeAddressQuotaRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeAddressQuota(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyVpnGatewayAttribute(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyVpnGatewayAttribute", g_param[OptionsDefine.Version])
        return

    param = {
        "VpnGatewayId": argv.get("--VpnGatewayId"),
        "VpnGatewayName": argv.get("--VpnGatewayName"),
        "InstanceChargeType": argv.get("--InstanceChargeType"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyVpnGatewayAttributeRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyVpnGatewayAttribute(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doResetVpnGatewayInternetMaxBandwidth(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ResetVpnGatewayInternetMaxBandwidth", g_param[OptionsDefine.Version])
        return

    param = {
        "VpnGatewayId": argv.get("--VpnGatewayId"),
        "InternetMaxBandwidthOut": Utils.try_to_json(argv, "--InternetMaxBandwidthOut"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ResetVpnGatewayInternetMaxBandwidthRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ResetVpnGatewayInternetMaxBandwidth(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteVpc(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteVpc", g_param[OptionsDefine.Version])
        return

    param = {
        "VpcId": argv.get("--VpcId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteVpcRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeleteVpc(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeSubnets(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeSubnets", g_param[OptionsDefine.Version])
        return

    param = {
        "SubnetIds": Utils.try_to_json(argv, "--SubnetIds"),
        "Filters": Utils.try_to_json(argv, "--Filters"),
        "Offset": argv.get("--Offset"),
        "Limit": argv.get("--Limit"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeSubnetsRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeSubnets(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateCcn(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateCcn", g_param[OptionsDefine.Version])
        return

    param = {
        "CcnName": argv.get("--CcnName"),
        "CcnDescription": argv.get("--CcnDescription"),
        "QosLevel": argv.get("--QosLevel"),
        "InstanceChargeType": argv.get("--InstanceChargeType"),
        "BandwidthLimitType": argv.get("--BandwidthLimitType"),
        "Tags": Utils.try_to_json(argv, "--Tags"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateCcnRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateCcn(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyCustomerGatewayAttribute(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyCustomerGatewayAttribute", g_param[OptionsDefine.Version])
        return

    param = {
        "CustomerGatewayId": argv.get("--CustomerGatewayId"),
        "CustomerGatewayName": argv.get("--CustomerGatewayName"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyCustomerGatewayAttributeRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyCustomerGatewayAttribute(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyVpnConnectionAttribute(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyVpnConnectionAttribute", g_param[OptionsDefine.Version])
        return

    param = {
        "VpnConnectionId": argv.get("--VpnConnectionId"),
        "VpnConnectionName": argv.get("--VpnConnectionName"),
        "PreShareKey": argv.get("--PreShareKey"),
        "SecurityPolicyDatabases": Utils.try_to_json(argv, "--SecurityPolicyDatabases"),
        "IKEOptionsSpecification": Utils.try_to_json(argv, "--IKEOptionsSpecification"),
        "IPSECOptionsSpecification": Utils.try_to_json(argv, "--IPSECOptionsSpecification"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyVpnConnectionAttributeRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyVpnConnectionAttribute(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeSecurityGroups(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeSecurityGroups", g_param[OptionsDefine.Version])
        return

    param = {
        "SecurityGroupIds": Utils.try_to_json(argv, "--SecurityGroupIds"),
        "Filters": Utils.try_to_json(argv, "--Filters"),
        "Offset": argv.get("--Offset"),
        "Limit": argv.get("--Limit"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeSecurityGroupsRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeSecurityGroups(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateVpnGateway(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateVpnGateway", g_param[OptionsDefine.Version])
        return

    param = {
        "VpcId": argv.get("--VpcId"),
        "VpnGatewayName": argv.get("--VpnGatewayName"),
        "InternetMaxBandwidthOut": Utils.try_to_json(argv, "--InternetMaxBandwidthOut"),
        "InstanceChargeType": argv.get("--InstanceChargeType"),
        "InstanceChargePrepaid": Utils.try_to_json(argv, "--InstanceChargePrepaid"),
        "Zone": argv.get("--Zone"),
        "Type": argv.get("--Type"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateVpnGatewayRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateVpnGateway(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeSecurityGroupPolicies(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeSecurityGroupPolicies", g_param[OptionsDefine.Version])
        return

    param = {
        "SecurityGroupId": argv.get("--SecurityGroupId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeSecurityGroupPoliciesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeSecurityGroupPolicies(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeAssistantCidr(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeAssistantCidr", g_param[OptionsDefine.Version])
        return

    param = {
        "VpcIds": Utils.try_to_json(argv, "--VpcIds"),
        "Filters": Utils.try_to_json(argv, "--Filters"),
        "Offset": Utils.try_to_json(argv, "--Offset"),
        "Limit": Utils.try_to_json(argv, "--Limit"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeAssistantCidrRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeAssistantCidr(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateDirectConnectGateway(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateDirectConnectGateway", g_param[OptionsDefine.Version])
        return

    param = {
        "DirectConnectGatewayName": argv.get("--DirectConnectGatewayName"),
        "NetworkType": argv.get("--NetworkType"),
        "NetworkInstanceId": argv.get("--NetworkInstanceId"),
        "GatewayType": argv.get("--GatewayType"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateDirectConnectGatewayRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateDirectConnectGateway(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeClassicLinkInstances(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeClassicLinkInstances", g_param[OptionsDefine.Version])
        return

    param = {
        "Filters": Utils.try_to_json(argv, "--Filters"),
        "Offset": argv.get("--Offset"),
        "Limit": argv.get("--Limit"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeClassicLinkInstancesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeClassicLinkInstances(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doTransformAddress(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("TransformAddress", g_param[OptionsDefine.Version])
        return

    param = {
        "InstanceId": argv.get("--InstanceId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.TransformAddressRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.TransformAddress(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doEnableRoutes(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("EnableRoutes", g_param[OptionsDefine.Version])
        return

    param = {
        "RouteTableId": argv.get("--RouteTableId"),
        "RouteIds": Utils.try_to_json(argv, "--RouteIds"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.EnableRoutesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.EnableRoutes(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDisassociateDhcpIpWithAddressIp(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DisassociateDhcpIpWithAddressIp", g_param[OptionsDefine.Version])
        return

    param = {
        "DhcpIpId": argv.get("--DhcpIpId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DisassociateDhcpIpWithAddressIpRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DisassociateDhcpIpWithAddressIp(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateHaVip(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateHaVip", g_param[OptionsDefine.Version])
        return

    param = {
        "VpcId": argv.get("--VpcId"),
        "SubnetId": argv.get("--SubnetId"),
        "HaVipName": argv.get("--HaVipName"),
        "Vip": argv.get("--Vip"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateHaVipRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateHaVip(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyServiceTemplateAttribute(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyServiceTemplateAttribute", g_param[OptionsDefine.Version])
        return

    param = {
        "ServiceTemplateId": argv.get("--ServiceTemplateId"),
        "ServiceTemplateName": argv.get("--ServiceTemplateName"),
        "Services": Utils.try_to_json(argv, "--Services"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyServiceTemplateAttributeRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyServiceTemplateAttribute(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteSecurityGroup(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteSecurityGroup", g_param[OptionsDefine.Version])
        return

    param = {
        "SecurityGroupId": argv.get("--SecurityGroupId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteSecurityGroupRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeleteSecurityGroup(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDisassociateNetworkAclSubnets(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DisassociateNetworkAclSubnets", g_param[OptionsDefine.Version])
        return

    param = {
        "NetworkAclId": argv.get("--NetworkAclId"),
        "SubnetIds": Utils.try_to_json(argv, "--SubnetIds"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DisassociateNetworkAclSubnetsRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DisassociateNetworkAclSubnets(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doEnableCcnRoutes(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("EnableCcnRoutes", g_param[OptionsDefine.Version])
        return

    param = {
        "CcnId": argv.get("--CcnId"),
        "RouteIds": Utils.try_to_json(argv, "--RouteIds"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.EnableCcnRoutesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.EnableCcnRoutes(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyRouteTableAttribute(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyRouteTableAttribute", g_param[OptionsDefine.Version])
        return

    param = {
        "RouteTableId": argv.get("--RouteTableId"),
        "RouteTableName": argv.get("--RouteTableName"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyRouteTableAttributeRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyRouteTableAttribute(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyNetDetect(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyNetDetect", g_param[OptionsDefine.Version])
        return

    param = {
        "NetDetectId": argv.get("--NetDetectId"),
        "NetDetectName": argv.get("--NetDetectName"),
        "DetectDestinationIp": Utils.try_to_json(argv, "--DetectDestinationIp"),
        "NextHopType": argv.get("--NextHopType"),
        "NextHopDestination": argv.get("--NextHopDestination"),
        "NetDetectDescription": argv.get("--NetDetectDescription"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyNetDetectRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyNetDetect(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDisableGatewayFlowMonitor(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DisableGatewayFlowMonitor", g_param[OptionsDefine.Version])
        return

    param = {
        "GatewayId": argv.get("--GatewayId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DisableGatewayFlowMonitorRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DisableGatewayFlowMonitor(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteNatGatewayDestinationIpPortTranslationNatRule(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteNatGatewayDestinationIpPortTranslationNatRule", g_param[OptionsDefine.Version])
        return

    param = {
        "NatGatewayId": argv.get("--NatGatewayId"),
        "DestinationIpPortTranslationNatRules": Utils.try_to_json(argv, "--DestinationIpPortTranslationNatRules"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteNatGatewayDestinationIpPortTranslationNatRuleRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeleteNatGatewayDestinationIpPortTranslationNatRule(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateRoutes(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateRoutes", g_param[OptionsDefine.Version])
        return

    param = {
        "RouteTableId": argv.get("--RouteTableId"),
        "Routes": Utils.try_to_json(argv, "--Routes"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateRoutesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateRoutes(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeBandwidthPackageQuota(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeBandwidthPackageQuota", g_param[OptionsDefine.Version])
        return

    param = {

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeBandwidthPackageQuotaRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeBandwidthPackageQuota(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyHaVipAttribute(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyHaVipAttribute", g_param[OptionsDefine.Version])
        return

    param = {
        "HaVipId": argv.get("--HaVipId"),
        "HaVipName": argv.get("--HaVipName"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyHaVipAttributeRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyHaVipAttribute(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doReleaseAddresses(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ReleaseAddresses", g_param[OptionsDefine.Version])
        return

    param = {
        "AddressIds": Utils.try_to_json(argv, "--AddressIds"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ReleaseAddressesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ReleaseAddresses(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeBandwidthPackages(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeBandwidthPackages", g_param[OptionsDefine.Version])
        return

    param = {
        "BandwidthPackageIds": Utils.try_to_json(argv, "--BandwidthPackageIds"),
        "Filters": Utils.try_to_json(argv, "--Filters"),
        "Offset": Utils.try_to_json(argv, "--Offset"),
        "Limit": Utils.try_to_json(argv, "--Limit"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeBandwidthPackagesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeBandwidthPackages(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateServiceTemplateGroup(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateServiceTemplateGroup", g_param[OptionsDefine.Version])
        return

    param = {
        "ServiceTemplateGroupName": argv.get("--ServiceTemplateGroupName"),
        "ServiceTemplateIds": Utils.try_to_json(argv, "--ServiceTemplateIds"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateServiceTemplateGroupRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateServiceTemplateGroup(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doReleaseIp6AddressesBandwidth(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ReleaseIp6AddressesBandwidth", g_param[OptionsDefine.Version])
        return

    param = {
        "Ip6Addresses": Utils.try_to_json(argv, "--Ip6Addresses"),
        "Ip6AddressIds": Utils.try_to_json(argv, "--Ip6AddressIds"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ReleaseIp6AddressesBandwidthRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ReleaseIp6AddressesBandwidth(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateDhcpIp(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateDhcpIp", g_param[OptionsDefine.Version])
        return

    param = {
        "VpcId": argv.get("--VpcId"),
        "SubnetId": argv.get("--SubnetId"),
        "DhcpIpName": argv.get("--DhcpIpName"),
        "SecondaryPrivateIpAddressCount": Utils.try_to_json(argv, "--SecondaryPrivateIpAddressCount"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateDhcpIpRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateDhcpIp(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doReplaceRoutes(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ReplaceRoutes", g_param[OptionsDefine.Version])
        return

    param = {
        "RouteTableId": argv.get("--RouteTableId"),
        "Routes": Utils.try_to_json(argv, "--Routes"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ReplaceRoutesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ReplaceRoutes(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyCcnAttribute(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyCcnAttribute", g_param[OptionsDefine.Version])
        return

    param = {
        "CcnId": argv.get("--CcnId"),
        "CcnName": argv.get("--CcnName"),
        "CcnDescription": argv.get("--CcnDescription"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyCcnAttributeRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyCcnAttribute(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeSecurityGroupReferences(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeSecurityGroupReferences", g_param[OptionsDefine.Version])
        return

    param = {
        "SecurityGroupIds": Utils.try_to_json(argv, "--SecurityGroupIds"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeSecurityGroupReferencesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeSecurityGroupReferences(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeSecurityGroupAssociationStatistics(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeSecurityGroupAssociationStatistics", g_param[OptionsDefine.Version])
        return

    param = {
        "SecurityGroupIds": Utils.try_to_json(argv, "--SecurityGroupIds"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeSecurityGroupAssociationStatisticsRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeSecurityGroupAssociationStatistics(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doUnassignIpv6SubnetCidrBlock(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("UnassignIpv6SubnetCidrBlock", g_param[OptionsDefine.Version])
        return

    param = {
        "VpcId": argv.get("--VpcId"),
        "Ipv6SubnetCidrBlocks": Utils.try_to_json(argv, "--Ipv6SubnetCidrBlocks"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.UnassignIpv6SubnetCidrBlockRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.UnassignIpv6SubnetCidrBlock(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyIp6AddressesBandwidth(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyIp6AddressesBandwidth", g_param[OptionsDefine.Version])
        return

    param = {
        "InternetMaxBandwidthOut": Utils.try_to_json(argv, "--InternetMaxBandwidthOut"),
        "Ip6Addresses": Utils.try_to_json(argv, "--Ip6Addresses"),
        "Ip6AddressIds": Utils.try_to_json(argv, "--Ip6AddressIds"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyIp6AddressesBandwidthRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyIp6AddressesBandwidth(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeAddressTemplates(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeAddressTemplates", g_param[OptionsDefine.Version])
        return

    param = {
        "Filters": Utils.try_to_json(argv, "--Filters"),
        "Offset": argv.get("--Offset"),
        "Limit": argv.get("--Limit"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeAddressTemplatesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeAddressTemplates(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateVpnConnection(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateVpnConnection", g_param[OptionsDefine.Version])
        return

    param = {
        "VpcId": argv.get("--VpcId"),
        "VpnGatewayId": argv.get("--VpnGatewayId"),
        "CustomerGatewayId": argv.get("--CustomerGatewayId"),
        "VpnConnectionName": argv.get("--VpnConnectionName"),
        "PreShareKey": argv.get("--PreShareKey"),
        "SecurityPolicyDatabases": Utils.try_to_json(argv, "--SecurityPolicyDatabases"),
        "IKEOptionsSpecification": Utils.try_to_json(argv, "--IKEOptionsSpecification"),
        "IPSECOptionsSpecification": Utils.try_to_json(argv, "--IPSECOptionsSpecification"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateVpnConnectionRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateVpnConnection(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyAddressAttribute(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyAddressAttribute", g_param[OptionsDefine.Version])
        return

    param = {
        "AddressId": argv.get("--AddressId"),
        "AddressName": argv.get("--AddressName"),
        "EipDirectConnection": argv.get("--EipDirectConnection"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyAddressAttributeRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyAddressAttribute(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeAddressTemplateGroups(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeAddressTemplateGroups", g_param[OptionsDefine.Version])
        return

    param = {
        "Filters": Utils.try_to_json(argv, "--Filters"),
        "Offset": argv.get("--Offset"),
        "Limit": argv.get("--Limit"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeAddressTemplateGroupsRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeAddressTemplateGroups(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDetachClassicLinkVpc(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DetachClassicLinkVpc", g_param[OptionsDefine.Version])
        return

    param = {
        "VpcId": argv.get("--VpcId"),
        "InstanceIds": Utils.try_to_json(argv, "--InstanceIds"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DetachClassicLinkVpcRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DetachClassicLinkVpc(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeIp6TranslatorQuota(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeIp6TranslatorQuota", g_param[OptionsDefine.Version])
        return

    param = {
        "Ip6TranslatorIds": Utils.try_to_json(argv, "--Ip6TranslatorIds"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeIp6TranslatorQuotaRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeIp6TranslatorQuota(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateSecurityGroupPolicies(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateSecurityGroupPolicies", g_param[OptionsDefine.Version])
        return

    param = {
        "SecurityGroupId": argv.get("--SecurityGroupId"),
        "SecurityGroupPolicySet": Utils.try_to_json(argv, "--SecurityGroupPolicySet"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateSecurityGroupPoliciesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateSecurityGroupPolicies(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyNetworkAclAttribute(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyNetworkAclAttribute", g_param[OptionsDefine.Version])
        return

    param = {
        "NetworkAclId": argv.get("--NetworkAclId"),
        "NetworkAclName": argv.get("--NetworkAclName"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyNetworkAclAttributeRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyNetworkAclAttribute(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doResetNatGatewayConnection(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ResetNatGatewayConnection", g_param[OptionsDefine.Version])
        return

    param = {
        "NatGatewayId": argv.get("--NatGatewayId"),
        "MaxConcurrentConnection": Utils.try_to_json(argv, "--MaxConcurrentConnection"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ResetNatGatewayConnectionRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ResetNatGatewayConnection(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyVpcAttribute(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyVpcAttribute", g_param[OptionsDefine.Version])
        return

    param = {
        "VpcId": argv.get("--VpcId"),
        "VpcName": argv.get("--VpcName"),
        "EnableMulticast": argv.get("--EnableMulticast"),
        "DnsServers": Utils.try_to_json(argv, "--DnsServers"),
        "DomainName": argv.get("--DomainName"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyVpcAttributeRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyVpcAttribute(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateSecurityGroupWithPolicies(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateSecurityGroupWithPolicies", g_param[OptionsDefine.Version])
        return

    param = {
        "GroupName": argv.get("--GroupName"),
        "GroupDescription": argv.get("--GroupDescription"),
        "ProjectId": argv.get("--ProjectId"),
        "SecurityGroupPolicySet": Utils.try_to_json(argv, "--SecurityGroupPolicySet"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateSecurityGroupWithPoliciesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateSecurityGroupWithPolicies(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


CLIENT_MAP = {
    "v20170312": vpc_client_v20170312,

}

MODELS_MAP = {
    "v20170312": models_v20170312,

}

ACTION_MAP = {
    "DescribeVpcResourceDashboard": doDescribeVpcResourceDashboard,
    "DescribeCcnRegionBandwidthLimits": doDescribeCcnRegionBandwidthLimits,
    "DescribeCustomerGateways": doDescribeCustomerGateways,
    "ReplaceSecurityGroupPolicy": doReplaceSecurityGroupPolicy,
    "CreateFlowLog": doCreateFlowLog,
    "ModifyNatGatewayAttribute": doModifyNatGatewayAttribute,
    "DescribeTaskResult": doDescribeTaskResult,
    "CreateNetworkAcl": doCreateNetworkAcl,
    "DescribeServiceTemplateGroups": doDescribeServiceTemplateGroups,
    "DescribeRouteTables": doDescribeRouteTables,
    "CreateBandwidthPackage": doCreateBandwidthPackage,
    "DeleteFlowLog": doDeleteFlowLog,
    "CreateRouteTable": doCreateRouteTable,
    "AssignIpv6CidrBlock": doAssignIpv6CidrBlock,
    "DeleteNetworkAcl": doDeleteNetworkAcl,
    "DescribeNatGatewayDestinationIpPortTranslationNatRules": doDescribeNatGatewayDestinationIpPortTranslationNatRules,
    "ModifyFlowLogAttribute": doModifyFlowLogAttribute,
    "DisassociateNetworkInterfaceSecurityGroups": doDisassociateNetworkInterfaceSecurityGroups,
    "ModifyAddressInternetChargeType": doModifyAddressInternetChargeType,
    "DescribeCcnAttachedInstances": doDescribeCcnAttachedInstances,
    "ResetRoutes": doResetRoutes,
    "DescribeNetworkInterfaceLimit": doDescribeNetworkInterfaceLimit,
    "DescribeNetDetects": doDescribeNetDetects,
    "ModifyCcnRegionBandwidthLimitsType": doModifyCcnRegionBandwidthLimitsType,
    "DescribeGatewayFlowMonitorDetail": doDescribeGatewayFlowMonitorDetail,
    "EnableGatewayFlowMonitor": doEnableGatewayFlowMonitor,
    "UnassignIpv6Addresses": doUnassignIpv6Addresses,
    "DescribeNetworkAcls": doDescribeNetworkAcls,
    "DeleteVpnConnection": doDeleteVpnConnection,
    "ModifyAddressTemplateGroupAttribute": doModifyAddressTemplateGroupAttribute,
    "DescribeCustomerGatewayVendors": doDescribeCustomerGatewayVendors,
    "DescribeAddresses": doDescribeAddresses,
    "DetachCcnInstances": doDetachCcnInstances,
    "AssociateNatGatewayAddress": doAssociateNatGatewayAddress,
    "ModifyPrivateIpAddressesAttribute": doModifyPrivateIpAddressesAttribute,
    "CreateDirectConnectGatewayCcnRoutes": doCreateDirectConnectGatewayCcnRoutes,
    "RemoveBandwidthPackageResources": doRemoveBandwidthPackageResources,
    "InquiryPriceRenewVpnGateway": doInquiryPriceRenewVpnGateway,
    "AssignPrivateIpAddresses": doAssignPrivateIpAddresses,
    "CreateAndAttachNetworkInterface": doCreateAndAttachNetworkInterface,
    "DescribeNatGateways": doDescribeNatGateways,
    "CreateSubnets": doCreateSubnets,
    "SetCcnRegionBandwidthLimits": doSetCcnRegionBandwidthLimits,
    "ReplaceRouteTableAssociation": doReplaceRouteTableAssociation,
    "DescribeTemplateLimits": doDescribeTemplateLimits,
    "CheckNetDetectState": doCheckNetDetectState,
    "DescribeDhcpIps": doDescribeDhcpIps,
    "InquiryPriceResetVpnGatewayInternetMaxBandwidth": doInquiryPriceResetVpnGatewayInternetMaxBandwidth,
    "DeleteDirectConnectGatewayCcnRoutes": doDeleteDirectConnectGatewayCcnRoutes,
    "RejectAttachCcnInstances": doRejectAttachCcnInstances,
    "MigrateNetworkInterface": doMigrateNetworkInterface,
    "ModifyAddressesBandwidth": doModifyAddressesBandwidth,
    "CreateNatGatewayDestinationIpPortTranslationNatRule": doCreateNatGatewayDestinationIpPortTranslationNatRule,
    "CreateSubnet": doCreateSubnet,
    "AllocateIp6AddressesBandwidth": doAllocateIp6AddressesBandwidth,
    "DeleteDhcpIp": doDeleteDhcpIp,
    "ModifyAddressTemplateAttribute": doModifyAddressTemplateAttribute,
    "AcceptAttachCcnInstances": doAcceptAttachCcnInstances,
    "DeleteServiceTemplateGroup": doDeleteServiceTemplateGroup,
    "DescribeGatewayFlowQos": doDescribeGatewayFlowQos,
    "DescribeIp6Translators": doDescribeIp6Translators,
    "ResetAttachCcnInstances": doResetAttachCcnInstances,
    "DeleteSecurityGroupPolicies": doDeleteSecurityGroupPolicies,
    "CreateVpc": doCreateVpc,
    "ModifyIp6Rule": doModifyIp6Rule,
    "AddBandwidthPackageResources": doAddBandwidthPackageResources,
    "AssignIpv6SubnetCidrBlock": doAssignIpv6SubnetCidrBlock,
    "DescribeVpnGatewayCcnRoutes": doDescribeVpnGatewayCcnRoutes,
    "AllocateAddresses": doAllocateAddresses,
    "CheckAssistantCidr": doCheckAssistantCidr,
    "DescribeVpcIpv6Addresses": doDescribeVpcIpv6Addresses,
    "DescribeIp6Addresses": doDescribeIp6Addresses,
    "RenewVpnGateway": doRenewVpnGateway,
    "DescribeVpcs": doDescribeVpcs,
    "AttachCcnInstances": doAttachCcnInstances,
    "AssociateAddress": doAssociateAddress,
    "DeleteCustomerGateway": doDeleteCustomerGateway,
    "DeleteSubnet": doDeleteSubnet,
    "AttachClassicLinkVpc": doAttachClassicLinkVpc,
    "DisassociateNatGatewayAddress": doDisassociateNatGatewayAddress,
    "DescribeFlowLogs": doDescribeFlowLogs,
    "DeleteDirectConnectGateway": doDeleteDirectConnectGateway,
    "DescribeDirectConnectGatewayCcnRoutes": doDescribeDirectConnectGatewayCcnRoutes,
    "CreateNetworkInterface": doCreateNetworkInterface,
    "DeleteBandwidthPackage": doDeleteBandwidthPackage,
    "ModifySecurityGroupPolicies": doModifySecurityGroupPolicies,
    "DescribeNetDetectStates": doDescribeNetDetectStates,
    "DescribeCcns": doDescribeCcns,
    "DeleteIp6Translators": doDeleteIp6Translators,
    "DeleteCcn": doDeleteCcn,
    "ModifyNetworkAclEntries": doModifyNetworkAclEntries,
    "HaVipDisassociateAddressIp": doHaVipDisassociateAddressIp,
    "ModifyVpnGatewayCcnRoutes": doModifyVpnGatewayCcnRoutes,
    "DetachNetworkInterface": doDetachNetworkInterface,
    "ModifyServiceTemplateGroupAttribute": doModifyServiceTemplateGroupAttribute,
    "DeleteAssistantCidr": doDeleteAssistantCidr,
    "ModifyDhcpIpAttribute": doModifyDhcpIpAttribute,
    "DeleteNetworkInterface": doDeleteNetworkInterface,
    "DescribeVpnConnections": doDescribeVpnConnections,
    "DescribeFlowLog": doDescribeFlowLog,
    "ModifyGatewayFlowQos": doModifyGatewayFlowQos,
    "DeleteNatGateway": doDeleteNatGateway,
    "DescribeRouteConflicts": doDescribeRouteConflicts,
    "DisableRoutes": doDisableRoutes,
    "CreateDefaultSecurityGroup": doCreateDefaultSecurityGroup,
    "AddIp6Rules": doAddIp6Rules,
    "AssociateDhcpIpWithAddressIp": doAssociateDhcpIpWithAddressIp,
    "DeleteServiceTemplate": doDeleteServiceTemplate,
    "UnassignPrivateIpAddresses": doUnassignPrivateIpAddresses,
    "DeleteAddressTemplateGroup": doDeleteAddressTemplateGroup,
    "DescribeCcnRoutes": doDescribeCcnRoutes,
    "CreateNetDetect": doCreateNetDetect,
    "CreateIp6Translators": doCreateIp6Translators,
    "CreateAssistantCidr": doCreateAssistantCidr,
    "CreateDefaultVpc": doCreateDefaultVpc,
    "AttachNetworkInterface": doAttachNetworkInterface,
    "ReplaceDirectConnectGatewayCcnRoutes": doReplaceDirectConnectGatewayCcnRoutes,
    "GetCcnRegionBandwidthLimits": doGetCcnRegionBandwidthLimits,
    "CreateNatGateway": doCreateNatGateway,
    "DeleteNetDetect": doDeleteNetDetect,
    "ModifySecurityGroupAttribute": doModifySecurityGroupAttribute,
    "DeleteAddressTemplate": doDeleteAddressTemplate,
    "ModifyAssistantCidr": doModifyAssistantCidr,
    "DeleteVpnGateway": doDeleteVpnGateway,
    "CreateServiceTemplate": doCreateServiceTemplate,
    "DeleteRoutes": doDeleteRoutes,
    "ModifyDirectConnectGatewayAttribute": doModifyDirectConnectGatewayAttribute,
    "ModifyNetworkInterfaceAttribute": doModifyNetworkInterfaceAttribute,
    "ModifySubnetAttribute": doModifySubnetAttribute,
    "DescribeNetworkInterfaces": doDescribeNetworkInterfaces,
    "DisableCcnRoutes": doDisableCcnRoutes,
    "InquiryPriceCreateVpnGateway": doInquiryPriceCreateVpnGateway,
    "ResetVpnConnection": doResetVpnConnection,
    "CreateCustomerGateway": doCreateCustomerGateway,
    "CreateAddressTemplateGroup": doCreateAddressTemplateGroup,
    "CreateAddressTemplate": doCreateAddressTemplate,
    "CreateSecurityGroup": doCreateSecurityGroup,
    "AssociateNetworkAclSubnets": doAssociateNetworkAclSubnets,
    "DescribeVpnGateways": doDescribeVpnGateways,
    "DownloadCustomerGatewayConfiguration": doDownloadCustomerGatewayConfiguration,
    "DescribeVpcInstances": doDescribeVpcInstances,
    "DeleteRouteTable": doDeleteRouteTable,
    "DescribeSecurityGroupLimits": doDescribeSecurityGroupLimits,
    "DisassociateAddress": doDisassociateAddress,
    "DescribeVpcPrivateIpAddresses": doDescribeVpcPrivateIpAddresses,
    "ModifyIpv6AddressesAttribute": doModifyIpv6AddressesAttribute,
    "DescribeDirectConnectGateways": doDescribeDirectConnectGateways,
    "ModifyIp6Translator": doModifyIp6Translator,
    "DescribeAccountAttributes": doDescribeAccountAttributes,
    "AssignIpv6Addresses": doAssignIpv6Addresses,
    "MigratePrivateIpAddress": doMigratePrivateIpAddress,
    "DescribeServiceTemplates": doDescribeServiceTemplates,
    "UnassignIpv6CidrBlock": doUnassignIpv6CidrBlock,
    "ModifyNatGatewayDestinationIpPortTranslationNatRule": doModifyNatGatewayDestinationIpPortTranslationNatRule,
    "DescribeVpcLimits": doDescribeVpcLimits,
    "HaVipAssociateAddressIp": doHaVipAssociateAddressIp,
    "RemoveIp6Rules": doRemoveIp6Rules,
    "CheckDefaultSubnet": doCheckDefaultSubnet,
    "DescribeHaVips": doDescribeHaVips,
    "AssociateNetworkInterfaceSecurityGroups": doAssociateNetworkInterfaceSecurityGroups,
    "DeleteHaVip": doDeleteHaVip,
    "ModifyBandwidthPackageAttribute": doModifyBandwidthPackageAttribute,
    "DescribeAddressQuota": doDescribeAddressQuota,
    "ModifyVpnGatewayAttribute": doModifyVpnGatewayAttribute,
    "ResetVpnGatewayInternetMaxBandwidth": doResetVpnGatewayInternetMaxBandwidth,
    "DeleteVpc": doDeleteVpc,
    "DescribeSubnets": doDescribeSubnets,
    "CreateCcn": doCreateCcn,
    "ModifyCustomerGatewayAttribute": doModifyCustomerGatewayAttribute,
    "ModifyVpnConnectionAttribute": doModifyVpnConnectionAttribute,
    "DescribeSecurityGroups": doDescribeSecurityGroups,
    "CreateVpnGateway": doCreateVpnGateway,
    "DescribeSecurityGroupPolicies": doDescribeSecurityGroupPolicies,
    "DescribeAssistantCidr": doDescribeAssistantCidr,
    "CreateDirectConnectGateway": doCreateDirectConnectGateway,
    "DescribeClassicLinkInstances": doDescribeClassicLinkInstances,
    "TransformAddress": doTransformAddress,
    "EnableRoutes": doEnableRoutes,
    "DisassociateDhcpIpWithAddressIp": doDisassociateDhcpIpWithAddressIp,
    "CreateHaVip": doCreateHaVip,
    "ModifyServiceTemplateAttribute": doModifyServiceTemplateAttribute,
    "DeleteSecurityGroup": doDeleteSecurityGroup,
    "DisassociateNetworkAclSubnets": doDisassociateNetworkAclSubnets,
    "EnableCcnRoutes": doEnableCcnRoutes,
    "ModifyRouteTableAttribute": doModifyRouteTableAttribute,
    "ModifyNetDetect": doModifyNetDetect,
    "DisableGatewayFlowMonitor": doDisableGatewayFlowMonitor,
    "DeleteNatGatewayDestinationIpPortTranslationNatRule": doDeleteNatGatewayDestinationIpPortTranslationNatRule,
    "CreateRoutes": doCreateRoutes,
    "DescribeBandwidthPackageQuota": doDescribeBandwidthPackageQuota,
    "ModifyHaVipAttribute": doModifyHaVipAttribute,
    "ReleaseAddresses": doReleaseAddresses,
    "DescribeBandwidthPackages": doDescribeBandwidthPackages,
    "CreateServiceTemplateGroup": doCreateServiceTemplateGroup,
    "ReleaseIp6AddressesBandwidth": doReleaseIp6AddressesBandwidth,
    "CreateDhcpIp": doCreateDhcpIp,
    "ReplaceRoutes": doReplaceRoutes,
    "ModifyCcnAttribute": doModifyCcnAttribute,
    "DescribeSecurityGroupReferences": doDescribeSecurityGroupReferences,
    "DescribeSecurityGroupAssociationStatistics": doDescribeSecurityGroupAssociationStatistics,
    "UnassignIpv6SubnetCidrBlock": doUnassignIpv6SubnetCidrBlock,
    "ModifyIp6AddressesBandwidth": doModifyIp6AddressesBandwidth,
    "DescribeAddressTemplates": doDescribeAddressTemplates,
    "CreateVpnConnection": doCreateVpnConnection,
    "ModifyAddressAttribute": doModifyAddressAttribute,
    "DescribeAddressTemplateGroups": doDescribeAddressTemplateGroups,
    "DetachClassicLinkVpc": doDetachClassicLinkVpc,
    "DescribeIp6TranslatorQuota": doDescribeIp6TranslatorQuota,
    "CreateSecurityGroupPolicies": doCreateSecurityGroupPolicies,
    "ModifyNetworkAclAttribute": doModifyNetworkAclAttribute,
    "ResetNatGatewayConnection": doResetNatGatewayConnection,
    "ModifyVpcAttribute": doModifyVpcAttribute,
    "CreateSecurityGroupWithPolicies": doCreateSecurityGroupWithPolicies,

}

AVAILABLE_VERSION_LIST = [
    v20170312.version,

]
AVAILABLE_VERSIONS = {
     'v' + v20170312.version.replace('-', ''): {"help": v20170312_help.INFO,"desc": v20170312_help.DESC},

}


def vpc_action(argv, arglist):
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
        helpstr = HelpTemplate.SERVICE % {"name": "vpc", "desc": desc, "actions": action_str}
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
    cmd = NiceCommand("vpc", vpc_action)
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
            version = config["vpc"][OptionsDefine.Version]
            params[OptionsDefine.Version] = "v" + version.replace('-', '')

        if params[OptionsDefine.Endpoint] is None:
            params[OptionsDefine.Endpoint] = config["vpc"][OptionsDefine.Endpoint]
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

    helpmsg = HelpTemplate.ACTION % {"name": action, "service": "vpc", "desc": desc, "params": docstr}
    print(helpmsg)


def get_actions_info():
    config = Configure()
    new_version = max(AVAILABLE_VERSIONS.keys())
    version = new_version
    try:
        profile = config._load_json_msg(os.path.join(config.cli_path, "default.configure"))
        version = profile["vpc"]["version"]
        version = "v" + version.replace('-', '')
    except Exception:
        pass
    if version not in AVAILABLE_VERSIONS.keys():
        version = new_version
    return AVAILABLE_VERSIONS[version]["help"]
