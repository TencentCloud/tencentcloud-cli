**Example 1: 部署容器应用**



Input: 

```
tccli tsf DeployContainerApplication --cli-unfold-argument  \
    --ApplicationId application-6ym5kebd \
    --GroupName test-group-1 \
    --ClusterId cls-23iwxs1l \
    --Alias app remark \
    --NamespaceId namespace-by8mg4xs \
    --Tags.0.TagKey tke-clusterId \
    --Tags.0.TagValue cls-23iwxs1l \
    --ContainerKind Deployment \
    --InstanceNum 1 \
    --SchedulingStrategy.Type NONE \
    --SchedulingStrategy.NodeScheduleStrategyType Default \
    --SchedulingStrategy.AvailableZoneScatterScheduleType None \
    --SchedulingStrategy.PodScheduleStrategyType None \
    --SchedulingStrategy.TolerateScheduleType None \
    --ServiceSettingList.0.LoadBalancingType Intranet \
    --ServiceSettingList.0.ExternalTrafficStrategy Local \
    --ServiceSettingList.0.ExternalTrafficPolicy Local \
    --ServiceSettingList.0.ServiceName test-svc-1 \
    --ServiceSettingList.0.HeadlessService True \
    --ServiceSettingList.0.AccessType 1 \
    --ServiceSettingList.0.SubnetId subnet-d15zonly \
    --ServiceSettingList.0.OpenSessionAffinity False \
    --ServiceSettingList.0.SessionAffinityTimeoutSeconds 10800 \
    --ServiceSettingList.0.ProtocolPorts.0.Protocol TCP \
    --ServiceSettingList.0.ProtocolPorts.0.TargetPort 80 \
    --ServiceSettingList.0.ProtocolPorts.0.Port 80 \
    --ServiceSettingList.0.ProtocolPorts.0.Name svc-1 \
    --ServiceClean False \
    --EnvClean True \
    --RestartPolicy Always \
    --CpuRequest 0.25 \
    --MemRequest 120 \
    --MemLimit 1280 \
    --CpuLimit 0.5 \
    --Server ccr.ccs.tencentyun.com \
    --RepoName tsf_700001025656/test-sts-1 \
    --TagName nginx-v1 \
    --Envs.0.ValueFrom.FieldRef.FieldPath metadata.name \
    --Envs.0.Name env1 \
    --Envs.1.ValueFrom.ResourceFieldRef.Resource limits.memory \
    --Envs.1.Name env2 \
    --Envs.2.ValueFrom.ConfigMapKeyRef.Name kube-root-ca.crt \
    --Envs.2.ValueFrom.ConfigMapKeyRef.Key ca.crt \
    --Envs.2.Name env3 \
    --Envs.3.ValueFrom.SecretKeyRef.Name qcloudregistrykey \
    --Envs.3.ValueFrom.SecretKeyRef.Key .dockercfg \
    --Envs.3.Name env4 \
    --RepoType personal \
    --PrivilegeContainerEnable True \
    --RunCommand /bin/sh \
    --RunArg -c
while true; do echo hello; sleep 10; done \
    --InitContainerEnable False \
    --LifeCycleHookList.0.HookType postStart \
    --LifeCycleHookList.0.ExecMode httpGet \
    --LifeCycleHookList.0.HttpGetOption.Scheme HTTP \
    --LifeCycleHookList.0.HttpGetOption.Host host.com \
    --LifeCycleHookList.0.HttpGetOption.Path /tmp \
    --LifeCycleHookList.0.HttpGetOption.Port 7998 \
    --LifeCycleHookList.1.HookType preStop \
    --LifeCycleHookList.1.ExecMode none \
    --LifeCycleHookList.1.HttpGetOption.Scheme HTTP \
    --HealthCheckSettings.LivenessProbe.Type K8S_NATIVE \
    --HealthCheckSettings.LivenessProbe.ActionType HTTP \
    --HealthCheckSettings.LivenessProbe.InitialDelaySeconds 0 \
    --HealthCheckSettings.LivenessProbe.TimeoutSeconds 3 \
    --HealthCheckSettings.LivenessProbe.PeriodSeconds 30 \
    --HealthCheckSettings.LivenessProbe.SuccessThreshold 1 \
    --HealthCheckSettings.LivenessProbe.FailureThreshold 3 \
    --HealthCheckSettings.LivenessProbe.Port 30000 \
    --HealthCheckSettings.LivenessProbe.Scheme HTTP \
    --HealthCheckSettings.LivenessProbe.Path /test \
    --HealthCheckSettings.ReadinessProbe.Type TSF_DEFAULT \
    --JvmOpts -Xms128m -Xmx512m -XX:MetaspaceSize=128m -XX:MaxMetaspaceSize=512m \
    --VolumeMountInfoList.0.VolumeMountPath /tmp \
    --VolumeMountInfoList.0.VolumeMountSubPath /test \
    --VolumeMountInfoList.0.ReadOrWrite 1 \
    --VolumeMountInfoList.0.VolumeMountName test-data-emptydir \
    --AgentCpuRequest 0.1 \
    --AgentCpuLimit 0.2 \
    --AgentMemRequest 125 \
    --AgentMemLimit 400 \
    --DeployAgent True \
    --AdditionalContainerList.0.CpuRequest 0.25 \
    --AdditionalContainerList.0.MemRequest 120 \
    --AdditionalContainerList.0.MemLimit 1280 \
    --AdditionalContainerList.0.CpuLimit 0.5 \
    --AdditionalContainerList.0.Server ccr.ccs.tencentyun.com \
    --AdditionalContainerList.0.RepoName tsf_700001025656/test-ns \
    --AdditionalContainerList.0.TagName polaris-1 \
    --AdditionalContainerList.0.RepoType personal \
    --AdditionalContainerList.0.PrivilegeContainerEnable False \
    --AdditionalContainerList.0.InitContainerEnable False \
    --AdditionalContainerList.0.LifeCycleHookList.0.HookType postStart \
    --AdditionalContainerList.0.LifeCycleHookList.0.ExecMode none \
    --AdditionalContainerList.0.LifeCycleHookList.0.HttpGetOption.Scheme HTTP \
    --AdditionalContainerList.0.LifeCycleHookList.1.HookType preStop \
    --AdditionalContainerList.0.LifeCycleHookList.1.ExecMode none \
    --AdditionalContainerList.0.LifeCycleHookList.1.HttpGetOption.Scheme HTTP \
    --AdditionalContainerList.0.JvmOpts -Xms128m -Xmx512m -XX:MetaspaceSize=128m -XX:MaxMetaspaceSize=512m \
    --VolumeInfoList.0.VolumeName test-data-emptydir \
    --VolumeInfoList.0.VolumeType emptyDir \
    --VolumeInfoList.0.EmptyDirOption.StorageCapacity 1 \
    --VolumeInfoList.0.EmptyDirOption.StorageUnit Gi \
    --VolumeInfoList.0.EmptyDirOption.EnableMemory True \
    --VolumeClean True \
    --ServiceGovernanceConfig.GovernanceType SHARE \
    --ServiceGovernanceConfig.EnableGovernance True \
    --ObservabilityConfig.BusinessLogConfigIdList apm-busi-log-cfg-lba2povk apm-busi-log-cfg-2vz5nm9v \
    --WarmupSetting.Enabled True \
    --WarmupSetting.WarmupTime 60 \
    --WarmupSetting.Curvature 2 \
    --WarmupSetting.EnabledProtection True \
    --AgentProfileList.0.AgentType OT_AGENT \
    --AgentProfileList.0.AgentVersion  \
    --UpdateType 1 \
    --UpdateIvl 10 \
    --MaxSurge 25% \
    --MaxUnavailable 0
```

Output: 
```
{
    "Response": {
        "Result": {
            "GroupId": "group-oydjq4my",
            "TaskId": "task-2.0-gvko6ona"
        },
        "RequestId": "a187dea0-773a-4076-a06b-ac6482f6f679"
    }
}
```

