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
    --SettingConfs.0.Data.0.Key xx \
    --OsFlavour ALPINE
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

**Example 2: nanjing-test-20220111**



Input: 

```
tccli tem DeployApplication --cli-unfold-argument  \
    --Service.Name 字符串 \
    --JvmOpts 字符串 \
    --SpeedUp false \
    --PreStop 字符串 \
    --ImgRepo 字符串 \
    --EnvConf.0.Config 字符串 \
    --EnvConf.0.Type 字符串 \
    --EnvConf.0.Key 字符串 \
    --EnvConf.0.Value 字符串 \
    --ImageCommand 字符串 \
    --Description 字符串 \
    --JdkVersion 字符串 \
    --ApplicationId 字符串 \
    --LogOutputConf.ClsLogTopicName 字符串 \
    --LogOutputConf.ClsLogsetName 字符串 \
    --LogOutputConf.ClsLogTopicId 字符串 \
    --LogOutputConf.OutputType 字符串 \
    --LogOutputConf.ClsLogsetId 字符串 \
    --ConfEdited false \
    --EnvironmentId 字符串 \
    --CpuSpec 0.1 \
    --DeployMode 字符串 \
    --SecurityGroupIds 字符串 \
    --SourceChannel 0 \
    --LogEnable 0 \
    --InitPodNum 2 \
    --VersionDesc 字符串 \
    --ImageArgs 字符串 \
    --MemorySpec 1024 \
    --UseRegistryDefaultConfig true \
    --LogConfs 字符串 \
    --PkgName 字符串 \
    --StorageMountConfs.0.VolumeName 字符串 \
    --StorageMountConfs.0.MountPath 字符串 \
    --DeployVersion 字符串 \
    --VersionId 字符串 \
    --SettingConfs.0.ConfigDataName 字符串 \
    --SettingConfs.0.MountedPath 字符串 \
    --SettingConfs.0.Data.0.Config 字符串 \
    --SettingConfs.0.Data.0.Type 字符串 \
    --SettingConfs.0.Data.0.Key 字符串 \
    --SettingConfs.0.Data.0.Value 字符串 \
    --StorageConfs.0.StorageVolPath 字符串 \
    --StorageConfs.0.StorageVolIp 字符串 \
    --StorageConfs.0.StorageVolName 字符串 \
    --PostStart 字符串 \
    --OsFlavour ALPINE
```

Output: 
```
{
    "Response": {
        "RequestId": "422a54ac-9913-4d46-8439-9c05600003b3",
        "Result": "version-success"
    }
}
```

