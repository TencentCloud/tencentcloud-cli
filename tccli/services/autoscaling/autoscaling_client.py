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
from tencentcloud.autoscaling.v20180419 import autoscaling_client as autoscaling_client_v20180419
from tencentcloud.autoscaling.v20180419 import models as models_v20180419
from tccli.services.autoscaling import v20180419
from tccli.services.autoscaling.v20180419 import help as v20180419_help


def doExecuteScalingPolicy(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ExecuteScalingPolicy", g_param[OptionsDefine.Version])
        return

    param = {
        "AutoScalingPolicyId": argv.get("--AutoScalingPolicyId"),
        "HonorCooldown": Utils.try_to_json(argv, "--HonorCooldown"),
        "TriggerSource": argv.get("--TriggerSource"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.AutoscalingClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ExecuteScalingPolicyRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ExecuteScalingPolicy(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateAutoScalingGroup(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateAutoScalingGroup", g_param[OptionsDefine.Version])
        return

    param = {
        "AutoScalingGroupName": argv.get("--AutoScalingGroupName"),
        "LaunchConfigurationId": argv.get("--LaunchConfigurationId"),
        "MaxSize": Utils.try_to_json(argv, "--MaxSize"),
        "MinSize": Utils.try_to_json(argv, "--MinSize"),
        "VpcId": argv.get("--VpcId"),
        "DefaultCooldown": Utils.try_to_json(argv, "--DefaultCooldown"),
        "DesiredCapacity": Utils.try_to_json(argv, "--DesiredCapacity"),
        "LoadBalancerIds": Utils.try_to_json(argv, "--LoadBalancerIds"),
        "ProjectId": Utils.try_to_json(argv, "--ProjectId"),
        "ForwardLoadBalancers": Utils.try_to_json(argv, "--ForwardLoadBalancers"),
        "SubnetIds": Utils.try_to_json(argv, "--SubnetIds"),
        "TerminationPolicies": Utils.try_to_json(argv, "--TerminationPolicies"),
        "Zones": Utils.try_to_json(argv, "--Zones"),
        "RetryPolicy": argv.get("--RetryPolicy"),
        "ZonesCheckPolicy": argv.get("--ZonesCheckPolicy"),
        "Tags": Utils.try_to_json(argv, "--Tags"),
        "ServiceSettings": Utils.try_to_json(argv, "--ServiceSettings"),
        "Ipv6AddressCount": Utils.try_to_json(argv, "--Ipv6AddressCount"),
        "MultiZoneSubnetPolicy": argv.get("--MultiZoneSubnetPolicy"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.AutoscalingClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateAutoScalingGroupRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateAutoScalingGroup(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doPreviewPaiDomainName(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("PreviewPaiDomainName", g_param[OptionsDefine.Version])
        return

    param = {
        "DomainNameType": argv.get("--DomainNameType"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.AutoscalingClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.PreviewPaiDomainNameRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.PreviewPaiDomainName(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyScalingPolicy(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyScalingPolicy", g_param[OptionsDefine.Version])
        return

    param = {
        "AutoScalingPolicyId": argv.get("--AutoScalingPolicyId"),
        "ScalingPolicyName": argv.get("--ScalingPolicyName"),
        "AdjustmentType": argv.get("--AdjustmentType"),
        "AdjustmentValue": Utils.try_to_json(argv, "--AdjustmentValue"),
        "Cooldown": Utils.try_to_json(argv, "--Cooldown"),
        "MetricAlarm": Utils.try_to_json(argv, "--MetricAlarm"),
        "NotificationUserGroupIds": Utils.try_to_json(argv, "--NotificationUserGroupIds"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.AutoscalingClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyScalingPolicyRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyScalingPolicy(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeNotificationConfigurations(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeNotificationConfigurations", g_param[OptionsDefine.Version])
        return

    param = {
        "AutoScalingNotificationIds": Utils.try_to_json(argv, "--AutoScalingNotificationIds"),
        "Filters": Utils.try_to_json(argv, "--Filters"),
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
    client = mod.AutoscalingClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeNotificationConfigurationsRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeNotificationConfigurations(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteAutoScalingGroup(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteAutoScalingGroup", g_param[OptionsDefine.Version])
        return

    param = {
        "AutoScalingGroupId": argv.get("--AutoScalingGroupId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.AutoscalingClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteAutoScalingGroupRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeleteAutoScalingGroup(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doStartAutoScalingInstances(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("StartAutoScalingInstances", g_param[OptionsDefine.Version])
        return

    param = {
        "AutoScalingGroupId": argv.get("--AutoScalingGroupId"),
        "InstanceIds": Utils.try_to_json(argv, "--InstanceIds"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.AutoscalingClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.StartAutoScalingInstancesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.StartAutoScalingInstances(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreatePaiInstance(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreatePaiInstance", g_param[OptionsDefine.Version])
        return

    param = {
        "DomainName": argv.get("--DomainName"),
        "InternetAccessible": Utils.try_to_json(argv, "--InternetAccessible"),
        "InitScript": argv.get("--InitScript"),
        "Zones": Utils.try_to_json(argv, "--Zones"),
        "VpcId": argv.get("--VpcId"),
        "SubnetIds": Utils.try_to_json(argv, "--SubnetIds"),
        "InstanceName": argv.get("--InstanceName"),
        "InstanceTypes": Utils.try_to_json(argv, "--InstanceTypes"),
        "LoginSettings": Utils.try_to_json(argv, "--LoginSettings"),
        "InstanceChargeType": argv.get("--InstanceChargeType"),
        "InstanceChargePrepaid": Utils.try_to_json(argv, "--InstanceChargePrepaid"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.AutoscalingClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreatePaiInstanceRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreatePaiInstance(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doUpgradeLaunchConfiguration(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("UpgradeLaunchConfiguration", g_param[OptionsDefine.Version])
        return

    param = {
        "LaunchConfigurationId": argv.get("--LaunchConfigurationId"),
        "ImageId": argv.get("--ImageId"),
        "InstanceTypes": Utils.try_to_json(argv, "--InstanceTypes"),
        "LaunchConfigurationName": argv.get("--LaunchConfigurationName"),
        "DataDisks": Utils.try_to_json(argv, "--DataDisks"),
        "EnhancedService": Utils.try_to_json(argv, "--EnhancedService"),
        "InstanceChargeType": argv.get("--InstanceChargeType"),
        "InstanceMarketOptions": Utils.try_to_json(argv, "--InstanceMarketOptions"),
        "InstanceTypesCheckPolicy": argv.get("--InstanceTypesCheckPolicy"),
        "InternetAccessible": Utils.try_to_json(argv, "--InternetAccessible"),
        "LoginSettings": Utils.try_to_json(argv, "--LoginSettings"),
        "ProjectId": Utils.try_to_json(argv, "--ProjectId"),
        "SecurityGroupIds": Utils.try_to_json(argv, "--SecurityGroupIds"),
        "SystemDisk": Utils.try_to_json(argv, "--SystemDisk"),
        "UserData": argv.get("--UserData"),
        "InstanceTags": Utils.try_to_json(argv, "--InstanceTags"),
        "CamRoleName": argv.get("--CamRoleName"),
        "HostNameSettings": Utils.try_to_json(argv, "--HostNameSettings"),
        "InstanceNameSettings": Utils.try_to_json(argv, "--InstanceNameSettings"),
        "InstanceChargePrepaid": Utils.try_to_json(argv, "--InstanceChargePrepaid"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.AutoscalingClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.UpgradeLaunchConfigurationRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.UpgradeLaunchConfiguration(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doAttachInstances(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("AttachInstances", g_param[OptionsDefine.Version])
        return

    param = {
        "AutoScalingGroupId": argv.get("--AutoScalingGroupId"),
        "InstanceIds": Utils.try_to_json(argv, "--InstanceIds"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.AutoscalingClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.AttachInstancesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.AttachInstances(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeScalingPolicies(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeScalingPolicies", g_param[OptionsDefine.Version])
        return

    param = {
        "AutoScalingPolicyIds": Utils.try_to_json(argv, "--AutoScalingPolicyIds"),
        "Filters": Utils.try_to_json(argv, "--Filters"),
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
    client = mod.AutoscalingClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeScalingPoliciesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeScalingPolicies(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteScheduledAction(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteScheduledAction", g_param[OptionsDefine.Version])
        return

    param = {
        "ScheduledActionId": argv.get("--ScheduledActionId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.AutoscalingClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteScheduledActionRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeleteScheduledAction(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDetachInstances(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DetachInstances", g_param[OptionsDefine.Version])
        return

    param = {
        "AutoScalingGroupId": argv.get("--AutoScalingGroupId"),
        "InstanceIds": Utils.try_to_json(argv, "--InstanceIds"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.AutoscalingClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DetachInstancesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DetachInstances(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateScheduledAction(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateScheduledAction", g_param[OptionsDefine.Version])
        return

    param = {
        "AutoScalingGroupId": argv.get("--AutoScalingGroupId"),
        "ScheduledActionName": argv.get("--ScheduledActionName"),
        "MaxSize": Utils.try_to_json(argv, "--MaxSize"),
        "MinSize": Utils.try_to_json(argv, "--MinSize"),
        "DesiredCapacity": Utils.try_to_json(argv, "--DesiredCapacity"),
        "StartTime": argv.get("--StartTime"),
        "EndTime": argv.get("--EndTime"),
        "Recurrence": argv.get("--Recurrence"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.AutoscalingClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateScheduledActionRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateScheduledAction(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doRemoveInstances(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("RemoveInstances", g_param[OptionsDefine.Version])
        return

    param = {
        "AutoScalingGroupId": argv.get("--AutoScalingGroupId"),
        "InstanceIds": Utils.try_to_json(argv, "--InstanceIds"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.AutoscalingClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.RemoveInstancesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.RemoveInstances(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteScalingPolicy(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteScalingPolicy", g_param[OptionsDefine.Version])
        return

    param = {
        "AutoScalingPolicyId": argv.get("--AutoScalingPolicyId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.AutoscalingClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteScalingPolicyRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeleteScalingPolicy(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCompleteLifecycleAction(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CompleteLifecycleAction", g_param[OptionsDefine.Version])
        return

    param = {
        "LifecycleHookId": argv.get("--LifecycleHookId"),
        "LifecycleActionResult": argv.get("--LifecycleActionResult"),
        "InstanceId": argv.get("--InstanceId"),
        "LifecycleActionToken": argv.get("--LifecycleActionToken"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.AutoscalingClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CompleteLifecycleActionRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CompleteLifecycleAction(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyLoadBalancers(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyLoadBalancers", g_param[OptionsDefine.Version])
        return

    param = {
        "AutoScalingGroupId": argv.get("--AutoScalingGroupId"),
        "LoadBalancerIds": Utils.try_to_json(argv, "--LoadBalancerIds"),
        "ForwardLoadBalancers": Utils.try_to_json(argv, "--ForwardLoadBalancers"),
        "LoadBalancersCheckPolicy": argv.get("--LoadBalancersCheckPolicy"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.AutoscalingClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyLoadBalancersRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyLoadBalancers(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyDesiredCapacity(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyDesiredCapacity", g_param[OptionsDefine.Version])
        return

    param = {
        "AutoScalingGroupId": argv.get("--AutoScalingGroupId"),
        "DesiredCapacity": Utils.try_to_json(argv, "--DesiredCapacity"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.AutoscalingClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyDesiredCapacityRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyDesiredCapacity(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doSetInstancesProtection(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("SetInstancesProtection", g_param[OptionsDefine.Version])
        return

    param = {
        "AutoScalingGroupId": argv.get("--AutoScalingGroupId"),
        "InstanceIds": Utils.try_to_json(argv, "--InstanceIds"),
        "ProtectedFromScaleIn": Utils.try_to_json(argv, "--ProtectedFromScaleIn"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.AutoscalingClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.SetInstancesProtectionRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.SetInstancesProtection(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyNotificationConfiguration(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyNotificationConfiguration", g_param[OptionsDefine.Version])
        return

    param = {
        "AutoScalingNotificationId": argv.get("--AutoScalingNotificationId"),
        "NotificationTypes": Utils.try_to_json(argv, "--NotificationTypes"),
        "NotificationUserGroupIds": Utils.try_to_json(argv, "--NotificationUserGroupIds"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.AutoscalingClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyNotificationConfigurationRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyNotificationConfiguration(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doStopAutoScalingInstances(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("StopAutoScalingInstances", g_param[OptionsDefine.Version])
        return

    param = {
        "AutoScalingGroupId": argv.get("--AutoScalingGroupId"),
        "InstanceIds": Utils.try_to_json(argv, "--InstanceIds"),
        "StoppedMode": argv.get("--StoppedMode"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.AutoscalingClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.StopAutoScalingInstancesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.StopAutoScalingInstances(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateLaunchConfiguration(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateLaunchConfiguration", g_param[OptionsDefine.Version])
        return

    param = {
        "LaunchConfigurationName": argv.get("--LaunchConfigurationName"),
        "ImageId": argv.get("--ImageId"),
        "ProjectId": Utils.try_to_json(argv, "--ProjectId"),
        "InstanceType": argv.get("--InstanceType"),
        "SystemDisk": Utils.try_to_json(argv, "--SystemDisk"),
        "DataDisks": Utils.try_to_json(argv, "--DataDisks"),
        "InternetAccessible": Utils.try_to_json(argv, "--InternetAccessible"),
        "LoginSettings": Utils.try_to_json(argv, "--LoginSettings"),
        "SecurityGroupIds": Utils.try_to_json(argv, "--SecurityGroupIds"),
        "EnhancedService": Utils.try_to_json(argv, "--EnhancedService"),
        "UserData": argv.get("--UserData"),
        "InstanceChargeType": argv.get("--InstanceChargeType"),
        "InstanceMarketOptions": Utils.try_to_json(argv, "--InstanceMarketOptions"),
        "InstanceTypes": Utils.try_to_json(argv, "--InstanceTypes"),
        "InstanceTypesCheckPolicy": argv.get("--InstanceTypesCheckPolicy"),
        "InstanceTags": Utils.try_to_json(argv, "--InstanceTags"),
        "CamRoleName": argv.get("--CamRoleName"),
        "HostNameSettings": Utils.try_to_json(argv, "--HostNameSettings"),
        "InstanceNameSettings": Utils.try_to_json(argv, "--InstanceNameSettings"),
        "InstanceChargePrepaid": Utils.try_to_json(argv, "--InstanceChargePrepaid"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.AutoscalingClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateLaunchConfigurationRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateLaunchConfiguration(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyAutoScalingGroup(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyAutoScalingGroup", g_param[OptionsDefine.Version])
        return

    param = {
        "AutoScalingGroupId": argv.get("--AutoScalingGroupId"),
        "AutoScalingGroupName": argv.get("--AutoScalingGroupName"),
        "DefaultCooldown": Utils.try_to_json(argv, "--DefaultCooldown"),
        "DesiredCapacity": Utils.try_to_json(argv, "--DesiredCapacity"),
        "LaunchConfigurationId": argv.get("--LaunchConfigurationId"),
        "MaxSize": Utils.try_to_json(argv, "--MaxSize"),
        "MinSize": Utils.try_to_json(argv, "--MinSize"),
        "ProjectId": Utils.try_to_json(argv, "--ProjectId"),
        "SubnetIds": Utils.try_to_json(argv, "--SubnetIds"),
        "TerminationPolicies": Utils.try_to_json(argv, "--TerminationPolicies"),
        "VpcId": argv.get("--VpcId"),
        "Zones": Utils.try_to_json(argv, "--Zones"),
        "RetryPolicy": argv.get("--RetryPolicy"),
        "ZonesCheckPolicy": argv.get("--ZonesCheckPolicy"),
        "ServiceSettings": Utils.try_to_json(argv, "--ServiceSettings"),
        "Ipv6AddressCount": Utils.try_to_json(argv, "--Ipv6AddressCount"),
        "MultiZoneSubnetPolicy": argv.get("--MultiZoneSubnetPolicy"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.AutoscalingClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyAutoScalingGroupRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyAutoScalingGroup(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateNotificationConfiguration(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateNotificationConfiguration", g_param[OptionsDefine.Version])
        return

    param = {
        "AutoScalingGroupId": argv.get("--AutoScalingGroupId"),
        "NotificationTypes": Utils.try_to_json(argv, "--NotificationTypes"),
        "NotificationUserGroupIds": Utils.try_to_json(argv, "--NotificationUserGroupIds"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.AutoscalingClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateNotificationConfigurationRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateNotificationConfiguration(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeAutoScalingInstances(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeAutoScalingInstances", g_param[OptionsDefine.Version])
        return

    param = {
        "InstanceIds": Utils.try_to_json(argv, "--InstanceIds"),
        "Filters": Utils.try_to_json(argv, "--Filters"),
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
    client = mod.AutoscalingClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeAutoScalingInstancesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeAutoScalingInstances(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateAutoScalingGroupFromInstance(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateAutoScalingGroupFromInstance", g_param[OptionsDefine.Version])
        return

    param = {
        "AutoScalingGroupName": argv.get("--AutoScalingGroupName"),
        "InstanceId": argv.get("--InstanceId"),
        "MinSize": Utils.try_to_json(argv, "--MinSize"),
        "MaxSize": Utils.try_to_json(argv, "--MaxSize"),
        "DesiredCapacity": Utils.try_to_json(argv, "--DesiredCapacity"),
        "InheritInstanceTag": Utils.try_to_json(argv, "--InheritInstanceTag"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.AutoscalingClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateAutoScalingGroupFromInstanceRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateAutoScalingGroupFromInstance(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateLifecycleHook(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateLifecycleHook", g_param[OptionsDefine.Version])
        return

    param = {
        "AutoScalingGroupId": argv.get("--AutoScalingGroupId"),
        "LifecycleHookName": argv.get("--LifecycleHookName"),
        "LifecycleTransition": argv.get("--LifecycleTransition"),
        "DefaultResult": argv.get("--DefaultResult"),
        "HeartbeatTimeout": Utils.try_to_json(argv, "--HeartbeatTimeout"),
        "NotificationMetadata": argv.get("--NotificationMetadata"),
        "NotificationTarget": Utils.try_to_json(argv, "--NotificationTarget"),
        "LifecycleTransitionType": argv.get("--LifecycleTransitionType"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.AutoscalingClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateLifecycleHookRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateLifecycleHook(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doUpgradeLifecycleHook(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("UpgradeLifecycleHook", g_param[OptionsDefine.Version])
        return

    param = {
        "LifecycleHookId": argv.get("--LifecycleHookId"),
        "LifecycleHookName": argv.get("--LifecycleHookName"),
        "LifecycleTransition": argv.get("--LifecycleTransition"),
        "DefaultResult": argv.get("--DefaultResult"),
        "HeartbeatTimeout": Utils.try_to_json(argv, "--HeartbeatTimeout"),
        "NotificationMetadata": argv.get("--NotificationMetadata"),
        "NotificationTarget": Utils.try_to_json(argv, "--NotificationTarget"),
        "LifecycleTransitionType": argv.get("--LifecycleTransitionType"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.AutoscalingClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.UpgradeLifecycleHookRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.UpgradeLifecycleHook(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDisableAutoScalingGroup(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DisableAutoScalingGroup", g_param[OptionsDefine.Version])
        return

    param = {
        "AutoScalingGroupId": argv.get("--AutoScalingGroupId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.AutoscalingClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DisableAutoScalingGroupRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DisableAutoScalingGroup(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeLaunchConfigurations(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeLaunchConfigurations", g_param[OptionsDefine.Version])
        return

    param = {
        "LaunchConfigurationIds": Utils.try_to_json(argv, "--LaunchConfigurationIds"),
        "Filters": Utils.try_to_json(argv, "--Filters"),
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
    client = mod.AutoscalingClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeLaunchConfigurationsRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeLaunchConfigurations(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribePaiInstances(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribePaiInstances", g_param[OptionsDefine.Version])
        return

    param = {
        "InstanceIds": Utils.try_to_json(argv, "--InstanceIds"),
        "Filters": Utils.try_to_json(argv, "--Filters"),
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
    client = mod.AutoscalingClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribePaiInstancesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribePaiInstances(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateScalingPolicy(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateScalingPolicy", g_param[OptionsDefine.Version])
        return

    param = {
        "AutoScalingGroupId": argv.get("--AutoScalingGroupId"),
        "ScalingPolicyName": argv.get("--ScalingPolicyName"),
        "AdjustmentType": argv.get("--AdjustmentType"),
        "AdjustmentValue": Utils.try_to_json(argv, "--AdjustmentValue"),
        "MetricAlarm": Utils.try_to_json(argv, "--MetricAlarm"),
        "Cooldown": Utils.try_to_json(argv, "--Cooldown"),
        "NotificationUserGroupIds": Utils.try_to_json(argv, "--NotificationUserGroupIds"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.AutoscalingClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateScalingPolicyRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateScalingPolicy(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteLaunchConfiguration(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteLaunchConfiguration", g_param[OptionsDefine.Version])
        return

    param = {
        "LaunchConfigurationId": argv.get("--LaunchConfigurationId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.AutoscalingClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteLaunchConfigurationRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeleteLaunchConfiguration(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteLifecycleHook(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteLifecycleHook", g_param[OptionsDefine.Version])
        return

    param = {
        "LifecycleHookId": argv.get("--LifecycleHookId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.AutoscalingClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteLifecycleHookRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeleteLifecycleHook(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeAutoScalingGroupLastActivities(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeAutoScalingGroupLastActivities", g_param[OptionsDefine.Version])
        return

    param = {
        "AutoScalingGroupIds": Utils.try_to_json(argv, "--AutoScalingGroupIds"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.AutoscalingClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeAutoScalingGroupLastActivitiesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeAutoScalingGroupLastActivities(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeLifecycleHooks(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeLifecycleHooks", g_param[OptionsDefine.Version])
        return

    param = {
        "LifecycleHookIds": Utils.try_to_json(argv, "--LifecycleHookIds"),
        "Filters": Utils.try_to_json(argv, "--Filters"),
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
    client = mod.AutoscalingClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeLifecycleHooksRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeLifecycleHooks(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doEnableAutoScalingGroup(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("EnableAutoScalingGroup", g_param[OptionsDefine.Version])
        return

    param = {
        "AutoScalingGroupId": argv.get("--AutoScalingGroupId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.AutoscalingClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.EnableAutoScalingGroupRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.EnableAutoScalingGroup(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeScheduledActions(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeScheduledActions", g_param[OptionsDefine.Version])
        return

    param = {
        "ScheduledActionIds": Utils.try_to_json(argv, "--ScheduledActionIds"),
        "Filters": Utils.try_to_json(argv, "--Filters"),
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
    client = mod.AutoscalingClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeScheduledActionsRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeScheduledActions(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeAutoScalingGroups(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeAutoScalingGroups", g_param[OptionsDefine.Version])
        return

    param = {
        "AutoScalingGroupIds": Utils.try_to_json(argv, "--AutoScalingGroupIds"),
        "Filters": Utils.try_to_json(argv, "--Filters"),
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
    client = mod.AutoscalingClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeAutoScalingGroupsRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeAutoScalingGroups(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyScheduledAction(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyScheduledAction", g_param[OptionsDefine.Version])
        return

    param = {
        "ScheduledActionId": argv.get("--ScheduledActionId"),
        "ScheduledActionName": argv.get("--ScheduledActionName"),
        "MaxSize": Utils.try_to_json(argv, "--MaxSize"),
        "MinSize": Utils.try_to_json(argv, "--MinSize"),
        "DesiredCapacity": Utils.try_to_json(argv, "--DesiredCapacity"),
        "StartTime": argv.get("--StartTime"),
        "EndTime": argv.get("--EndTime"),
        "Recurrence": argv.get("--Recurrence"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.AutoscalingClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyScheduledActionRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyScheduledAction(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeAutoScalingActivities(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeAutoScalingActivities", g_param[OptionsDefine.Version])
        return

    param = {
        "ActivityIds": Utils.try_to_json(argv, "--ActivityIds"),
        "Filters": Utils.try_to_json(argv, "--Filters"),
        "Limit": Utils.try_to_json(argv, "--Limit"),
        "Offset": Utils.try_to_json(argv, "--Offset"),
        "StartTime": argv.get("--StartTime"),
        "EndTime": argv.get("--EndTime"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.AutoscalingClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeAutoScalingActivitiesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeAutoScalingActivities(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteNotificationConfiguration(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteNotificationConfiguration", g_param[OptionsDefine.Version])
        return

    param = {
        "AutoScalingNotificationId": argv.get("--AutoScalingNotificationId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.AutoscalingClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteNotificationConfigurationRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeleteNotificationConfiguration(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeAccountLimits(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeAccountLimits", g_param[OptionsDefine.Version])
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
    client = mod.AutoscalingClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeAccountLimitsRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeAccountLimits(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyLaunchConfigurationAttributes(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyLaunchConfigurationAttributes", g_param[OptionsDefine.Version])
        return

    param = {
        "LaunchConfigurationId": argv.get("--LaunchConfigurationId"),
        "ImageId": argv.get("--ImageId"),
        "InstanceTypes": Utils.try_to_json(argv, "--InstanceTypes"),
        "InstanceTypesCheckPolicy": argv.get("--InstanceTypesCheckPolicy"),
        "LaunchConfigurationName": argv.get("--LaunchConfigurationName"),
        "UserData": argv.get("--UserData"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.AutoscalingClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyLaunchConfigurationAttributesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyLaunchConfigurationAttributes(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


CLIENT_MAP = {
    "v20180419": autoscaling_client_v20180419,

}

MODELS_MAP = {
    "v20180419": models_v20180419,

}

ACTION_MAP = {
    "ExecuteScalingPolicy": doExecuteScalingPolicy,
    "CreateAutoScalingGroup": doCreateAutoScalingGroup,
    "PreviewPaiDomainName": doPreviewPaiDomainName,
    "ModifyScalingPolicy": doModifyScalingPolicy,
    "DescribeNotificationConfigurations": doDescribeNotificationConfigurations,
    "DeleteAutoScalingGroup": doDeleteAutoScalingGroup,
    "StartAutoScalingInstances": doStartAutoScalingInstances,
    "CreatePaiInstance": doCreatePaiInstance,
    "UpgradeLaunchConfiguration": doUpgradeLaunchConfiguration,
    "AttachInstances": doAttachInstances,
    "DescribeScalingPolicies": doDescribeScalingPolicies,
    "DeleteScheduledAction": doDeleteScheduledAction,
    "DetachInstances": doDetachInstances,
    "CreateScheduledAction": doCreateScheduledAction,
    "RemoveInstances": doRemoveInstances,
    "DeleteScalingPolicy": doDeleteScalingPolicy,
    "CompleteLifecycleAction": doCompleteLifecycleAction,
    "ModifyLoadBalancers": doModifyLoadBalancers,
    "ModifyDesiredCapacity": doModifyDesiredCapacity,
    "SetInstancesProtection": doSetInstancesProtection,
    "ModifyNotificationConfiguration": doModifyNotificationConfiguration,
    "StopAutoScalingInstances": doStopAutoScalingInstances,
    "CreateLaunchConfiguration": doCreateLaunchConfiguration,
    "ModifyAutoScalingGroup": doModifyAutoScalingGroup,
    "CreateNotificationConfiguration": doCreateNotificationConfiguration,
    "DescribeAutoScalingInstances": doDescribeAutoScalingInstances,
    "CreateAutoScalingGroupFromInstance": doCreateAutoScalingGroupFromInstance,
    "CreateLifecycleHook": doCreateLifecycleHook,
    "UpgradeLifecycleHook": doUpgradeLifecycleHook,
    "DisableAutoScalingGroup": doDisableAutoScalingGroup,
    "DescribeLaunchConfigurations": doDescribeLaunchConfigurations,
    "DescribePaiInstances": doDescribePaiInstances,
    "CreateScalingPolicy": doCreateScalingPolicy,
    "DeleteLaunchConfiguration": doDeleteLaunchConfiguration,
    "DeleteLifecycleHook": doDeleteLifecycleHook,
    "DescribeAutoScalingGroupLastActivities": doDescribeAutoScalingGroupLastActivities,
    "DescribeLifecycleHooks": doDescribeLifecycleHooks,
    "EnableAutoScalingGroup": doEnableAutoScalingGroup,
    "DescribeScheduledActions": doDescribeScheduledActions,
    "DescribeAutoScalingGroups": doDescribeAutoScalingGroups,
    "ModifyScheduledAction": doModifyScheduledAction,
    "DescribeAutoScalingActivities": doDescribeAutoScalingActivities,
    "DeleteNotificationConfiguration": doDeleteNotificationConfiguration,
    "DescribeAccountLimits": doDescribeAccountLimits,
    "ModifyLaunchConfigurationAttributes": doModifyLaunchConfigurationAttributes,

}

AVAILABLE_VERSION_LIST = [
    v20180419.version,

]
AVAILABLE_VERSIONS = {
     'v' + v20180419.version.replace('-', ''): {"help": v20180419_help.INFO,"desc": v20180419_help.DESC},

}


def autoscaling_action(argv, arglist):
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
        helpstr = HelpTemplate.SERVICE % {"name": "autoscaling", "desc": desc, "actions": action_str}
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
    cmd = NiceCommand("autoscaling", autoscaling_action)
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
            version = config["autoscaling"][OptionsDefine.Version]
            params[OptionsDefine.Version] = "v" + version.replace('-', '')

        if params[OptionsDefine.Endpoint] is None:
            params[OptionsDefine.Endpoint] = config["autoscaling"][OptionsDefine.Endpoint]
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

    helpmsg = HelpTemplate.ACTION % {"name": action, "service": "autoscaling", "desc": desc, "params": docstr}
    print(helpmsg)


def get_actions_info():
    config = Configure()
    new_version = max(AVAILABLE_VERSIONS.keys())
    version = new_version
    try:
        profile = config._load_json_msg(os.path.join(config.cli_path, "default.configure"))
        version = profile["autoscaling"]["version"]
        version = "v" + version.replace('-', '')
    except Exception:
        pass
    if version not in AVAILABLE_VERSIONS.keys():
        version = new_version
    return AVAILABLE_VERSIONS[version]["help"]
