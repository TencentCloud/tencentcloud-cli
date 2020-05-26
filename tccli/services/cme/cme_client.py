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
from tencentcloud.cme.v20191029 import cme_client as cme_client_v20191029
from tencentcloud.cme.v20191029 import models as models_v20191029
from tccli.services.cme import v20191029
from tccli.services.cme.v20191029 import help as v20191029_help


def doDescribeMaterials(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeMaterials", g_param[OptionsDefine.Version])
        return

    param = {
        "Platform": argv.get("--Platform"),
        "MaterialIds": Utils.try_to_json(argv, "--MaterialIds"),
        "Sort": Utils.try_to_json(argv, "--Sort"),
        "Operator": argv.get("--Operator"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CmeClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeMaterialsRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeMaterials(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeTeams(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeTeams", g_param[OptionsDefine.Version])
        return

    param = {
        "Platform": argv.get("--Platform"),
        "TeamIds": Utils.try_to_json(argv, "--TeamIds"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CmeClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeTeamsRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeTeams(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doExportVideoEditProject(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ExportVideoEditProject", g_param[OptionsDefine.Version])
        return

    param = {
        "Platform": argv.get("--Platform"),
        "ProjectId": argv.get("--ProjectId"),
        "Definition": Utils.try_to_json(argv, "--Definition"),
        "ExportDestination": argv.get("--ExportDestination"),
        "CMEExportInfo": Utils.try_to_json(argv, "--CMEExportInfo"),
        "VODExportInfo": Utils.try_to_json(argv, "--VODExportInfo"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CmeClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ExportVideoEditProjectRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ExportVideoEditProject(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeSharedSpace(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeSharedSpace", g_param[OptionsDefine.Version])
        return

    param = {
        "Platform": argv.get("--Platform"),
        "Authorizee": Utils.try_to_json(argv, "--Authorizee"),
        "Operator": argv.get("--Operator"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CmeClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeSharedSpaceRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeSharedSpace(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doGrantResourceAuthorization(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("GrantResourceAuthorization", g_param[OptionsDefine.Version])
        return

    param = {
        "Platform": argv.get("--Platform"),
        "Owner": Utils.try_to_json(argv, "--Owner"),
        "Resources": Utils.try_to_json(argv, "--Resources"),
        "Authorizees": Utils.try_to_json(argv, "--Authorizees"),
        "Permissions": Utils.try_to_json(argv, "--Permissions"),
        "Operator": argv.get("--Operator"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CmeClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.GrantResourceAuthorizationRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.GrantResourceAuthorization(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doSearchMaterial(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("SearchMaterial", g_param[OptionsDefine.Version])
        return

    param = {
        "Platform": argv.get("--Platform"),
        "SearchScopes": Utils.try_to_json(argv, "--SearchScopes"),
        "MaterialTypes": Utils.try_to_json(argv, "--MaterialTypes"),
        "Text": argv.get("--Text"),
        "Resolution": argv.get("--Resolution"),
        "DurationRange": Utils.try_to_json(argv, "--DurationRange"),
        "CreateTimeRange": Utils.try_to_json(argv, "--CreateTimeRange"),
        "Tags": Utils.try_to_json(argv, "--Tags"),
        "Sort": Utils.try_to_json(argv, "--Sort"),
        "Offset": Utils.try_to_json(argv, "--Offset"),
        "Limit": Utils.try_to_json(argv, "--Limit"),
        "Operator": argv.get("--Operator"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CmeClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.SearchMaterialRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.SearchMaterial(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doRevokeResourceAuthorization(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("RevokeResourceAuthorization", g_param[OptionsDefine.Version])
        return

    param = {
        "Platform": argv.get("--Platform"),
        "Owner": Utils.try_to_json(argv, "--Owner"),
        "Resources": Utils.try_to_json(argv, "--Resources"),
        "Authorizees": Utils.try_to_json(argv, "--Authorizees"),
        "Permissions": Utils.try_to_json(argv, "--Permissions"),
        "Operator": argv.get("--Operator"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CmeClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.RevokeResourceAuthorizationRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.RevokeResourceAuthorization(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeJoinTeams(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeJoinTeams", g_param[OptionsDefine.Version])
        return

    param = {
        "Platform": argv.get("--Platform"),
        "MemberId": argv.get("--MemberId"),
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
    client = mod.CmeClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeJoinTeamsRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeJoinTeams(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeResourceAuthorization(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeResourceAuthorization", g_param[OptionsDefine.Version])
        return

    param = {
        "Platform": argv.get("--Platform"),
        "Owner": Utils.try_to_json(argv, "--Owner"),
        "Resource": Utils.try_to_json(argv, "--Resource"),
        "Operator": argv.get("--Operator"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CmeClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeResourceAuthorizationRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeResourceAuthorization(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doImportMaterial(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ImportMaterial", g_param[OptionsDefine.Version])
        return

    param = {
        "Platform": argv.get("--Platform"),
        "VodFileId": argv.get("--VodFileId"),
        "Owner": Utils.try_to_json(argv, "--Owner"),
        "Name": argv.get("--Name"),
        "ClassPath": argv.get("--ClassPath"),
        "PreProcessDefinition": Utils.try_to_json(argv, "--PreProcessDefinition"),
        "Operator": argv.get("--Operator"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CmeClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ImportMaterialRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ImportMaterial(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doExportVideoByEditorTrackData(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ExportVideoByEditorTrackData", g_param[OptionsDefine.Version])
        return

    param = {
        "Platform": argv.get("--Platform"),
        "Definition": Utils.try_to_json(argv, "--Definition"),
        "ExportDestination": argv.get("--ExportDestination"),
        "TrackData": argv.get("--TrackData"),
        "CMEExportInfo": Utils.try_to_json(argv, "--CMEExportInfo"),
        "VODExportInfo": Utils.try_to_json(argv, "--VODExportInfo"),
        "Operator": argv.get("--Operator"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CmeClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ExportVideoByEditorTrackDataRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ExportVideoByEditorTrackData(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeTaskDetail(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeTaskDetail", g_param[OptionsDefine.Version])
        return

    param = {
        "Platform": argv.get("--Platform"),
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
    client = mod.CmeClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeTaskDetailRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeTaskDetail(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateLink(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateLink", g_param[OptionsDefine.Version])
        return

    param = {
        "Platform": argv.get("--Platform"),
        "Type": argv.get("--Type"),
        "Name": argv.get("--Name"),
        "Owner": Utils.try_to_json(argv, "--Owner"),
        "DestinationId": argv.get("--DestinationId"),
        "DestinationOwner": Utils.try_to_json(argv, "--DestinationOwner"),
        "ClassPath": argv.get("--ClassPath"),
        "Operator": argv.get("--Operator"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CmeClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateLinkRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateLink(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyTeam(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyTeam", g_param[OptionsDefine.Version])
        return

    param = {
        "Platform": argv.get("--Platform"),
        "TeamId": argv.get("--TeamId"),
        "Name": argv.get("--Name"),
        "Operator": argv.get("--Operator"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CmeClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyTeamRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyTeam(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteMaterial(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteMaterial", g_param[OptionsDefine.Version])
        return

    param = {
        "Platform": argv.get("--Platform"),
        "MaterialId": argv.get("--MaterialId"),
        "Operator": argv.get("--Operator"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CmeClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteMaterialRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeleteMaterial(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyMaterial(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyMaterial", g_param[OptionsDefine.Version])
        return

    param = {
        "Platform": argv.get("--Platform"),
        "MaterialId": argv.get("--MaterialId"),
        "Owner": Utils.try_to_json(argv, "--Owner"),
        "Name": argv.get("--Name"),
        "ClassPath": argv.get("--ClassPath"),
        "Operator": argv.get("--Operator"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CmeClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyMaterialRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyMaterial(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteTeam(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteTeam", g_param[OptionsDefine.Version])
        return

    param = {
        "Platform": argv.get("--Platform"),
        "TeamId": argv.get("--TeamId"),
        "Operator": argv.get("--Operator"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CmeClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteTeamRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeleteTeam(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doAddTeamMember(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("AddTeamMember", g_param[OptionsDefine.Version])
        return

    param = {
        "Platform": argv.get("--Platform"),
        "TeamId": argv.get("--TeamId"),
        "TeamMembers": Utils.try_to_json(argv, "--TeamMembers"),
        "Operator": argv.get("--Operator"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CmeClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.AddTeamMemberRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.AddTeamMember(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doMoveClass(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("MoveClass", g_param[OptionsDefine.Version])
        return

    param = {
        "Platform": argv.get("--Platform"),
        "Owner": Utils.try_to_json(argv, "--Owner"),
        "SourceClassPath": argv.get("--SourceClassPath"),
        "DestinationClassPath": argv.get("--DestinationClassPath"),
        "Operator": argv.get("--Operator"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CmeClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.MoveClassRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.MoveClass(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyTeamMember(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyTeamMember", g_param[OptionsDefine.Version])
        return

    param = {
        "Platform": argv.get("--Platform"),
        "TeamId": argv.get("--TeamId"),
        "MemberId": argv.get("--MemberId"),
        "Remark": argv.get("--Remark"),
        "Role": argv.get("--Role"),
        "Operator": argv.get("--Operator"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CmeClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyTeamMemberRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyTeamMember(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteTeamMembers(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteTeamMembers", g_param[OptionsDefine.Version])
        return

    param = {
        "Platform": argv.get("--Platform"),
        "TeamId": argv.get("--TeamId"),
        "MemberIds": Utils.try_to_json(argv, "--MemberIds"),
        "Operator": argv.get("--Operator"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CmeClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteTeamMembersRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeleteTeamMembers(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteLoginStatus(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteLoginStatus", g_param[OptionsDefine.Version])
        return

    param = {
        "Platform": argv.get("--Platform"),
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
    client = mod.CmeClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteLoginStatusRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeleteLoginStatus(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeProjects(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeProjects", g_param[OptionsDefine.Version])
        return

    param = {
        "Platform": argv.get("--Platform"),
        "ProjectIds": Utils.try_to_json(argv, "--ProjectIds"),
        "AspectRatioSet": Utils.try_to_json(argv, "--AspectRatioSet"),
        "CategorySet": Utils.try_to_json(argv, "--CategorySet"),
        "Sort": Utils.try_to_json(argv, "--Sort"),
        "Owner": Utils.try_to_json(argv, "--Owner"),
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
    client = mod.CmeClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeProjectsRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeProjects(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeLoginStatus(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeLoginStatus", g_param[OptionsDefine.Version])
        return

    param = {
        "Platform": argv.get("--Platform"),
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
    client = mod.CmeClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeLoginStatusRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeLoginStatus(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeTasks(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeTasks", g_param[OptionsDefine.Version])
        return

    param = {
        "Platform": argv.get("--Platform"),
        "ProjectId": argv.get("--ProjectId"),
        "TaskTypeSet": Utils.try_to_json(argv, "--TaskTypeSet"),
        "StatusSet": Utils.try_to_json(argv, "--StatusSet"),
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
    client = mod.CmeClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeTasksRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeTasks(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeClass(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeClass", g_param[OptionsDefine.Version])
        return

    param = {
        "Platform": argv.get("--Platform"),
        "Owner": Utils.try_to_json(argv, "--Owner"),
        "Operator": argv.get("--Operator"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CmeClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeClassRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeClass(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateTeam(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateTeam", g_param[OptionsDefine.Version])
        return

    param = {
        "Platform": argv.get("--Platform"),
        "Name": argv.get("--Name"),
        "OwnerId": argv.get("--OwnerId"),
        "OwnerRemark": argv.get("--OwnerRemark"),
        "TeamId": argv.get("--TeamId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CmeClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateTeamRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateTeam(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyProject(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyProject", g_param[OptionsDefine.Version])
        return

    param = {
        "Platform": argv.get("--Platform"),
        "ProjectId": argv.get("--ProjectId"),
        "Name": argv.get("--Name"),
        "AspectRatio": argv.get("--AspectRatio"),
        "Owner": Utils.try_to_json(argv, "--Owner"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CmeClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyProjectRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyProject(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateClass(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateClass", g_param[OptionsDefine.Version])
        return

    param = {
        "Platform": argv.get("--Platform"),
        "Owner": Utils.try_to_json(argv, "--Owner"),
        "ClassPath": argv.get("--ClassPath"),
        "Operator": argv.get("--Operator"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CmeClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateClassRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateClass(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doImportMediaToProject(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ImportMediaToProject", g_param[OptionsDefine.Version])
        return

    param = {
        "Platform": argv.get("--Platform"),
        "ProjectId": argv.get("--ProjectId"),
        "VodFileId": argv.get("--VodFileId"),
        "Name": argv.get("--Name"),
        "PreProcessDefinition": Utils.try_to_json(argv, "--PreProcessDefinition"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CmeClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ImportMediaToProjectRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ImportMediaToProject(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doListMedia(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ListMedia", g_param[OptionsDefine.Version])
        return

    param = {
        "Platform": argv.get("--Platform"),
        "ClassPath": argv.get("--ClassPath"),
        "Owner": Utils.try_to_json(argv, "--Owner"),
        "Offset": Utils.try_to_json(argv, "--Offset"),
        "Limit": Utils.try_to_json(argv, "--Limit"),
        "Operator": argv.get("--Operator"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CmeClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ListMediaRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ListMedia(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateProject(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateProject", g_param[OptionsDefine.Version])
        return

    param = {
        "Platform": argv.get("--Platform"),
        "Category": argv.get("--Category"),
        "Name": argv.get("--Name"),
        "AspectRatio": argv.get("--AspectRatio"),
        "Owner": Utils.try_to_json(argv, "--Owner"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CmeClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateProjectRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateProject(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteClass(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteClass", g_param[OptionsDefine.Version])
        return

    param = {
        "Platform": argv.get("--Platform"),
        "Owner": Utils.try_to_json(argv, "--Owner"),
        "ClassPath": argv.get("--ClassPath"),
        "Operator": argv.get("--Operator"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CmeClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteClassRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeleteClass(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteProject(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteProject", g_param[OptionsDefine.Version])
        return

    param = {
        "Platform": argv.get("--Platform"),
        "ProjectId": argv.get("--ProjectId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CmeClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteProjectRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeleteProject(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doFlattenListMedia(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("FlattenListMedia", g_param[OptionsDefine.Version])
        return

    param = {
        "Platform": argv.get("--Platform"),
        "ClassPath": argv.get("--ClassPath"),
        "Owner": Utils.try_to_json(argv, "--Owner"),
        "Offset": Utils.try_to_json(argv, "--Offset"),
        "Limit": Utils.try_to_json(argv, "--Limit"),
        "Operator": argv.get("--Operator"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CmeClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.FlattenListMediaRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.FlattenListMedia(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeTeamMembers(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeTeamMembers", g_param[OptionsDefine.Version])
        return

    param = {
        "Platform": argv.get("--Platform"),
        "TeamId": argv.get("--TeamId"),
        "MemberIds": Utils.try_to_json(argv, "--MemberIds"),
        "Offset": Utils.try_to_json(argv, "--Offset"),
        "Limit": Utils.try_to_json(argv, "--Limit"),
        "Operator": argv.get("--Operator"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CmeClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeTeamMembersRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeTeamMembers(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


CLIENT_MAP = {
    "v20191029": cme_client_v20191029,

}

MODELS_MAP = {
    "v20191029": models_v20191029,

}

ACTION_MAP = {
    "DescribeMaterials": doDescribeMaterials,
    "DescribeTeams": doDescribeTeams,
    "ExportVideoEditProject": doExportVideoEditProject,
    "DescribeSharedSpace": doDescribeSharedSpace,
    "GrantResourceAuthorization": doGrantResourceAuthorization,
    "SearchMaterial": doSearchMaterial,
    "RevokeResourceAuthorization": doRevokeResourceAuthorization,
    "DescribeJoinTeams": doDescribeJoinTeams,
    "DescribeResourceAuthorization": doDescribeResourceAuthorization,
    "ImportMaterial": doImportMaterial,
    "ExportVideoByEditorTrackData": doExportVideoByEditorTrackData,
    "DescribeTaskDetail": doDescribeTaskDetail,
    "CreateLink": doCreateLink,
    "ModifyTeam": doModifyTeam,
    "DeleteMaterial": doDeleteMaterial,
    "ModifyMaterial": doModifyMaterial,
    "DeleteTeam": doDeleteTeam,
    "AddTeamMember": doAddTeamMember,
    "MoveClass": doMoveClass,
    "ModifyTeamMember": doModifyTeamMember,
    "DeleteTeamMembers": doDeleteTeamMembers,
    "DeleteLoginStatus": doDeleteLoginStatus,
    "DescribeProjects": doDescribeProjects,
    "DescribeLoginStatus": doDescribeLoginStatus,
    "DescribeTasks": doDescribeTasks,
    "DescribeClass": doDescribeClass,
    "CreateTeam": doCreateTeam,
    "ModifyProject": doModifyProject,
    "CreateClass": doCreateClass,
    "ImportMediaToProject": doImportMediaToProject,
    "ListMedia": doListMedia,
    "CreateProject": doCreateProject,
    "DeleteClass": doDeleteClass,
    "DeleteProject": doDeleteProject,
    "FlattenListMedia": doFlattenListMedia,
    "DescribeTeamMembers": doDescribeTeamMembers,

}

AVAILABLE_VERSION_LIST = [
    v20191029.version,

]
AVAILABLE_VERSIONS = {
     'v' + v20191029.version.replace('-', ''): {"help": v20191029_help.INFO,"desc": v20191029_help.DESC},

}


def cme_action(argv, arglist):
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
        helpstr = HelpTemplate.SERVICE % {"name": "cme", "desc": desc, "actions": action_str}
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
    cmd = NiceCommand("cme", cme_action)
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
            version = config["cme"][OptionsDefine.Version]
            params[OptionsDefine.Version] = "v" + version.replace('-', '')

        if params[OptionsDefine.Endpoint] is None:
            params[OptionsDefine.Endpoint] = config["cme"][OptionsDefine.Endpoint]
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

    helpmsg = HelpTemplate.ACTION % {"name": action, "service": "cme", "desc": desc, "params": docstr}
    print(helpmsg)


def get_actions_info():
    config = Configure()
    new_version = max(AVAILABLE_VERSIONS.keys())
    version = new_version
    try:
        profile = config._load_json_msg(os.path.join(config.cli_path, "default.configure"))
        version = profile["cme"]["version"]
        version = "v" + version.replace('-', '')
    except Exception:
        pass
    if version not in AVAILABLE_VERSIONS.keys():
        version = new_version
    return AVAILABLE_VERSIONS[version]["help"]
