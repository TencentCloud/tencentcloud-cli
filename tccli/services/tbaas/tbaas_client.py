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


def doInvoke(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("Invoke", g_param[OptionsDefine.Version])
        return

    param = {
        "Module": Utils.try_to_json(argv, "--Module"),
        "Operation": Utils.try_to_json(argv, "--Operation"),
        "ClusterId": Utils.try_to_json(argv, "--ClusterId"),
        "ChaincodeName": Utils.try_to_json(argv, "--ChaincodeName"),
        "ChannelName": Utils.try_to_json(argv, "--ChannelName"),
        "Peers": Utils.try_to_json(argv, "--Peers"),
        "FuncName": Utils.try_to_json(argv, "--FuncName"),
        "GroupName": Utils.try_to_json(argv, "--GroupName"),
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
        "Module": Utils.try_to_json(argv, "--Module"),
        "Operation": Utils.try_to_json(argv, "--Operation"),
        "ClusterId": Utils.try_to_json(argv, "--ClusterId"),
        "GroupId": Utils.try_to_json(argv, "--GroupId"),
        "GroupName": Utils.try_to_json(argv, "--GroupName"),

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


def doGetInvokeTx(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("GetInvokeTx", g_param[OptionsDefine.Version])
        return

    param = {
        "Module": Utils.try_to_json(argv, "--Module"),
        "Operation": Utils.try_to_json(argv, "--Operation"),
        "ClusterId": Utils.try_to_json(argv, "--ClusterId"),
        "ChannelName": Utils.try_to_json(argv, "--ChannelName"),
        "PeerName": Utils.try_to_json(argv, "--PeerName"),
        "PeerGroup": Utils.try_to_json(argv, "--PeerGroup"),
        "TxId": Utils.try_to_json(argv, "--TxId"),
        "GroupName": Utils.try_to_json(argv, "--GroupName"),

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


def doGetBlockList(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("GetBlockList", g_param[OptionsDefine.Version])
        return

    param = {
        "Module": Utils.try_to_json(argv, "--Module"),
        "Operation": Utils.try_to_json(argv, "--Operation"),
        "ChannelId": Utils.try_to_json(argv, "--ChannelId"),
        "GroupId": Utils.try_to_json(argv, "--GroupId"),
        "ChannelName": Utils.try_to_json(argv, "--ChannelName"),
        "GroupName": Utils.try_to_json(argv, "--GroupName"),
        "ClusterId": Utils.try_to_json(argv, "--ClusterId"),
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
        "Module": Utils.try_to_json(argv, "--Module"),
        "Operation": Utils.try_to_json(argv, "--Operation"),
        "ClusterId": Utils.try_to_json(argv, "--ClusterId"),
        "ChaincodeName": Utils.try_to_json(argv, "--ChaincodeName"),
        "ChannelName": Utils.try_to_json(argv, "--ChannelName"),
        "Peers": Utils.try_to_json(argv, "--Peers"),
        "FuncName": Utils.try_to_json(argv, "--FuncName"),
        "GroupName": Utils.try_to_json(argv, "--GroupName"),
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


def doGetLatesdTransactionList(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("GetLatesdTransactionList", g_param[OptionsDefine.Version])
        return

    param = {
        "Module": Utils.try_to_json(argv, "--Module"),
        "Operation": Utils.try_to_json(argv, "--Operation"),
        "GroupId": Utils.try_to_json(argv, "--GroupId"),
        "ChannelId": Utils.try_to_json(argv, "--ChannelId"),
        "LatestBlockNumber": Utils.try_to_json(argv, "--LatestBlockNumber"),
        "GroupName": Utils.try_to_json(argv, "--GroupName"),
        "ChannelName": Utils.try_to_json(argv, "--ChannelName"),
        "ClusterId": Utils.try_to_json(argv, "--ClusterId"),
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
    "Invoke": doInvoke,
    "GetClusterSummary": doGetClusterSummary,
    "GetInvokeTx": doGetInvokeTx,
    "GetBlockList": doGetBlockList,
    "Query": doQuery,
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
