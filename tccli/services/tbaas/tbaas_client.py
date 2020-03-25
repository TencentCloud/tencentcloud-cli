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
from tencentcloud.tbaas.v20180416 import tbaas_client as tbaas_client_v20180416
from tencentcloud.tbaas.v20180416 import models as models_v20180416
from tccli.services.tbaas import v20180416
from tccli.services.tbaas.v20180416 import help as v20180416_help


def doApplyUserCert(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ApplyUserCert", g_param[OptionsDefine.Version])
        return

    param = {
        "Module": argv.get("--Module"),
        "Operation": argv.get("--Operation"),
        "ClusterId": argv.get("--ClusterId"),
        "GroupName": argv.get("--GroupName"),
        "UserIdentity": argv.get("--UserIdentity"),
        "Applicant": argv.get("--Applicant"),
        "IdentityNum": argv.get("--IdentityNum"),
        "CsrData": argv.get("--CsrData"),
        "Notes": argv.get("--Notes"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.TbaasClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ApplyUserCertRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ApplyUserCert(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doTransByDynamicContractHandler(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("TransByDynamicContractHandler", g_param[OptionsDefine.Version])
        return

    param = {
        "Module": argv.get("--Module"),
        "Operation": argv.get("--Operation"),
        "GroupPk": argv.get("--GroupPk"),
        "ContractAddress": argv.get("--ContractAddress"),
        "ContractName": argv.get("--ContractName"),
        "AbiInfo": argv.get("--AbiInfo"),
        "FuncName": argv.get("--FuncName"),
        "FuncParam": Utils.try_to_json(argv, "--FuncParam"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.TbaasClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.TransByDynamicContractHandlerRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.TransByDynamicContractHandler(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doSrvInvoke(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("SrvInvoke", g_param[OptionsDefine.Version])
        return

    param = {
        "Service": argv.get("--Service"),
        "Method": argv.get("--Method"),
        "Param": argv.get("--Param"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.TbaasClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.SrvInvokeRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.SrvInvoke(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doInvoke(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("Invoke", g_param[OptionsDefine.Version])
        return

    param = {
        "Module": argv.get("--Module"),
        "Operation": argv.get("--Operation"),
        "ClusterId": argv.get("--ClusterId"),
        "ChaincodeName": argv.get("--ChaincodeName"),
        "ChannelName": argv.get("--ChannelName"),
        "Peers": Utils.try_to_json(argv, "--Peers"),
        "FuncName": argv.get("--FuncName"),
        "GroupName": argv.get("--GroupName"),
        "Args": Utils.try_to_json(argv, "--Args"),
        "AsyncFlag": Utils.try_to_json(argv, "--AsyncFlag"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.TbaasClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.InvokeRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.Invoke(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doGetClusterSummary(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("GetClusterSummary", g_param[OptionsDefine.Version])
        return

    param = {
        "Module": argv.get("--Module"),
        "Operation": argv.get("--Operation"),
        "ClusterId": argv.get("--ClusterId"),
        "GroupId": Utils.try_to_json(argv, "--GroupId"),
        "GroupName": argv.get("--GroupName"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.TbaasClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.GetClusterSummaryRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.GetClusterSummary(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doGetTransactionDetailForUser(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("GetTransactionDetailForUser", g_param[OptionsDefine.Version])
        return

    param = {
        "Module": argv.get("--Module"),
        "Operation": argv.get("--Operation"),
        "ClusterId": argv.get("--ClusterId"),
        "GroupName": argv.get("--GroupName"),
        "ChannelName": argv.get("--ChannelName"),
        "BlockId": Utils.try_to_json(argv, "--BlockId"),
        "TransactionId": argv.get("--TransactionId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.TbaasClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.GetTransactionDetailForUserRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.GetTransactionDetailForUser(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doBlockByNumberHandler(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("BlockByNumberHandler", g_param[OptionsDefine.Version])
        return

    param = {
        "Module": argv.get("--Module"),
        "Operation": argv.get("--Operation"),
        "GroupPk": argv.get("--GroupPk"),
        "BlockNumber": Utils.try_to_json(argv, "--BlockNumber"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.TbaasClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.BlockByNumberHandlerRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.BlockByNumberHandler(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doGetInvokeTx(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("GetInvokeTx", g_param[OptionsDefine.Version])
        return

    param = {
        "Module": argv.get("--Module"),
        "Operation": argv.get("--Operation"),
        "ClusterId": argv.get("--ClusterId"),
        "ChannelName": argv.get("--ChannelName"),
        "PeerName": argv.get("--PeerName"),
        "PeerGroup": argv.get("--PeerGroup"),
        "TxId": argv.get("--TxId"),
        "GroupName": argv.get("--GroupName"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.TbaasClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.GetInvokeTxRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.GetInvokeTx(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doGetTransListHandler(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("GetTransListHandler", g_param[OptionsDefine.Version])
        return

    param = {
        "Module": argv.get("--Module"),
        "Operation": argv.get("--Operation"),
        "Offset": Utils.try_to_json(argv, "--Offset"),
        "Limit": Utils.try_to_json(argv, "--Limit"),
        "GroupPk": argv.get("--GroupPk"),
        "TransHash": argv.get("--TransHash"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.TbaasClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.GetTransListHandlerRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.GetTransListHandler(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doSendTransactionHandler(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("SendTransactionHandler", g_param[OptionsDefine.Version])
        return

    param = {
        "Module": argv.get("--Module"),
        "Operation": argv.get("--Operation"),
        "GroupPk": argv.get("--GroupPk"),
        "ContractId": Utils.try_to_json(argv, "--ContractId"),
        "FuncName": argv.get("--FuncName"),
        "FuncParam": Utils.try_to_json(argv, "--FuncParam"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.TbaasClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.SendTransactionHandlerRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.SendTransactionHandler(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDownloadUserCert(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DownloadUserCert", g_param[OptionsDefine.Version])
        return

    param = {
        "Module": argv.get("--Module"),
        "Operation": argv.get("--Operation"),
        "CertId": Utils.try_to_json(argv, "--CertId"),
        "CertDn": argv.get("--CertDn"),
        "ClusterId": argv.get("--ClusterId"),
        "GroupName": argv.get("--GroupName"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.TbaasClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DownloadUserCertRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DownloadUserCert(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doGetBlockTransactionListForUser(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("GetBlockTransactionListForUser", g_param[OptionsDefine.Version])
        return

    param = {
        "Module": argv.get("--Module"),
        "Operation": argv.get("--Operation"),
        "ClusterId": argv.get("--ClusterId"),
        "GroupName": argv.get("--GroupName"),
        "ChannelName": argv.get("--ChannelName"),
        "BlockId": Utils.try_to_json(argv, "--BlockId"),
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
    client = mod.TbaasClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.GetBlockTransactionListForUserRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.GetBlockTransactionListForUser(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doGetBlockList(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("GetBlockList", g_param[OptionsDefine.Version])
        return

    param = {
        "Module": argv.get("--Module"),
        "Operation": argv.get("--Operation"),
        "ChannelId": Utils.try_to_json(argv, "--ChannelId"),
        "GroupId": Utils.try_to_json(argv, "--GroupId"),
        "ChannelName": argv.get("--ChannelName"),
        "GroupName": argv.get("--GroupName"),
        "ClusterId": argv.get("--ClusterId"),
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
    client = mod.TbaasClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.GetBlockListRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.GetBlockList(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doQuery(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("Query", g_param[OptionsDefine.Version])
        return

    param = {
        "Module": argv.get("--Module"),
        "Operation": argv.get("--Operation"),
        "ClusterId": argv.get("--ClusterId"),
        "ChaincodeName": argv.get("--ChaincodeName"),
        "ChannelName": argv.get("--ChannelName"),
        "Peers": Utils.try_to_json(argv, "--Peers"),
        "FuncName": argv.get("--FuncName"),
        "GroupName": argv.get("--GroupName"),
        "Args": Utils.try_to_json(argv, "--Args"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.TbaasClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.QueryRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.Query(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeployDynamicContractHandler(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeployDynamicContractHandler", g_param[OptionsDefine.Version])
        return

    param = {
        "Module": argv.get("--Module"),
        "Operation": argv.get("--Operation"),
        "GroupPk": argv.get("--GroupPk"),
        "ContractName": argv.get("--ContractName"),
        "AbiInfo": argv.get("--AbiInfo"),
        "ByteCodeBin": argv.get("--ByteCodeBin"),
        "ConstructorParams": Utils.try_to_json(argv, "--ConstructorParams"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.TbaasClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeployDynamicContractHandlerRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeployDynamicContractHandler(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doGetTransByHashHandler(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("GetTransByHashHandler", g_param[OptionsDefine.Version])
        return

    param = {
        "Module": argv.get("--Module"),
        "Operation": argv.get("--Operation"),
        "GroupPk": argv.get("--GroupPk"),
        "TransHash": argv.get("--TransHash"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.TbaasClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.GetTransByHashHandlerRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.GetTransByHashHandler(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doGetBlockListHandler(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("GetBlockListHandler", g_param[OptionsDefine.Version])
        return

    param = {
        "Module": argv.get("--Module"),
        "Operation": argv.get("--Operation"),
        "Offset": Utils.try_to_json(argv, "--Offset"),
        "Limit": Utils.try_to_json(argv, "--Limit"),
        "GroupPk": argv.get("--GroupPk"),
        "BlockHash": argv.get("--BlockHash"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.TbaasClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.GetBlockListHandlerRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.GetBlockListHandler(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doGetLatesdTransactionList(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("GetLatesdTransactionList", g_param[OptionsDefine.Version])
        return

    param = {
        "Module": argv.get("--Module"),
        "Operation": argv.get("--Operation"),
        "GroupId": Utils.try_to_json(argv, "--GroupId"),
        "ChannelId": Utils.try_to_json(argv, "--ChannelId"),
        "LatestBlockNumber": Utils.try_to_json(argv, "--LatestBlockNumber"),
        "GroupName": argv.get("--GroupName"),
        "ChannelName": argv.get("--ChannelName"),
        "ClusterId": argv.get("--ClusterId"),
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
    client = mod.TbaasClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.GetLatesdTransactionListRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.GetLatesdTransactionList(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


CLIENT_MAP = {
    "v20180416": tbaas_client_v20180416,

}

MODELS_MAP = {
    "v20180416": models_v20180416,

}

ACTION_MAP = {
    "ApplyUserCert": doApplyUserCert,
    "TransByDynamicContractHandler": doTransByDynamicContractHandler,
    "SrvInvoke": doSrvInvoke,
    "Invoke": doInvoke,
    "GetClusterSummary": doGetClusterSummary,
    "GetTransactionDetailForUser": doGetTransactionDetailForUser,
    "BlockByNumberHandler": doBlockByNumberHandler,
    "GetInvokeTx": doGetInvokeTx,
    "GetTransListHandler": doGetTransListHandler,
    "SendTransactionHandler": doSendTransactionHandler,
    "DownloadUserCert": doDownloadUserCert,
    "GetBlockTransactionListForUser": doGetBlockTransactionListForUser,
    "GetBlockList": doGetBlockList,
    "Query": doQuery,
    "DeployDynamicContractHandler": doDeployDynamicContractHandler,
    "GetTransByHashHandler": doGetTransByHashHandler,
    "GetBlockListHandler": doGetBlockListHandler,
    "GetLatesdTransactionList": doGetLatesdTransactionList,

}

AVAILABLE_VERSION_LIST = [
    v20180416.version,

]
AVAILABLE_VERSIONS = {
     'v' + v20180416.version.replace('-', ''): {"help": v20180416_help.INFO,"desc": v20180416_help.DESC},

}


def tbaas_action(argv, arglist):
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
        helpstr = HelpTemplate.SERVICE % {"name": "tbaas", "desc": desc, "actions": action_str}
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
    cmd = NiceCommand("tbaas", tbaas_action)
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
            version = config["tbaas"][OptionsDefine.Version]
            params[OptionsDefine.Version] = "v" + version.replace('-', '')

        if params[OptionsDefine.Endpoint] is None:
            params[OptionsDefine.Endpoint] = config["tbaas"][OptionsDefine.Endpoint]
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

    helpmsg = HelpTemplate.ACTION % {"name": action, "service": "tbaas", "desc": desc, "params": docstr}
    print(helpmsg)


def get_actions_info():
    config = Configure()
    new_version = max(AVAILABLE_VERSIONS.keys())
    version = new_version
    try:
        profile = config._load_json_msg(os.path.join(config.cli_path, "default.configure"))
        version = profile["tbaas"]["version"]
        version = "v" + version.replace('-', '')
    except Exception:
        pass
    if version not in AVAILABLE_VERSIONS.keys():
        version = new_version
    return AVAILABLE_VERSIONS[version]["help"]
