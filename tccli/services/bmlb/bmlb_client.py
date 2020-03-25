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
from tencentcloud.bmlb.v20180625 import bmlb_client as bmlb_client_v20180625
from tencentcloud.bmlb.v20180625 import models as models_v20180625
from tccli.services.bmlb import v20180625
from tccli.services.bmlb.v20180625 import help as v20180625_help


def doDescribeL7Listeners(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeL7Listeners", g_param[OptionsDefine.Version])
        return

    param = {
        "LoadBalancerId": argv.get("--LoadBalancerId"),
        "ListenerIds": Utils.try_to_json(argv, "--ListenerIds"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.BmlbClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeL7ListenersRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeL7Listeners(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doUnbindTrafficMirrorReceivers(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("UnbindTrafficMirrorReceivers", g_param[OptionsDefine.Version])
        return

    param = {
        "TrafficMirrorId": argv.get("--TrafficMirrorId"),
        "ReceiverSet": Utils.try_to_json(argv, "--ReceiverSet"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.BmlbClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.UnbindTrafficMirrorReceiversRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.UnbindTrafficMirrorReceivers(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyL7BackendWeight(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyL7BackendWeight", g_param[OptionsDefine.Version])
        return

    param = {
        "LoadBalancerId": argv.get("--LoadBalancerId"),
        "ListenerId": argv.get("--ListenerId"),
        "DomainId": argv.get("--DomainId"),
        "LocationId": argv.get("--LocationId"),
        "InstanceId": argv.get("--InstanceId"),
        "Weight": Utils.try_to_json(argv, "--Weight"),
        "Port": Utils.try_to_json(argv, "--Port"),
        "BindType": Utils.try_to_json(argv, "--BindType"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.BmlbClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyL7BackendWeightRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyL7BackendWeight(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyL4BackendWeight(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyL4BackendWeight", g_param[OptionsDefine.Version])
        return

    param = {
        "LoadBalancerId": argv.get("--LoadBalancerId"),
        "ListenerId": argv.get("--ListenerId"),
        "InstanceId": argv.get("--InstanceId"),
        "Weight": Utils.try_to_json(argv, "--Weight"),
        "Port": Utils.try_to_json(argv, "--Port"),
        "BindType": Utils.try_to_json(argv, "--BindType"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.BmlbClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyL4BackendWeightRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyL4BackendWeight(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateL4Listeners(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateL4Listeners", g_param[OptionsDefine.Version])
        return

    param = {
        "LoadBalancerId": argv.get("--LoadBalancerId"),
        "ListenerSet": Utils.try_to_json(argv, "--ListenerSet"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.BmlbClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateL4ListenersRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateL4Listeners(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doUnbindL4Backends(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("UnbindL4Backends", g_param[OptionsDefine.Version])
        return

    param = {
        "LoadBalancerId": argv.get("--LoadBalancerId"),
        "ListenerId": argv.get("--ListenerId"),
        "BackendSet": Utils.try_to_json(argv, "--BackendSet"),
        "BindType": Utils.try_to_json(argv, "--BindType"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.BmlbClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.UnbindL4BackendsRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.UnbindL4Backends(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyL7Listener(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyL7Listener", g_param[OptionsDefine.Version])
        return

    param = {
        "LoadBalancerId": argv.get("--LoadBalancerId"),
        "ListenerId": argv.get("--ListenerId"),
        "ListenerName": argv.get("--ListenerName"),
        "SslMode": Utils.try_to_json(argv, "--SslMode"),
        "CertId": argv.get("--CertId"),
        "CertName": argv.get("--CertName"),
        "CertContent": argv.get("--CertContent"),
        "CertKey": argv.get("--CertKey"),
        "CertCaId": argv.get("--CertCaId"),
        "CertCaName": argv.get("--CertCaName"),
        "CertCaContent": argv.get("--CertCaContent"),
        "Bandwidth": Utils.try_to_json(argv, "--Bandwidth"),
        "ForwardProtocol": Utils.try_to_json(argv, "--ForwardProtocol"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.BmlbClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyL7ListenerRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyL7Listener(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteTrafficMirror(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteTrafficMirror", g_param[OptionsDefine.Version])
        return

    param = {
        "TrafficMirrorIds": Utils.try_to_json(argv, "--TrafficMirrorIds"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.BmlbClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteTrafficMirrorRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeleteTrafficMirror(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateL7Rules(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateL7Rules", g_param[OptionsDefine.Version])
        return

    param = {
        "LoadBalancerId": argv.get("--LoadBalancerId"),
        "ListenerId": argv.get("--ListenerId"),
        "RuleSet": Utils.try_to_json(argv, "--RuleSet"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.BmlbClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateL7RulesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateL7Rules(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeTrafficMirrorReceiverHealthStatus(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeTrafficMirrorReceiverHealthStatus", g_param[OptionsDefine.Version])
        return

    param = {
        "TrafficMirrorId": argv.get("--TrafficMirrorId"),
        "ReceiverSet": Utils.try_to_json(argv, "--ReceiverSet"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.BmlbClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeTrafficMirrorReceiverHealthStatusRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeTrafficMirrorReceiverHealthStatus(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doUnbindL7Backends(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("UnbindL7Backends", g_param[OptionsDefine.Version])
        return

    param = {
        "LoadBalancerId": argv.get("--LoadBalancerId"),
        "ListenerId": argv.get("--ListenerId"),
        "DomainId": argv.get("--DomainId"),
        "LocationId": argv.get("--LocationId"),
        "BackendSet": Utils.try_to_json(argv, "--BackendSet"),
        "BindType": Utils.try_to_json(argv, "--BindType"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.BmlbClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.UnbindL7BackendsRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.UnbindL7Backends(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteL7Rules(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteL7Rules", g_param[OptionsDefine.Version])
        return

    param = {
        "LoadBalancerId": argv.get("--LoadBalancerId"),
        "ListenerId": argv.get("--ListenerId"),
        "DomainId": argv.get("--DomainId"),
        "LocationIds": Utils.try_to_json(argv, "--LocationIds"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.BmlbClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteL7RulesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeleteL7Rules(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeL4ListenerInfo(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeL4ListenerInfo", g_param[OptionsDefine.Version])
        return

    param = {
        "LoadBalancerId": argv.get("--LoadBalancerId"),
        "SearchKey": argv.get("--SearchKey"),
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
    client = mod.BmlbClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeL4ListenerInfoRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeL4ListenerInfo(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeTrafficMirrorListeners(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeTrafficMirrorListeners", g_param[OptionsDefine.Version])
        return

    param = {
        "TrafficMirrorId": argv.get("--TrafficMirrorId"),
        "Offset": Utils.try_to_json(argv, "--Offset"),
        "Limit": Utils.try_to_json(argv, "--Limit"),
        "SearchLoadBalancerIds": Utils.try_to_json(argv, "--SearchLoadBalancerIds"),
        "SearchLoadBalancerNames": Utils.try_to_json(argv, "--SearchLoadBalancerNames"),
        "SearchVips": Utils.try_to_json(argv, "--SearchVips"),
        "SearchListenerIds": Utils.try_to_json(argv, "--SearchListenerIds"),
        "SearchListenerNames": Utils.try_to_json(argv, "--SearchListenerNames"),
        "SearchProtocols": Utils.try_to_json(argv, "--SearchProtocols"),
        "SearchLoadBalancerPorts": Utils.try_to_json(argv, "--SearchLoadBalancerPorts"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.BmlbClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeTrafficMirrorListenersRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeTrafficMirrorListeners(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyL7Locations(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyL7Locations", g_param[OptionsDefine.Version])
        return

    param = {
        "LoadBalancerId": argv.get("--LoadBalancerId"),
        "ListenerId": argv.get("--ListenerId"),
        "RuleSet": Utils.try_to_json(argv, "--RuleSet"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.BmlbClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyL7LocationsRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyL7Locations(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyL4BackendPort(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyL4BackendPort", g_param[OptionsDefine.Version])
        return

    param = {
        "LoadBalancerId": argv.get("--LoadBalancerId"),
        "ListenerId": argv.get("--ListenerId"),
        "InstanceId": argv.get("--InstanceId"),
        "Port": Utils.try_to_json(argv, "--Port"),
        "NewPort": Utils.try_to_json(argv, "--NewPort"),
        "BindType": Utils.try_to_json(argv, "--BindType"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.BmlbClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyL4BackendPortRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyL4BackendPort(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteLoadBalancer(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteLoadBalancer", g_param[OptionsDefine.Version])
        return

    param = {
        "LoadBalancerId": argv.get("--LoadBalancerId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.BmlbClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteLoadBalancerRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeleteLoadBalancer(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateLoadBalancers(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateLoadBalancers", g_param[OptionsDefine.Version])
        return

    param = {
        "VpcId": argv.get("--VpcId"),
        "LoadBalancerType": argv.get("--LoadBalancerType"),
        "SubnetId": argv.get("--SubnetId"),
        "ProjectId": Utils.try_to_json(argv, "--ProjectId"),
        "GoodsNum": Utils.try_to_json(argv, "--GoodsNum"),
        "PayMode": argv.get("--PayMode"),
        "TgwSetType": argv.get("--TgwSetType"),
        "Exclusive": Utils.try_to_json(argv, "--Exclusive"),
        "SpecifiedVips": Utils.try_to_json(argv, "--SpecifiedVips"),
        "BzConf": Utils.try_to_json(argv, "--BzConf"),
        "IpProtocolType": argv.get("--IpProtocolType"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.BmlbClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateLoadBalancersRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateLoadBalancers(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeL7Rules(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeL7Rules", g_param[OptionsDefine.Version])
        return

    param = {
        "LoadBalancerId": argv.get("--LoadBalancerId"),
        "ListenerId": argv.get("--ListenerId"),
        "DomainIds": Utils.try_to_json(argv, "--DomainIds"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.BmlbClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeL7RulesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeL7Rules(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeLoadBalancerTaskResult(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeLoadBalancerTaskResult", g_param[OptionsDefine.Version])
        return

    param = {
        "TaskId": argv.get("--TaskId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.BmlbClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeLoadBalancerTaskResultRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeLoadBalancerTaskResult(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeL7ListenerInfo(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeL7ListenerInfo", g_param[OptionsDefine.Version])
        return

    param = {
        "LoadBalancerId": argv.get("--LoadBalancerId"),
        "SearchKey": argv.get("--SearchKey"),
        "InstanceIds": Utils.try_to_json(argv, "--InstanceIds"),
        "IfGetBackendInfo": Utils.try_to_json(argv, "--IfGetBackendInfo"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.BmlbClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeL7ListenerInfoRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeL7ListenerInfo(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeL4Listeners(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeL4Listeners", g_param[OptionsDefine.Version])
        return

    param = {
        "LoadBalancerId": argv.get("--LoadBalancerId"),
        "ListenerIds": Utils.try_to_json(argv, "--ListenerIds"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.BmlbClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeL4ListenersRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeL4Listeners(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doSetTrafficMirrorHealthSwitch(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("SetTrafficMirrorHealthSwitch", g_param[OptionsDefine.Version])
        return

    param = {
        "TrafficMirrorId": argv.get("--TrafficMirrorId"),
        "HealthSwitch": Utils.try_to_json(argv, "--HealthSwitch"),
        "HealthNum": Utils.try_to_json(argv, "--HealthNum"),
        "UnhealthNum": Utils.try_to_json(argv, "--UnhealthNum"),
        "IntervalTime": Utils.try_to_json(argv, "--IntervalTime"),
        "HttpCheckDomain": argv.get("--HttpCheckDomain"),
        "HttpCheckPath": argv.get("--HttpCheckPath"),
        "HttpCodes": Utils.try_to_json(argv, "--HttpCodes"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.BmlbClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.SetTrafficMirrorHealthSwitchRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.SetTrafficMirrorHealthSwitch(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeLoadBalancers(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeLoadBalancers", g_param[OptionsDefine.Version])
        return

    param = {
        "LoadBalancerIds": Utils.try_to_json(argv, "--LoadBalancerIds"),
        "LoadBalancerType": argv.get("--LoadBalancerType"),
        "LoadBalancerName": argv.get("--LoadBalancerName"),
        "Domain": argv.get("--Domain"),
        "LoadBalancerVips": Utils.try_to_json(argv, "--LoadBalancerVips"),
        "Offset": Utils.try_to_json(argv, "--Offset"),
        "Limit": Utils.try_to_json(argv, "--Limit"),
        "SearchKey": argv.get("--SearchKey"),
        "OrderBy": argv.get("--OrderBy"),
        "OrderType": Utils.try_to_json(argv, "--OrderType"),
        "ProjectId": Utils.try_to_json(argv, "--ProjectId"),
        "Exclusive": Utils.try_to_json(argv, "--Exclusive"),
        "TgwSetType": argv.get("--TgwSetType"),
        "VpcId": argv.get("--VpcId"),
        "QueryType": argv.get("--QueryType"),
        "ConfId": argv.get("--ConfId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.BmlbClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeLoadBalancersRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeLoadBalancers(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteListeners(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteListeners", g_param[OptionsDefine.Version])
        return

    param = {
        "LoadBalancerId": argv.get("--LoadBalancerId"),
        "ListenerIds": Utils.try_to_json(argv, "--ListenerIds"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.BmlbClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteListenersRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeleteListeners(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeCertDetail(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeCertDetail", g_param[OptionsDefine.Version])
        return

    param = {
        "CertId": argv.get("--CertId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.BmlbClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeCertDetailRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeCertDetail(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doUnbindTrafficMirrorListeners(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("UnbindTrafficMirrorListeners", g_param[OptionsDefine.Version])
        return

    param = {
        "TrafficMirrorId": argv.get("--TrafficMirrorId"),
        "ListenerIds": Utils.try_to_json(argv, "--ListenerIds"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.BmlbClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.UnbindTrafficMirrorListenersRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.UnbindTrafficMirrorListeners(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyL7BackendPort(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyL7BackendPort", g_param[OptionsDefine.Version])
        return

    param = {
        "LoadBalancerId": argv.get("--LoadBalancerId"),
        "ListenerId": argv.get("--ListenerId"),
        "DomainId": argv.get("--DomainId"),
        "LocationId": argv.get("--LocationId"),
        "InstanceId": argv.get("--InstanceId"),
        "Port": Utils.try_to_json(argv, "--Port"),
        "NewPort": Utils.try_to_json(argv, "--NewPort"),
        "BindType": Utils.try_to_json(argv, "--BindType"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.BmlbClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyL7BackendPortRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyL7BackendPort(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeL7Backends(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeL7Backends", g_param[OptionsDefine.Version])
        return

    param = {
        "LoadBalancerId": argv.get("--LoadBalancerId"),
        "ListenerId": argv.get("--ListenerId"),
        "DomainId": argv.get("--DomainId"),
        "LocationId": argv.get("--LocationId"),
        "QueryType": argv.get("--QueryType"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.BmlbClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeL7BackendsRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeL7Backends(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateTrafficMirror(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateTrafficMirror", g_param[OptionsDefine.Version])
        return

    param = {
        "Alias": argv.get("--Alias"),
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
    client = mod.BmlbClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateTrafficMirrorRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateTrafficMirror(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyL4BackendProbePort(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyL4BackendProbePort", g_param[OptionsDefine.Version])
        return

    param = {
        "LoadBalancerId": argv.get("--LoadBalancerId"),
        "ListenerId": argv.get("--ListenerId"),
        "InstanceId": argv.get("--InstanceId"),
        "Port": Utils.try_to_json(argv, "--Port"),
        "ProbePort": Utils.try_to_json(argv, "--ProbePort"),
        "BindType": Utils.try_to_json(argv, "--BindType"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.BmlbClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyL4BackendProbePortRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyL4BackendProbePort(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doBindL4Backends(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("BindL4Backends", g_param[OptionsDefine.Version])
        return

    param = {
        "LoadBalancerId": argv.get("--LoadBalancerId"),
        "ListenerId": argv.get("--ListenerId"),
        "BackendSet": Utils.try_to_json(argv, "--BackendSet"),
        "BindType": Utils.try_to_json(argv, "--BindType"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.BmlbClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.BindL4BackendsRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.BindL4Backends(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doBindTrafficMirrorReceivers(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("BindTrafficMirrorReceivers", g_param[OptionsDefine.Version])
        return

    param = {
        "TrafficMirrorId": argv.get("--TrafficMirrorId"),
        "ReceiverSet": Utils.try_to_json(argv, "--ReceiverSet"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.BmlbClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.BindTrafficMirrorReceiversRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.BindTrafficMirrorReceivers(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doReplaceCert(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ReplaceCert", g_param[OptionsDefine.Version])
        return

    param = {
        "OldCertId": argv.get("--OldCertId"),
        "NewCert": argv.get("--NewCert"),
        "NewAlias": argv.get("--NewAlias"),
        "NewKey": argv.get("--NewKey"),
        "DeleteOld": Utils.try_to_json(argv, "--DeleteOld"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.BmlbClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ReplaceCertRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ReplaceCert(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteL7Domains(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteL7Domains", g_param[OptionsDefine.Version])
        return

    param = {
        "LoadBalancerId": argv.get("--LoadBalancerId"),
        "ListenerId": argv.get("--ListenerId"),
        "DomainIds": Utils.try_to_json(argv, "--DomainIds"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.BmlbClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteL7DomainsRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeleteL7Domains(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeTrafficMirrors(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeTrafficMirrors", g_param[OptionsDefine.Version])
        return

    param = {
        "TrafficMirrorIds": Utils.try_to_json(argv, "--TrafficMirrorIds"),
        "Aliases": Utils.try_to_json(argv, "--Aliases"),
        "VpcIds": Utils.try_to_json(argv, "--VpcIds"),
        "Offset": Utils.try_to_json(argv, "--Offset"),
        "Limit": Utils.try_to_json(argv, "--Limit"),
        "OrderField": argv.get("--OrderField"),
        "Order": Utils.try_to_json(argv, "--Order"),
        "SearchKey": argv.get("--SearchKey"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.BmlbClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeTrafficMirrorsRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeTrafficMirrors(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeL7ListenersEx(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeL7ListenersEx", g_param[OptionsDefine.Version])
        return

    param = {
        "TrafficMirrorId": argv.get("--TrafficMirrorId"),
        "VpcId": argv.get("--VpcId"),
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
    client = mod.BmlbClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeL7ListenersExRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeL7ListenersEx(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doUploadCert(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("UploadCert", g_param[OptionsDefine.Version])
        return

    param = {
        "CertType": argv.get("--CertType"),
        "Cert": argv.get("--Cert"),
        "Alias": argv.get("--Alias"),
        "Key": argv.get("--Key"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.BmlbClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.UploadCertRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.UploadCert(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doBindL7Backends(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("BindL7Backends", g_param[OptionsDefine.Version])
        return

    param = {
        "LoadBalancerId": argv.get("--LoadBalancerId"),
        "ListenerId": argv.get("--ListenerId"),
        "DomainId": argv.get("--DomainId"),
        "LocationId": argv.get("--LocationId"),
        "BackendSet": Utils.try_to_json(argv, "--BackendSet"),
        "BindType": Utils.try_to_json(argv, "--BindType"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.BmlbClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.BindL7BackendsRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.BindL7Backends(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeL4Backends(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeL4Backends", g_param[OptionsDefine.Version])
        return

    param = {
        "LoadBalancerId": argv.get("--LoadBalancerId"),
        "ListenerId": argv.get("--ListenerId"),
        "BackendSet": Utils.try_to_json(argv, "--BackendSet"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.BmlbClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeL4BackendsRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeL4Backends(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doBindTrafficMirrorListeners(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("BindTrafficMirrorListeners", g_param[OptionsDefine.Version])
        return

    param = {
        "TrafficMirrorId": argv.get("--TrafficMirrorId"),
        "ListenerIds": Utils.try_to_json(argv, "--ListenerIds"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.BmlbClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.BindTrafficMirrorListenersRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.BindTrafficMirrorListeners(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyLoadBalancer(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyLoadBalancer", g_param[OptionsDefine.Version])
        return

    param = {
        "LoadBalancerId": argv.get("--LoadBalancerId"),
        "LoadBalancerName": argv.get("--LoadBalancerName"),
        "DomainPrefix": argv.get("--DomainPrefix"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.BmlbClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyLoadBalancerRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyLoadBalancer(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doSetTrafficMirrorAlias(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("SetTrafficMirrorAlias", g_param[OptionsDefine.Version])
        return

    param = {
        "TrafficMirrorId": argv.get("--TrafficMirrorId"),
        "Alias": argv.get("--Alias"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.BmlbClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.SetTrafficMirrorAliasRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.SetTrafficMirrorAlias(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeLoadBalancerPortInfo(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeLoadBalancerPortInfo", g_param[OptionsDefine.Version])
        return

    param = {
        "LoadBalancerId": argv.get("--LoadBalancerId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.BmlbClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeLoadBalancerPortInfoRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeLoadBalancerPortInfo(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyLoadBalancerChargeMode(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyLoadBalancerChargeMode", g_param[OptionsDefine.Version])
        return

    param = {
        "LoadBalancerId": argv.get("--LoadBalancerId"),
        "PayMode": argv.get("--PayMode"),
        "ListenerSet": Utils.try_to_json(argv, "--ListenerSet"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.BmlbClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyLoadBalancerChargeModeRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyLoadBalancerChargeMode(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateL7Listeners(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateL7Listeners", g_param[OptionsDefine.Version])
        return

    param = {
        "LoadBalancerId": argv.get("--LoadBalancerId"),
        "ListenerSet": Utils.try_to_json(argv, "--ListenerSet"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.BmlbClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateL7ListenersRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateL7Listeners(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeDevicesBindInfo(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeDevicesBindInfo", g_param[OptionsDefine.Version])
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
    client = mod.BmlbClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeDevicesBindInfoRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeDevicesBindInfo(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyL4Listener(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyL4Listener", g_param[OptionsDefine.Version])
        return

    param = {
        "LoadBalancerId": argv.get("--LoadBalancerId"),
        "ListenerId": argv.get("--ListenerId"),
        "ListenerName": argv.get("--ListenerName"),
        "SessionExpire": Utils.try_to_json(argv, "--SessionExpire"),
        "HealthSwitch": Utils.try_to_json(argv, "--HealthSwitch"),
        "TimeOut": Utils.try_to_json(argv, "--TimeOut"),
        "IntervalTime": Utils.try_to_json(argv, "--IntervalTime"),
        "HealthNum": Utils.try_to_json(argv, "--HealthNum"),
        "UnhealthNum": Utils.try_to_json(argv, "--UnhealthNum"),
        "Bandwidth": Utils.try_to_json(argv, "--Bandwidth"),
        "CustomHealthSwitch": Utils.try_to_json(argv, "--CustomHealthSwitch"),
        "InputType": argv.get("--InputType"),
        "LineSeparatorType": Utils.try_to_json(argv, "--LineSeparatorType"),
        "HealthRequest": argv.get("--HealthRequest"),
        "HealthResponse": argv.get("--HealthResponse"),
        "ToaFlag": Utils.try_to_json(argv, "--ToaFlag"),
        "BalanceMode": argv.get("--BalanceMode"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.BmlbClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyL4ListenerRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyL4Listener(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeTrafficMirrorReceivers(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeTrafficMirrorReceivers", g_param[OptionsDefine.Version])
        return

    param = {
        "TrafficMirrorId": argv.get("--TrafficMirrorId"),
        "InstanceIds": Utils.try_to_json(argv, "--InstanceIds"),
        "Ports": Utils.try_to_json(argv, "--Ports"),
        "Weights": Utils.try_to_json(argv, "--Weights"),
        "Offset": Utils.try_to_json(argv, "--Offset"),
        "Limit": Utils.try_to_json(argv, "--Limit"),
        "VagueStr": argv.get("--VagueStr"),
        "VagueIp": argv.get("--VagueIp"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.BmlbClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeTrafficMirrorReceiversRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeTrafficMirrorReceivers(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


CLIENT_MAP = {
    "v20180625": bmlb_client_v20180625,

}

MODELS_MAP = {
    "v20180625": models_v20180625,

}

ACTION_MAP = {
    "DescribeL7Listeners": doDescribeL7Listeners,
    "UnbindTrafficMirrorReceivers": doUnbindTrafficMirrorReceivers,
    "ModifyL7BackendWeight": doModifyL7BackendWeight,
    "ModifyL4BackendWeight": doModifyL4BackendWeight,
    "CreateL4Listeners": doCreateL4Listeners,
    "UnbindL4Backends": doUnbindL4Backends,
    "ModifyL7Listener": doModifyL7Listener,
    "DeleteTrafficMirror": doDeleteTrafficMirror,
    "CreateL7Rules": doCreateL7Rules,
    "DescribeTrafficMirrorReceiverHealthStatus": doDescribeTrafficMirrorReceiverHealthStatus,
    "UnbindL7Backends": doUnbindL7Backends,
    "DeleteL7Rules": doDeleteL7Rules,
    "DescribeL4ListenerInfo": doDescribeL4ListenerInfo,
    "DescribeTrafficMirrorListeners": doDescribeTrafficMirrorListeners,
    "ModifyL7Locations": doModifyL7Locations,
    "ModifyL4BackendPort": doModifyL4BackendPort,
    "DeleteLoadBalancer": doDeleteLoadBalancer,
    "CreateLoadBalancers": doCreateLoadBalancers,
    "DescribeL7Rules": doDescribeL7Rules,
    "DescribeLoadBalancerTaskResult": doDescribeLoadBalancerTaskResult,
    "DescribeL7ListenerInfo": doDescribeL7ListenerInfo,
    "DescribeL4Listeners": doDescribeL4Listeners,
    "SetTrafficMirrorHealthSwitch": doSetTrafficMirrorHealthSwitch,
    "DescribeLoadBalancers": doDescribeLoadBalancers,
    "DeleteListeners": doDeleteListeners,
    "DescribeCertDetail": doDescribeCertDetail,
    "UnbindTrafficMirrorListeners": doUnbindTrafficMirrorListeners,
    "ModifyL7BackendPort": doModifyL7BackendPort,
    "DescribeL7Backends": doDescribeL7Backends,
    "CreateTrafficMirror": doCreateTrafficMirror,
    "ModifyL4BackendProbePort": doModifyL4BackendProbePort,
    "BindL4Backends": doBindL4Backends,
    "BindTrafficMirrorReceivers": doBindTrafficMirrorReceivers,
    "ReplaceCert": doReplaceCert,
    "DeleteL7Domains": doDeleteL7Domains,
    "DescribeTrafficMirrors": doDescribeTrafficMirrors,
    "DescribeL7ListenersEx": doDescribeL7ListenersEx,
    "UploadCert": doUploadCert,
    "BindL7Backends": doBindL7Backends,
    "DescribeL4Backends": doDescribeL4Backends,
    "BindTrafficMirrorListeners": doBindTrafficMirrorListeners,
    "ModifyLoadBalancer": doModifyLoadBalancer,
    "SetTrafficMirrorAlias": doSetTrafficMirrorAlias,
    "DescribeLoadBalancerPortInfo": doDescribeLoadBalancerPortInfo,
    "ModifyLoadBalancerChargeMode": doModifyLoadBalancerChargeMode,
    "CreateL7Listeners": doCreateL7Listeners,
    "DescribeDevicesBindInfo": doDescribeDevicesBindInfo,
    "ModifyL4Listener": doModifyL4Listener,
    "DescribeTrafficMirrorReceivers": doDescribeTrafficMirrorReceivers,

}

AVAILABLE_VERSION_LIST = [
    v20180625.version,

]
AVAILABLE_VERSIONS = {
     'v' + v20180625.version.replace('-', ''): {"help": v20180625_help.INFO,"desc": v20180625_help.DESC},

}


def bmlb_action(argv, arglist):
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
        helpstr = HelpTemplate.SERVICE % {"name": "bmlb", "desc": desc, "actions": action_str}
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
    cmd = NiceCommand("bmlb", bmlb_action)
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
            version = config["bmlb"][OptionsDefine.Version]
            params[OptionsDefine.Version] = "v" + version.replace('-', '')

        if params[OptionsDefine.Endpoint] is None:
            params[OptionsDefine.Endpoint] = config["bmlb"][OptionsDefine.Endpoint]
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

    helpmsg = HelpTemplate.ACTION % {"name": action, "service": "bmlb", "desc": desc, "params": docstr}
    print(helpmsg)


def get_actions_info():
    config = Configure()
    new_version = max(AVAILABLE_VERSIONS.keys())
    version = new_version
    try:
        profile = config._load_json_msg(os.path.join(config.cli_path, "default.configure"))
        version = profile["bmlb"]["version"]
        version = "v" + version.replace('-', '')
    except Exception:
        pass
    if version not in AVAILABLE_VERSIONS.keys():
        version = new_version
    return AVAILABLE_VERSIONS[version]["help"]
