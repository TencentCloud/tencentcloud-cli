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
from tencentcloud.ds.v20180523 import ds_client as ds_client_v20180523
from tencentcloud.ds.v20180523 import models as models_v20180523
from tccli.services.ds import v20180523
from tccli.services.ds.v20180523 import help as v20180523_help


def doCreateContractByUpload(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateContractByUpload", g_param[OptionsDefine.Version])
        return

    param = {
        "Module": Utils.try_to_json(argv, "--Module"),
        "Operation": Utils.try_to_json(argv, "--Operation"),
        "SignInfos": Utils.try_to_json(argv, "--SignInfos"),
        "ContractFile": Utils.try_to_json(argv, "--ContractFile"),
        "ContractName": Utils.try_to_json(argv, "--ContractName"),
        "Initiator": Utils.try_to_json(argv, "--Initiator"),
        "Remarks": Utils.try_to_json(argv, "--Remarks"),
        "ExpireTime": Utils.try_to_json(argv, "--ExpireTime"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.DsClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateContractByUploadRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateContractByUpload(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateSeal(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateSeal", g_param[OptionsDefine.Version])
        return

    param = {
        "Module": Utils.try_to_json(argv, "--Module"),
        "Operation": Utils.try_to_json(argv, "--Operation"),
        "AccountResId": Utils.try_to_json(argv, "--AccountResId"),
        "ImgUrl": Utils.try_to_json(argv, "--ImgUrl"),
        "ImgData": Utils.try_to_json(argv, "--ImgData"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.DsClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateSealRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateSeal(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDownloadContract(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DownloadContract", g_param[OptionsDefine.Version])
        return

    param = {
        "Module": Utils.try_to_json(argv, "--Module"),
        "Operation": Utils.try_to_json(argv, "--Operation"),
        "ContractResId": Utils.try_to_json(argv, "--ContractResId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.DsClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DownloadContractRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DownloadContract(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteAccount(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteAccount", g_param[OptionsDefine.Version])
        return

    param = {
        "Module": Utils.try_to_json(argv, "--Module"),
        "Operation": Utils.try_to_json(argv, "--Operation"),
        "AccountList": Utils.try_to_json(argv, "--AccountList"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.DsClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteAccountRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeleteAccount(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeTaskStatus(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeTaskStatus", g_param[OptionsDefine.Version])
        return

    param = {
        "Module": Utils.try_to_json(argv, "--Module"),
        "Operation": Utils.try_to_json(argv, "--Operation"),
        "TaskId": Utils.try_to_json(argv, "--TaskId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.DsClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeTaskStatusRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeTaskStatus(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreatePersonalAccount(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreatePersonalAccount", g_param[OptionsDefine.Version])
        return

    param = {
        "Module": Utils.try_to_json(argv, "--Module"),
        "Operation": Utils.try_to_json(argv, "--Operation"),
        "Name": Utils.try_to_json(argv, "--Name"),
        "IdentType": Utils.try_to_json(argv, "--IdentType"),
        "IdentNo": Utils.try_to_json(argv, "--IdentNo"),
        "MobilePhone": Utils.try_to_json(argv, "--MobilePhone"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.DsClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreatePersonalAccountRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreatePersonalAccount(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doSignContractByKeyword(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("SignContractByKeyword", g_param[OptionsDefine.Version])
        return

    param = {
        "Module": Utils.try_to_json(argv, "--Module"),
        "Operation": Utils.try_to_json(argv, "--Operation"),
        "ContractResId": Utils.try_to_json(argv, "--ContractResId"),
        "AccountResId": Utils.try_to_json(argv, "--AccountResId"),
        "AuthorizationTime": Utils.try_to_json(argv, "--AuthorizationTime"),
        "Position": Utils.try_to_json(argv, "--Position"),
        "SignKeyword": Utils.try_to_json(argv, "--SignKeyword"),
        "SealResId": Utils.try_to_json(argv, "--SealResId"),
        "CertType": Utils.try_to_json(argv, "--CertType"),
        "ImageData": Utils.try_to_json(argv, "--ImageData"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.DsClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.SignContractByKeywordRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.SignContractByKeyword(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteSeal(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteSeal", g_param[OptionsDefine.Version])
        return

    param = {
        "Module": Utils.try_to_json(argv, "--Module"),
        "Operation": Utils.try_to_json(argv, "--Operation"),
        "AccountResId": Utils.try_to_json(argv, "--AccountResId"),
        "SealResId": Utils.try_to_json(argv, "--SealResId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.DsClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteSealRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeleteSeal(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateEnterpriseAccount(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateEnterpriseAccount", g_param[OptionsDefine.Version])
        return

    param = {
        "Module": Utils.try_to_json(argv, "--Module"),
        "Operation": Utils.try_to_json(argv, "--Operation"),
        "Name": Utils.try_to_json(argv, "--Name"),
        "IdentType": Utils.try_to_json(argv, "--IdentType"),
        "IdentNo": Utils.try_to_json(argv, "--IdentNo"),
        "MobilePhone": Utils.try_to_json(argv, "--MobilePhone"),
        "TransactorName": Utils.try_to_json(argv, "--TransactorName"),
        "TransactorIdentType": Utils.try_to_json(argv, "--TransactorIdentType"),
        "TransactorIdentNo": Utils.try_to_json(argv, "--TransactorIdentNo"),
        "TransactorPhone": Utils.try_to_json(argv, "--TransactorPhone"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.DsClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateEnterpriseAccountRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateEnterpriseAccount(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doSendVcode(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("SendVcode", g_param[OptionsDefine.Version])
        return

    param = {
        "Module": Utils.try_to_json(argv, "--Module"),
        "Operation": Utils.try_to_json(argv, "--Operation"),
        "ContractResId": Utils.try_to_json(argv, "--ContractResId"),
        "AccountResId": Utils.try_to_json(argv, "--AccountResId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.DsClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.SendVcodeRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.SendVcode(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCheckVcode(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CheckVcode", g_param[OptionsDefine.Version])
        return

    param = {
        "Module": Utils.try_to_json(argv, "--Module"),
        "Operation": Utils.try_to_json(argv, "--Operation"),
        "AccountResId": Utils.try_to_json(argv, "--AccountResId"),
        "ContractResId": Utils.try_to_json(argv, "--ContractResId"),
        "VerifyCode": Utils.try_to_json(argv, "--VerifyCode"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.DsClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CheckVcodeRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CheckVcode(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doSignContractByCoordinate(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("SignContractByCoordinate", g_param[OptionsDefine.Version])
        return

    param = {
        "Module": Utils.try_to_json(argv, "--Module"),
        "Operation": Utils.try_to_json(argv, "--Operation"),
        "ContractResId": Utils.try_to_json(argv, "--ContractResId"),
        "AccountResId": Utils.try_to_json(argv, "--AccountResId"),
        "AuthorizationTime": Utils.try_to_json(argv, "--AuthorizationTime"),
        "Position": Utils.try_to_json(argv, "--Position"),
        "SignLocations": Utils.try_to_json(argv, "--SignLocations"),
        "SealResId": Utils.try_to_json(argv, "--SealResId"),
        "CertType": Utils.try_to_json(argv, "--CertType"),
        "ImageData": Utils.try_to_json(argv, "--ImageData"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.DsClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.SignContractByCoordinateRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.SignContractByCoordinate(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


CLIENT_MAP = {
    "v20180523": ds_client_v20180523,

}

MODELS_MAP = {
    "v20180523": models_v20180523,

}

ACTION_MAP = {
    "CreateContractByUpload": doCreateContractByUpload,
    "CreateSeal": doCreateSeal,
    "DownloadContract": doDownloadContract,
    "DeleteAccount": doDeleteAccount,
    "DescribeTaskStatus": doDescribeTaskStatus,
    "CreatePersonalAccount": doCreatePersonalAccount,
    "SignContractByKeyword": doSignContractByKeyword,
    "DeleteSeal": doDeleteSeal,
    "CreateEnterpriseAccount": doCreateEnterpriseAccount,
    "SendVcode": doSendVcode,
    "CheckVcode": doCheckVcode,
    "SignContractByCoordinate": doSignContractByCoordinate,

}

AVAILABLE_VERSION_LIST = [
    v20180523.version,

]
AVAILABLE_VERSIONS = {
     'v' + v20180523.version.replace('-', ''): {"help": v20180523_help.INFO,"desc": v20180523_help.DESC},

}


def ds_action(argv, arglist):
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
        helpstr = HelpTemplate.SERVICE % {"name": "ds", "desc": desc, "actions": action_str}
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
    cmd = NiceCommand("ds", ds_action)
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
            version = config["ds"][OptionsDefine.Version]
            params[OptionsDefine.Version] = "v" + version.replace('-', '')

        if params[OptionsDefine.Endpoint] is None:
            params[OptionsDefine.Endpoint] = config["ds"][OptionsDefine.Endpoint]
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

    helpmsg = HelpTemplate.ACTION % {"name": action, "service": "ds", "desc": desc, "params": docstr}
    print(helpmsg)


def get_actions_info():
    config = Configure()
    new_version = max(AVAILABLE_VERSIONS.keys())
    version = new_version
    try:
        profile = config._load_json_msg(os.path.join(config.cli_path, "default.configure"))
        version = profile["ds"]["version"]
        version = "v" + version.replace('-', '')
    except Exception:
        pass
    if version not in AVAILABLE_VERSIONS.keys():
        version = new_version
    return AVAILABLE_VERSIONS[version]["help"]
