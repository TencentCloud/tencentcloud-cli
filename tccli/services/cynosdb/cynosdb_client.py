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
from tencentcloud.cynosdb.v20190107 import cynosdb_client as cynosdb_client_v20190107
from tencentcloud.cynosdb.v20190107 import models as models_v20190107
from tccli.services.cynosdb import v20190107
from tccli.services.cynosdb.v20190107 import help as v20190107_help


def doModifyBackupConfig(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyBackupConfig", g_param[OptionsDefine.Version])
        return

    param = {
        "ClusterId": argv.get("--ClusterId"),
        "BackupTimeBeg": Utils.try_to_json(argv, "--BackupTimeBeg"),
        "BackupTimeEnd": Utils.try_to_json(argv, "--BackupTimeEnd"),
        "ReserveDuration": Utils.try_to_json(argv, "--ReserveDuration"),
        "BackupFreq": Utils.try_to_json(argv, "--BackupFreq"),
        "BackupType": argv.get("--BackupType"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile)
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CynosdbClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyBackupConfigRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyBackupConfig(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doSetRenewFlag(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("SetRenewFlag", g_param[OptionsDefine.Version])
        return

    param = {
        "ResourceIds": Utils.try_to_json(argv, "--ResourceIds"),
        "AutoRenewFlag": Utils.try_to_json(argv, "--AutoRenewFlag"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile)
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CynosdbClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.SetRenewFlagRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.SetRenewFlag(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doUpgradeInstance(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("UpgradeInstance", g_param[OptionsDefine.Version])
        return

    param = {
        "InstanceId": argv.get("--InstanceId"),
        "Cpu": Utils.try_to_json(argv, "--Cpu"),
        "Memory": Utils.try_to_json(argv, "--Memory"),
        "UpgradeType": argv.get("--UpgradeType"),
        "StorageLimit": Utils.try_to_json(argv, "--StorageLimit"),
        "AutoVoucher": Utils.try_to_json(argv, "--AutoVoucher"),
        "DbType": argv.get("--DbType"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile)
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CynosdbClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.UpgradeInstanceRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.UpgradeInstance(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateClusters(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateClusters", g_param[OptionsDefine.Version])
        return

    param = {
        "Zone": argv.get("--Zone"),
        "VpcId": argv.get("--VpcId"),
        "SubnetId": argv.get("--SubnetId"),
        "DbType": argv.get("--DbType"),
        "DbVersion": argv.get("--DbVersion"),
        "Cpu": Utils.try_to_json(argv, "--Cpu"),
        "Memory": Utils.try_to_json(argv, "--Memory"),
        "StorageLimit": Utils.try_to_json(argv, "--StorageLimit"),
        "ProjectId": Utils.try_to_json(argv, "--ProjectId"),
        "Storage": Utils.try_to_json(argv, "--Storage"),
        "ClusterName": argv.get("--ClusterName"),
        "AdminPassword": argv.get("--AdminPassword"),
        "Port": Utils.try_to_json(argv, "--Port"),
        "PayMode": Utils.try_to_json(argv, "--PayMode"),
        "Count": Utils.try_to_json(argv, "--Count"),
        "RollbackStrategy": argv.get("--RollbackStrategy"),
        "RollbackId": Utils.try_to_json(argv, "--RollbackId"),
        "OriginalClusterId": argv.get("--OriginalClusterId"),
        "ExpectTime": argv.get("--ExpectTime"),
        "ExpectTimeThresh": Utils.try_to_json(argv, "--ExpectTimeThresh"),
        "InstanceCount": Utils.try_to_json(argv, "--InstanceCount"),
        "TimeSpan": Utils.try_to_json(argv, "--TimeSpan"),
        "TimeUnit": argv.get("--TimeUnit"),
        "AutoRenewFlag": Utils.try_to_json(argv, "--AutoRenewFlag"),
        "AutoVoucher": Utils.try_to_json(argv, "--AutoVoucher"),
        "HaCount": Utils.try_to_json(argv, "--HaCount"),
        "OrderSource": argv.get("--OrderSource"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile)
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CynosdbClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateClustersRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateClusters(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doOfflineCluster(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("OfflineCluster", g_param[OptionsDefine.Version])
        return

    param = {
        "ClusterId": argv.get("--ClusterId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile)
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CynosdbClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.OfflineClusterRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.OfflineCluster(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doIsolateInstance(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("IsolateInstance", g_param[OptionsDefine.Version])
        return

    param = {
        "ClusterId": argv.get("--ClusterId"),
        "InstanceIdList": Utils.try_to_json(argv, "--InstanceIdList"),
        "DbType": argv.get("--DbType"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile)
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CynosdbClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.IsolateInstanceRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.IsolateInstance(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeRollbackTimeValidity(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeRollbackTimeValidity", g_param[OptionsDefine.Version])
        return

    param = {
        "ClusterId": argv.get("--ClusterId"),
        "ExpectTime": argv.get("--ExpectTime"),
        "ExpectTimeThresh": Utils.try_to_json(argv, "--ExpectTimeThresh"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile)
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CynosdbClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeRollbackTimeValidityRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeRollbackTimeValidity(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeInstanceSpecs(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeInstanceSpecs", g_param[OptionsDefine.Version])
        return

    param = {
        "DbType": argv.get("--DbType"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile)
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CynosdbClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeInstanceSpecsRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeInstanceSpecs(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeClusterDetail(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeClusterDetail", g_param[OptionsDefine.Version])
        return

    param = {
        "ClusterId": argv.get("--ClusterId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile)
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CynosdbClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeClusterDetailRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeClusterDetail(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyDBInstanceSecurityGroups(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyDBInstanceSecurityGroups", g_param[OptionsDefine.Version])
        return

    param = {
        "InstanceId": argv.get("--InstanceId"),
        "SecurityGroupIds": Utils.try_to_json(argv, "--SecurityGroupIds"),
        "Zone": argv.get("--Zone"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile)
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CynosdbClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyDBInstanceSecurityGroupsRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyDBInstanceSecurityGroups(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doIsolateCluster(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("IsolateCluster", g_param[OptionsDefine.Version])
        return

    param = {
        "ClusterId": argv.get("--ClusterId"),
        "DbType": argv.get("--DbType"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile)
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CynosdbClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.IsolateClusterRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.IsolateCluster(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeBackupList(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeBackupList", g_param[OptionsDefine.Version])
        return

    param = {
        "ClusterId": argv.get("--ClusterId"),
        "Limit": Utils.try_to_json(argv, "--Limit"),
        "Offset": Utils.try_to_json(argv, "--Offset"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile)
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CynosdbClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeBackupListRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeBackupList(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeMaintainPeriod(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeMaintainPeriod", g_param[OptionsDefine.Version])
        return

    param = {
        "InstanceId": argv.get("--InstanceId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile)
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CynosdbClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeMaintainPeriodRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeMaintainPeriod(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeBackupConfig(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeBackupConfig", g_param[OptionsDefine.Version])
        return

    param = {
        "ClusterId": argv.get("--ClusterId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile)
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CynosdbClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeBackupConfigRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeBackupConfig(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeClusters(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeClusters", g_param[OptionsDefine.Version])
        return

    param = {
        "DbType": argv.get("--DbType"),
        "Limit": Utils.try_to_json(argv, "--Limit"),
        "Offset": Utils.try_to_json(argv, "--Offset"),
        "OrderBy": argv.get("--OrderBy"),
        "OrderByType": argv.get("--OrderByType"),
        "Filters": Utils.try_to_json(argv, "--Filters"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile)
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CynosdbClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeClustersRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeClusters(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeAccounts(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeAccounts", g_param[OptionsDefine.Version])
        return

    param = {
        "ClusterId": argv.get("--ClusterId"),
        "AccountNames": Utils.try_to_json(argv, "--AccountNames"),
        "DbType": argv.get("--DbType"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile)
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CynosdbClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeAccountsRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeAccounts(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyMaintainPeriodConfig(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyMaintainPeriodConfig", g_param[OptionsDefine.Version])
        return

    param = {
        "InstanceId": argv.get("--InstanceId"),
        "MaintainStartTime": Utils.try_to_json(argv, "--MaintainStartTime"),
        "MaintainDuration": Utils.try_to_json(argv, "--MaintainDuration"),
        "MaintainWeekDays": Utils.try_to_json(argv, "--MaintainWeekDays"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile)
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CynosdbClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyMaintainPeriodConfigRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyMaintainPeriodConfig(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeRollbackTimeRange(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeRollbackTimeRange", g_param[OptionsDefine.Version])
        return

    param = {
        "ClusterId": argv.get("--ClusterId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile)
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CynosdbClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeRollbackTimeRangeRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeRollbackTimeRange(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doAddInstances(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("AddInstances", g_param[OptionsDefine.Version])
        return

    param = {
        "ClusterId": argv.get("--ClusterId"),
        "Cpu": Utils.try_to_json(argv, "--Cpu"),
        "Memory": Utils.try_to_json(argv, "--Memory"),
        "ReadOnlyCount": Utils.try_to_json(argv, "--ReadOnlyCount"),
        "InstanceGrpId": argv.get("--InstanceGrpId"),
        "VpcId": argv.get("--VpcId"),
        "SubnetId": argv.get("--SubnetId"),
        "Port": Utils.try_to_json(argv, "--Port"),
        "InstanceName": argv.get("--InstanceName"),
        "AutoVoucher": Utils.try_to_json(argv, "--AutoVoucher"),
        "DbType": argv.get("--DbType"),
        "OrderSource": argv.get("--OrderSource"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile)
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CynosdbClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.AddInstancesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.AddInstances(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


CLIENT_MAP = {
    "v20190107": cynosdb_client_v20190107,

}

MODELS_MAP = {
    "v20190107": models_v20190107,

}

ACTION_MAP = {
    "ModifyBackupConfig": doModifyBackupConfig,
    "SetRenewFlag": doSetRenewFlag,
    "UpgradeInstance": doUpgradeInstance,
    "CreateClusters": doCreateClusters,
    "OfflineCluster": doOfflineCluster,
    "IsolateInstance": doIsolateInstance,
    "DescribeRollbackTimeValidity": doDescribeRollbackTimeValidity,
    "DescribeInstanceSpecs": doDescribeInstanceSpecs,
    "DescribeClusterDetail": doDescribeClusterDetail,
    "ModifyDBInstanceSecurityGroups": doModifyDBInstanceSecurityGroups,
    "IsolateCluster": doIsolateCluster,
    "DescribeBackupList": doDescribeBackupList,
    "DescribeMaintainPeriod": doDescribeMaintainPeriod,
    "DescribeBackupConfig": doDescribeBackupConfig,
    "DescribeClusters": doDescribeClusters,
    "DescribeAccounts": doDescribeAccounts,
    "ModifyMaintainPeriodConfig": doModifyMaintainPeriodConfig,
    "DescribeRollbackTimeRange": doDescribeRollbackTimeRange,
    "AddInstances": doAddInstances,

}

AVAILABLE_VERSION_LIST = [
    v20190107.version,

]
AVAILABLE_VERSIONS = {
     'v' + v20190107.version.replace('-', ''): {"help": v20190107_help.INFO,"desc": v20190107_help.DESC},

}


def cynosdb_action(argv, arglist):
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
        helpstr = HelpTemplate.SERVICE % {"name": "cynosdb", "desc": desc, "actions": action_str}
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
    cmd = NiceCommand("cynosdb", cynosdb_action)
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
            version = config["cynosdb"][OptionsDefine.Version]
            params[OptionsDefine.Version] = "v" + version.replace('-', '')

        if params[OptionsDefine.Endpoint] is None:
            params[OptionsDefine.Endpoint] = config["cynosdb"][OptionsDefine.Endpoint]
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

    helpmsg = HelpTemplate.ACTION % {"name": action, "service": "cynosdb", "desc": desc, "params": docstr}
    print(helpmsg)


def get_actions_info():
    config = Configure()
    new_version = max(AVAILABLE_VERSIONS.keys())
    version = new_version
    try:
        profile = config._load_json_msg(os.path.join(config.cli_path, "default.configure"))
        version = profile["cynosdb"]["version"]
        version = "v" + version.replace('-', '')
    except Exception:
        pass
    if version not in AVAILABLE_VERSIONS.keys():
        version = new_version
    return AVAILABLE_VERSIONS[version]["help"]
