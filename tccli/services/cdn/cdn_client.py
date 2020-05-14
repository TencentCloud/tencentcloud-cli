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
from tencentcloud.cdn.v20180606 import cdn_client as cdn_client_v20180606
from tencentcloud.cdn.v20180606 import models as models_v20180606
from tccli.services.cdn import v20180606
from tccli.services.cdn.v20180606 import help as v20180606_help


def doDescribeIpStatus(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeIpStatus", g_param[OptionsDefine.Version])
        return

    param = {
        "Domain": argv.get("--Domain"),
        "Layer": argv.get("--Layer"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CdnClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeIpStatusRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeIpStatus(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeMapInfo(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeMapInfo", g_param[OptionsDefine.Version])
        return

    param = {
        "Name": argv.get("--Name"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CdnClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeMapInfoRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeMapInfo(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteCdnDomain(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteCdnDomain", g_param[OptionsDefine.Version])
        return

    param = {
        "Domain": argv.get("--Domain"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CdnClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteCdnDomainRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeleteCdnDomain(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribePurgeTasks(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribePurgeTasks", g_param[OptionsDefine.Version])
        return

    param = {
        "PurgeType": argv.get("--PurgeType"),
        "StartTime": argv.get("--StartTime"),
        "EndTime": argv.get("--EndTime"),
        "TaskId": argv.get("--TaskId"),
        "Offset": Utils.try_to_json(argv, "--Offset"),
        "Limit": Utils.try_to_json(argv, "--Limit"),
        "Keyword": argv.get("--Keyword"),
        "Status": argv.get("--Status"),
        "Area": argv.get("--Area"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CdnClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribePurgeTasksRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribePurgeTasks(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribePayType(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribePayType", g_param[OptionsDefine.Version])
        return

    param = {
        "Area": argv.get("--Area"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CdnClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribePayTypeRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribePayType(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeDomainsConfig(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeDomainsConfig", g_param[OptionsDefine.Version])
        return

    param = {
        "Offset": Utils.try_to_json(argv, "--Offset"),
        "Limit": Utils.try_to_json(argv, "--Limit"),
        "Filters": Utils.try_to_json(argv, "--Filters"),
        "Sort": Utils.try_to_json(argv, "--Sort"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CdnClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeDomainsConfigRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeDomainsConfig(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doAddCdnDomain(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("AddCdnDomain", g_param[OptionsDefine.Version])
        return

    param = {
        "Domain": argv.get("--Domain"),
        "ServiceType": argv.get("--ServiceType"),
        "Origin": Utils.try_to_json(argv, "--Origin"),
        "ProjectId": Utils.try_to_json(argv, "--ProjectId"),
        "IpFilter": Utils.try_to_json(argv, "--IpFilter"),
        "IpFreqLimit": Utils.try_to_json(argv, "--IpFreqLimit"),
        "StatusCodeCache": Utils.try_to_json(argv, "--StatusCodeCache"),
        "Compression": Utils.try_to_json(argv, "--Compression"),
        "BandwidthAlert": Utils.try_to_json(argv, "--BandwidthAlert"),
        "RangeOriginPull": Utils.try_to_json(argv, "--RangeOriginPull"),
        "FollowRedirect": Utils.try_to_json(argv, "--FollowRedirect"),
        "ErrorPage": Utils.try_to_json(argv, "--ErrorPage"),
        "RequestHeader": Utils.try_to_json(argv, "--RequestHeader"),
        "ResponseHeader": Utils.try_to_json(argv, "--ResponseHeader"),
        "DownstreamCapping": Utils.try_to_json(argv, "--DownstreamCapping"),
        "CacheKey": Utils.try_to_json(argv, "--CacheKey"),
        "ResponseHeaderCache": Utils.try_to_json(argv, "--ResponseHeaderCache"),
        "VideoSeek": Utils.try_to_json(argv, "--VideoSeek"),
        "Cache": Utils.try_to_json(argv, "--Cache"),
        "OriginPullOptimization": Utils.try_to_json(argv, "--OriginPullOptimization"),
        "Https": Utils.try_to_json(argv, "--Https"),
        "Authentication": Utils.try_to_json(argv, "--Authentication"),
        "Seo": Utils.try_to_json(argv, "--Seo"),
        "ForceRedirect": Utils.try_to_json(argv, "--ForceRedirect"),
        "Referer": Utils.try_to_json(argv, "--Referer"),
        "MaxAge": Utils.try_to_json(argv, "--MaxAge"),
        "Ipv6": Utils.try_to_json(argv, "--Ipv6"),
        "SpecificConfig": Utils.try_to_json(argv, "--SpecificConfig"),
        "Area": argv.get("--Area"),
        "OriginPullTimeout": Utils.try_to_json(argv, "--OriginPullTimeout"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CdnClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.AddCdnDomainRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.AddCdnDomain(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeIpVisit(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeIpVisit", g_param[OptionsDefine.Version])
        return

    param = {
        "StartTime": argv.get("--StartTime"),
        "EndTime": argv.get("--EndTime"),
        "Domains": Utils.try_to_json(argv, "--Domains"),
        "Project": Utils.try_to_json(argv, "--Project"),
        "Interval": argv.get("--Interval"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CdnClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeIpVisitRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeIpVisit(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeCdnData(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeCdnData", g_param[OptionsDefine.Version])
        return

    param = {
        "StartTime": argv.get("--StartTime"),
        "EndTime": argv.get("--EndTime"),
        "Metric": argv.get("--Metric"),
        "Domains": Utils.try_to_json(argv, "--Domains"),
        "Project": Utils.try_to_json(argv, "--Project"),
        "Interval": argv.get("--Interval"),
        "Detail": Utils.try_to_json(argv, "--Detail"),
        "Isp": Utils.try_to_json(argv, "--Isp"),
        "District": Utils.try_to_json(argv, "--District"),
        "Protocol": argv.get("--Protocol"),
        "DataSource": argv.get("--DataSource"),
        "IpProtocol": argv.get("--IpProtocol"),
        "Area": argv.get("--Area"),
        "AreaType": argv.get("--AreaType"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CdnClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeCdnDataRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeCdnData(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDisableCaches(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DisableCaches", g_param[OptionsDefine.Version])
        return

    param = {
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
    client = mod.CdnClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DisableCachesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DisableCaches(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeDomains(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeDomains", g_param[OptionsDefine.Version])
        return

    param = {
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
    client = mod.CdnClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeDomainsRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeDomains(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doManageClsTopicDomains(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ManageClsTopicDomains", g_param[OptionsDefine.Version])
        return

    param = {
        "LogsetId": argv.get("--LogsetId"),
        "TopicId": argv.get("--TopicId"),
        "Channel": argv.get("--Channel"),
        "DomainAreaConfigs": Utils.try_to_json(argv, "--DomainAreaConfigs"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CdnClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ManageClsTopicDomainsRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ManageClsTopicDomains(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doStartCdnDomain(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("StartCdnDomain", g_param[OptionsDefine.Version])
        return

    param = {
        "Domain": argv.get("--Domain"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CdnClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.StartCdnDomainRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.StartCdnDomain(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doStopCdnDomain(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("StopCdnDomain", g_param[OptionsDefine.Version])
        return

    param = {
        "Domain": argv.get("--Domain"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CdnClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.StopCdnDomainRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.StopCdnDomain(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribePurgeQuota(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribePurgeQuota", g_param[OptionsDefine.Version])
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
    client = mod.CdnClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribePurgeQuotaRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribePurgeQuota(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeImageConfig(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeImageConfig", g_param[OptionsDefine.Version])
        return

    param = {
        "Domain": argv.get("--Domain"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CdnClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeImageConfigRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeImageConfig(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doSearchClsLog(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("SearchClsLog", g_param[OptionsDefine.Version])
        return

    param = {
        "LogsetId": argv.get("--LogsetId"),
        "TopicIds": argv.get("--TopicIds"),
        "StartTime": argv.get("--StartTime"),
        "EndTime": argv.get("--EndTime"),
        "Limit": Utils.try_to_json(argv, "--Limit"),
        "Channel": argv.get("--Channel"),
        "Query": argv.get("--Query"),
        "Context": argv.get("--Context"),
        "Sort": argv.get("--Sort"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CdnClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.SearchClsLogRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.SearchClsLog(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doListTopData(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ListTopData", g_param[OptionsDefine.Version])
        return

    param = {
        "StartTime": argv.get("--StartTime"),
        "EndTime": argv.get("--EndTime"),
        "Metric": argv.get("--Metric"),
        "Filter": argv.get("--Filter"),
        "Domains": Utils.try_to_json(argv, "--Domains"),
        "Project": Utils.try_to_json(argv, "--Project"),
        "Detail": Utils.try_to_json(argv, "--Detail"),
        "Code": argv.get("--Code"),
        "Area": argv.get("--Area"),
        "AreaType": argv.get("--AreaType"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CdnClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ListTopDataRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ListTopData(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeOriginData(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeOriginData", g_param[OptionsDefine.Version])
        return

    param = {
        "StartTime": argv.get("--StartTime"),
        "EndTime": argv.get("--EndTime"),
        "Metric": argv.get("--Metric"),
        "Domains": Utils.try_to_json(argv, "--Domains"),
        "Project": Utils.try_to_json(argv, "--Project"),
        "Interval": argv.get("--Interval"),
        "Detail": Utils.try_to_json(argv, "--Detail"),
        "Area": argv.get("--Area"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CdnClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeOriginDataRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeOriginData(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeCdnIp(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeCdnIp", g_param[OptionsDefine.Version])
        return

    param = {
        "Ips": Utils.try_to_json(argv, "--Ips"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CdnClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeCdnIpRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeCdnIp(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doPurgePathCache(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("PurgePathCache", g_param[OptionsDefine.Version])
        return

    param = {
        "Paths": Utils.try_to_json(argv, "--Paths"),
        "FlushType": argv.get("--FlushType"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CdnClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.PurgePathCacheRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.PurgePathCache(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeUrlViolations(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeUrlViolations", g_param[OptionsDefine.Version])
        return

    param = {
        "Offset": Utils.try_to_json(argv, "--Offset"),
        "Limit": Utils.try_to_json(argv, "--Limit"),
        "Domains": Utils.try_to_json(argv, "--Domains"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CdnClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeUrlViolationsRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeUrlViolations(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doPurgeUrlsCache(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("PurgeUrlsCache", g_param[OptionsDefine.Version])
        return

    param = {
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
    client = mod.CdnClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.PurgeUrlsCacheRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.PurgeUrlsCache(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeTrafficPackages(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeTrafficPackages", g_param[OptionsDefine.Version])
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
    client = mod.CdnClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeTrafficPackagesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeTrafficPackages(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doUpdateDomainConfig(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("UpdateDomainConfig", g_param[OptionsDefine.Version])
        return

    param = {
        "Domain": argv.get("--Domain"),
        "ProjectId": Utils.try_to_json(argv, "--ProjectId"),
        "Origin": Utils.try_to_json(argv, "--Origin"),
        "IpFilter": Utils.try_to_json(argv, "--IpFilter"),
        "IpFreqLimit": Utils.try_to_json(argv, "--IpFreqLimit"),
        "StatusCodeCache": Utils.try_to_json(argv, "--StatusCodeCache"),
        "Compression": Utils.try_to_json(argv, "--Compression"),
        "BandwidthAlert": Utils.try_to_json(argv, "--BandwidthAlert"),
        "RangeOriginPull": Utils.try_to_json(argv, "--RangeOriginPull"),
        "FollowRedirect": Utils.try_to_json(argv, "--FollowRedirect"),
        "ErrorPage": Utils.try_to_json(argv, "--ErrorPage"),
        "RequestHeader": Utils.try_to_json(argv, "--RequestHeader"),
        "ResponseHeader": Utils.try_to_json(argv, "--ResponseHeader"),
        "DownstreamCapping": Utils.try_to_json(argv, "--DownstreamCapping"),
        "CacheKey": Utils.try_to_json(argv, "--CacheKey"),
        "ResponseHeaderCache": Utils.try_to_json(argv, "--ResponseHeaderCache"),
        "VideoSeek": Utils.try_to_json(argv, "--VideoSeek"),
        "Cache": Utils.try_to_json(argv, "--Cache"),
        "OriginPullOptimization": Utils.try_to_json(argv, "--OriginPullOptimization"),
        "Https": Utils.try_to_json(argv, "--Https"),
        "Authentication": Utils.try_to_json(argv, "--Authentication"),
        "Seo": Utils.try_to_json(argv, "--Seo"),
        "ForceRedirect": Utils.try_to_json(argv, "--ForceRedirect"),
        "Referer": Utils.try_to_json(argv, "--Referer"),
        "MaxAge": Utils.try_to_json(argv, "--MaxAge"),
        "ServiceType": argv.get("--ServiceType"),
        "SpecificConfig": Utils.try_to_json(argv, "--SpecificConfig"),
        "Area": argv.get("--Area"),
        "OriginPullTimeout": Utils.try_to_json(argv, "--OriginPullTimeout"),
        "AwsPrivateAccess": Utils.try_to_json(argv, "--AwsPrivateAccess"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CdnClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.UpdateDomainConfigRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.UpdateDomainConfig(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeCdnDomainLogs(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeCdnDomainLogs", g_param[OptionsDefine.Version])
        return

    param = {
        "Domain": argv.get("--Domain"),
        "StartTime": argv.get("--StartTime"),
        "EndTime": argv.get("--EndTime"),
        "Offset": Utils.try_to_json(argv, "--Offset"),
        "Limit": Utils.try_to_json(argv, "--Limit"),
        "Area": argv.get("--Area"),
        "LogType": argv.get("--LogType"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CdnClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeCdnDomainLogsRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeCdnDomainLogs(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribePushTasks(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribePushTasks", g_param[OptionsDefine.Version])
        return

    param = {
        "StartTime": argv.get("--StartTime"),
        "EndTime": argv.get("--EndTime"),
        "TaskId": argv.get("--TaskId"),
        "Keyword": argv.get("--Keyword"),
        "Offset": Utils.try_to_json(argv, "--Offset"),
        "Limit": Utils.try_to_json(argv, "--Limit"),
        "Area": argv.get("--Area"),
        "Status": argv.get("--Status"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CdnClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribePushTasksRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribePushTasks(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeCertDomains(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeCertDomains", g_param[OptionsDefine.Version])
        return

    param = {
        "Cert": argv.get("--Cert"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CdnClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeCertDomainsRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeCertDomains(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateClsLogTopic(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateClsLogTopic", g_param[OptionsDefine.Version])
        return

    param = {
        "TopicName": argv.get("--TopicName"),
        "LogsetId": argv.get("--LogsetId"),
        "Channel": argv.get("--Channel"),
        "DomainAreaConfigs": Utils.try_to_json(argv, "--DomainAreaConfigs"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CdnClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateClsLogTopicRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateClsLogTopic(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doPushUrlsCache(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("PushUrlsCache", g_param[OptionsDefine.Version])
        return

    param = {
        "Urls": Utils.try_to_json(argv, "--Urls"),
        "UserAgent": argv.get("--UserAgent"),
        "Area": argv.get("--Area"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CdnClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.PushUrlsCacheRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.PushUrlsCache(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doUpdateImageConfig(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("UpdateImageConfig", g_param[OptionsDefine.Version])
        return

    param = {
        "Domain": argv.get("--Domain"),
        "WebpAdapter": Utils.try_to_json(argv, "--WebpAdapter"),
        "TpgAdapter": Utils.try_to_json(argv, "--TpgAdapter"),
        "GuetzliAdapter": Utils.try_to_json(argv, "--GuetzliAdapter"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CdnClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.UpdateImageConfigRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.UpdateImageConfig(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDisableClsLogTopic(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DisableClsLogTopic", g_param[OptionsDefine.Version])
        return

    param = {
        "LogsetId": argv.get("--LogsetId"),
        "TopicId": argv.get("--TopicId"),
        "Channel": argv.get("--Channel"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CdnClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DisableClsLogTopicRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DisableClsLogTopic(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doListClsTopicDomains(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ListClsTopicDomains", g_param[OptionsDefine.Version])
        return

    param = {
        "LogsetId": argv.get("--LogsetId"),
        "TopicId": argv.get("--TopicId"),
        "Channel": argv.get("--Channel"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CdnClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ListClsTopicDomainsRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ListClsTopicDomains(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doListClsLogTopics(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ListClsLogTopics", g_param[OptionsDefine.Version])
        return

    param = {
        "Channel": argv.get("--Channel"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CdnClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ListClsLogTopicsRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ListClsLogTopics(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doGetDisableRecords(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("GetDisableRecords", g_param[OptionsDefine.Version])
        return

    param = {
        "StartTime": argv.get("--StartTime"),
        "EndTime": argv.get("--EndTime"),
        "Url": argv.get("--Url"),
        "Status": argv.get("--Status"),
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
    client = mod.CdnClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.GetDisableRecordsRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.GetDisableRecords(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteClsLogTopic(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteClsLogTopic", g_param[OptionsDefine.Version])
        return

    param = {
        "TopicId": argv.get("--TopicId"),
        "LogsetId": argv.get("--LogsetId"),
        "Channel": argv.get("--Channel"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CdnClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteClsLogTopicRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeleteClsLogTopic(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeBillingData(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeBillingData", g_param[OptionsDefine.Version])
        return

    param = {
        "StartTime": argv.get("--StartTime"),
        "EndTime": argv.get("--EndTime"),
        "Interval": argv.get("--Interval"),
        "Domain": argv.get("--Domain"),
        "Project": Utils.try_to_json(argv, "--Project"),
        "Area": argv.get("--Area"),
        "District": Utils.try_to_json(argv, "--District"),
        "Metric": argv.get("--Metric"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CdnClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeBillingDataRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeBillingData(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribePushQuota(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribePushQuota", g_param[OptionsDefine.Version])
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
    client = mod.CdnClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribePushQuotaRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribePushQuota(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doEnableClsLogTopic(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("EnableClsLogTopic", g_param[OptionsDefine.Version])
        return

    param = {
        "LogsetId": argv.get("--LogsetId"),
        "TopicId": argv.get("--TopicId"),
        "Channel": argv.get("--Channel"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CdnClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.EnableClsLogTopicRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.EnableClsLogTopic(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeReportData(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeReportData", g_param[OptionsDefine.Version])
        return

    param = {
        "StartTime": argv.get("--StartTime"),
        "EndTime": argv.get("--EndTime"),
        "ReportType": argv.get("--ReportType"),
        "Area": argv.get("--Area"),
        "Offset": Utils.try_to_json(argv, "--Offset"),
        "Limit": Utils.try_to_json(argv, "--Limit"),
        "Project": Utils.try_to_json(argv, "--Project"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CdnClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeReportDataRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeReportData(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doUpdatePayType(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("UpdatePayType", g_param[OptionsDefine.Version])
        return

    param = {
        "Area": argv.get("--Area"),
        "PayType": argv.get("--PayType"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CdnClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.UpdatePayTypeRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.UpdatePayType(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doEnableCaches(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("EnableCaches", g_param[OptionsDefine.Version])
        return

    param = {
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
    client = mod.CdnClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.EnableCachesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.EnableCaches(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


CLIENT_MAP = {
    "v20180606": cdn_client_v20180606,

}

MODELS_MAP = {
    "v20180606": models_v20180606,

}

ACTION_MAP = {
    "DescribeIpStatus": doDescribeIpStatus,
    "DescribeMapInfo": doDescribeMapInfo,
    "DeleteCdnDomain": doDeleteCdnDomain,
    "DescribePurgeTasks": doDescribePurgeTasks,
    "DescribePayType": doDescribePayType,
    "DescribeDomainsConfig": doDescribeDomainsConfig,
    "AddCdnDomain": doAddCdnDomain,
    "DescribeIpVisit": doDescribeIpVisit,
    "DescribeCdnData": doDescribeCdnData,
    "DisableCaches": doDisableCaches,
    "DescribeDomains": doDescribeDomains,
    "ManageClsTopicDomains": doManageClsTopicDomains,
    "StartCdnDomain": doStartCdnDomain,
    "StopCdnDomain": doStopCdnDomain,
    "DescribePurgeQuota": doDescribePurgeQuota,
    "DescribeImageConfig": doDescribeImageConfig,
    "SearchClsLog": doSearchClsLog,
    "ListTopData": doListTopData,
    "DescribeOriginData": doDescribeOriginData,
    "DescribeCdnIp": doDescribeCdnIp,
    "PurgePathCache": doPurgePathCache,
    "DescribeUrlViolations": doDescribeUrlViolations,
    "PurgeUrlsCache": doPurgeUrlsCache,
    "DescribeTrafficPackages": doDescribeTrafficPackages,
    "UpdateDomainConfig": doUpdateDomainConfig,
    "DescribeCdnDomainLogs": doDescribeCdnDomainLogs,
    "DescribePushTasks": doDescribePushTasks,
    "DescribeCertDomains": doDescribeCertDomains,
    "CreateClsLogTopic": doCreateClsLogTopic,
    "PushUrlsCache": doPushUrlsCache,
    "UpdateImageConfig": doUpdateImageConfig,
    "DisableClsLogTopic": doDisableClsLogTopic,
    "ListClsTopicDomains": doListClsTopicDomains,
    "ListClsLogTopics": doListClsLogTopics,
    "GetDisableRecords": doGetDisableRecords,
    "DeleteClsLogTopic": doDeleteClsLogTopic,
    "DescribeBillingData": doDescribeBillingData,
    "DescribePushQuota": doDescribePushQuota,
    "EnableClsLogTopic": doEnableClsLogTopic,
    "DescribeReportData": doDescribeReportData,
    "UpdatePayType": doUpdatePayType,
    "EnableCaches": doEnableCaches,

}

AVAILABLE_VERSION_LIST = [
    v20180606.version,

]
AVAILABLE_VERSIONS = {
     'v' + v20180606.version.replace('-', ''): {"help": v20180606_help.INFO,"desc": v20180606_help.DESC},

}


def cdn_action(argv, arglist):
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
        helpstr = HelpTemplate.SERVICE % {"name": "cdn", "desc": desc, "actions": action_str}
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
    cmd = NiceCommand("cdn", cdn_action)
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
            version = config["cdn"][OptionsDefine.Version]
            params[OptionsDefine.Version] = "v" + version.replace('-', '')

        if params[OptionsDefine.Endpoint] is None:
            params[OptionsDefine.Endpoint] = config["cdn"][OptionsDefine.Endpoint]
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

    helpmsg = HelpTemplate.ACTION % {"name": action, "service": "cdn", "desc": desc, "params": docstr}
    print(helpmsg)


def get_actions_info():
    config = Configure()
    new_version = max(AVAILABLE_VERSIONS.keys())
    version = new_version
    try:
        profile = config._load_json_msg(os.path.join(config.cli_path, "default.configure"))
        version = profile["cdn"]["version"]
        version = "v" + version.replace('-', '')
    except Exception:
        pass
    if version not in AVAILABLE_VERSIONS.keys():
        version = new_version
    return AVAILABLE_VERSIONS[version]["help"]
