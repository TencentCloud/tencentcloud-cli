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
from tencentcloud.live.v20180801 import live_client as live_client_v20180801
from tencentcloud.live.v20180801 import models as models_v20180801
from tccli.services.live import v20180801
from tccli.services.live.v20180801 import help as v20180801_help


def doDropLiveStream(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DropLiveStream", g_param[OptionsDefine.Version])
        return

    param = {
        "StreamName": Utils.try_to_json(argv, "--StreamName"),
        "DomainName": Utils.try_to_json(argv, "--DomainName"),
        "AppName": Utils.try_to_json(argv, "--AppName"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DropLiveStreamRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DropLiveStream(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeLiveWatermarks(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeLiveWatermarks", g_param[OptionsDefine.Version])
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
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeLiveWatermarksRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeLiveWatermarks(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateLiveRecord(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateLiveRecord", g_param[OptionsDefine.Version])
        return

    param = {
        "StreamName": Utils.try_to_json(argv, "--StreamName"),
        "AppName": Utils.try_to_json(argv, "--AppName"),
        "DomainName": Utils.try_to_json(argv, "--DomainName"),
        "StartTime": Utils.try_to_json(argv, "--StartTime"),
        "EndTime": Utils.try_to_json(argv, "--EndTime"),
        "RecordType": Utils.try_to_json(argv, "--RecordType"),
        "FileFormat": Utils.try_to_json(argv, "--FileFormat"),
        "Highlight": Utils.try_to_json(argv, "--Highlight"),
        "MixStream": Utils.try_to_json(argv, "--MixStream"),
        "StreamParam": Utils.try_to_json(argv, "--StreamParam"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateLiveRecordRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateLiveRecord(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doUpdateLiveWatermark(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("UpdateLiveWatermark", g_param[OptionsDefine.Version])
        return

    param = {
        "WatermarkId": Utils.try_to_json(argv, "--WatermarkId"),
        "PictureUrl": Utils.try_to_json(argv, "--PictureUrl"),
        "XPosition": Utils.try_to_json(argv, "--XPosition"),
        "YPosition": Utils.try_to_json(argv, "--YPosition"),
        "WatermarkName": Utils.try_to_json(argv, "--WatermarkName"),
        "Width": Utils.try_to_json(argv, "--Width"),
        "Height": Utils.try_to_json(argv, "--Height"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.UpdateLiveWatermarkRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.UpdateLiveWatermark(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyLiveSnapshotTemplate(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyLiveSnapshotTemplate", g_param[OptionsDefine.Version])
        return

    param = {
        "TemplateId": Utils.try_to_json(argv, "--TemplateId"),
        "TemplateName": Utils.try_to_json(argv, "--TemplateName"),
        "Description": Utils.try_to_json(argv, "--Description"),
        "SnapshotInterval": Utils.try_to_json(argv, "--SnapshotInterval"),
        "Width": Utils.try_to_json(argv, "--Width"),
        "Height": Utils.try_to_json(argv, "--Height"),
        "PornFlag": Utils.try_to_json(argv, "--PornFlag"),
        "CosAppId": Utils.try_to_json(argv, "--CosAppId"),
        "CosBucket": Utils.try_to_json(argv, "--CosBucket"),
        "CosRegion": Utils.try_to_json(argv, "--CosRegion"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyLiveSnapshotTemplateRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyLiveSnapshotTemplate(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyLiveRecordTemplate(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyLiveRecordTemplate", g_param[OptionsDefine.Version])
        return

    param = {
        "TemplateId": Utils.try_to_json(argv, "--TemplateId"),
        "TemplateName": Utils.try_to_json(argv, "--TemplateName"),
        "Description": Utils.try_to_json(argv, "--Description"),
        "FlvParam": Utils.try_to_json(argv, "--FlvParam"),
        "HlsParam": Utils.try_to_json(argv, "--HlsParam"),
        "Mp4Param": Utils.try_to_json(argv, "--Mp4Param"),
        "AacParam": Utils.try_to_json(argv, "--AacParam"),
        "HlsSpecialParam": Utils.try_to_json(argv, "--HlsSpecialParam"),
        "Mp3Param": Utils.try_to_json(argv, "--Mp3Param"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyLiveRecordTemplateRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyLiveRecordTemplate(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateLiveWatermarkRule(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateLiveWatermarkRule", g_param[OptionsDefine.Version])
        return

    param = {
        "DomainName": Utils.try_to_json(argv, "--DomainName"),
        "AppName": Utils.try_to_json(argv, "--AppName"),
        "StreamName": Utils.try_to_json(argv, "--StreamName"),
        "TemplateId": Utils.try_to_json(argv, "--TemplateId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateLiveWatermarkRuleRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateLiveWatermarkRule(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeLiveStreamEventList(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeLiveStreamEventList", g_param[OptionsDefine.Version])
        return

    param = {
        "StartTime": Utils.try_to_json(argv, "--StartTime"),
        "EndTime": Utils.try_to_json(argv, "--EndTime"),
        "AppName": Utils.try_to_json(argv, "--AppName"),
        "DomainName": Utils.try_to_json(argv, "--DomainName"),
        "StreamName": Utils.try_to_json(argv, "--StreamName"),
        "PageNum": Utils.try_to_json(argv, "--PageNum"),
        "PageSize": Utils.try_to_json(argv, "--PageSize"),
        "IsFilter": Utils.try_to_json(argv, "--IsFilter"),
        "IsStrict": Utils.try_to_json(argv, "--IsStrict"),
        "IsAsc": Utils.try_to_json(argv, "--IsAsc"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeLiveStreamEventListRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeLiveStreamEventList(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribePullStreamConfigs(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribePullStreamConfigs", g_param[OptionsDefine.Version])
        return

    param = {
        "ConfigId": Utils.try_to_json(argv, "--ConfigId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribePullStreamConfigsRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribePullStreamConfigs(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeHttpStatusInfoList(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeHttpStatusInfoList", g_param[OptionsDefine.Version])
        return

    param = {
        "StartTime": Utils.try_to_json(argv, "--StartTime"),
        "EndTime": Utils.try_to_json(argv, "--EndTime"),
        "PlayDomains": Utils.try_to_json(argv, "--PlayDomains"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeHttpStatusInfoListRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeHttpStatusInfoList(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeProvinceIspPlayInfoList(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeProvinceIspPlayInfoList", g_param[OptionsDefine.Version])
        return

    param = {
        "StartTime": Utils.try_to_json(argv, "--StartTime"),
        "EndTime": Utils.try_to_json(argv, "--EndTime"),
        "Granularity": Utils.try_to_json(argv, "--Granularity"),
        "StatType": Utils.try_to_json(argv, "--StatType"),
        "PlayDomains": Utils.try_to_json(argv, "--PlayDomains"),
        "ProvinceNames": Utils.try_to_json(argv, "--ProvinceNames"),
        "IspNames": Utils.try_to_json(argv, "--IspNames"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeProvinceIspPlayInfoListRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeProvinceIspPlayInfoList(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyLivePushAuthKey(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyLivePushAuthKey", g_param[OptionsDefine.Version])
        return

    param = {
        "DomainName": Utils.try_to_json(argv, "--DomainName"),
        "Enable": Utils.try_to_json(argv, "--Enable"),
        "MasterAuthKey": Utils.try_to_json(argv, "--MasterAuthKey"),
        "BackupAuthKey": Utils.try_to_json(argv, "--BackupAuthKey"),
        "AuthDelta": Utils.try_to_json(argv, "--AuthDelta"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyLivePushAuthKeyRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyLivePushAuthKey(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeStreamPushInfoList(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeStreamPushInfoList", g_param[OptionsDefine.Version])
        return

    param = {
        "StreamName": Utils.try_to_json(argv, "--StreamName"),
        "StartTime": Utils.try_to_json(argv, "--StartTime"),
        "EndTime": Utils.try_to_json(argv, "--EndTime"),
        "PushDomain": Utils.try_to_json(argv, "--PushDomain"),
        "AppName": Utils.try_to_json(argv, "--AppName"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeStreamPushInfoListRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeStreamPushInfoList(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeLiveSnapshotRules(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeLiveSnapshotRules", g_param[OptionsDefine.Version])
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
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeLiveSnapshotRulesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeLiveSnapshotRules(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteLiveTranscodeTemplate(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteLiveTranscodeTemplate", g_param[OptionsDefine.Version])
        return

    param = {
        "TemplateId": Utils.try_to_json(argv, "--TemplateId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteLiveTranscodeTemplateRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeleteLiveTranscodeTemplate(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeTopClientIpSumInfoList(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeTopClientIpSumInfoList", g_param[OptionsDefine.Version])
        return

    param = {
        "StartTime": Utils.try_to_json(argv, "--StartTime"),
        "EndTime": Utils.try_to_json(argv, "--EndTime"),
        "PlayDomains": Utils.try_to_json(argv, "--PlayDomains"),
        "PageNum": Utils.try_to_json(argv, "--PageNum"),
        "PageSize": Utils.try_to_json(argv, "--PageSize"),
        "OrderParam": Utils.try_to_json(argv, "--OrderParam"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeTopClientIpSumInfoListRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeTopClientIpSumInfoList(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyPullStreamStatus(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyPullStreamStatus", g_param[OptionsDefine.Version])
        return

    param = {
        "ConfigIds": Utils.try_to_json(argv, "--ConfigIds"),
        "Status": Utils.try_to_json(argv, "--Status"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyPullStreamStatusRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyPullStreamStatus(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeLiveRecordTemplates(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeLiveRecordTemplates", g_param[OptionsDefine.Version])
        return

    param = {
        "IsDelayLive": Utils.try_to_json(argv, "--IsDelayLive"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeLiveRecordTemplatesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeLiveRecordTemplates(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyLiveDomainCert(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyLiveDomainCert", g_param[OptionsDefine.Version])
        return

    param = {
        "DomainName": Utils.try_to_json(argv, "--DomainName"),
        "CertId": Utils.try_to_json(argv, "--CertId"),
        "Status": Utils.try_to_json(argv, "--Status"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyLiveDomainCertRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyLiveDomainCert(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeVisitTopSumInfoList(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeVisitTopSumInfoList", g_param[OptionsDefine.Version])
        return

    param = {
        "StartTime": Utils.try_to_json(argv, "--StartTime"),
        "EndTime": Utils.try_to_json(argv, "--EndTime"),
        "TopIndex": Utils.try_to_json(argv, "--TopIndex"),
        "PlayDomains": Utils.try_to_json(argv, "--PlayDomains"),
        "PageNum": Utils.try_to_json(argv, "--PageNum"),
        "PageSize": Utils.try_to_json(argv, "--PageSize"),
        "OrderParam": Utils.try_to_json(argv, "--OrderParam"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeVisitTopSumInfoListRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeVisitTopSumInfoList(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeLiveDomainCert(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeLiveDomainCert", g_param[OptionsDefine.Version])
        return

    param = {
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
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeLiveDomainCertRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeLiveDomainCert(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doAddLiveWatermark(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("AddLiveWatermark", g_param[OptionsDefine.Version])
        return

    param = {
        "PictureUrl": Utils.try_to_json(argv, "--PictureUrl"),
        "WatermarkName": Utils.try_to_json(argv, "--WatermarkName"),
        "XPosition": Utils.try_to_json(argv, "--XPosition"),
        "YPosition": Utils.try_to_json(argv, "--YPosition"),
        "Width": Utils.try_to_json(argv, "--Width"),
        "Height": Utils.try_to_json(argv, "--Height"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.AddLiveWatermarkRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.AddLiveWatermark(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteLiveWatermarkRule(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteLiveWatermarkRule", g_param[OptionsDefine.Version])
        return

    param = {
        "DomainName": Utils.try_to_json(argv, "--DomainName"),
        "AppName": Utils.try_to_json(argv, "--AppName"),
        "StreamName": Utils.try_to_json(argv, "--StreamName"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteLiveWatermarkRuleRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeleteLiveWatermarkRule(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteLiveCallbackRule(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteLiveCallbackRule", g_param[OptionsDefine.Version])
        return

    param = {
        "DomainName": Utils.try_to_json(argv, "--DomainName"),
        "AppName": Utils.try_to_json(argv, "--AppName"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteLiveCallbackRuleRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeleteLiveCallbackRule(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyPullStreamConfig(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyPullStreamConfig", g_param[OptionsDefine.Version])
        return

    param = {
        "ConfigId": Utils.try_to_json(argv, "--ConfigId"),
        "FromUrl": Utils.try_to_json(argv, "--FromUrl"),
        "ToUrl": Utils.try_to_json(argv, "--ToUrl"),
        "AreaId": Utils.try_to_json(argv, "--AreaId"),
        "IspId": Utils.try_to_json(argv, "--IspId"),
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
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyPullStreamConfigRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyPullStreamConfig(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateLiveSnapshotTemplate(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateLiveSnapshotTemplate", g_param[OptionsDefine.Version])
        return

    param = {
        "TemplateName": Utils.try_to_json(argv, "--TemplateName"),
        "CosAppId": Utils.try_to_json(argv, "--CosAppId"),
        "CosBucket": Utils.try_to_json(argv, "--CosBucket"),
        "CosRegion": Utils.try_to_json(argv, "--CosRegion"),
        "Description": Utils.try_to_json(argv, "--Description"),
        "SnapshotInterval": Utils.try_to_json(argv, "--SnapshotInterval"),
        "Width": Utils.try_to_json(argv, "--Width"),
        "Height": Utils.try_to_json(argv, "--Height"),
        "PornFlag": Utils.try_to_json(argv, "--PornFlag"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateLiveSnapshotTemplateRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateLiveSnapshotTemplate(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeLiveStreamOnlineList(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeLiveStreamOnlineList", g_param[OptionsDefine.Version])
        return

    param = {
        "DomainName": Utils.try_to_json(argv, "--DomainName"),
        "AppName": Utils.try_to_json(argv, "--AppName"),
        "PageNum": Utils.try_to_json(argv, "--PageNum"),
        "PageSize": Utils.try_to_json(argv, "--PageSize"),
        "StreamName": Utils.try_to_json(argv, "--StreamName"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeLiveStreamOnlineListRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeLiveStreamOnlineList(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteLiveCallbackTemplate(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteLiveCallbackTemplate", g_param[OptionsDefine.Version])
        return

    param = {
        "TemplateId": Utils.try_to_json(argv, "--TemplateId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteLiveCallbackTemplateRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeleteLiveCallbackTemplate(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeLivePushAuthKey(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeLivePushAuthKey", g_param[OptionsDefine.Version])
        return

    param = {
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
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeLivePushAuthKeyRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeLivePushAuthKey(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeletePullStreamConfig(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeletePullStreamConfig", g_param[OptionsDefine.Version])
        return

    param = {
        "ConfigId": Utils.try_to_json(argv, "--ConfigId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeletePullStreamConfigRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeletePullStreamConfig(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeLiveRecordTemplate(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeLiveRecordTemplate", g_param[OptionsDefine.Version])
        return

    param = {
        "TemplateId": Utils.try_to_json(argv, "--TemplateId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeLiveRecordTemplateRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeLiveRecordTemplate(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteLiveWatermark(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteLiveWatermark", g_param[OptionsDefine.Version])
        return

    param = {
        "WatermarkId": Utils.try_to_json(argv, "--WatermarkId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteLiveWatermarkRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeleteLiveWatermark(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doUnBindLiveDomainCert(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("UnBindLiveDomainCert", g_param[OptionsDefine.Version])
        return

    param = {
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
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.UnBindLiveDomainCertRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.UnBindLiveDomainCert(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribePlayErrorCodeSumInfoList(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribePlayErrorCodeSumInfoList", g_param[OptionsDefine.Version])
        return

    param = {
        "StartTime": Utils.try_to_json(argv, "--StartTime"),
        "EndTime": Utils.try_to_json(argv, "--EndTime"),
        "PlayDomains": Utils.try_to_json(argv, "--PlayDomains"),
        "PageNum": Utils.try_to_json(argv, "--PageNum"),
        "PageSize": Utils.try_to_json(argv, "--PageSize"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribePlayErrorCodeSumInfoListRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribePlayErrorCodeSumInfoList(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doAddDelayLiveStream(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("AddDelayLiveStream", g_param[OptionsDefine.Version])
        return

    param = {
        "AppName": Utils.try_to_json(argv, "--AppName"),
        "DomainName": Utils.try_to_json(argv, "--DomainName"),
        "StreamName": Utils.try_to_json(argv, "--StreamName"),
        "DelayTime": Utils.try_to_json(argv, "--DelayTime"),
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
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.AddDelayLiveStreamRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.AddDelayLiveStream(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeStreamDayPlayInfoList(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeStreamDayPlayInfoList", g_param[OptionsDefine.Version])
        return

    param = {
        "DayTime": Utils.try_to_json(argv, "--DayTime"),
        "PlayDomain": Utils.try_to_json(argv, "--PlayDomain"),
        "PageNum": Utils.try_to_json(argv, "--PageNum"),
        "PageSize": Utils.try_to_json(argv, "--PageSize"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeStreamDayPlayInfoListRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeStreamDayPlayInfoList(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyLivePlayDomain(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyLivePlayDomain", g_param[OptionsDefine.Version])
        return

    param = {
        "DomainName": Utils.try_to_json(argv, "--DomainName"),
        "PlayType": Utils.try_to_json(argv, "--PlayType"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyLivePlayDomainRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyLivePlayDomain(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyLiveTranscodeTemplate(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyLiveTranscodeTemplate", g_param[OptionsDefine.Version])
        return

    param = {
        "TemplateId": Utils.try_to_json(argv, "--TemplateId"),
        "Vcodec": Utils.try_to_json(argv, "--Vcodec"),
        "Acodec": Utils.try_to_json(argv, "--Acodec"),
        "AudioBitrate": Utils.try_to_json(argv, "--AudioBitrate"),
        "Description": Utils.try_to_json(argv, "--Description"),
        "VideoBitrate": Utils.try_to_json(argv, "--VideoBitrate"),
        "Width": Utils.try_to_json(argv, "--Width"),
        "NeedVideo": Utils.try_to_json(argv, "--NeedVideo"),
        "NeedAudio": Utils.try_to_json(argv, "--NeedAudio"),
        "Height": Utils.try_to_json(argv, "--Height"),
        "Fps": Utils.try_to_json(argv, "--Fps"),
        "Gop": Utils.try_to_json(argv, "--Gop"),
        "Rotate": Utils.try_to_json(argv, "--Rotate"),
        "Profile": Utils.try_to_json(argv, "--Profile"),
        "BitrateToOrig": Utils.try_to_json(argv, "--BitrateToOrig"),
        "HeightToOrig": Utils.try_to_json(argv, "--HeightToOrig"),
        "FpsToOrig": Utils.try_to_json(argv, "--FpsToOrig"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyLiveTranscodeTemplateRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyLiveTranscodeTemplate(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteLiveTranscodeRule(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteLiveTranscodeRule", g_param[OptionsDefine.Version])
        return

    param = {
        "DomainName": Utils.try_to_json(argv, "--DomainName"),
        "AppName": Utils.try_to_json(argv, "--AppName"),
        "StreamName": Utils.try_to_json(argv, "--StreamName"),
        "TemplateId": Utils.try_to_json(argv, "--TemplateId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteLiveTranscodeRuleRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeleteLiveTranscodeRule(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteLiveSnapshotRule(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteLiveSnapshotRule", g_param[OptionsDefine.Version])
        return

    param = {
        "DomainName": Utils.try_to_json(argv, "--DomainName"),
        "AppName": Utils.try_to_json(argv, "--AppName"),
        "StreamName": Utils.try_to_json(argv, "--StreamName"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteLiveSnapshotRuleRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeleteLiveSnapshotRule(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeLiveForbidStreamList(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeLiveForbidStreamList", g_param[OptionsDefine.Version])
        return

    param = {
        "PageNum": Utils.try_to_json(argv, "--PageNum"),
        "PageSize": Utils.try_to_json(argv, "--PageSize"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeLiveForbidStreamListRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeLiveForbidStreamList(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeLiveCert(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeLiveCert", g_param[OptionsDefine.Version])
        return

    param = {
        "CertId": Utils.try_to_json(argv, "--CertId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeLiveCertRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeLiveCert(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyLiveCert(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyLiveCert", g_param[OptionsDefine.Version])
        return

    param = {
        "CertId": Utils.try_to_json(argv, "--CertId"),
        "CertType": Utils.try_to_json(argv, "--CertType"),
        "CertName": Utils.try_to_json(argv, "--CertName"),
        "HttpsCrt": Utils.try_to_json(argv, "--HttpsCrt"),
        "HttpsKey": Utils.try_to_json(argv, "--HttpsKey"),
        "Description": Utils.try_to_json(argv, "--Description"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyLiveCertRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyLiveCert(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeLiveDomains(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeLiveDomains", g_param[OptionsDefine.Version])
        return

    param = {
        "DomainStatus": Utils.try_to_json(argv, "--DomainStatus"),
        "DomainType": Utils.try_to_json(argv, "--DomainType"),
        "PageSize": Utils.try_to_json(argv, "--PageSize"),
        "PageNum": Utils.try_to_json(argv, "--PageNum"),
        "IsDelayLive": Utils.try_to_json(argv, "--IsDelayLive"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeLiveDomainsRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeLiveDomains(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteLiveCert(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteLiveCert", g_param[OptionsDefine.Version])
        return

    param = {
        "CertId": Utils.try_to_json(argv, "--CertId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteLiveCertRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeleteLiveCert(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateLiveCallbackTemplate(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateLiveCallbackTemplate", g_param[OptionsDefine.Version])
        return

    param = {
        "TemplateName": Utils.try_to_json(argv, "--TemplateName"),
        "Description": Utils.try_to_json(argv, "--Description"),
        "StreamBeginNotifyUrl": Utils.try_to_json(argv, "--StreamBeginNotifyUrl"),
        "StreamEndNotifyUrl": Utils.try_to_json(argv, "--StreamEndNotifyUrl"),
        "RecordNotifyUrl": Utils.try_to_json(argv, "--RecordNotifyUrl"),
        "SnapshotNotifyUrl": Utils.try_to_json(argv, "--SnapshotNotifyUrl"),
        "PornCensorshipNotifyUrl": Utils.try_to_json(argv, "--PornCensorshipNotifyUrl"),
        "CallbackKey": Utils.try_to_json(argv, "--CallbackKey"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateLiveCallbackTemplateRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateLiveCallbackTemplate(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doResumeLiveStream(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ResumeLiveStream", g_param[OptionsDefine.Version])
        return

    param = {
        "AppName": Utils.try_to_json(argv, "--AppName"),
        "DomainName": Utils.try_to_json(argv, "--DomainName"),
        "StreamName": Utils.try_to_json(argv, "--StreamName"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ResumeLiveStreamRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ResumeLiveStream(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeLiveCallbackTemplate(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeLiveCallbackTemplate", g_param[OptionsDefine.Version])
        return

    param = {
        "TemplateId": Utils.try_to_json(argv, "--TemplateId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeLiveCallbackTemplateRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeLiveCallbackTemplate(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteLiveDomain(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteLiveDomain", g_param[OptionsDefine.Version])
        return

    param = {
        "DomainName": Utils.try_to_json(argv, "--DomainName"),
        "DomainType": Utils.try_to_json(argv, "--DomainType"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteLiveDomainRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeleteLiveDomain(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyLiveCallbackTemplate(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyLiveCallbackTemplate", g_param[OptionsDefine.Version])
        return

    param = {
        "TemplateId": Utils.try_to_json(argv, "--TemplateId"),
        "TemplateName": Utils.try_to_json(argv, "--TemplateName"),
        "Description": Utils.try_to_json(argv, "--Description"),
        "StreamBeginNotifyUrl": Utils.try_to_json(argv, "--StreamBeginNotifyUrl"),
        "StreamEndNotifyUrl": Utils.try_to_json(argv, "--StreamEndNotifyUrl"),
        "RecordNotifyUrl": Utils.try_to_json(argv, "--RecordNotifyUrl"),
        "SnapshotNotifyUrl": Utils.try_to_json(argv, "--SnapshotNotifyUrl"),
        "PornCensorshipNotifyUrl": Utils.try_to_json(argv, "--PornCensorshipNotifyUrl"),
        "CallbackKey": Utils.try_to_json(argv, "--CallbackKey"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyLiveCallbackTemplateRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyLiveCallbackTemplate(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeProIspPlaySumInfoList(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeProIspPlaySumInfoList", g_param[OptionsDefine.Version])
        return

    param = {
        "StartTime": Utils.try_to_json(argv, "--StartTime"),
        "EndTime": Utils.try_to_json(argv, "--EndTime"),
        "StatType": Utils.try_to_json(argv, "--StatType"),
        "PlayDomains": Utils.try_to_json(argv, "--PlayDomains"),
        "PageNum": Utils.try_to_json(argv, "--PageNum"),
        "PageSize": Utils.try_to_json(argv, "--PageSize"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeProIspPlaySumInfoListRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeProIspPlaySumInfoList(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeStreamPlayInfoList(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeStreamPlayInfoList", g_param[OptionsDefine.Version])
        return

    param = {
        "StartTime": Utils.try_to_json(argv, "--StartTime"),
        "EndTime": Utils.try_to_json(argv, "--EndTime"),
        "PlayDomain": Utils.try_to_json(argv, "--PlayDomain"),
        "StreamName": Utils.try_to_json(argv, "--StreamName"),
        "AppName": Utils.try_to_json(argv, "--AppName"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeStreamPlayInfoListRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeStreamPlayInfoList(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateLiveCert(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateLiveCert", g_param[OptionsDefine.Version])
        return

    param = {
        "CertType": Utils.try_to_json(argv, "--CertType"),
        "HttpsCrt": Utils.try_to_json(argv, "--HttpsCrt"),
        "HttpsKey": Utils.try_to_json(argv, "--HttpsKey"),
        "CertName": Utils.try_to_json(argv, "--CertName"),
        "Description": Utils.try_to_json(argv, "--Description"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateLiveCertRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateLiveCert(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeLiveTranscodeRules(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeLiveTranscodeRules", g_param[OptionsDefine.Version])
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
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeLiveTranscodeRulesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeLiveTranscodeRules(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeLiveSnapshotTemplate(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeLiveSnapshotTemplate", g_param[OptionsDefine.Version])
        return

    param = {
        "TemplateId": Utils.try_to_json(argv, "--TemplateId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeLiveSnapshotTemplateRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeLiveSnapshotTemplate(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeLiveCallbackTemplates(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeLiveCallbackTemplates", g_param[OptionsDefine.Version])
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
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeLiveCallbackTemplatesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeLiveCallbackTemplates(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeLiveSnapshotTemplates(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeLiveSnapshotTemplates", g_param[OptionsDefine.Version])
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
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeLiveSnapshotTemplatesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeLiveSnapshotTemplates(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doStopLiveRecord(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("StopLiveRecord", g_param[OptionsDefine.Version])
        return

    param = {
        "StreamName": Utils.try_to_json(argv, "--StreamName"),
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
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.StopLiveRecordRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.StopLiveRecord(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyLivePlayAuthKey(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyLivePlayAuthKey", g_param[OptionsDefine.Version])
        return

    param = {
        "DomainName": Utils.try_to_json(argv, "--DomainName"),
        "Enable": Utils.try_to_json(argv, "--Enable"),
        "AuthKey": Utils.try_to_json(argv, "--AuthKey"),
        "AuthDelta": Utils.try_to_json(argv, "--AuthDelta"),
        "AuthBackKey": Utils.try_to_json(argv, "--AuthBackKey"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyLivePlayAuthKeyRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyLivePlayAuthKey(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeLiveTranscodeTemplate(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeLiveTranscodeTemplate", g_param[OptionsDefine.Version])
        return

    param = {
        "TemplateId": Utils.try_to_json(argv, "--TemplateId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeLiveTranscodeTemplateRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeLiveTranscodeTemplate(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doSetLiveWatermarkStatus(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("SetLiveWatermarkStatus", g_param[OptionsDefine.Version])
        return

    param = {
        "WatermarkId": Utils.try_to_json(argv, "--WatermarkId"),
        "Status": Utils.try_to_json(argv, "--Status"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.SetLiveWatermarkStatusRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.SetLiveWatermarkStatus(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeLiveTranscodeDetailInfo(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeLiveTranscodeDetailInfo", g_param[OptionsDefine.Version])
        return

    param = {
        "DayTime": Utils.try_to_json(argv, "--DayTime"),
        "PushDomain": Utils.try_to_json(argv, "--PushDomain"),
        "StreamName": Utils.try_to_json(argv, "--StreamName"),
        "PageNum": Utils.try_to_json(argv, "--PageNum"),
        "PageSize": Utils.try_to_json(argv, "--PageSize"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeLiveTranscodeDetailInfoRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeLiveTranscodeDetailInfo(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeLogDownloadList(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeLogDownloadList", g_param[OptionsDefine.Version])
        return

    param = {
        "StartTime": Utils.try_to_json(argv, "--StartTime"),
        "EndTime": Utils.try_to_json(argv, "--EndTime"),
        "PlayDomains": Utils.try_to_json(argv, "--PlayDomains"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeLogDownloadListRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeLogDownloadList(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeLiveStreamOnlineInfo(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeLiveStreamOnlineInfo", g_param[OptionsDefine.Version])
        return

    param = {
        "PageNum": Utils.try_to_json(argv, "--PageNum"),
        "PageSize": Utils.try_to_json(argv, "--PageSize"),
        "Status": Utils.try_to_json(argv, "--Status"),
        "StreamName": Utils.try_to_json(argv, "--StreamName"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeLiveStreamOnlineInfoRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeLiveStreamOnlineInfo(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeLiveRecordRules(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeLiveRecordRules", g_param[OptionsDefine.Version])
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
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeLiveRecordRulesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeLiveRecordRules(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeLiveDelayInfoList(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeLiveDelayInfoList", g_param[OptionsDefine.Version])
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
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeLiveDelayInfoListRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeLiveDelayInfoList(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteLiveRecordRule(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteLiveRecordRule", g_param[OptionsDefine.Version])
        return

    param = {
        "DomainName": Utils.try_to_json(argv, "--DomainName"),
        "AppName": Utils.try_to_json(argv, "--AppName"),
        "StreamName": Utils.try_to_json(argv, "--StreamName"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteLiveRecordRuleRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeleteLiveRecordRule(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeLiveDomain(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeLiveDomain", g_param[OptionsDefine.Version])
        return

    param = {
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
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeLiveDomainRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeLiveDomain(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateLiveCallbackRule(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateLiveCallbackRule", g_param[OptionsDefine.Version])
        return

    param = {
        "DomainName": Utils.try_to_json(argv, "--DomainName"),
        "AppName": Utils.try_to_json(argv, "--AppName"),
        "TemplateId": Utils.try_to_json(argv, "--TemplateId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateLiveCallbackRuleRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateLiveCallbackRule(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doBindLiveDomainCert(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("BindLiveDomainCert", g_param[OptionsDefine.Version])
        return

    param = {
        "CertId": Utils.try_to_json(argv, "--CertId"),
        "DomainName": Utils.try_to_json(argv, "--DomainName"),
        "Status": Utils.try_to_json(argv, "--Status"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.BindLiveDomainCertRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.BindLiveDomainCert(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeLiveCallbackRules(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeLiveCallbackRules", g_param[OptionsDefine.Version])
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
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeLiveCallbackRulesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeLiveCallbackRules(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribePlayErrorCodeDetailInfoList(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribePlayErrorCodeDetailInfoList", g_param[OptionsDefine.Version])
        return

    param = {
        "StartTime": Utils.try_to_json(argv, "--StartTime"),
        "EndTime": Utils.try_to_json(argv, "--EndTime"),
        "Granularity": Utils.try_to_json(argv, "--Granularity"),
        "StatType": Utils.try_to_json(argv, "--StatType"),
        "PlayDomains": Utils.try_to_json(argv, "--PlayDomains"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribePlayErrorCodeDetailInfoListRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribePlayErrorCodeDetailInfoList(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeLiveStreamPublishedList(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeLiveStreamPublishedList", g_param[OptionsDefine.Version])
        return

    param = {
        "DomainName": Utils.try_to_json(argv, "--DomainName"),
        "EndTime": Utils.try_to_json(argv, "--EndTime"),
        "StartTime": Utils.try_to_json(argv, "--StartTime"),
        "AppName": Utils.try_to_json(argv, "--AppName"),
        "PageNum": Utils.try_to_json(argv, "--PageNum"),
        "PageSize": Utils.try_to_json(argv, "--PageSize"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeLiveStreamPublishedListRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeLiveStreamPublishedList(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doForbidLiveStream(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ForbidLiveStream", g_param[OptionsDefine.Version])
        return

    param = {
        "AppName": Utils.try_to_json(argv, "--AppName"),
        "DomainName": Utils.try_to_json(argv, "--DomainName"),
        "StreamName": Utils.try_to_json(argv, "--StreamName"),
        "ResumeTime": Utils.try_to_json(argv, "--ResumeTime"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ForbidLiveStreamRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ForbidLiveStream(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doAddLiveDomain(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("AddLiveDomain", g_param[OptionsDefine.Version])
        return

    param = {
        "DomainName": Utils.try_to_json(argv, "--DomainName"),
        "DomainType": Utils.try_to_json(argv, "--DomainType"),
        "PlayType": Utils.try_to_json(argv, "--PlayType"),
        "IsDelayLive": Utils.try_to_json(argv, "--IsDelayLive"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.AddLiveDomainRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.AddLiveDomain(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeLiveDomainPlayInfoList(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeLiveDomainPlayInfoList", g_param[OptionsDefine.Version])
        return

    param = {
        "PlayDomains": Utils.try_to_json(argv, "--PlayDomains"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeLiveDomainPlayInfoListRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeLiveDomainPlayInfoList(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateLiveRecordRule(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateLiveRecordRule", g_param[OptionsDefine.Version])
        return

    param = {
        "DomainName": Utils.try_to_json(argv, "--DomainName"),
        "TemplateId": Utils.try_to_json(argv, "--TemplateId"),
        "AppName": Utils.try_to_json(argv, "--AppName"),
        "StreamName": Utils.try_to_json(argv, "--StreamName"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateLiveRecordRuleRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateLiveRecordRule(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeLiveWatermark(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeLiveWatermark", g_param[OptionsDefine.Version])
        return

    param = {
        "WatermarkId": Utils.try_to_json(argv, "--WatermarkId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeLiveWatermarkRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeLiveWatermark(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeLiveTranscodeTemplates(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeLiveTranscodeTemplates", g_param[OptionsDefine.Version])
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
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeLiveTranscodeTemplatesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeLiveTranscodeTemplates(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateLiveRecordTemplate(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateLiveRecordTemplate", g_param[OptionsDefine.Version])
        return

    param = {
        "TemplateName": Utils.try_to_json(argv, "--TemplateName"),
        "Description": Utils.try_to_json(argv, "--Description"),
        "FlvParam": Utils.try_to_json(argv, "--FlvParam"),
        "HlsParam": Utils.try_to_json(argv, "--HlsParam"),
        "Mp4Param": Utils.try_to_json(argv, "--Mp4Param"),
        "AacParam": Utils.try_to_json(argv, "--AacParam"),
        "IsDelayLive": Utils.try_to_json(argv, "--IsDelayLive"),
        "HlsSpecialParam": Utils.try_to_json(argv, "--HlsSpecialParam"),
        "Mp3Param": Utils.try_to_json(argv, "--Mp3Param"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateLiveRecordTemplateRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateLiveRecordTemplate(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeBillBandwidthAndFluxList(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeBillBandwidthAndFluxList", g_param[OptionsDefine.Version])
        return

    param = {
        "StartTime": Utils.try_to_json(argv, "--StartTime"),
        "EndTime": Utils.try_to_json(argv, "--EndTime"),
        "PlayDomains": Utils.try_to_json(argv, "--PlayDomains"),
        "MainlandOrOversea": Utils.try_to_json(argv, "--MainlandOrOversea"),
        "Granularity": Utils.try_to_json(argv, "--Granularity"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeBillBandwidthAndFluxListRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeBillBandwidthAndFluxList(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doForbidLiveDomain(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ForbidLiveDomain", g_param[OptionsDefine.Version])
        return

    param = {
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
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ForbidLiveDomainRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ForbidLiveDomain(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateLiveTranscodeRule(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateLiveTranscodeRule", g_param[OptionsDefine.Version])
        return

    param = {
        "DomainName": Utils.try_to_json(argv, "--DomainName"),
        "AppName": Utils.try_to_json(argv, "--AppName"),
        "StreamName": Utils.try_to_json(argv, "--StreamName"),
        "TemplateId": Utils.try_to_json(argv, "--TemplateId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateLiveTranscodeRuleRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateLiveTranscodeRule(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeLiveWatermarkRules(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeLiveWatermarkRules", g_param[OptionsDefine.Version])
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
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeLiveWatermarkRulesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeLiveWatermarkRules(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteLiveRecord(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteLiveRecord", g_param[OptionsDefine.Version])
        return

    param = {
        "StreamName": Utils.try_to_json(argv, "--StreamName"),
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
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteLiveRecordRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeleteLiveRecord(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateLiveSnapshotRule(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateLiveSnapshotRule", g_param[OptionsDefine.Version])
        return

    param = {
        "DomainName": Utils.try_to_json(argv, "--DomainName"),
        "TemplateId": Utils.try_to_json(argv, "--TemplateId"),
        "AppName": Utils.try_to_json(argv, "--AppName"),
        "StreamName": Utils.try_to_json(argv, "--StreamName"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateLiveSnapshotRuleRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateLiveSnapshotRule(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeGroupProIspPlayInfoList(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeGroupProIspPlayInfoList", g_param[OptionsDefine.Version])
        return

    param = {
        "StartTime": Utils.try_to_json(argv, "--StartTime"),
        "EndTime": Utils.try_to_json(argv, "--EndTime"),
        "PlayDomains": Utils.try_to_json(argv, "--PlayDomains"),
        "ProvinceNames": Utils.try_to_json(argv, "--ProvinceNames"),
        "IspNames": Utils.try_to_json(argv, "--IspNames"),
        "MainlandOrOversea": Utils.try_to_json(argv, "--MainlandOrOversea"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeGroupProIspPlayInfoListRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeGroupProIspPlayInfoList(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeLivePlayAuthKey(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeLivePlayAuthKey", g_param[OptionsDefine.Version])
        return

    param = {
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
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeLivePlayAuthKeyRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeLivePlayAuthKey(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeLiveStreamState(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeLiveStreamState", g_param[OptionsDefine.Version])
        return

    param = {
        "AppName": Utils.try_to_json(argv, "--AppName"),
        "DomainName": Utils.try_to_json(argv, "--DomainName"),
        "StreamName": Utils.try_to_json(argv, "--StreamName"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeLiveStreamStateRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeLiveStreamState(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteLiveRecordTemplate(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteLiveRecordTemplate", g_param[OptionsDefine.Version])
        return

    param = {
        "TemplateId": Utils.try_to_json(argv, "--TemplateId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteLiveRecordTemplateRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeleteLiveRecordTemplate(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doResumeDelayLiveStream(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ResumeDelayLiveStream", g_param[OptionsDefine.Version])
        return

    param = {
        "AppName": Utils.try_to_json(argv, "--AppName"),
        "DomainName": Utils.try_to_json(argv, "--DomainName"),
        "StreamName": Utils.try_to_json(argv, "--StreamName"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ResumeDelayLiveStreamRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ResumeDelayLiveStream(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateLiveTranscodeTemplate(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateLiveTranscodeTemplate", g_param[OptionsDefine.Version])
        return

    param = {
        "TemplateName": Utils.try_to_json(argv, "--TemplateName"),
        "VideoBitrate": Utils.try_to_json(argv, "--VideoBitrate"),
        "Vcodec": Utils.try_to_json(argv, "--Vcodec"),
        "Acodec": Utils.try_to_json(argv, "--Acodec"),
        "AudioBitrate": Utils.try_to_json(argv, "--AudioBitrate"),
        "Description": Utils.try_to_json(argv, "--Description"),
        "Width": Utils.try_to_json(argv, "--Width"),
        "NeedVideo": Utils.try_to_json(argv, "--NeedVideo"),
        "NeedAudio": Utils.try_to_json(argv, "--NeedAudio"),
        "Height": Utils.try_to_json(argv, "--Height"),
        "Fps": Utils.try_to_json(argv, "--Fps"),
        "Gop": Utils.try_to_json(argv, "--Gop"),
        "Rotate": Utils.try_to_json(argv, "--Rotate"),
        "Profile": Utils.try_to_json(argv, "--Profile"),
        "BitrateToOrig": Utils.try_to_json(argv, "--BitrateToOrig"),
        "HeightToOrig": Utils.try_to_json(argv, "--HeightToOrig"),
        "FpsToOrig": Utils.try_to_json(argv, "--FpsToOrig"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateLiveTranscodeTemplateRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateLiveTranscodeTemplate(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeLiveCerts(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeLiveCerts", g_param[OptionsDefine.Version])
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
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeLiveCertsRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeLiveCerts(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doEnableLiveDomain(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("EnableLiveDomain", g_param[OptionsDefine.Version])
        return

    param = {
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
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.EnableLiveDomainRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.EnableLiveDomain(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreatePullStreamConfig(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreatePullStreamConfig", g_param[OptionsDefine.Version])
        return

    param = {
        "FromUrl": Utils.try_to_json(argv, "--FromUrl"),
        "ToUrl": Utils.try_to_json(argv, "--ToUrl"),
        "AreaId": Utils.try_to_json(argv, "--AreaId"),
        "IspId": Utils.try_to_json(argv, "--IspId"),
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
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreatePullStreamConfigRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreatePullStreamConfig(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeLiveStreamPushInfoList(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeLiveStreamPushInfoList", g_param[OptionsDefine.Version])
        return

    param = {
        "PushDomain": Utils.try_to_json(argv, "--PushDomain"),
        "AppName": Utils.try_to_json(argv, "--AppName"),
        "PageNum": Utils.try_to_json(argv, "--PageNum"),
        "PageSize": Utils.try_to_json(argv, "--PageSize"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeLiveStreamPushInfoListRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeLiveStreamPushInfoList(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteLiveSnapshotTemplate(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteLiveSnapshotTemplate", g_param[OptionsDefine.Version])
        return

    param = {
        "TemplateId": Utils.try_to_json(argv, "--TemplateId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.LiveClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteLiveSnapshotTemplateRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeleteLiveSnapshotTemplate(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


CLIENT_MAP = {
    "v20180801": live_client_v20180801,

}

MODELS_MAP = {
    "v20180801": models_v20180801,

}

ACTION_MAP = {
    "DropLiveStream": doDropLiveStream,
    "DescribeLiveWatermarks": doDescribeLiveWatermarks,
    "CreateLiveRecord": doCreateLiveRecord,
    "UpdateLiveWatermark": doUpdateLiveWatermark,
    "ModifyLiveSnapshotTemplate": doModifyLiveSnapshotTemplate,
    "ModifyLiveRecordTemplate": doModifyLiveRecordTemplate,
    "CreateLiveWatermarkRule": doCreateLiveWatermarkRule,
    "DescribeLiveStreamEventList": doDescribeLiveStreamEventList,
    "DescribePullStreamConfigs": doDescribePullStreamConfigs,
    "DescribeHttpStatusInfoList": doDescribeHttpStatusInfoList,
    "DescribeProvinceIspPlayInfoList": doDescribeProvinceIspPlayInfoList,
    "ModifyLivePushAuthKey": doModifyLivePushAuthKey,
    "DescribeStreamPushInfoList": doDescribeStreamPushInfoList,
    "DescribeLiveSnapshotRules": doDescribeLiveSnapshotRules,
    "DeleteLiveTranscodeTemplate": doDeleteLiveTranscodeTemplate,
    "DescribeTopClientIpSumInfoList": doDescribeTopClientIpSumInfoList,
    "ModifyPullStreamStatus": doModifyPullStreamStatus,
    "DescribeLiveRecordTemplates": doDescribeLiveRecordTemplates,
    "ModifyLiveDomainCert": doModifyLiveDomainCert,
    "DescribeVisitTopSumInfoList": doDescribeVisitTopSumInfoList,
    "DescribeLiveDomainCert": doDescribeLiveDomainCert,
    "AddLiveWatermark": doAddLiveWatermark,
    "DeleteLiveWatermarkRule": doDeleteLiveWatermarkRule,
    "DeleteLiveCallbackRule": doDeleteLiveCallbackRule,
    "ModifyPullStreamConfig": doModifyPullStreamConfig,
    "CreateLiveSnapshotTemplate": doCreateLiveSnapshotTemplate,
    "DescribeLiveStreamOnlineList": doDescribeLiveStreamOnlineList,
    "DeleteLiveCallbackTemplate": doDeleteLiveCallbackTemplate,
    "DescribeLivePushAuthKey": doDescribeLivePushAuthKey,
    "DeletePullStreamConfig": doDeletePullStreamConfig,
    "DescribeLiveRecordTemplate": doDescribeLiveRecordTemplate,
    "DeleteLiveWatermark": doDeleteLiveWatermark,
    "UnBindLiveDomainCert": doUnBindLiveDomainCert,
    "DescribePlayErrorCodeSumInfoList": doDescribePlayErrorCodeSumInfoList,
    "AddDelayLiveStream": doAddDelayLiveStream,
    "DescribeStreamDayPlayInfoList": doDescribeStreamDayPlayInfoList,
    "ModifyLivePlayDomain": doModifyLivePlayDomain,
    "ModifyLiveTranscodeTemplate": doModifyLiveTranscodeTemplate,
    "DeleteLiveTranscodeRule": doDeleteLiveTranscodeRule,
    "DeleteLiveSnapshotRule": doDeleteLiveSnapshotRule,
    "DescribeLiveForbidStreamList": doDescribeLiveForbidStreamList,
    "DescribeLiveCert": doDescribeLiveCert,
    "ModifyLiveCert": doModifyLiveCert,
    "DescribeLiveDomains": doDescribeLiveDomains,
    "DeleteLiveCert": doDeleteLiveCert,
    "CreateLiveCallbackTemplate": doCreateLiveCallbackTemplate,
    "ResumeLiveStream": doResumeLiveStream,
    "DescribeLiveCallbackTemplate": doDescribeLiveCallbackTemplate,
    "DeleteLiveDomain": doDeleteLiveDomain,
    "ModifyLiveCallbackTemplate": doModifyLiveCallbackTemplate,
    "DescribeProIspPlaySumInfoList": doDescribeProIspPlaySumInfoList,
    "DescribeStreamPlayInfoList": doDescribeStreamPlayInfoList,
    "CreateLiveCert": doCreateLiveCert,
    "DescribeLiveTranscodeRules": doDescribeLiveTranscodeRules,
    "DescribeLiveSnapshotTemplate": doDescribeLiveSnapshotTemplate,
    "DescribeLiveCallbackTemplates": doDescribeLiveCallbackTemplates,
    "DescribeLiveSnapshotTemplates": doDescribeLiveSnapshotTemplates,
    "StopLiveRecord": doStopLiveRecord,
    "ModifyLivePlayAuthKey": doModifyLivePlayAuthKey,
    "DescribeLiveTranscodeTemplate": doDescribeLiveTranscodeTemplate,
    "SetLiveWatermarkStatus": doSetLiveWatermarkStatus,
    "DescribeLiveTranscodeDetailInfo": doDescribeLiveTranscodeDetailInfo,
    "DescribeLogDownloadList": doDescribeLogDownloadList,
    "DescribeLiveStreamOnlineInfo": doDescribeLiveStreamOnlineInfo,
    "DescribeLiveRecordRules": doDescribeLiveRecordRules,
    "DescribeLiveDelayInfoList": doDescribeLiveDelayInfoList,
    "DeleteLiveRecordRule": doDeleteLiveRecordRule,
    "DescribeLiveDomain": doDescribeLiveDomain,
    "CreateLiveCallbackRule": doCreateLiveCallbackRule,
    "BindLiveDomainCert": doBindLiveDomainCert,
    "DescribeLiveCallbackRules": doDescribeLiveCallbackRules,
    "DescribePlayErrorCodeDetailInfoList": doDescribePlayErrorCodeDetailInfoList,
    "DescribeLiveStreamPublishedList": doDescribeLiveStreamPublishedList,
    "ForbidLiveStream": doForbidLiveStream,
    "AddLiveDomain": doAddLiveDomain,
    "DescribeLiveDomainPlayInfoList": doDescribeLiveDomainPlayInfoList,
    "CreateLiveRecordRule": doCreateLiveRecordRule,
    "DescribeLiveWatermark": doDescribeLiveWatermark,
    "DescribeLiveTranscodeTemplates": doDescribeLiveTranscodeTemplates,
    "CreateLiveRecordTemplate": doCreateLiveRecordTemplate,
    "DescribeBillBandwidthAndFluxList": doDescribeBillBandwidthAndFluxList,
    "ForbidLiveDomain": doForbidLiveDomain,
    "CreateLiveTranscodeRule": doCreateLiveTranscodeRule,
    "DescribeLiveWatermarkRules": doDescribeLiveWatermarkRules,
    "DeleteLiveRecord": doDeleteLiveRecord,
    "CreateLiveSnapshotRule": doCreateLiveSnapshotRule,
    "DescribeGroupProIspPlayInfoList": doDescribeGroupProIspPlayInfoList,
    "DescribeLivePlayAuthKey": doDescribeLivePlayAuthKey,
    "DescribeLiveStreamState": doDescribeLiveStreamState,
    "DeleteLiveRecordTemplate": doDeleteLiveRecordTemplate,
    "ResumeDelayLiveStream": doResumeDelayLiveStream,
    "CreateLiveTranscodeTemplate": doCreateLiveTranscodeTemplate,
    "DescribeLiveCerts": doDescribeLiveCerts,
    "EnableLiveDomain": doEnableLiveDomain,
    "CreatePullStreamConfig": doCreatePullStreamConfig,
    "DescribeLiveStreamPushInfoList": doDescribeLiveStreamPushInfoList,
    "DeleteLiveSnapshotTemplate": doDeleteLiveSnapshotTemplate,

}

AVAILABLE_VERSION_LIST = [
    v20180801.version,

]
AVAILABLE_VERSIONS = {
     'v' + v20180801.version.replace('-', ''): {"help": v20180801_help.INFO,"desc": v20180801_help.DESC},

}


def live_action(argv, arglist):
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
        helpstr = HelpTemplate.SERVICE % {"name": "live", "desc": desc, "actions": action_str}
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
    cmd = NiceCommand("live", live_action)
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
            version = config["live"][OptionsDefine.Version]
            params[OptionsDefine.Version] = "v" + version.replace('-', '')

        if params[OptionsDefine.Endpoint] is None:
            params[OptionsDefine.Endpoint] = config["live"][OptionsDefine.Endpoint]
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

    helpmsg = HelpTemplate.ACTION % {"name": action, "service": "live", "desc": desc, "params": docstr}
    print(helpmsg)


def get_actions_info():
    config = Configure()
    new_version = max(AVAILABLE_VERSIONS.keys())
    version = new_version
    try:
        profile = config._load_json_msg(os.path.join(config.cli_path, "default.configure"))
        version = profile["live"]["version"]
        version = "v" + version.replace('-', '')
    except Exception:
        pass
    if version not in AVAILABLE_VERSIONS.keys():
        version = new_version
    return AVAILABLE_VERSIONS[version]["help"]
