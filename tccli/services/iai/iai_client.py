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
from tencentcloud.iai.v20200303 import iai_client as iai_client_v20200303
from tencentcloud.iai.v20200303 import models as models_v20200303
from tencentcloud.iai.v20180301 import iai_client as iai_client_v20180301
from tencentcloud.iai.v20180301 import models as models_v20180301
from tccli.services.iai import v20200303
from tccli.services.iai.v20200303 import help as v20200303_help
from tccli.services.iai import v20180301
from tccli.services.iai.v20180301 import help as v20180301_help


def doDeletePersonFromGroup(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeletePersonFromGroup", g_param[OptionsDefine.Version])
        return

    param = {
        "PersonId": argv.get("--PersonId"),
        "GroupId": argv.get("--GroupId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.IaiClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeletePersonFromGroupRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeletePersonFromGroup(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doSearchFacesReturnsByGroup(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("SearchFacesReturnsByGroup", g_param[OptionsDefine.Version])
        return

    param = {
        "GroupIds": Utils.try_to_json(argv, "--GroupIds"),
        "Image": argv.get("--Image"),
        "Url": argv.get("--Url"),
        "MaxFaceNum": Utils.try_to_json(argv, "--MaxFaceNum"),
        "MinFaceSize": Utils.try_to_json(argv, "--MinFaceSize"),
        "MaxPersonNumPerGroup": Utils.try_to_json(argv, "--MaxPersonNumPerGroup"),
        "NeedPersonInfo": Utils.try_to_json(argv, "--NeedPersonInfo"),
        "QualityControl": Utils.try_to_json(argv, "--QualityControl"),
        "FaceMatchThreshold": Utils.try_to_json(argv, "--FaceMatchThreshold"),
        "NeedRotateDetection": Utils.try_to_json(argv, "--NeedRotateDetection"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.IaiClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.SearchFacesReturnsByGroupRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.SearchFacesReturnsByGroup(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateGroup(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateGroup", g_param[OptionsDefine.Version])
        return

    param = {
        "GroupName": argv.get("--GroupName"),
        "GroupId": argv.get("--GroupId"),
        "GroupExDescriptions": Utils.try_to_json(argv, "--GroupExDescriptions"),
        "Tag": argv.get("--Tag"),
        "FaceModelVersion": argv.get("--FaceModelVersion"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.IaiClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateGroupRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateGroup(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doGetCheckSimilarPersonJobIdList(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("GetCheckSimilarPersonJobIdList", g_param[OptionsDefine.Version])
        return

    param = {
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
    client = mod.IaiClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.GetCheckSimilarPersonJobIdListRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.GetCheckSimilarPersonJobIdList(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doGetPersonBaseInfo(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("GetPersonBaseInfo", g_param[OptionsDefine.Version])
        return

    param = {
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
    client = mod.IaiClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.GetPersonBaseInfoRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.GetPersonBaseInfo(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDetectLiveFace(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DetectLiveFace", g_param[OptionsDefine.Version])
        return

    param = {
        "Image": argv.get("--Image"),
        "Url": argv.get("--Url"),
        "FaceModelVersion": argv.get("--FaceModelVersion"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.IaiClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DetectLiveFaceRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DetectLiveFace(model)
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
        "Urls": Utils.try_to_json(argv, "--Urls"),
        "FaceMatchThreshold": Utils.try_to_json(argv, "--FaceMatchThreshold"),
        "QualityControl": Utils.try_to_json(argv, "--QualityControl"),
        "NeedRotateDetection": Utils.try_to_json(argv, "--NeedRotateDetection"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.IaiClient(cred, g_param[OptionsDefine.Region], profile)
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


def doGetPersonListNum(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("GetPersonListNum", g_param[OptionsDefine.Version])
        return

    param = {
        "GroupId": argv.get("--GroupId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.IaiClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.GetPersonListNumRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.GetPersonListNum(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doGetPersonGroupInfo(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("GetPersonGroupInfo", g_param[OptionsDefine.Version])
        return

    param = {
        "PersonId": argv.get("--PersonId"),
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
    client = mod.IaiClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.GetPersonGroupInfoRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.GetPersonGroupInfo(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doAnalyzeFace(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("AnalyzeFace", g_param[OptionsDefine.Version])
        return

    param = {
        "Mode": Utils.try_to_json(argv, "--Mode"),
        "Image": argv.get("--Image"),
        "Url": argv.get("--Url"),
        "FaceModelVersion": argv.get("--FaceModelVersion"),
        "NeedRotateDetection": Utils.try_to_json(argv, "--NeedRotateDetection"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.IaiClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.AnalyzeFaceRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.AnalyzeFace(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyPersonBaseInfo(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyPersonBaseInfo", g_param[OptionsDefine.Version])
        return

    param = {
        "PersonId": argv.get("--PersonId"),
        "PersonName": argv.get("--PersonName"),
        "Gender": Utils.try_to_json(argv, "--Gender"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.IaiClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyPersonBaseInfoRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyPersonBaseInfo(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doSearchFaces(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("SearchFaces", g_param[OptionsDefine.Version])
        return

    param = {
        "GroupIds": Utils.try_to_json(argv, "--GroupIds"),
        "Image": argv.get("--Image"),
        "Url": argv.get("--Url"),
        "MaxFaceNum": Utils.try_to_json(argv, "--MaxFaceNum"),
        "MinFaceSize": Utils.try_to_json(argv, "--MinFaceSize"),
        "MaxPersonNum": Utils.try_to_json(argv, "--MaxPersonNum"),
        "NeedPersonInfo": Utils.try_to_json(argv, "--NeedPersonInfo"),
        "QualityControl": Utils.try_to_json(argv, "--QualityControl"),
        "FaceMatchThreshold": Utils.try_to_json(argv, "--FaceMatchThreshold"),
        "NeedRotateDetection": Utils.try_to_json(argv, "--NeedRotateDetection"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.IaiClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.SearchFacesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.SearchFaces(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCopyPerson(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CopyPerson", g_param[OptionsDefine.Version])
        return

    param = {
        "PersonId": argv.get("--PersonId"),
        "GroupIds": Utils.try_to_json(argv, "--GroupIds"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.IaiClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CopyPersonRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CopyPerson(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCheckSimilarPerson(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CheckSimilarPerson", g_param[OptionsDefine.Version])
        return

    param = {
        "GroupIds": Utils.try_to_json(argv, "--GroupIds"),
        "UniquePersonControl": Utils.try_to_json(argv, "--UniquePersonControl"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.IaiClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CheckSimilarPersonRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CheckSimilarPerson(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteGroup(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteGroup", g_param[OptionsDefine.Version])
        return

    param = {
        "GroupId": argv.get("--GroupId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.IaiClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteGroupRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeleteGroup(model)
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
    client = mod.IaiClient(cred, g_param[OptionsDefine.Region], profile)
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


def doModifyGroup(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyGroup", g_param[OptionsDefine.Version])
        return

    param = {
        "GroupId": argv.get("--GroupId"),
        "GroupName": argv.get("--GroupName"),
        "GroupExDescriptionInfos": Utils.try_to_json(argv, "--GroupExDescriptionInfos"),
        "Tag": argv.get("--Tag"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.IaiClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyGroupRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyGroup(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doGetSimilarPersonResult(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("GetSimilarPersonResult", g_param[OptionsDefine.Version])
        return

    param = {
        "JobId": argv.get("--JobId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.IaiClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.GetSimilarPersonResultRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.GetSimilarPersonResult(model)
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
        "GroupId": argv.get("--GroupId"),
        "PersonName": argv.get("--PersonName"),
        "PersonId": argv.get("--PersonId"),
        "Gender": Utils.try_to_json(argv, "--Gender"),
        "PersonExDescriptionInfos": Utils.try_to_json(argv, "--PersonExDescriptionInfos"),
        "Image": argv.get("--Image"),
        "Url": argv.get("--Url"),
        "UniquePersonControl": Utils.try_to_json(argv, "--UniquePersonControl"),
        "QualityControl": Utils.try_to_json(argv, "--QualityControl"),
        "NeedRotateDetection": Utils.try_to_json(argv, "--NeedRotateDetection"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.IaiClient(cred, g_param[OptionsDefine.Region], profile)
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


def doGetGroupInfo(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("GetGroupInfo", g_param[OptionsDefine.Version])
        return

    param = {
        "GroupId": argv.get("--GroupId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.IaiClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.GetGroupInfoRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.GetGroupInfo(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDetectFace(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DetectFace", g_param[OptionsDefine.Version])
        return

    param = {
        "MaxFaceNum": Utils.try_to_json(argv, "--MaxFaceNum"),
        "MinFaceSize": Utils.try_to_json(argv, "--MinFaceSize"),
        "Image": argv.get("--Image"),
        "Url": argv.get("--Url"),
        "NeedFaceAttributes": Utils.try_to_json(argv, "--NeedFaceAttributes"),
        "NeedQualityDetection": Utils.try_to_json(argv, "--NeedQualityDetection"),
        "FaceModelVersion": argv.get("--FaceModelVersion"),
        "NeedRotateDetection": Utils.try_to_json(argv, "--NeedRotateDetection"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.IaiClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DetectFaceRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DetectFace(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doGetPersonList(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("GetPersonList", g_param[OptionsDefine.Version])
        return

    param = {
        "GroupId": argv.get("--GroupId"),
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
    client = mod.IaiClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.GetPersonListRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.GetPersonList(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doVerifyPerson(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("VerifyPerson", g_param[OptionsDefine.Version])
        return

    param = {
        "Image": argv.get("--Image"),
        "Url": argv.get("--Url"),
        "PersonId": argv.get("--PersonId"),
        "QualityControl": Utils.try_to_json(argv, "--QualityControl"),
        "NeedRotateDetection": Utils.try_to_json(argv, "--NeedRotateDetection"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.IaiClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.VerifyPersonRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.VerifyPerson(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyPersonGroupInfo(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyPersonGroupInfo", g_param[OptionsDefine.Version])
        return

    param = {
        "GroupId": argv.get("--GroupId"),
        "PersonId": argv.get("--PersonId"),
        "PersonExDescriptionInfos": Utils.try_to_json(argv, "--PersonExDescriptionInfos"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.IaiClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyPersonGroupInfoRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyPersonGroupInfo(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doVerifyFace(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("VerifyFace", g_param[OptionsDefine.Version])
        return

    param = {
        "PersonId": argv.get("--PersonId"),
        "Image": argv.get("--Image"),
        "Url": argv.get("--Url"),
        "QualityControl": Utils.try_to_json(argv, "--QualityControl"),
        "NeedRotateDetection": Utils.try_to_json(argv, "--NeedRotateDetection"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.IaiClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.VerifyFaceRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.VerifyFace(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doSearchPersons(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("SearchPersons", g_param[OptionsDefine.Version])
        return

    param = {
        "GroupIds": Utils.try_to_json(argv, "--GroupIds"),
        "Image": argv.get("--Image"),
        "Url": argv.get("--Url"),
        "MaxFaceNum": Utils.try_to_json(argv, "--MaxFaceNum"),
        "MinFaceSize": Utils.try_to_json(argv, "--MinFaceSize"),
        "MaxPersonNum": Utils.try_to_json(argv, "--MaxPersonNum"),
        "QualityControl": Utils.try_to_json(argv, "--QualityControl"),
        "FaceMatchThreshold": Utils.try_to_json(argv, "--FaceMatchThreshold"),
        "NeedPersonInfo": Utils.try_to_json(argv, "--NeedPersonInfo"),
        "NeedRotateDetection": Utils.try_to_json(argv, "--NeedRotateDetection"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.IaiClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.SearchPersonsRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.SearchPersons(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCompareFace(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CompareFace", g_param[OptionsDefine.Version])
        return

    param = {
        "ImageA": argv.get("--ImageA"),
        "ImageB": argv.get("--ImageB"),
        "UrlA": argv.get("--UrlA"),
        "UrlB": argv.get("--UrlB"),
        "FaceModelVersion": argv.get("--FaceModelVersion"),
        "QualityControl": Utils.try_to_json(argv, "--QualityControl"),
        "NeedRotateDetection": Utils.try_to_json(argv, "--NeedRotateDetection"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.IaiClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CompareFaceRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CompareFace(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doSearchPersonsReturnsByGroup(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("SearchPersonsReturnsByGroup", g_param[OptionsDefine.Version])
        return

    param = {
        "GroupIds": Utils.try_to_json(argv, "--GroupIds"),
        "Image": argv.get("--Image"),
        "Url": argv.get("--Url"),
        "MaxFaceNum": Utils.try_to_json(argv, "--MaxFaceNum"),
        "MinFaceSize": Utils.try_to_json(argv, "--MinFaceSize"),
        "MaxPersonNumPerGroup": Utils.try_to_json(argv, "--MaxPersonNumPerGroup"),
        "QualityControl": Utils.try_to_json(argv, "--QualityControl"),
        "FaceMatchThreshold": Utils.try_to_json(argv, "--FaceMatchThreshold"),
        "NeedPersonInfo": Utils.try_to_json(argv, "--NeedPersonInfo"),
        "NeedRotateDetection": Utils.try_to_json(argv, "--NeedRotateDetection"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.IaiClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.SearchPersonsReturnsByGroupRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.SearchPersonsReturnsByGroup(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doGetGroupList(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("GetGroupList", g_param[OptionsDefine.Version])
        return

    param = {
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
    client = mod.IaiClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.GetGroupListRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.GetGroupList(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doEstimateCheckSimilarPersonCostTime(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("EstimateCheckSimilarPersonCostTime", g_param[OptionsDefine.Version])
        return

    param = {
        "GroupIds": Utils.try_to_json(argv, "--GroupIds"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.IaiClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.EstimateCheckSimilarPersonCostTimeRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.EstimateCheckSimilarPersonCostTime(model)
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
        "PersonId": argv.get("--PersonId"),
        "FaceIds": Utils.try_to_json(argv, "--FaceIds"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.IaiClient(cred, g_param[OptionsDefine.Region], profile)
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


CLIENT_MAP = {
    "v20200303": iai_client_v20200303,
    "v20180301": iai_client_v20180301,

}

MODELS_MAP = {
    "v20200303": models_v20200303,
    "v20180301": models_v20180301,

}

ACTION_MAP = {
    "DeletePersonFromGroup": doDeletePersonFromGroup,
    "SearchFacesReturnsByGroup": doSearchFacesReturnsByGroup,
    "CreateGroup": doCreateGroup,
    "GetCheckSimilarPersonJobIdList": doGetCheckSimilarPersonJobIdList,
    "GetPersonBaseInfo": doGetPersonBaseInfo,
    "DetectLiveFace": doDetectLiveFace,
    "CreateFace": doCreateFace,
    "GetPersonListNum": doGetPersonListNum,
    "GetPersonGroupInfo": doGetPersonGroupInfo,
    "AnalyzeFace": doAnalyzeFace,
    "ModifyPersonBaseInfo": doModifyPersonBaseInfo,
    "SearchFaces": doSearchFaces,
    "CopyPerson": doCopyPerson,
    "CheckSimilarPerson": doCheckSimilarPerson,
    "DeleteGroup": doDeleteGroup,
    "DeletePerson": doDeletePerson,
    "ModifyGroup": doModifyGroup,
    "GetSimilarPersonResult": doGetSimilarPersonResult,
    "CreatePerson": doCreatePerson,
    "GetGroupInfo": doGetGroupInfo,
    "DetectFace": doDetectFace,
    "GetPersonList": doGetPersonList,
    "VerifyPerson": doVerifyPerson,
    "ModifyPersonGroupInfo": doModifyPersonGroupInfo,
    "VerifyFace": doVerifyFace,
    "SearchPersons": doSearchPersons,
    "CompareFace": doCompareFace,
    "SearchPersonsReturnsByGroup": doSearchPersonsReturnsByGroup,
    "GetGroupList": doGetGroupList,
    "EstimateCheckSimilarPersonCostTime": doEstimateCheckSimilarPersonCostTime,
    "DeleteFace": doDeleteFace,

}

AVAILABLE_VERSION_LIST = [
    v20200303.version,
    v20180301.version,

]
AVAILABLE_VERSIONS = {
     'v' + v20200303.version.replace('-', ''): {"help": v20200303_help.INFO,"desc": v20200303_help.DESC},
     'v' + v20180301.version.replace('-', ''): {"help": v20180301_help.INFO,"desc": v20180301_help.DESC},

}


def iai_action(argv, arglist):
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
        helpstr = HelpTemplate.SERVICE % {"name": "iai", "desc": desc, "actions": action_str}
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
    cmd = NiceCommand("iai", iai_action)
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
            version = config["iai"][OptionsDefine.Version]
            params[OptionsDefine.Version] = "v" + version.replace('-', '')

        if params[OptionsDefine.Endpoint] is None:
            params[OptionsDefine.Endpoint] = config["iai"][OptionsDefine.Endpoint]
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

    helpmsg = HelpTemplate.ACTION % {"name": action, "service": "iai", "desc": desc, "params": docstr}
    print(helpmsg)


def get_actions_info():
    config = Configure()
    new_version = max(AVAILABLE_VERSIONS.keys())
    version = new_version
    try:
        profile = config._load_json_msg(os.path.join(config.cli_path, "default.configure"))
        version = profile["iai"]["version"]
        version = "v" + version.replace('-', '')
    except Exception:
        pass
    if version not in AVAILABLE_VERSIONS.keys():
        version = new_version
    return AVAILABLE_VERSIONS[version]["help"]
