# -*- coding: utf-8 -*-
import os
import json
import tccli.options_define as OptionsDefine
import tccli.format_output as FormatOutput
from tccli import __version__
from tccli.utils import Utils
from tccli.exceptions import ConfigurationError
from tencentcloud.common import credential
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.autoscaling.v20180419 import autoscaling_client as autoscaling_client_v20180419
from tencentcloud.autoscaling.v20180419 import models as models_v20180419


def doExecuteScalingPolicy(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
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
    model.from_json_string(json.dumps(args))
    rsp = client.ExecuteScalingPolicy(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateAutoScalingGroup(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
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
    model.from_json_string(json.dumps(args))
    rsp = client.CreateAutoScalingGroup(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doClearLaunchConfigurationAttributes(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
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
    model = models.ClearLaunchConfigurationAttributesRequest()
    model.from_json_string(json.dumps(args))
    rsp = client.ClearLaunchConfigurationAttributes(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyScalingPolicy(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
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
    model.from_json_string(json.dumps(args))
    rsp = client.ModifyScalingPolicy(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyScheduledAction(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
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
    model.from_json_string(json.dumps(args))
    rsp = client.ModifyScheduledAction(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeNotificationConfigurations(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
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
    model.from_json_string(json.dumps(args))
    rsp = client.DescribeNotificationConfigurations(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteAutoScalingGroup(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
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
    model.from_json_string(json.dumps(args))
    rsp = client.DeleteAutoScalingGroup(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doScaleOutInstances(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
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
    model = models.ScaleOutInstancesRequest()
    model.from_json_string(json.dumps(args))
    rsp = client.ScaleOutInstances(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doStartAutoScalingInstances(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
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
    model.from_json_string(json.dumps(args))
    rsp = client.StartAutoScalingInstances(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreatePaiInstance(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
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
    model.from_json_string(json.dumps(args))
    rsp = client.CreatePaiInstance(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doUpgradeLaunchConfiguration(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
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
    model.from_json_string(json.dumps(args))
    rsp = client.UpgradeLaunchConfiguration(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeLaunchConfigurations(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
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
    model.from_json_string(json.dumps(args))
    rsp = client.DescribeLaunchConfigurations(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doAttachInstances(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
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
    model.from_json_string(json.dumps(args))
    rsp = client.AttachInstances(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeScalingPolicies(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
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
    model.from_json_string(json.dumps(args))
    rsp = client.DescribeScalingPolicies(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteScheduledAction(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
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
    model.from_json_string(json.dumps(args))
    rsp = client.DeleteScheduledAction(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDetachInstances(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
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
    model.from_json_string(json.dumps(args))
    rsp = client.DetachInstances(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doScaleInInstances(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
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
    model = models.ScaleInInstancesRequest()
    model.from_json_string(json.dumps(args))
    rsp = client.ScaleInInstances(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateScheduledAction(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
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
    model.from_json_string(json.dumps(args))
    rsp = client.CreateScheduledAction(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doRemoveInstances(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
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
    model.from_json_string(json.dumps(args))
    rsp = client.RemoveInstances(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteScalingPolicy(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
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
    model.from_json_string(json.dumps(args))
    rsp = client.DeleteScalingPolicy(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCompleteLifecycleAction(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
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
    model.from_json_string(json.dumps(args))
    rsp = client.CompleteLifecycleAction(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyLoadBalancers(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
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
    model.from_json_string(json.dumps(args))
    rsp = client.ModifyLoadBalancers(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyDesiredCapacity(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
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
    model.from_json_string(json.dumps(args))
    rsp = client.ModifyDesiredCapacity(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doSetInstancesProtection(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
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
    model.from_json_string(json.dumps(args))
    rsp = client.SetInstancesProtection(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateLaunchConfiguration(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
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
    model.from_json_string(json.dumps(args))
    rsp = client.CreateLaunchConfiguration(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyNotificationConfiguration(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
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
    model.from_json_string(json.dumps(args))
    rsp = client.ModifyNotificationConfiguration(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyAutoScalingGroup(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
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
    model.from_json_string(json.dumps(args))
    rsp = client.ModifyAutoScalingGroup(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateNotificationConfiguration(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
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
    model.from_json_string(json.dumps(args))
    rsp = client.CreateNotificationConfiguration(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeAutoScalingInstances(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
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
    model.from_json_string(json.dumps(args))
    rsp = client.DescribeAutoScalingInstances(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateAutoScalingGroupFromInstance(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
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
    model.from_json_string(json.dumps(args))
    rsp = client.CreateAutoScalingGroupFromInstance(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateLifecycleHook(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
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
    model.from_json_string(json.dumps(args))
    rsp = client.CreateLifecycleHook(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doUpgradeLifecycleHook(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
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
    model.from_json_string(json.dumps(args))
    rsp = client.UpgradeLifecycleHook(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDisableAutoScalingGroup(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
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
    model.from_json_string(json.dumps(args))
    rsp = client.DisableAutoScalingGroup(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doPreviewPaiDomainName(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
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
    model.from_json_string(json.dumps(args))
    rsp = client.PreviewPaiDomainName(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribePaiInstances(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
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
    model.from_json_string(json.dumps(args))
    rsp = client.DescribePaiInstances(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateScalingPolicy(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
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
    model.from_json_string(json.dumps(args))
    rsp = client.CreateScalingPolicy(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteLaunchConfiguration(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
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
    model.from_json_string(json.dumps(args))
    rsp = client.DeleteLaunchConfiguration(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteLifecycleHook(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
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
    model.from_json_string(json.dumps(args))
    rsp = client.DeleteLifecycleHook(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeAutoScalingGroupLastActivities(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
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
    model.from_json_string(json.dumps(args))
    rsp = client.DescribeAutoScalingGroupLastActivities(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeLifecycleHooks(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
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
    model.from_json_string(json.dumps(args))
    rsp = client.DescribeLifecycleHooks(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doEnableAutoScalingGroup(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
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
    model.from_json_string(json.dumps(args))
    rsp = client.EnableAutoScalingGroup(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeAccountLimits(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
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
    model.from_json_string(json.dumps(args))
    rsp = client.DescribeAccountLimits(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeAutoScalingGroups(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
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
    model.from_json_string(json.dumps(args))
    rsp = client.DescribeAutoScalingGroups(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doStopAutoScalingInstances(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
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
    model.from_json_string(json.dumps(args))
    rsp = client.StopAutoScalingInstances(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeAutoScalingActivities(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
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
    model.from_json_string(json.dumps(args))
    rsp = client.DescribeAutoScalingActivities(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteNotificationConfiguration(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
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
    model.from_json_string(json.dumps(args))
    rsp = client.DeleteNotificationConfiguration(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeScheduledActions(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
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
    model.from_json_string(json.dumps(args))
    rsp = client.DescribeScheduledActions(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyLaunchConfigurationAttributes(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
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
    model.from_json_string(json.dumps(args))
    rsp = client.ModifyLaunchConfigurationAttributes(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


CLIENT_MAP = {
    "v20180419": autoscaling_client_v20180419,

}

MODELS_MAP = {
    "v20180419": models_v20180419,

}

ACTION_MAP = {
    "ExecuteScalingPolicy": doExecuteScalingPolicy,
    "CreateAutoScalingGroup": doCreateAutoScalingGroup,
    "ClearLaunchConfigurationAttributes": doClearLaunchConfigurationAttributes,
    "ModifyScalingPolicy": doModifyScalingPolicy,
    "ModifyScheduledAction": doModifyScheduledAction,
    "DescribeNotificationConfigurations": doDescribeNotificationConfigurations,
    "DeleteAutoScalingGroup": doDeleteAutoScalingGroup,
    "ScaleOutInstances": doScaleOutInstances,
    "StartAutoScalingInstances": doStartAutoScalingInstances,
    "CreatePaiInstance": doCreatePaiInstance,
    "UpgradeLaunchConfiguration": doUpgradeLaunchConfiguration,
    "DescribeLaunchConfigurations": doDescribeLaunchConfigurations,
    "AttachInstances": doAttachInstances,
    "DescribeScalingPolicies": doDescribeScalingPolicies,
    "DeleteScheduledAction": doDeleteScheduledAction,
    "DetachInstances": doDetachInstances,
    "ScaleInInstances": doScaleInInstances,
    "CreateScheduledAction": doCreateScheduledAction,
    "RemoveInstances": doRemoveInstances,
    "DeleteScalingPolicy": doDeleteScalingPolicy,
    "CompleteLifecycleAction": doCompleteLifecycleAction,
    "ModifyLoadBalancers": doModifyLoadBalancers,
    "ModifyDesiredCapacity": doModifyDesiredCapacity,
    "SetInstancesProtection": doSetInstancesProtection,
    "CreateLaunchConfiguration": doCreateLaunchConfiguration,
    "ModifyNotificationConfiguration": doModifyNotificationConfiguration,
    "ModifyAutoScalingGroup": doModifyAutoScalingGroup,
    "CreateNotificationConfiguration": doCreateNotificationConfiguration,
    "DescribeAutoScalingInstances": doDescribeAutoScalingInstances,
    "CreateAutoScalingGroupFromInstance": doCreateAutoScalingGroupFromInstance,
    "CreateLifecycleHook": doCreateLifecycleHook,
    "UpgradeLifecycleHook": doUpgradeLifecycleHook,
    "DisableAutoScalingGroup": doDisableAutoScalingGroup,
    "PreviewPaiDomainName": doPreviewPaiDomainName,
    "DescribePaiInstances": doDescribePaiInstances,
    "CreateScalingPolicy": doCreateScalingPolicy,
    "DeleteLaunchConfiguration": doDeleteLaunchConfiguration,
    "DeleteLifecycleHook": doDeleteLifecycleHook,
    "DescribeAutoScalingGroupLastActivities": doDescribeAutoScalingGroupLastActivities,
    "DescribeLifecycleHooks": doDescribeLifecycleHooks,
    "EnableAutoScalingGroup": doEnableAutoScalingGroup,
    "DescribeAccountLimits": doDescribeAccountLimits,
    "DescribeAutoScalingGroups": doDescribeAutoScalingGroups,
    "StopAutoScalingInstances": doStopAutoScalingInstances,
    "DescribeAutoScalingActivities": doDescribeAutoScalingActivities,
    "DeleteNotificationConfiguration": doDeleteNotificationConfiguration,
    "DescribeScheduledActions": doDescribeScheduledActions,
    "ModifyLaunchConfigurationAttributes": doModifyLaunchConfigurationAttributes,

}

AVAILABLE_VERSION_LIST = [
    "v20180419",

]


def action_caller():
    return ACTION_MAP


def parse_global_arg(parsed_globals):
    g_param = parsed_globals

    is_exist_profile = True
    if not parsed_globals["profile"]:
        is_exist_profile = False
        g_param["profile"] = "default"

    configure_path = os.path.join(os.path.expanduser("~"), ".tccli")
    is_conf_exist, conf_path = Utils.file_existed(configure_path, g_param["profile"] + ".configure")
    is_cred_exist, cred_path = Utils.file_existed(configure_path, g_param["profile"] + ".credential")

    conf = {}
    cred = {}

    if is_conf_exist:
        conf = Utils.load_json_msg(conf_path)
    if is_cred_exist:
        cred = Utils.load_json_msg(cred_path)

    if not (isinstance(conf, dict) and isinstance(cred, dict)):
        raise ConfigurationError(
            "file: %s or %s is not json format"
            % (g_param["profile"] + ".configure", g_param["profile"] + ".credential"))

    if OptionsDefine.Token not in cred:
        cred[OptionsDefine.Token] = None

    if not is_exist_profile:
        if os.environ.get(OptionsDefine.ENV_SECRET_ID) and os.environ.get(OptionsDefine.ENV_SECRET_KEY):
            cred[OptionsDefine.SecretId] = os.environ.get(OptionsDefine.ENV_SECRET_ID)
            cred[OptionsDefine.SecretKey] = os.environ.get(OptionsDefine.ENV_SECRET_KEY)
            cred[OptionsDefine.Token] = os.environ.get(OptionsDefine.ENV_TOKEN)

        if os.environ.get(OptionsDefine.ENV_REGION):
            conf[OptionsDefine.Region] = os.environ.get(OptionsDefine.ENV_REGION)

    for param in g_param.keys():
        if g_param[param] is None:
            if param in [OptionsDefine.SecretKey, OptionsDefine.SecretId, OptionsDefine.Token]:
                if param in cred:
                    g_param[param] = cred[param]
                else:
                    raise ConfigurationError("%s is invalid" % param)
            elif param in [OptionsDefine.Region, OptionsDefine.Output]:
                if param in conf:
                    g_param[param] = conf[param]
                else:
                    raise ConfigurationError("%s is invalid" % param)

    try:
        if g_param[OptionsDefine.ServiceVersion]:
            g_param[OptionsDefine.Version] = "v" + g_param[OptionsDefine.ServiceVersion].replace('-', '')
        else:
            version = conf["autoscaling"][OptionsDefine.Version]
            g_param[OptionsDefine.Version] = "v" + version.replace('-', '')

        if g_param[OptionsDefine.Endpoint] is None:
            g_param[OptionsDefine.Endpoint] = conf["autoscaling"][OptionsDefine.Endpoint]
    except Exception as err:
        raise ConfigurationError("config file:%s error, %s" % (conf_path, str(err)))

    if g_param[OptionsDefine.Version] not in AVAILABLE_VERSION_LIST:
        raise Exception("available versions: %s" % " ".join(AVAILABLE_VERSION_LIST))

    return g_param

