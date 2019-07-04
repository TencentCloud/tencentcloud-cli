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


def doDownloadCustomerGatewayConfiguration(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DownloadCustomerGatewayConfiguration", g_param[OptionsDefine.Version])
        return

    param = {
        "VpnGatewayId": Utils.try_to_json(argv, "--VpnGatewayId"),
        "VpnConnectionId": Utils.try_to_json(argv, "--VpnConnectionId"),
        "CustomerGatewayVendor": Utils.try_to_json(argv, "--CustomerGatewayVendor"),
        "InterfaceName": Utils.try_to_json(argv, "--InterfaceName"),

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
        "SecurityGroupId": Utils.try_to_json(argv, "--SecurityGroupId"),
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
        "VpcId": Utils.try_to_json(argv, "--VpcId"),
        "FlowLogName": Utils.try_to_json(argv, "--FlowLogName"),
        "ResourceType": Utils.try_to_json(argv, "--ResourceType"),
        "ResourceId": Utils.try_to_json(argv, "--ResourceId"),
        "TrafficType": Utils.try_to_json(argv, "--TrafficType"),
        "CloudLogId": Utils.try_to_json(argv, "--CloudLogId"),
        "FlowLogDescription": Utils.try_to_json(argv, "--FlowLogDescription"),

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


def doDescribeServiceTemplateGroups(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeServiceTemplateGroups", g_param[OptionsDefine.Version])
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
        "NetworkType": Utils.try_to_json(argv, "--NetworkType"),
        "ChargeType": Utils.try_to_json(argv, "--ChargeType"),
        "BandwidthPackageName": Utils.try_to_json(argv, "--BandwidthPackageName"),
        "BandwidthPackageCount": Utils.try_to_json(argv, "--BandwidthPackageCount"),
        "InternetMaxBandwidth": Utils.try_to_json(argv, "--InternetMaxBandwidth"),

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
        "VpcId": Utils.try_to_json(argv, "--VpcId"),
        "FlowLogId": Utils.try_to_json(argv, "--FlowLogId"),

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
        "VpcId": Utils.try_to_json(argv, "--VpcId"),
        "RouteTableName": Utils.try_to_json(argv, "--RouteTableName"),

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
        "VpcId": Utils.try_to_json(argv, "--VpcId"),

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


def doEnableCcnRoutes(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("EnableCcnRoutes", g_param[OptionsDefine.Version])
        return

    param = {
        "CcnId": Utils.try_to_json(argv, "--CcnId"),
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


def doModifyFlowLogAttribute(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyFlowLogAttribute", g_param[OptionsDefine.Version])
        return

    param = {
        "VpcId": Utils.try_to_json(argv, "--VpcId"),
        "FlowLogId": Utils.try_to_json(argv, "--FlowLogId"),
        "FlowLogName": Utils.try_to_json(argv, "--FlowLogName"),
        "FlowLogDescription": Utils.try_to_json(argv, "--FlowLogDescription"),

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


def doModifyServiceTemplateGroupAttribute(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyServiceTemplateGroupAttribute", g_param[OptionsDefine.Version])
        return

    param = {
        "ServiceTemplateGroupId": Utils.try_to_json(argv, "--ServiceTemplateGroupId"),
        "ServiceTemplateGroupName": Utils.try_to_json(argv, "--ServiceTemplateGroupName"),
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


def doDescribeCcnAttachedInstances(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeCcnAttachedInstances", g_param[OptionsDefine.Version])
        return

    param = {
        "Offset": Utils.try_to_json(argv, "--Offset"),
        "Limit": Utils.try_to_json(argv, "--Limit"),
        "Filters": Utils.try_to_json(argv, "--Filters"),
        "CcnId": Utils.try_to_json(argv, "--CcnId"),
        "OrderField": Utils.try_to_json(argv, "--OrderField"),
        "OrderDirection": Utils.try_to_json(argv, "--OrderDirection"),

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
        "RouteTableId": Utils.try_to_json(argv, "--RouteTableId"),
        "RouteTableName": Utils.try_to_json(argv, "--RouteTableName"),
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


def doModifyPrivateIpAddressesAttribute(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyPrivateIpAddressesAttribute", g_param[OptionsDefine.Version])
        return

    param = {
        "NetworkInterfaceId": Utils.try_to_json(argv, "--NetworkInterfaceId"),
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


def doDescribeGatewayFlowMonitorDetail(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeGatewayFlowMonitorDetail", g_param[OptionsDefine.Version])
        return

    param = {
        "TimePoint": Utils.try_to_json(argv, "--TimePoint"),
        "VpnId": Utils.try_to_json(argv, "--VpnId"),
        "DirectConnectGatewayId": Utils.try_to_json(argv, "--DirectConnectGatewayId"),
        "PeeringConnectionId": Utils.try_to_json(argv, "--PeeringConnectionId"),
        "NatId": Utils.try_to_json(argv, "--NatId"),
        "Offset": Utils.try_to_json(argv, "--Offset"),
        "Limit": Utils.try_to_json(argv, "--Limit"),
        "OrderField": Utils.try_to_json(argv, "--OrderField"),
        "OrderDirection": Utils.try_to_json(argv, "--OrderDirection"),

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


def doUnassignIpv6Addresses(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("UnassignIpv6Addresses", g_param[OptionsDefine.Version])
        return

    param = {
        "NetworkInterfaceId": Utils.try_to_json(argv, "--NetworkInterfaceId"),
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


def doDeleteVpnConnection(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteVpnConnection", g_param[OptionsDefine.Version])
        return

    param = {
        "VpnGatewayId": Utils.try_to_json(argv, "--VpnGatewayId"),
        "VpnConnectionId": Utils.try_to_json(argv, "--VpnConnectionId"),

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
        "AddressTemplateGroupId": Utils.try_to_json(argv, "--AddressTemplateGroupId"),
        "AddressTemplateGroupName": Utils.try_to_json(argv, "--AddressTemplateGroupName"),
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


def doModifyServiceTemplateAttribute(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyServiceTemplateAttribute", g_param[OptionsDefine.Version])
        return

    param = {
        "ServiceTemplateId": Utils.try_to_json(argv, "--ServiceTemplateId"),
        "ServiceTemplateName": Utils.try_to_json(argv, "--ServiceTemplateName"),
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


def doDetachCcnInstances(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DetachCcnInstances", g_param[OptionsDefine.Version])
        return

    param = {
        "CcnId": Utils.try_to_json(argv, "--CcnId"),
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


def doCreateDirectConnectGatewayCcnRoutes(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateDirectConnectGatewayCcnRoutes", g_param[OptionsDefine.Version])
        return

    param = {
        "DirectConnectGatewayId": Utils.try_to_json(argv, "--DirectConnectGatewayId"),
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
        "BandwidthPackageId": Utils.try_to_json(argv, "--BandwidthPackageId"),
        "ResourceType": Utils.try_to_json(argv, "--ResourceType"),
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
        "VpnGatewayId": Utils.try_to_json(argv, "--VpnGatewayId"),
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
        "NetworkInterfaceId": Utils.try_to_json(argv, "--NetworkInterfaceId"),
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
        "VpcId": Utils.try_to_json(argv, "--VpcId"),
        "Subnets": Utils.try_to_json(argv, "--Subnets"),

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


def doReplaceRouteTableAssociation(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ReplaceRouteTableAssociation", g_param[OptionsDefine.Version])
        return

    param = {
        "SubnetId": Utils.try_to_json(argv, "--SubnetId"),
        "RouteTableId": Utils.try_to_json(argv, "--RouteTableId"),

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


def doDescribeVpcs(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeVpcs", g_param[OptionsDefine.Version])
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


def doInquiryPriceResetVpnGatewayInternetMaxBandwidth(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("InquiryPriceResetVpnGatewayInternetMaxBandwidth", g_param[OptionsDefine.Version])
        return

    param = {
        "VpnGatewayId": Utils.try_to_json(argv, "--VpnGatewayId"),
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
        "DirectConnectGatewayId": Utils.try_to_json(argv, "--DirectConnectGatewayId"),
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
        "CcnId": Utils.try_to_json(argv, "--CcnId"),
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
        "NetworkInterfaceId": Utils.try_to_json(argv, "--NetworkInterfaceId"),
        "SourceInstanceId": Utils.try_to_json(argv, "--SourceInstanceId"),
        "DestinationInstanceId": Utils.try_to_json(argv, "--DestinationInstanceId"),

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
        "StartTime": Utils.try_to_json(argv, "--StartTime"),
        "EndTime": Utils.try_to_json(argv, "--EndTime"),

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


def doCreateSubnet(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateSubnet", g_param[OptionsDefine.Version])
        return

    param = {
        "VpcId": Utils.try_to_json(argv, "--VpcId"),
        "SubnetName": Utils.try_to_json(argv, "--SubnetName"),
        "CidrBlock": Utils.try_to_json(argv, "--CidrBlock"),
        "Zone": Utils.try_to_json(argv, "--Zone"),

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


def doModifyAddressTemplateAttribute(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyAddressTemplateAttribute", g_param[OptionsDefine.Version])
        return

    param = {
        "AddressTemplateId": Utils.try_to_json(argv, "--AddressTemplateId"),
        "AddressTemplateName": Utils.try_to_json(argv, "--AddressTemplateName"),
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
        "CcnId": Utils.try_to_json(argv, "--CcnId"),
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
        "ServiceTemplateGroupId": Utils.try_to_json(argv, "--ServiceTemplateGroupId"),

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
        "CcnId": Utils.try_to_json(argv, "--CcnId"),
        "CcnUin": Utils.try_to_json(argv, "--CcnUin"),
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


def doCreateVpc(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateVpc", g_param[OptionsDefine.Version])
        return

    param = {
        "VpcName": Utils.try_to_json(argv, "--VpcName"),
        "CidrBlock": Utils.try_to_json(argv, "--CidrBlock"),
        "EnableMulticast": Utils.try_to_json(argv, "--EnableMulticast"),
        "DnsServers": Utils.try_to_json(argv, "--DnsServers"),
        "DomainName": Utils.try_to_json(argv, "--DomainName"),

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
        "Ip6TranslatorId": Utils.try_to_json(argv, "--Ip6TranslatorId"),
        "Ip6RuleId": Utils.try_to_json(argv, "--Ip6RuleId"),
        "Ip6RuleName": Utils.try_to_json(argv, "--Ip6RuleName"),
        "Vip": Utils.try_to_json(argv, "--Vip"),
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
        "BandwidthPackageId": Utils.try_to_json(argv, "--BandwidthPackageId"),
        "NetworkType": Utils.try_to_json(argv, "--NetworkType"),
        "ResourceType": Utils.try_to_json(argv, "--ResourceType"),

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
        "VpcId": Utils.try_to_json(argv, "--VpcId"),
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


def doAllocateAddresses(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("AllocateAddresses", g_param[OptionsDefine.Version])
        return

    param = {
        "AddressCount": Utils.try_to_json(argv, "--AddressCount"),

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


def doDescribeVpcIpv6Addresses(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeVpcIpv6Addresses", g_param[OptionsDefine.Version])
        return

    param = {
        "VpcId": Utils.try_to_json(argv, "--VpcId"),
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


def doRenewVpnGateway(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("RenewVpnGateway", g_param[OptionsDefine.Version])
        return

    param = {
        "VpnGatewayId": Utils.try_to_json(argv, "--VpnGatewayId"),
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


def doAttachCcnInstances(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("AttachCcnInstances", g_param[OptionsDefine.Version])
        return

    param = {
        "CcnId": Utils.try_to_json(argv, "--CcnId"),
        "Instances": Utils.try_to_json(argv, "--Instances"),
        "CcnUin": Utils.try_to_json(argv, "--CcnUin"),

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
        "AddressId": Utils.try_to_json(argv, "--AddressId"),
        "InstanceId": Utils.try_to_json(argv, "--InstanceId"),
        "NetworkInterfaceId": Utils.try_to_json(argv, "--NetworkInterfaceId"),
        "PrivateIpAddress": Utils.try_to_json(argv, "--PrivateIpAddress"),

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
        "CustomerGatewayId": Utils.try_to_json(argv, "--CustomerGatewayId"),

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
        "SubnetId": Utils.try_to_json(argv, "--SubnetId"),

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
        "VpcId": Utils.try_to_json(argv, "--VpcId"),
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


def doDescribeFlowLogs(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeFlowLogs", g_param[OptionsDefine.Version])
        return

    param = {
        "VpcId": Utils.try_to_json(argv, "--VpcId"),
        "FlowLogId": Utils.try_to_json(argv, "--FlowLogId"),
        "FlowLogName": Utils.try_to_json(argv, "--FlowLogName"),
        "ResourceType": Utils.try_to_json(argv, "--ResourceType"),
        "ResourceId": Utils.try_to_json(argv, "--ResourceId"),
        "TrafficType": Utils.try_to_json(argv, "--TrafficType"),
        "CloudLogId": Utils.try_to_json(argv, "--CloudLogId"),
        "CloudLogState": Utils.try_to_json(argv, "--CloudLogState"),
        "OrderField": Utils.try_to_json(argv, "--OrderField"),
        "OrderDirection": Utils.try_to_json(argv, "--OrderDirection"),
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
        "DirectConnectGatewayId": Utils.try_to_json(argv, "--DirectConnectGatewayId"),

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
        "DirectConnectGatewayId": Utils.try_to_json(argv, "--DirectConnectGatewayId"),
        "CcnRouteType": Utils.try_to_json(argv, "--CcnRouteType"),
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
        "VpcId": Utils.try_to_json(argv, "--VpcId"),
        "NetworkInterfaceName": Utils.try_to_json(argv, "--NetworkInterfaceName"),
        "SubnetId": Utils.try_to_json(argv, "--SubnetId"),
        "NetworkInterfaceDescription": Utils.try_to_json(argv, "--NetworkInterfaceDescription"),
        "SecondaryPrivateIpAddressCount": Utils.try_to_json(argv, "--SecondaryPrivateIpAddressCount"),
        "SecurityGroupIds": Utils.try_to_json(argv, "--SecurityGroupIds"),
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
        "BandwidthPackageId": Utils.try_to_json(argv, "--BandwidthPackageId"),

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
        "SecurityGroupId": Utils.try_to_json(argv, "--SecurityGroupId"),
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
        "OrderField": Utils.try_to_json(argv, "--OrderField"),
        "OrderDirection": Utils.try_to_json(argv, "--OrderDirection"),

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
        "CcnId": Utils.try_to_json(argv, "--CcnId"),

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


def doHaVipDisassociateAddressIp(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("HaVipDisassociateAddressIp", g_param[OptionsDefine.Version])
        return

    param = {
        "HaVipId": Utils.try_to_json(argv, "--HaVipId"),

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


def doDetachNetworkInterface(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DetachNetworkInterface", g_param[OptionsDefine.Version])
        return

    param = {
        "NetworkInterfaceId": Utils.try_to_json(argv, "--NetworkInterfaceId"),
        "InstanceId": Utils.try_to_json(argv, "--InstanceId"),

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


def doDeleteNetworkInterface(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteNetworkInterface", g_param[OptionsDefine.Version])
        return

    param = {
        "NetworkInterfaceId": Utils.try_to_json(argv, "--NetworkInterfaceId"),

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


def doDescribeFlowLog(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeFlowLog", g_param[OptionsDefine.Version])
        return

    param = {
        "VpcId": Utils.try_to_json(argv, "--VpcId"),
        "FlowLogId": Utils.try_to_json(argv, "--FlowLogId"),

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


def doReplaceRoutes(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ReplaceRoutes", g_param[OptionsDefine.Version])
        return

    param = {
        "RouteTableId": Utils.try_to_json(argv, "--RouteTableId"),
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


def doUnassignIpv6SubnetCidrBlock(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("UnassignIpv6SubnetCidrBlock", g_param[OptionsDefine.Version])
        return

    param = {
        "VpcId": Utils.try_to_json(argv, "--VpcId"),
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


def doDescribeRouteConflicts(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeRouteConflicts", g_param[OptionsDefine.Version])
        return

    param = {
        "RouteTableId": Utils.try_to_json(argv, "--RouteTableId"),
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
        "RouteTableId": Utils.try_to_json(argv, "--RouteTableId"),
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


def doDescribeCcnRegionBandwidthLimits(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeCcnRegionBandwidthLimits", g_param[OptionsDefine.Version])
        return

    param = {
        "CcnId": Utils.try_to_json(argv, "--CcnId"),

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


def doAddIp6Rules(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("AddIp6Rules", g_param[OptionsDefine.Version])
        return

    param = {
        "Ip6TranslatorId": Utils.try_to_json(argv, "--Ip6TranslatorId"),
        "Ip6RuleInfos": Utils.try_to_json(argv, "--Ip6RuleInfos"),
        "Ip6RuleName": Utils.try_to_json(argv, "--Ip6RuleName"),

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


def doDeleteServiceTemplate(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteServiceTemplate", g_param[OptionsDefine.Version])
        return

    param = {
        "ServiceTemplateId": Utils.try_to_json(argv, "--ServiceTemplateId"),

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
        "NetworkInterfaceId": Utils.try_to_json(argv, "--NetworkInterfaceId"),
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
        "AddressTemplateGroupId": Utils.try_to_json(argv, "--AddressTemplateGroupId"),

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
        "CcnId": Utils.try_to_json(argv, "--CcnId"),
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


def doCreateIp6Translators(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateIp6Translators", g_param[OptionsDefine.Version])
        return

    param = {
        "Ip6TranslatorName": Utils.try_to_json(argv, "--Ip6TranslatorName"),
        "Ip6TranslatorCount": Utils.try_to_json(argv, "--Ip6TranslatorCount"),
        "Ip6InternetServiceProvider": Utils.try_to_json(argv, "--Ip6InternetServiceProvider"),

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


def doCreateDefaultVpc(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateDefaultVpc", g_param[OptionsDefine.Version])
        return

    param = {
        "Zone": Utils.try_to_json(argv, "--Zone"),
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
        "NetworkInterfaceId": Utils.try_to_json(argv, "--NetworkInterfaceId"),
        "InstanceId": Utils.try_to_json(argv, "--InstanceId"),

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
        "DirectConnectGatewayId": Utils.try_to_json(argv, "--DirectConnectGatewayId"),
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


def doDeleteSecurityGroupPolicies(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteSecurityGroupPolicies", g_param[OptionsDefine.Version])
        return

    param = {
        "SecurityGroupId": Utils.try_to_json(argv, "--SecurityGroupId"),
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


def doModifySecurityGroupAttribute(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifySecurityGroupAttribute", g_param[OptionsDefine.Version])
        return

    param = {
        "SecurityGroupId": Utils.try_to_json(argv, "--SecurityGroupId"),
        "GroupName": Utils.try_to_json(argv, "--GroupName"),
        "GroupDescription": Utils.try_to_json(argv, "--GroupDescription"),

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
        "AddressTemplateId": Utils.try_to_json(argv, "--AddressTemplateId"),

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


def doDeleteVpnGateway(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteVpnGateway", g_param[OptionsDefine.Version])
        return

    param = {
        "VpnGatewayId": Utils.try_to_json(argv, "--VpnGatewayId"),

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
        "ServiceTemplateName": Utils.try_to_json(argv, "--ServiceTemplateName"),
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
        "RouteTableId": Utils.try_to_json(argv, "--RouteTableId"),
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
        "DirectConnectGatewayId": Utils.try_to_json(argv, "--DirectConnectGatewayId"),
        "DirectConnectGatewayName": Utils.try_to_json(argv, "--DirectConnectGatewayName"),
        "CcnRouteType": Utils.try_to_json(argv, "--CcnRouteType"),

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


def doModifySubnetAttribute(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifySubnetAttribute", g_param[OptionsDefine.Version])
        return

    param = {
        "SubnetId": Utils.try_to_json(argv, "--SubnetId"),
        "SubnetName": Utils.try_to_json(argv, "--SubnetName"),
        "EnableBroadcast": Utils.try_to_json(argv, "--EnableBroadcast"),

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
        "CcnId": Utils.try_to_json(argv, "--CcnId"),
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
        "InstanceChargeType": Utils.try_to_json(argv, "--InstanceChargeType"),
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
        "VpnGatewayId": Utils.try_to_json(argv, "--VpnGatewayId"),
        "VpnConnectionId": Utils.try_to_json(argv, "--VpnConnectionId"),

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
        "CustomerGatewayName": Utils.try_to_json(argv, "--CustomerGatewayName"),
        "IpAddress": Utils.try_to_json(argv, "--IpAddress"),

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
        "AddressTemplateGroupName": Utils.try_to_json(argv, "--AddressTemplateGroupName"),
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
        "AddressTemplateName": Utils.try_to_json(argv, "--AddressTemplateName"),
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
        "GroupName": Utils.try_to_json(argv, "--GroupName"),
        "GroupDescription": Utils.try_to_json(argv, "--GroupDescription"),
        "ProjectId": Utils.try_to_json(argv, "--ProjectId"),

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


def doModifyNetworkInterfaceAttribute(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyNetworkInterfaceAttribute", g_param[OptionsDefine.Version])
        return

    param = {
        "NetworkInterfaceId": Utils.try_to_json(argv, "--NetworkInterfaceId"),
        "NetworkInterfaceName": Utils.try_to_json(argv, "--NetworkInterfaceName"),
        "NetworkInterfaceDescription": Utils.try_to_json(argv, "--NetworkInterfaceDescription"),
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


def doDeleteRouteTable(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteRouteTable", g_param[OptionsDefine.Version])
        return

    param = {
        "RouteTableId": Utils.try_to_json(argv, "--RouteTableId"),

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


def doDisassociateAddress(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DisassociateAddress", g_param[OptionsDefine.Version])
        return

    param = {
        "AddressId": Utils.try_to_json(argv, "--AddressId"),
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


def doModifyIpv6AddressesAttribute(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyIpv6AddressesAttribute", g_param[OptionsDefine.Version])
        return

    param = {
        "NetworkInterfaceId": Utils.try_to_json(argv, "--NetworkInterfaceId"),
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
        "Ip6TranslatorId": Utils.try_to_json(argv, "--Ip6TranslatorId"),
        "Ip6TranslatorName": Utils.try_to_json(argv, "--Ip6TranslatorName"),

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
        "NetworkInterfaceId": Utils.try_to_json(argv, "--NetworkInterfaceId"),
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
        "SourceNetworkInterfaceId": Utils.try_to_json(argv, "--SourceNetworkInterfaceId"),
        "DestinationNetworkInterfaceId": Utils.try_to_json(argv, "--DestinationNetworkInterfaceId"),
        "PrivateIpAddress": Utils.try_to_json(argv, "--PrivateIpAddress"),

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
        "VpcId": Utils.try_to_json(argv, "--VpcId"),
        "Ipv6CidrBlock": Utils.try_to_json(argv, "--Ipv6CidrBlock"),

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


def doHaVipAssociateAddressIp(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("HaVipAssociateAddressIp", g_param[OptionsDefine.Version])
        return

    param = {
        "HaVipId": Utils.try_to_json(argv, "--HaVipId"),
        "AddressIp": Utils.try_to_json(argv, "--AddressIp"),

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
        "Ip6TranslatorId": Utils.try_to_json(argv, "--Ip6TranslatorId"),
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


def doDeleteHaVip(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteHaVip", g_param[OptionsDefine.Version])
        return

    param = {
        "HaVipId": Utils.try_to_json(argv, "--HaVipId"),

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
        "BandwidthPackageId": Utils.try_to_json(argv, "--BandwidthPackageId"),
        "BandwidthPackageName": Utils.try_to_json(argv, "--BandwidthPackageName"),

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
        "VpnGatewayId": Utils.try_to_json(argv, "--VpnGatewayId"),
        "VpnGatewayName": Utils.try_to_json(argv, "--VpnGatewayName"),
        "InstanceChargeType": Utils.try_to_json(argv, "--InstanceChargeType"),

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
        "VpnGatewayId": Utils.try_to_json(argv, "--VpnGatewayId"),
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
        "VpcId": Utils.try_to_json(argv, "--VpcId"),

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
        "CcnName": Utils.try_to_json(argv, "--CcnName"),
        "CcnDescription": Utils.try_to_json(argv, "--CcnDescription"),
        "QosLevel": Utils.try_to_json(argv, "--QosLevel"),

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
        "CustomerGatewayId": Utils.try_to_json(argv, "--CustomerGatewayId"),
        "CustomerGatewayName": Utils.try_to_json(argv, "--CustomerGatewayName"),

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
        "VpnConnectionId": Utils.try_to_json(argv, "--VpnConnectionId"),
        "VpnConnectionName": Utils.try_to_json(argv, "--VpnConnectionName"),
        "PreShareKey": Utils.try_to_json(argv, "--PreShareKey"),
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
        "VpcId": Utils.try_to_json(argv, "--VpcId"),
        "VpnGatewayName": Utils.try_to_json(argv, "--VpnGatewayName"),
        "InternetMaxBandwidthOut": Utils.try_to_json(argv, "--InternetMaxBandwidthOut"),
        "InstanceChargeType": Utils.try_to_json(argv, "--InstanceChargeType"),
        "InstanceChargePrepaid": Utils.try_to_json(argv, "--InstanceChargePrepaid"),
        "Zone": Utils.try_to_json(argv, "--Zone"),

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
        "SecurityGroupId": Utils.try_to_json(argv, "--SecurityGroupId"),

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


def doCreateDirectConnectGateway(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateDirectConnectGateway", g_param[OptionsDefine.Version])
        return

    param = {
        "DirectConnectGatewayName": Utils.try_to_json(argv, "--DirectConnectGatewayName"),
        "NetworkType": Utils.try_to_json(argv, "--NetworkType"),
        "NetworkInstanceId": Utils.try_to_json(argv, "--NetworkInstanceId"),
        "GatewayType": Utils.try_to_json(argv, "--GatewayType"),

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
        "InstanceId": Utils.try_to_json(argv, "--InstanceId"),

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
        "RouteTableId": Utils.try_to_json(argv, "--RouteTableId"),
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


def doSetCcnRegionBandwidthLimits(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("SetCcnRegionBandwidthLimits", g_param[OptionsDefine.Version])
        return

    param = {
        "CcnId": Utils.try_to_json(argv, "--CcnId"),
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


def doCreateHaVip(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateHaVip", g_param[OptionsDefine.Version])
        return

    param = {
        "VpcId": Utils.try_to_json(argv, "--VpcId"),
        "SubnetId": Utils.try_to_json(argv, "--SubnetId"),
        "HaVipName": Utils.try_to_json(argv, "--HaVipName"),
        "Vip": Utils.try_to_json(argv, "--Vip"),

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


def doDeleteSecurityGroup(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteSecurityGroup", g_param[OptionsDefine.Version])
        return

    param = {
        "SecurityGroupId": Utils.try_to_json(argv, "--SecurityGroupId"),

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


def doModifyRouteTableAttribute(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyRouteTableAttribute", g_param[OptionsDefine.Version])
        return

    param = {
        "RouteTableId": Utils.try_to_json(argv, "--RouteTableId"),
        "RouteTableName": Utils.try_to_json(argv, "--RouteTableName"),

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


def doCreateRoutes(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateRoutes", g_param[OptionsDefine.Version])
        return

    param = {
        "RouteTableId": Utils.try_to_json(argv, "--RouteTableId"),
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
        "HaVipId": Utils.try_to_json(argv, "--HaVipId"),
        "HaVipName": Utils.try_to_json(argv, "--HaVipName"),

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
        "ServiceTemplateGroupName": Utils.try_to_json(argv, "--ServiceTemplateGroupName"),
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


def doModifyCcnAttribute(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyCcnAttribute", g_param[OptionsDefine.Version])
        return

    param = {
        "CcnId": Utils.try_to_json(argv, "--CcnId"),
        "CcnName": Utils.try_to_json(argv, "--CcnName"),
        "CcnDescription": Utils.try_to_json(argv, "--CcnDescription"),

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


def doDescribeVpcPrivateIpAddresses(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeVpcPrivateIpAddresses", g_param[OptionsDefine.Version])
        return

    param = {
        "VpcId": Utils.try_to_json(argv, "--VpcId"),
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


def doDescribeAddressTemplates(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeAddressTemplates", g_param[OptionsDefine.Version])
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
        "VpcId": Utils.try_to_json(argv, "--VpcId"),
        "VpnGatewayId": Utils.try_to_json(argv, "--VpnGatewayId"),
        "CustomerGatewayId": Utils.try_to_json(argv, "--CustomerGatewayId"),
        "VpnConnectionName": Utils.try_to_json(argv, "--VpnConnectionName"),
        "PreShareKey": Utils.try_to_json(argv, "--PreShareKey"),
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
        "AddressId": Utils.try_to_json(argv, "--AddressId"),
        "AddressName": Utils.try_to_json(argv, "--AddressName"),

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
        "VpcId": Utils.try_to_json(argv, "--VpcId"),
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


def doCreateSecurityGroupPolicies(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateSecurityGroupPolicies", g_param[OptionsDefine.Version])
        return

    param = {
        "SecurityGroupId": Utils.try_to_json(argv, "--SecurityGroupId"),
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


def doModifyVpcAttribute(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyVpcAttribute", g_param[OptionsDefine.Version])
        return

    param = {
        "VpcId": Utils.try_to_json(argv, "--VpcId"),
        "VpcName": Utils.try_to_json(argv, "--VpcName"),
        "EnableMulticast": Utils.try_to_json(argv, "--EnableMulticast"),
        "DnsServers": Utils.try_to_json(argv, "--DnsServers"),
        "DomainName": Utils.try_to_json(argv, "--DomainName"),

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


CLIENT_MAP = {
    "v20170312": vpc_client_v20170312,

}

MODELS_MAP = {
    "v20170312": models_v20170312,

}

ACTION_MAP = {
    "DownloadCustomerGatewayConfiguration": doDownloadCustomerGatewayConfiguration,
    "DescribeCustomerGateways": doDescribeCustomerGateways,
    "ReplaceSecurityGroupPolicy": doReplaceSecurityGroupPolicy,
    "CreateFlowLog": doCreateFlowLog,
    "DescribeServiceTemplateGroups": doDescribeServiceTemplateGroups,
    "DescribeRouteTables": doDescribeRouteTables,
    "CreateBandwidthPackage": doCreateBandwidthPackage,
    "DeleteFlowLog": doDeleteFlowLog,
    "CreateRouteTable": doCreateRouteTable,
    "AssignIpv6CidrBlock": doAssignIpv6CidrBlock,
    "EnableCcnRoutes": doEnableCcnRoutes,
    "ModifyFlowLogAttribute": doModifyFlowLogAttribute,
    "ModifyServiceTemplateGroupAttribute": doModifyServiceTemplateGroupAttribute,
    "DescribeCcnAttachedInstances": doDescribeCcnAttachedInstances,
    "ResetRoutes": doResetRoutes,
    "ModifyPrivateIpAddressesAttribute": doModifyPrivateIpAddressesAttribute,
    "DescribeGatewayFlowMonitorDetail": doDescribeGatewayFlowMonitorDetail,
    "UnassignIpv6Addresses": doUnassignIpv6Addresses,
    "DeleteVpnConnection": doDeleteVpnConnection,
    "ModifyAddressTemplateGroupAttribute": doModifyAddressTemplateGroupAttribute,
    "DescribeCustomerGatewayVendors": doDescribeCustomerGatewayVendors,
    "DescribeAddresses": doDescribeAddresses,
    "ModifyServiceTemplateAttribute": doModifyServiceTemplateAttribute,
    "DetachCcnInstances": doDetachCcnInstances,
    "CreateDirectConnectGatewayCcnRoutes": doCreateDirectConnectGatewayCcnRoutes,
    "RemoveBandwidthPackageResources": doRemoveBandwidthPackageResources,
    "InquiryPriceRenewVpnGateway": doInquiryPriceRenewVpnGateway,
    "AssignPrivateIpAddresses": doAssignPrivateIpAddresses,
    "DescribeNatGateways": doDescribeNatGateways,
    "CreateSubnets": doCreateSubnets,
    "ReplaceRouteTableAssociation": doReplaceRouteTableAssociation,
    "DescribeVpcs": doDescribeVpcs,
    "InquiryPriceResetVpnGatewayInternetMaxBandwidth": doInquiryPriceResetVpnGatewayInternetMaxBandwidth,
    "DeleteDirectConnectGatewayCcnRoutes": doDeleteDirectConnectGatewayCcnRoutes,
    "RejectAttachCcnInstances": doRejectAttachCcnInstances,
    "MigrateNetworkInterface": doMigrateNetworkInterface,
    "ModifyAddressesBandwidth": doModifyAddressesBandwidth,
    "DescribeVpnConnections": doDescribeVpnConnections,
    "CreateSubnet": doCreateSubnet,
    "ModifyAddressTemplateAttribute": doModifyAddressTemplateAttribute,
    "AcceptAttachCcnInstances": doAcceptAttachCcnInstances,
    "DeleteServiceTemplateGroup": doDeleteServiceTemplateGroup,
    "DescribeIp6Translators": doDescribeIp6Translators,
    "ResetAttachCcnInstances": doResetAttachCcnInstances,
    "CreateVpc": doCreateVpc,
    "ModifyIp6Rule": doModifyIp6Rule,
    "AddBandwidthPackageResources": doAddBandwidthPackageResources,
    "AssignIpv6SubnetCidrBlock": doAssignIpv6SubnetCidrBlock,
    "AllocateAddresses": doAllocateAddresses,
    "DescribeVpcIpv6Addresses": doDescribeVpcIpv6Addresses,
    "RenewVpnGateway": doRenewVpnGateway,
    "AttachCcnInstances": doAttachCcnInstances,
    "AssociateAddress": doAssociateAddress,
    "DeleteCustomerGateway": doDeleteCustomerGateway,
    "DeleteSubnet": doDeleteSubnet,
    "AttachClassicLinkVpc": doAttachClassicLinkVpc,
    "DescribeFlowLogs": doDescribeFlowLogs,
    "DeleteDirectConnectGateway": doDeleteDirectConnectGateway,
    "DescribeDirectConnectGatewayCcnRoutes": doDescribeDirectConnectGatewayCcnRoutes,
    "CreateNetworkInterface": doCreateNetworkInterface,
    "DeleteBandwidthPackage": doDeleteBandwidthPackage,
    "ModifySecurityGroupPolicies": doModifySecurityGroupPolicies,
    "DescribeCcns": doDescribeCcns,
    "DeleteIp6Translators": doDeleteIp6Translators,
    "DeleteCcn": doDeleteCcn,
    "HaVipDisassociateAddressIp": doHaVipDisassociateAddressIp,
    "DetachNetworkInterface": doDetachNetworkInterface,
    "DeleteNetworkInterface": doDeleteNetworkInterface,
    "DescribeFlowLog": doDescribeFlowLog,
    "ReplaceRoutes": doReplaceRoutes,
    "UnassignIpv6SubnetCidrBlock": doUnassignIpv6SubnetCidrBlock,
    "DescribeRouteConflicts": doDescribeRouteConflicts,
    "DisableRoutes": doDisableRoutes,
    "DescribeCcnRegionBandwidthLimits": doDescribeCcnRegionBandwidthLimits,
    "AddIp6Rules": doAddIp6Rules,
    "DeleteServiceTemplate": doDeleteServiceTemplate,
    "UnassignPrivateIpAddresses": doUnassignPrivateIpAddresses,
    "DeleteAddressTemplateGroup": doDeleteAddressTemplateGroup,
    "DescribeCcnRoutes": doDescribeCcnRoutes,
    "CreateIp6Translators": doCreateIp6Translators,
    "CreateDefaultVpc": doCreateDefaultVpc,
    "AttachNetworkInterface": doAttachNetworkInterface,
    "ReplaceDirectConnectGatewayCcnRoutes": doReplaceDirectConnectGatewayCcnRoutes,
    "DeleteSecurityGroupPolicies": doDeleteSecurityGroupPolicies,
    "ModifySecurityGroupAttribute": doModifySecurityGroupAttribute,
    "DeleteAddressTemplate": doDeleteAddressTemplate,
    "DeleteVpnGateway": doDeleteVpnGateway,
    "CreateServiceTemplate": doCreateServiceTemplate,
    "DeleteRoutes": doDeleteRoutes,
    "ModifyDirectConnectGatewayAttribute": doModifyDirectConnectGatewayAttribute,
    "ModifySubnetAttribute": doModifySubnetAttribute,
    "DescribeNetworkInterfaces": doDescribeNetworkInterfaces,
    "DisableCcnRoutes": doDisableCcnRoutes,
    "InquiryPriceCreateVpnGateway": doInquiryPriceCreateVpnGateway,
    "ResetVpnConnection": doResetVpnConnection,
    "CreateCustomerGateway": doCreateCustomerGateway,
    "CreateAddressTemplateGroup": doCreateAddressTemplateGroup,
    "CreateAddressTemplate": doCreateAddressTemplate,
    "CreateSecurityGroup": doCreateSecurityGroup,
    "ModifyNetworkInterfaceAttribute": doModifyNetworkInterfaceAttribute,
    "DescribeVpnGateways": doDescribeVpnGateways,
    "DeleteRouteTable": doDeleteRouteTable,
    "DisassociateAddress": doDisassociateAddress,
    "ModifyIpv6AddressesAttribute": doModifyIpv6AddressesAttribute,
    "DescribeDirectConnectGateways": doDescribeDirectConnectGateways,
    "ModifyIp6Translator": doModifyIp6Translator,
    "DescribeAccountAttributes": doDescribeAccountAttributes,
    "AssignIpv6Addresses": doAssignIpv6Addresses,
    "MigratePrivateIpAddress": doMigratePrivateIpAddress,
    "DescribeServiceTemplates": doDescribeServiceTemplates,
    "UnassignIpv6CidrBlock": doUnassignIpv6CidrBlock,
    "HaVipAssociateAddressIp": doHaVipAssociateAddressIp,
    "RemoveIp6Rules": doRemoveIp6Rules,
    "DescribeHaVips": doDescribeHaVips,
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
    "CreateDirectConnectGateway": doCreateDirectConnectGateway,
    "DescribeClassicLinkInstances": doDescribeClassicLinkInstances,
    "TransformAddress": doTransformAddress,
    "EnableRoutes": doEnableRoutes,
    "SetCcnRegionBandwidthLimits": doSetCcnRegionBandwidthLimits,
    "CreateHaVip": doCreateHaVip,
    "DeleteSecurityGroup": doDeleteSecurityGroup,
    "ModifyRouteTableAttribute": doModifyRouteTableAttribute,
    "CreateRoutes": doCreateRoutes,
    "DescribeBandwidthPackageQuota": doDescribeBandwidthPackageQuota,
    "ModifyHaVipAttribute": doModifyHaVipAttribute,
    "ReleaseAddresses": doReleaseAddresses,
    "DescribeBandwidthPackages": doDescribeBandwidthPackages,
    "CreateServiceTemplateGroup": doCreateServiceTemplateGroup,
    "ModifyCcnAttribute": doModifyCcnAttribute,
    "DescribeVpcPrivateIpAddresses": doDescribeVpcPrivateIpAddresses,
    "DescribeSecurityGroupAssociationStatistics": doDescribeSecurityGroupAssociationStatistics,
    "DescribeAddressTemplates": doDescribeAddressTemplates,
    "CreateVpnConnection": doCreateVpnConnection,
    "ModifyAddressAttribute": doModifyAddressAttribute,
    "DescribeAddressTemplateGroups": doDescribeAddressTemplateGroups,
    "DetachClassicLinkVpc": doDetachClassicLinkVpc,
    "CreateSecurityGroupPolicies": doCreateSecurityGroupPolicies,
    "ModifyVpcAttribute": doModifyVpcAttribute,
    "DescribeIp6TranslatorQuota": doDescribeIp6TranslatorQuota,

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
