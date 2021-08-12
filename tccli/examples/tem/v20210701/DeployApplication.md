**Example 1: 应用部署**

应用部署

Input: 

```
tccli tem DeployApplication --cli-unfold-argument  \
    --Service.ApplicationName xx \
    --Service.ExternalIp xx \
    --Service.Name xx \
    --Service.PortMappings.0.Protocol xx \
    --Service.PortMappings.0.TargetPort 0 \
    --Service.PortMappings.0.Port 0 \
    --Service.Yaml xx \
    --Service.LoadBalanceId xx \
    --Service.VersionName xx \
    --Service.ClusterIp xx \
    --Service.SubnetId xx \
    --Service.Type xx \
    --Service.Ports 0 \
    --JvmOpts xx \
    --StorageConfs.0.StorageVolName xx \
    --StorageConfs.0.StorageVolIp xx \
    --StorageConfs.0.StorageVolPath xx \
    --ImgRepo xx \
    --EnvConf.0.Value xx \
    --EnvConf.0.Key xx \
    --ImageCommand xx \
    --Description xx \
    --JdkVersion xx \
    --ApplicationId xx \
    --LogOutputConf.ClsLogTopicId xx \
    --LogOutputConf.ClsLogsetName xx \
    --LogOutputConf.ClsLogsetId xx \
    --LogOutputConf.ClsLogTopicName xx \
    --LogOutputConf.OutputType xx \
    --UseRegistryDefaultConfig True \
    --CpuSpec 0.0 \
    --DeployMode xx \
    --SecurityGroupIds xx \
    --SourceChannel 0 \
    --DeployVersion xx \
    --InitPodNum 1 \
    --VersionDesc xx \
    --ImageArgs xx \
    --MemorySpec 0.0 \
    --EnvironmentId xx \
    --LogConfs xx \
    --PkgName xx \
    --StorageMountConfs.0.VolumeName xx \
    --StorageMountConfs.0.MountPath xx \
    --EsInfo.MinAliveInstances 0 \
    --EsInfo.EsStrategy 0 \
    --EsInfo.VersionId xx \
    --EsInfo.Threshold 1 \
    --EsInfo.MaxAliveInstances 2 \
    --VersionId xx \
    --SettingConfs.0.ConfigDataName xx \
    --SettingConfs.0.MountedPath xx \
    --SettingConfs.0.Data.0.Value xx \
    --SettingConfs.0.Data.0.Key xx
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

