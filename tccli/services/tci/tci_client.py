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
from tencentcloud.tci.v20190318 import tci_client as tci_client_v20190318
from tencentcloud.tci.v20190318 import models as models_v20190318
from tccli.services.tci import v20190318
from tccli.services.tci.v20190318 import help as v20190318_help


def doSubmitOpenClassTask(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("SubmitOpenClassTask", g_param[OptionsDefine.Version])
        return

    param = {
        "FileContent": argv.get("--FileContent"),
        "FileType": argv.get("--FileType"),
        "LibrarySet": Utils.try_to_json(argv, "--LibrarySet"),
        "MaxVideoDuration": Utils.try_to_json(argv, "--MaxVideoDuration"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.TciClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.SubmitOpenClassTaskRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.SubmitOpenClassTask(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doSubmitCheckAttendanceTaskPlus(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("SubmitCheckAttendanceTaskPlus", g_param[OptionsDefine.Version])
        return

    param = {
        "FileContent": Utils.try_to_json(argv, "--FileContent"),
        "FileType": argv.get("--FileType"),
        "LibraryIds": Utils.try_to_json(argv, "--LibraryIds"),
        "AttendanceThreshold": Utils.try_to_json(argv, "--AttendanceThreshold"),
        "EnableStranger": Utils.try_to_json(argv, "--EnableStranger"),
        "EndTime": Utils.try_to_json(argv, "--EndTime"),
        "NoticeUrl": argv.get("--NoticeUrl"),
        "StartTime": Utils.try_to_json(argv, "--StartTime"),
        "Threshold": Utils.try_to_json(argv, "--Threshold"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.TciClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.SubmitCheckAttendanceTaskPlusRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.SubmitCheckAttendanceTaskPlus(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateLibrary(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateLibrary", g_param[OptionsDefine.Version])
        return

    param = {
        "LibraryName": argv.get("--LibraryName"),
        "LibraryId": argv.get("--LibraryId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.TciClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateLibraryRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateLibrary(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doSubmitAudioTask(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("SubmitAudioTask", g_param[OptionsDefine.Version])
        return

    param = {
        "Lang": Utils.try_to_json(argv, "--Lang"),
        "Url": argv.get("--Url"),
        "VoiceEncodeType": Utils.try_to_json(argv, "--VoiceEncodeType"),
        "VoiceFileType": Utils.try_to_json(argv, "--VoiceFileType"),
        "Functions": Utils.try_to_json(argv, "--Functions"),
        "FileType": argv.get("--FileType"),
        "MuteThreshold": Utils.try_to_json(argv, "--MuteThreshold"),
        "VocabLibNameList": Utils.try_to_json(argv, "--VocabLibNameList"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.TciClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.SubmitAudioTaskRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.SubmitAudioTask(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateFace(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateFace", g_param[OptionsDefine.Version])
        return

    param = {
        "PersonId": argv.get("--PersonId"),
        "Images": Utils.try_to_json(argv, "--Images"),
        "LibraryId": argv.get("--LibraryId"),
        "Urls": Utils.try_to_json(argv, "--Urls"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.TciClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateFaceRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateFace(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyPerson(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyPerson", g_param[OptionsDefine.Version])
        return

    param = {
        "LibraryId": argv.get("--LibraryId"),
        "PersonId": argv.get("--PersonId"),
        "JobNumber": argv.get("--JobNumber"),
        "Mail": argv.get("--Mail"),
        "Male": Utils.try_to_json(argv, "--Male"),
        "PersonName": argv.get("--PersonName"),
        "PhoneNumber": argv.get("--PhoneNumber"),
        "StudentNumber": argv.get("--StudentNumber"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.TciClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyPersonRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyPerson(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeImageTaskStatistic(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeImageTaskStatistic", g_param[OptionsDefine.Version])
        return

    param = {
        "JobId": Utils.try_to_json(argv, "--JobId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.TciClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeImageTaskStatisticRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeImageTaskStatistic(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doAIAssistant(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("AIAssistant", g_param[OptionsDefine.Version])
        return

    param = {
        "FileContent": argv.get("--FileContent"),
        "FileType": argv.get("--FileType"),
        "Lang": Utils.try_to_json(argv, "--Lang"),
        "LibrarySet": Utils.try_to_json(argv, "--LibrarySet"),
        "MaxVideoDuration": Utils.try_to_json(argv, "--MaxVideoDuration"),
        "Template": Utils.try_to_json(argv, "--Template"),
        "VocabLibNameList": Utils.try_to_json(argv, "--VocabLibNameList"),
        "VoiceEncodeType": Utils.try_to_json(argv, "--VoiceEncodeType"),
        "VoiceFileType": Utils.try_to_json(argv, "--VoiceFileType"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.TciClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.AIAssistantRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.AIAssistant(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyLibrary(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyLibrary", g_param[OptionsDefine.Version])
        return

    param = {
        "LibraryId": argv.get("--LibraryId"),
        "LibraryName": argv.get("--LibraryName"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.TciClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyLibraryRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyLibrary(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doSubmitDoubleVideoHighlights(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("SubmitDoubleVideoHighlights", g_param[OptionsDefine.Version])
        return

    param = {
        "FileContent": argv.get("--FileContent"),
        "LibIds": Utils.try_to_json(argv, "--LibIds"),
        "Functions": Utils.try_to_json(argv, "--Functions"),
        "PersonInfoList": Utils.try_to_json(argv, "--PersonInfoList"),
        "FrameInterval": Utils.try_to_json(argv, "--FrameInterval"),
        "PersonIds": Utils.try_to_json(argv, "--PersonIds"),
        "SimThreshold": Utils.try_to_json(argv, "--SimThreshold"),
        "TeacherFileContent": argv.get("--TeacherFileContent"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.TciClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.SubmitDoubleVideoHighlightsRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.SubmitDoubleVideoHighlights(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribePersons(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribePersons", g_param[OptionsDefine.Version])
        return

    param = {
        "LibraryId": argv.get("--LibraryId"),
        "Limit": Utils.try_to_json(argv, "--Limit"),
        "Offset": Utils.try_to_json(argv, "--Offset"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.TciClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribePersonsRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribePersons(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doSubmitConversationTask(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("SubmitConversationTask", g_param[OptionsDefine.Version])
        return

    param = {
        "Lang": Utils.try_to_json(argv, "--Lang"),
        "StudentUrl": argv.get("--StudentUrl"),
        "TeacherUrl": argv.get("--TeacherUrl"),
        "VoiceEncodeType": Utils.try_to_json(argv, "--VoiceEncodeType"),
        "VoiceFileType": Utils.try_to_json(argv, "--VoiceFileType"),
        "Functions": Utils.try_to_json(argv, "--Functions"),
        "VocabLibNameList": Utils.try_to_json(argv, "--VocabLibNameList"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.TciClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.SubmitConversationTaskRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.SubmitConversationTask(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeHighlightResult(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeHighlightResult", g_param[OptionsDefine.Version])
        return

    param = {
        "JobId": Utils.try_to_json(argv, "--JobId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.TciClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeHighlightResultRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeHighlightResult(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doSubmitTraditionalClassTask(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("SubmitTraditionalClassTask", g_param[OptionsDefine.Version])
        return

    param = {
        "FileContent": argv.get("--FileContent"),
        "FileType": argv.get("--FileType"),
        "LibrarySet": Utils.try_to_json(argv, "--LibrarySet"),
        "MaxVideoDuration": Utils.try_to_json(argv, "--MaxVideoDuration"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.TciClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.SubmitTraditionalClassTaskRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.SubmitTraditionalClassTask(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeAITaskResult(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeAITaskResult", g_param[OptionsDefine.Version])
        return

    param = {
        "TaskId": Utils.try_to_json(argv, "--TaskId"),
        "Limit": Utils.try_to_json(argv, "--Limit"),
        "Offset": Utils.try_to_json(argv, "--Offset"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.TciClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeAITaskResultRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeAITaskResult(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeletePerson(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeletePerson", g_param[OptionsDefine.Version])
        return

    param = {
        "LibraryId": argv.get("--LibraryId"),
        "PersonId": argv.get("--PersonId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.TciClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeletePersonRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeletePerson(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeLibraries(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeLibraries", g_param[OptionsDefine.Version])
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
    client = mod.TciClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeLibrariesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeLibraries(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCancelTask(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CancelTask", g_param[OptionsDefine.Version])
        return

    param = {
        "JobId": Utils.try_to_json(argv, "--JobId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.TciClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CancelTaskRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CancelTask(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doSubmitHighlights(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("SubmitHighlights", g_param[OptionsDefine.Version])
        return

    param = {
        "Functions": Utils.try_to_json(argv, "--Functions"),
        "FileContent": argv.get("--FileContent"),
        "FileType": argv.get("--FileType"),
        "LibIds": Utils.try_to_json(argv, "--LibIds"),
        "FrameInterval": Utils.try_to_json(argv, "--FrameInterval"),
        "KeywordsLanguage": Utils.try_to_json(argv, "--KeywordsLanguage"),
        "KeywordsStrings": Utils.try_to_json(argv, "--KeywordsStrings"),
        "MaxVideoDuration": Utils.try_to_json(argv, "--MaxVideoDuration"),
        "SimThreshold": Utils.try_to_json(argv, "--SimThreshold"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.TciClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.SubmitHighlightsRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.SubmitHighlights(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeVocabLib(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeVocabLib", g_param[OptionsDefine.Version])
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
    client = mod.TciClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeVocabLibRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeVocabLib(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateVocab(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateVocab", g_param[OptionsDefine.Version])
        return

    param = {
        "VocabLibName": argv.get("--VocabLibName"),
        "VocabList": Utils.try_to_json(argv, "--VocabList"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.TciClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateVocabRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateVocab(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doSubmitOneByOneClassTask(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("SubmitOneByOneClassTask", g_param[OptionsDefine.Version])
        return

    param = {
        "FileContent": argv.get("--FileContent"),
        "FileType": argv.get("--FileType"),
        "Lang": Utils.try_to_json(argv, "--Lang"),
        "LibrarySet": Utils.try_to_json(argv, "--LibrarySet"),
        "MaxVideoDuration": Utils.try_to_json(argv, "--MaxVideoDuration"),
        "VocabLibNameList": Utils.try_to_json(argv, "--VocabLibNameList"),
        "VoiceEncodeType": Utils.try_to_json(argv, "--VoiceEncodeType"),
        "VoiceFileType": Utils.try_to_json(argv, "--VoiceFileType"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.TciClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.SubmitOneByOneClassTaskRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.SubmitOneByOneClassTask(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doSubmitPartialBodyClassTask(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("SubmitPartialBodyClassTask", g_param[OptionsDefine.Version])
        return

    param = {
        "FileContent": argv.get("--FileContent"),
        "FileType": argv.get("--FileType"),
        "Lang": Utils.try_to_json(argv, "--Lang"),
        "LibrarySet": Utils.try_to_json(argv, "--LibrarySet"),
        "MaxVideoDuration": Utils.try_to_json(argv, "--MaxVideoDuration"),
        "VocabLibNameList": Utils.try_to_json(argv, "--VocabLibNameList"),
        "VoiceEncodeType": Utils.try_to_json(argv, "--VoiceEncodeType"),
        "VoiceFileType": Utils.try_to_json(argv, "--VoiceFileType"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.TciClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.SubmitPartialBodyClassTaskRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.SubmitPartialBodyClassTask(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doSubmitCheckAttendanceTask(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("SubmitCheckAttendanceTask", g_param[OptionsDefine.Version])
        return

    param = {
        "FileContent": argv.get("--FileContent"),
        "FileType": argv.get("--FileType"),
        "LibraryIds": Utils.try_to_json(argv, "--LibraryIds"),
        "AttendanceThreshold": Utils.try_to_json(argv, "--AttendanceThreshold"),
        "EnableStranger": Utils.try_to_json(argv, "--EnableStranger"),
        "EndTime": Utils.try_to_json(argv, "--EndTime"),
        "NoticeUrl": argv.get("--NoticeUrl"),
        "StartTime": Utils.try_to_json(argv, "--StartTime"),
        "Threshold": Utils.try_to_json(argv, "--Threshold"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.TciClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.SubmitCheckAttendanceTaskRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.SubmitCheckAttendanceTask(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreatePerson(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreatePerson", g_param[OptionsDefine.Version])
        return

    param = {
        "LibraryId": argv.get("--LibraryId"),
        "PersonName": argv.get("--PersonName"),
        "Images": Utils.try_to_json(argv, "--Images"),
        "JobNumber": argv.get("--JobNumber"),
        "Mail": argv.get("--Mail"),
        "Male": Utils.try_to_json(argv, "--Male"),
        "PersonId": argv.get("--PersonId"),
        "PhoneNumber": argv.get("--PhoneNumber"),
        "StudentNumber": argv.get("--StudentNumber"),
        "Urls": Utils.try_to_json(argv, "--Urls"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.TciClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreatePersonRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreatePerson(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeConversationTask(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeConversationTask", g_param[OptionsDefine.Version])
        return

    param = {
        "JobId": Utils.try_to_json(argv, "--JobId"),
        "Identity": Utils.try_to_json(argv, "--Identity"),
        "Limit": Utils.try_to_json(argv, "--Limit"),
        "Offset": Utils.try_to_json(argv, "--Offset"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.TciClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeConversationTaskRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeConversationTask(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteLibrary(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteLibrary", g_param[OptionsDefine.Version])
        return

    param = {
        "LibraryId": argv.get("--LibraryId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.TciClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteLibraryRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeleteLibrary(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeImageTask(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeImageTask", g_param[OptionsDefine.Version])
        return

    param = {
        "JobId": Utils.try_to_json(argv, "--JobId"),
        "Limit": Utils.try_to_json(argv, "--Limit"),
        "Offset": Utils.try_to_json(argv, "--Offset"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.TciClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeImageTaskRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeImageTask(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doSubmitImageTask(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("SubmitImageTask", g_param[OptionsDefine.Version])
        return

    param = {
        "FileContent": argv.get("--FileContent"),
        "FileType": argv.get("--FileType"),
        "Functions": Utils.try_to_json(argv, "--Functions"),
        "LightStandardSet": Utils.try_to_json(argv, "--LightStandardSet"),
        "EventsCallBack": argv.get("--EventsCallBack"),
        "FrameInterval": Utils.try_to_json(argv, "--FrameInterval"),
        "LibrarySet": Utils.try_to_json(argv, "--LibrarySet"),
        "MaxVideoDuration": Utils.try_to_json(argv, "--MaxVideoDuration"),
        "SimThreshold": Utils.try_to_json(argv, "--SimThreshold"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.TciClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.SubmitImageTaskRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.SubmitImageTask(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeAttendanceResult(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeAttendanceResult", g_param[OptionsDefine.Version])
        return

    param = {
        "JobId": Utils.try_to_json(argv, "--JobId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.TciClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeAttendanceResultRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeAttendanceResult(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doSubmitImageTaskPlus(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("SubmitImageTaskPlus", g_param[OptionsDefine.Version])
        return

    param = {
        "FileContent": Utils.try_to_json(argv, "--FileContent"),
        "FileType": argv.get("--FileType"),
        "Functions": Utils.try_to_json(argv, "--Functions"),
        "LightStandardSet": Utils.try_to_json(argv, "--LightStandardSet"),
        "FrameInterval": Utils.try_to_json(argv, "--FrameInterval"),
        "LibrarySet": Utils.try_to_json(argv, "--LibrarySet"),
        "MaxVideoDuration": Utils.try_to_json(argv, "--MaxVideoDuration"),
        "SimThreshold": Utils.try_to_json(argv, "--SimThreshold"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.TciClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.SubmitImageTaskPlusRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.SubmitImageTaskPlus(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateVocabLib(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateVocabLib", g_param[OptionsDefine.Version])
        return

    param = {
        "VocabLibName": argv.get("--VocabLibName"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.TciClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateVocabLibRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateVocabLib(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteVocab(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteVocab", g_param[OptionsDefine.Version])
        return

    param = {
        "VocabLibName": argv.get("--VocabLibName"),
        "VocabList": Utils.try_to_json(argv, "--VocabList"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.TciClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteVocabRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeleteVocab(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doSubmitFullBodyClassTask(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("SubmitFullBodyClassTask", g_param[OptionsDefine.Version])
        return

    param = {
        "FileContent": argv.get("--FileContent"),
        "FileType": argv.get("--FileType"),
        "Lang": Utils.try_to_json(argv, "--Lang"),
        "LibrarySet": Utils.try_to_json(argv, "--LibrarySet"),
        "MaxVideoDuration": Utils.try_to_json(argv, "--MaxVideoDuration"),
        "VocabLibNameList": Utils.try_to_json(argv, "--VocabLibNameList"),
        "VoiceEncodeType": Utils.try_to_json(argv, "--VoiceEncodeType"),
        "VoiceFileType": Utils.try_to_json(argv, "--VoiceFileType"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.TciClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.SubmitFullBodyClassTaskRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.SubmitFullBodyClassTask(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCheckFacePhoto(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CheckFacePhoto", g_param[OptionsDefine.Version])
        return

    param = {
        "FileContent": argv.get("--FileContent"),
        "FileType": argv.get("--FileType"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.TciClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CheckFacePhotoRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CheckFacePhoto(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeVocab(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeVocab", g_param[OptionsDefine.Version])
        return

    param = {
        "VocabLibName": argv.get("--VocabLibName"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.TciClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeVocabRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeVocab(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteVocabLib(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteVocabLib", g_param[OptionsDefine.Version])
        return

    param = {
        "VocabLibName": argv.get("--VocabLibName"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.TciClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteVocabLibRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeleteVocabLib(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribePerson(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribePerson", g_param[OptionsDefine.Version])
        return

    param = {
        "LibraryId": argv.get("--LibraryId"),
        "PersonId": argv.get("--PersonId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.TciClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribePersonRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribePerson(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteFace(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteFace", g_param[OptionsDefine.Version])
        return

    param = {
        "FaceIdSet": Utils.try_to_json(argv, "--FaceIdSet"),
        "PersonId": argv.get("--PersonId"),
        "LibraryId": argv.get("--LibraryId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.TciClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteFaceRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeleteFace(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeAudioTask(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeAudioTask", g_param[OptionsDefine.Version])
        return

    param = {
        "JobId": Utils.try_to_json(argv, "--JobId"),
        "Limit": Utils.try_to_json(argv, "--Limit"),
        "Offset": Utils.try_to_json(argv, "--Offset"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.TciClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeAudioTaskRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeAudioTask(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doTransmitAudioStream(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("TransmitAudioStream", g_param[OptionsDefine.Version])
        return

    param = {
        "Functions": Utils.try_to_json(argv, "--Functions"),
        "SeqId": Utils.try_to_json(argv, "--SeqId"),
        "SessionId": argv.get("--SessionId"),
        "UserVoiceData": argv.get("--UserVoiceData"),
        "VoiceEncodeType": Utils.try_to_json(argv, "--VoiceEncodeType"),
        "VoiceFileType": Utils.try_to_json(argv, "--VoiceFileType"),
        "IsEnd": Utils.try_to_json(argv, "--IsEnd"),
        "Lang": Utils.try_to_json(argv, "--Lang"),
        "StorageMode": Utils.try_to_json(argv, "--StorageMode"),
        "VocabLibNameList": Utils.try_to_json(argv, "--VocabLibNameList"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.TciClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.TransmitAudioStreamRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.TransmitAudioStream(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


CLIENT_MAP = {
    "v20190318": tci_client_v20190318,

}

MODELS_MAP = {
    "v20190318": models_v20190318,

}

ACTION_MAP = {
    "SubmitOpenClassTask": doSubmitOpenClassTask,
    "SubmitCheckAttendanceTaskPlus": doSubmitCheckAttendanceTaskPlus,
    "CreateLibrary": doCreateLibrary,
    "SubmitAudioTask": doSubmitAudioTask,
    "CreateFace": doCreateFace,
    "ModifyPerson": doModifyPerson,
    "DescribeImageTaskStatistic": doDescribeImageTaskStatistic,
    "AIAssistant": doAIAssistant,
    "ModifyLibrary": doModifyLibrary,
    "SubmitDoubleVideoHighlights": doSubmitDoubleVideoHighlights,
    "DescribePersons": doDescribePersons,
    "SubmitConversationTask": doSubmitConversationTask,
    "DescribeHighlightResult": doDescribeHighlightResult,
    "SubmitTraditionalClassTask": doSubmitTraditionalClassTask,
    "DescribeAITaskResult": doDescribeAITaskResult,
    "DeletePerson": doDeletePerson,
    "DescribeLibraries": doDescribeLibraries,
    "CancelTask": doCancelTask,
    "SubmitHighlights": doSubmitHighlights,
    "DescribeVocabLib": doDescribeVocabLib,
    "CreateVocab": doCreateVocab,
    "SubmitOneByOneClassTask": doSubmitOneByOneClassTask,
    "SubmitPartialBodyClassTask": doSubmitPartialBodyClassTask,
    "SubmitCheckAttendanceTask": doSubmitCheckAttendanceTask,
    "CreatePerson": doCreatePerson,
    "DescribeConversationTask": doDescribeConversationTask,
    "DeleteLibrary": doDeleteLibrary,
    "DescribeImageTask": doDescribeImageTask,
    "SubmitImageTask": doSubmitImageTask,
    "DescribeAttendanceResult": doDescribeAttendanceResult,
    "SubmitImageTaskPlus": doSubmitImageTaskPlus,
    "CreateVocabLib": doCreateVocabLib,
    "DeleteVocab": doDeleteVocab,
    "SubmitFullBodyClassTask": doSubmitFullBodyClassTask,
    "CheckFacePhoto": doCheckFacePhoto,
    "DescribeVocab": doDescribeVocab,
    "DeleteVocabLib": doDeleteVocabLib,
    "DescribePerson": doDescribePerson,
    "DeleteFace": doDeleteFace,
    "DescribeAudioTask": doDescribeAudioTask,
    "TransmitAudioStream": doTransmitAudioStream,

}

AVAILABLE_VERSION_LIST = [
    v20190318.version,

]
AVAILABLE_VERSIONS = {
     'v' + v20190318.version.replace('-', ''): {"help": v20190318_help.INFO,"desc": v20190318_help.DESC},

}


def tci_action(argv, arglist):
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
        helpstr = HelpTemplate.SERVICE % {"name": "tci", "desc": desc, "actions": action_str}
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
    cmd = NiceCommand("tci", tci_action)
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
            version = config["tci"][OptionsDefine.Version]
            params[OptionsDefine.Version] = "v" + version.replace('-', '')

        if params[OptionsDefine.Endpoint] is None:
            params[OptionsDefine.Endpoint] = config["tci"][OptionsDefine.Endpoint]
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

    helpmsg = HelpTemplate.ACTION % {"name": action, "service": "tci", "desc": desc, "params": docstr}
    print(helpmsg)


def get_actions_info():
    config = Configure()
    new_version = max(AVAILABLE_VERSIONS.keys())
    version = new_version
    try:
        profile = config._load_json_msg(os.path.join(config.cli_path, "default.configure"))
        version = profile["tci"]["version"]
        version = "v" + version.replace('-', '')
    except Exception:
        pass
    if version not in AVAILABLE_VERSIONS.keys():
        version = new_version
    return AVAILABLE_VERSIONS[version]["help"]
