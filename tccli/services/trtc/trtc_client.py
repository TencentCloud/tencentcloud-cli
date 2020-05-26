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
from tencentcloud.trtc.v20190722 import trtc_client as trtc_client_v20190722
from tencentcloud.trtc.v20190722 import models as models_v20190722
from tccli.services.trtc import v20190722
from tccli.services.trtc.v20190722 import help as v20190722_help


def doRemoveUser(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("RemoveUser", g_param[OptionsDefine.Version])
        return

    param = {
        "SdkAppId": Utils.try_to_json(argv, "--SdkAppId"),
        "RoomId": Utils.try_to_json(argv, "--RoomId"),
        "UserIds": Utils.try_to_json(argv, "--UserIds"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.TrtcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.RemoveUserRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.RemoveUser(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeRealtimeQuality(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeRealtimeQuality", g_param[OptionsDefine.Version])
        return

    param = {
        "StartTime": Utils.try_to_json(argv, "--StartTime"),
        "EndTime": Utils.try_to_json(argv, "--EndTime"),
        "SdkAppId": argv.get("--SdkAppId"),
        "DataType": Utils.try_to_json(argv, "--DataType"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.TrtcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeRealtimeQualityRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeRealtimeQuality(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeHistoryScale(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeHistoryScale", g_param[OptionsDefine.Version])
        return

    param = {
        "SdkAppId": argv.get("--SdkAppId"),
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
    client = mod.TrtcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeHistoryScaleRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeHistoryScale(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doStartMCUMixTranscode(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("StartMCUMixTranscode", g_param[OptionsDefine.Version])
        return

    param = {
        "SdkAppId": Utils.try_to_json(argv, "--SdkAppId"),
        "RoomId": Utils.try_to_json(argv, "--RoomId"),
        "OutputParams": Utils.try_to_json(argv, "--OutputParams"),
        "EncodeParams": Utils.try_to_json(argv, "--EncodeParams"),
        "LayoutParams": Utils.try_to_json(argv, "--LayoutParams"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.TrtcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.StartMCUMixTranscodeRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.StartMCUMixTranscode(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeRealtimeScale(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeRealtimeScale", g_param[OptionsDefine.Version])
        return

    param = {
        "StartTime": Utils.try_to_json(argv, "--StartTime"),
        "EndTime": Utils.try_to_json(argv, "--EndTime"),
        "SdkAppId": argv.get("--SdkAppId"),
        "DataType": Utils.try_to_json(argv, "--DataType"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.TrtcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeRealtimeScaleRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeRealtimeScale(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeRealtimeNetwork(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeRealtimeNetwork", g_param[OptionsDefine.Version])
        return

    param = {
        "StartTime": Utils.try_to_json(argv, "--StartTime"),
        "EndTime": Utils.try_to_json(argv, "--EndTime"),
        "SdkAppId": argv.get("--SdkAppId"),
        "DataType": Utils.try_to_json(argv, "--DataType"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.TrtcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeRealtimeNetworkRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeRealtimeNetwork(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeRoomInformation(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeRoomInformation", g_param[OptionsDefine.Version])
        return

    param = {
        "SdkAppId": argv.get("--SdkAppId"),
        "StartTime": Utils.try_to_json(argv, "--StartTime"),
        "EndTime": Utils.try_to_json(argv, "--EndTime"),
        "RoomId": argv.get("--RoomId"),
        "PageNumber": argv.get("--PageNumber"),
        "PageSize": argv.get("--PageSize"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.TrtcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeRoomInformationRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeRoomInformation(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeDetailEvent(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeDetailEvent", g_param[OptionsDefine.Version])
        return

    param = {
        "CommId": argv.get("--CommId"),
        "StartTime": Utils.try_to_json(argv, "--StartTime"),
        "EndTime": Utils.try_to_json(argv, "--EndTime"),
        "UserId": argv.get("--UserId"),
        "RoomId": argv.get("--RoomId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.TrtcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeDetailEventRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeDetailEvent(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeCallDetail(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeCallDetail", g_param[OptionsDefine.Version])
        return

    param = {
        "CommId": argv.get("--CommId"),
        "StartTime": Utils.try_to_json(argv, "--StartTime"),
        "EndTime": Utils.try_to_json(argv, "--EndTime"),
        "SdkAppId": argv.get("--SdkAppId"),
        "UserIds": Utils.try_to_json(argv, "--UserIds"),
        "DataType": Utils.try_to_json(argv, "--DataType"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.TrtcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeCallDetailRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeCallDetail(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doStopMCUMixTranscode(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("StopMCUMixTranscode", g_param[OptionsDefine.Version])
        return

    param = {
        "SdkAppId": Utils.try_to_json(argv, "--SdkAppId"),
        "RoomId": Utils.try_to_json(argv, "--RoomId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.TrtcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.StopMCUMixTranscodeRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.StopMCUMixTranscode(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateTroubleInfo(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateTroubleInfo", g_param[OptionsDefine.Version])
        return

    param = {
        "SdkAppId": argv.get("--SdkAppId"),
        "RoomId": argv.get("--RoomId"),
        "TeacherUserId": argv.get("--TeacherUserId"),
        "StudentUserId": argv.get("--StudentUserId"),
        "TroubleUserId": argv.get("--TroubleUserId"),
        "TroubleType": Utils.try_to_json(argv, "--TroubleType"),
        "TroubleTime": Utils.try_to_json(argv, "--TroubleTime"),
        "TroubleMsg": argv.get("--TroubleMsg"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.TrtcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateTroubleInfoRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateTroubleInfo(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDismissRoom(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DismissRoom", g_param[OptionsDefine.Version])
        return

    param = {
        "SdkAppId": Utils.try_to_json(argv, "--SdkAppId"),
        "RoomId": Utils.try_to_json(argv, "--RoomId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.TrtcClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DismissRoomRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DismissRoom(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


CLIENT_MAP = {
    "v20190722": trtc_client_v20190722,

}

MODELS_MAP = {
    "v20190722": models_v20190722,

}

ACTION_MAP = {
    "RemoveUser": doRemoveUser,
    "DescribeRealtimeQuality": doDescribeRealtimeQuality,
    "DescribeHistoryScale": doDescribeHistoryScale,
    "StartMCUMixTranscode": doStartMCUMixTranscode,
    "DescribeRealtimeScale": doDescribeRealtimeScale,
    "DescribeRealtimeNetwork": doDescribeRealtimeNetwork,
    "DescribeRoomInformation": doDescribeRoomInformation,
    "DescribeDetailEvent": doDescribeDetailEvent,
    "DescribeCallDetail": doDescribeCallDetail,
    "StopMCUMixTranscode": doStopMCUMixTranscode,
    "CreateTroubleInfo": doCreateTroubleInfo,
    "DismissRoom": doDismissRoom,

}

AVAILABLE_VERSION_LIST = [
    v20190722.version,

]
AVAILABLE_VERSIONS = {
     'v' + v20190722.version.replace('-', ''): {"help": v20190722_help.INFO,"desc": v20190722_help.DESC},

}


def trtc_action(argv, arglist):
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
        helpstr = HelpTemplate.SERVICE % {"name": "trtc", "desc": desc, "actions": action_str}
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
    cmd = NiceCommand("trtc", trtc_action)
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
            version = config["trtc"][OptionsDefine.Version]
            params[OptionsDefine.Version] = "v" + version.replace('-', '')

        if params[OptionsDefine.Endpoint] is None:
            params[OptionsDefine.Endpoint] = config["trtc"][OptionsDefine.Endpoint]
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

    helpmsg = HelpTemplate.ACTION % {"name": action, "service": "trtc", "desc": desc, "params": docstr}
    print(helpmsg)


def get_actions_info():
    config = Configure()
    new_version = max(AVAILABLE_VERSIONS.keys())
    version = new_version
    try:
        profile = config._load_json_msg(os.path.join(config.cli_path, "default.configure"))
        version = profile["trtc"]["version"]
        version = "v" + version.replace('-', '')
    except Exception:
        pass
    if version not in AVAILABLE_VERSIONS.keys():
        version = new_version
    return AVAILABLE_VERSIONS[version]["help"]
