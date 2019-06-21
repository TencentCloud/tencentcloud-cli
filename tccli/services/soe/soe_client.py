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
from tencentcloud.soe.v20180724 import soe_client as soe_client_v20180724
from tencentcloud.soe.v20180724 import models as models_v20180724
from tccli.services.soe import v20180724
from tccli.services.soe.v20180724 import help as v20180724_help


def doInitOralProcess(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("InitOralProcess", g_param[OptionsDefine.Version])
        return

    param = {
        "SessionId": Utils.try_to_json(argv, "--SessionId"),
        "RefText": Utils.try_to_json(argv, "--RefText"),
        "WorkMode": Utils.try_to_json(argv, "--WorkMode"),
        "EvalMode": Utils.try_to_json(argv, "--EvalMode"),
        "ScoreCoeff": Utils.try_to_json(argv, "--ScoreCoeff"),
        "SoeAppId": Utils.try_to_json(argv, "--SoeAppId"),
        "IsLongLifeSession": Utils.try_to_json(argv, "--IsLongLifeSession"),
        "StorageMode": Utils.try_to_json(argv, "--StorageMode"),
        "SentenceInfoEnabled": Utils.try_to_json(argv, "--SentenceInfoEnabled"),
        "ServerType": Utils.try_to_json(argv, "--ServerType"),
        "IsAsync": Utils.try_to_json(argv, "--IsAsync"),
        "TextMode": Utils.try_to_json(argv, "--TextMode"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.SoeClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.InitOralProcessRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.InitOralProcess(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doKeywordEvaluate(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("KeywordEvaluate", g_param[OptionsDefine.Version])
        return

    param = {
        "SeqId": Utils.try_to_json(argv, "--SeqId"),
        "IsEnd": Utils.try_to_json(argv, "--IsEnd"),
        "VoiceFileType": Utils.try_to_json(argv, "--VoiceFileType"),
        "VoiceEncodeType": Utils.try_to_json(argv, "--VoiceEncodeType"),
        "UserVoiceData": Utils.try_to_json(argv, "--UserVoiceData"),
        "SessionId": Utils.try_to_json(argv, "--SessionId"),
        "Keywords": Utils.try_to_json(argv, "--Keywords"),
        "SoeAppId": Utils.try_to_json(argv, "--SoeAppId"),
        "IsQuery": Utils.try_to_json(argv, "--IsQuery"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.SoeClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.KeywordEvaluateRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.KeywordEvaluate(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doTransmitOralProcess(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("TransmitOralProcess", g_param[OptionsDefine.Version])
        return

    param = {
        "SeqId": Utils.try_to_json(argv, "--SeqId"),
        "IsEnd": Utils.try_to_json(argv, "--IsEnd"),
        "VoiceFileType": Utils.try_to_json(argv, "--VoiceFileType"),
        "VoiceEncodeType": Utils.try_to_json(argv, "--VoiceEncodeType"),
        "UserVoiceData": Utils.try_to_json(argv, "--UserVoiceData"),
        "SessionId": Utils.try_to_json(argv, "--SessionId"),
        "SoeAppId": Utils.try_to_json(argv, "--SoeAppId"),
        "IsLongLifeSession": Utils.try_to_json(argv, "--IsLongLifeSession"),
        "IsQuery": Utils.try_to_json(argv, "--IsQuery"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.SoeClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.TransmitOralProcessRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.TransmitOralProcess(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doTransmitOralProcessWithInit(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("TransmitOralProcessWithInit", g_param[OptionsDefine.Version])
        return

    param = {
        "SeqId": Utils.try_to_json(argv, "--SeqId"),
        "IsEnd": Utils.try_to_json(argv, "--IsEnd"),
        "VoiceFileType": Utils.try_to_json(argv, "--VoiceFileType"),
        "VoiceEncodeType": Utils.try_to_json(argv, "--VoiceEncodeType"),
        "UserVoiceData": Utils.try_to_json(argv, "--UserVoiceData"),
        "SessionId": Utils.try_to_json(argv, "--SessionId"),
        "RefText": Utils.try_to_json(argv, "--RefText"),
        "WorkMode": Utils.try_to_json(argv, "--WorkMode"),
        "EvalMode": Utils.try_to_json(argv, "--EvalMode"),
        "ScoreCoeff": Utils.try_to_json(argv, "--ScoreCoeff"),
        "SoeAppId": Utils.try_to_json(argv, "--SoeAppId"),
        "StorageMode": Utils.try_to_json(argv, "--StorageMode"),
        "SentenceInfoEnabled": Utils.try_to_json(argv, "--SentenceInfoEnabled"),
        "ServerType": Utils.try_to_json(argv, "--ServerType"),
        "IsAsync": Utils.try_to_json(argv, "--IsAsync"),
        "IsQuery": Utils.try_to_json(argv, "--IsQuery"),
        "TextMode": Utils.try_to_json(argv, "--TextMode"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.SoeClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.TransmitOralProcessWithInitRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.TransmitOralProcessWithInit(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


CLIENT_MAP = {
    "v20180724": soe_client_v20180724,

}

MODELS_MAP = {
    "v20180724": models_v20180724,

}

ACTION_MAP = {
    "InitOralProcess": doInitOralProcess,
    "KeywordEvaluate": doKeywordEvaluate,
    "TransmitOralProcess": doTransmitOralProcess,
    "TransmitOralProcessWithInit": doTransmitOralProcessWithInit,

}

AVAILABLE_VERSION_LIST = [
    v20180724.version,

]
AVAILABLE_VERSIONS = {
     'v' + v20180724.version.replace('-', ''): {"help": v20180724_help.INFO,"desc": v20180724_help.DESC},

}


def soe_action(argv, arglist):
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
        helpstr = HelpTemplate.SERVICE % {"name": "soe", "desc": desc, "actions": action_str}
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
    cmd = NiceCommand("soe", soe_action)
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
            version = config["soe"][OptionsDefine.Version]
            params[OptionsDefine.Version] = "v" + version.replace('-', '')

        if params[OptionsDefine.Endpoint] is None:
            params[OptionsDefine.Endpoint] = config["soe"][OptionsDefine.Endpoint]
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

    helpmsg = HelpTemplate.ACTION % {"name": action, "service": "soe", "desc": desc, "params": docstr}
    print(helpmsg)


def get_actions_info():
    config = Configure()
    new_version = max(AVAILABLE_VERSIONS.keys())
    version = new_version
    try:
        profile = config._load_json_msg(os.path.join(config.cli_path, "default.configure"))
        version = profile["soe"]["version"]
        version = "v" + version.replace('-', '')
    except Exception:
        pass
    if version not in AVAILABLE_VERSIONS.keys():
        version = new_version
    return AVAILABLE_VERSIONS[version]["help"]
