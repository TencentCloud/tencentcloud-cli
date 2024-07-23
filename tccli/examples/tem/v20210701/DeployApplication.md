**Example 1: 应用部署**

应用部署

Input: 

```
tccli tem DeployApplication --cli-unfold-argument  \
    --ApplicationId abc \
    --ImgRepo abc \
    --VersionDesc abc \
    --JvmOpts abc \
    --InitPodNum 1 \
    --EsInfo.MinAliveInstances 0 \
    --EsInfo.MaxAliveInstances 0 \
    --EsInfo.EsStrategy 0 \
    --EsInfo.VersionId abc \
    --EsInfo.Threshold 1 \
    --EnvConf.0.Key abc \
    --EnvConf.0.Value abc \
    --EnvConf.0.Type abc \
    --EnvConf.0.Config abc \
    --EnvConf.0.Secret abc \
    --LogConfs abc \
    --StorageConfs.0.StorageVolName abc \
    --StorageConfs.0.StorageVolPath abc \
    --StorageConfs.0.StorageVolIp abc \
    --StorageMountConfs.0.VolumeName abc \
    --StorageMountConfs.0.MountPath abc \
    --DeployMode abc \
    --DeployVersion abc \
    --PkgName abc \
    --CpuSpec 0 \
    --MemorySpec 0 \
    --JdkVersion abc \
    --SecurityGroupIds abc \
    --LogOutputConf.OutputType abc \
    --LogOutputConf.ClsLogsetName abc \
    --LogOutputConf.ClsLogTopicId abc \
    --LogOutputConf.ClsLogsetId abc \
    --LogOutputConf.ClsLogTopicName abc \
    --SourceChannel 0 \
    --Description abc \
    --EnvironmentId abc \
    --ImageCommand abc \
    --ImageArgs abc \
    --UseRegistryDefaultConfig True \
    --SettingConfs.0.ConfigDataName abc \
    --SettingConfs.0.MountedPath abc \
    --SettingConfs.0.Data.0.Key abc \
    --SettingConfs.0.Data.0.Value abc \
    --SettingConfs.0.Data.0.Type abc \
    --SettingConfs.0.Data.0.Config abc \
    --SettingConfs.0.Data.0.Secret abc \
    --SettingConfs.0.SecretDataName abc \
    --Service.Name abc \
    --Service.Ports 0 \
    --Service.Yaml abc \
    --Service.ApplicationName abc \
    --Service.VersionName abc \
    --Service.ClusterIp abc \
    --Service.ExternalIp abc \
    --Service.Type abc \
    --Service.SubnetId abc \
    --Service.LoadBalanceId abc \
    --Service.PortMappings.0.Port 0 \
    --Service.PortMappings.0.TargetPort 0 \
    --Service.PortMappings.0.Protocol abc \
    --Service.PortMappings.0.ServiceName abc \
    --Service.ServicePortMappingList.0.Type abc \
    --Service.ServicePortMappingList.0.ServiceName abc \
    --Service.ServicePortMappingList.0.ClusterIp abc \
    --Service.ServicePortMappingList.0.ExternalIp abc \
    --Service.ServicePortMappingList.0.SubnetId abc \
    --Service.ServicePortMappingList.0.VpcId abc \
    --Service.ServicePortMappingList.0.LoadBalanceId abc \
    --Service.ServicePortMappingList.0.Yaml abc \
    --Service.ServicePortMappingList.0.Ports 0 \
    --Service.ServicePortMappingList.0.PortMappingItemList.0.Port 0 \
    --Service.ServicePortMappingList.0.PortMappingItemList.0.TargetPort 0 \
    --Service.ServicePortMappingList.0.PortMappingItemList.0.Protocol abc \
    --Service.ServicePortMappingList.0.ExternalDomain abc \
    --Service.FlushAll True \
    --Service.EnableRegistryNextDeploy 0 \
    --Service.ApplicationId abc \
    --Service.AllIpDone True \
    --Service.ExternalDomain abc \
    --VersionId abc \
    --PostStart abc \
    --PreStop abc \
    --Liveness.Type abc \
    --Liveness.Protocol abc \
    --Liveness.Path abc \
    --Liveness.Exec abc \
    --Liveness.Port 0 \
    --Liveness.InitialDelaySeconds 0 \
    --Liveness.TimeoutSeconds 0 \
    --Liveness.PeriodSeconds 0 \
    --Readiness.Type abc \
    --Readiness.Protocol abc \
    --Readiness.Path abc \
    --Readiness.Exec abc \
    --Readiness.Port 0 \
    --Readiness.InitialDelaySeconds 0 \
    --Readiness.TimeoutSeconds 0 \
    --Readiness.PeriodSeconds 0 \
    --DeployStrategyConf.TotalBatchCount 0 \
    --DeployStrategyConf.BetaBatchNum 0 \
    --DeployStrategyConf.DeployStrategyType 0 \
    --DeployStrategyConf.BatchInterval 0 \
    --DeployStrategyConf.MinAvailable 0 \
    --DeployStrategyConf.Force True \
    --HorizontalAutoscaler.0.MinReplicas 0 \
    --HorizontalAutoscaler.0.MaxReplicas 0 \
    --HorizontalAutoscaler.0.Metrics abc \
    --HorizontalAutoscaler.0.Threshold 0 \
    --HorizontalAutoscaler.0.Enabled True \
    --HorizontalAutoscaler.0.DoubleThreshold 0 \
    --CronHorizontalAutoscaler.0.Name abc \
    --CronHorizontalAutoscaler.0.Period abc \
    --CronHorizontalAutoscaler.0.Schedules.0.StartAt abc \
    --CronHorizontalAutoscaler.0.Schedules.0.TargetReplicas 0 \
    --CronHorizontalAutoscaler.0.Enabled True \
    --CronHorizontalAutoscaler.0.Priority 0 \
    --LogEnable 0 \
    --ConfEdited True \
    --SpeedUp True \
    --StartupProbe.Type abc \
    --StartupProbe.Protocol abc \
    --StartupProbe.Path abc \
    --StartupProbe.Exec abc \
    --StartupProbe.Port 0 \
    --StartupProbe.InitialDelaySeconds 0 \
    --StartupProbe.TimeoutSeconds 0 \
    --StartupProbe.PeriodSeconds 0 \
    --OsFlavour abc \
    --EnablePrometheusConf.Port 0 \
    --EnablePrometheusConf.Path abc \
    --EnableTracing 0 \
    --EnableMetrics 0 \
    --TcrInstanceId abc \
    --RepoServer abc \
    --RepoType 0 \
    --PostStartEncoded abc \
    --PreStopEncoded abc
```

Output: 
```
{
    "Response": {
        "RequestId": "81f74023-563c-437d-abf7-8139449ef178",
        "Result": "version-xxx"
    }
}
```

