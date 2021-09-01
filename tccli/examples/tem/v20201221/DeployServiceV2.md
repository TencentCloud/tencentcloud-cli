**Example 1: 服务版本部署**

服务版本部署

Input: 

```
tccli tem DeployServiceV2 --cli-unfold-argument  \
    --JvmOpts xx \
    --StorageConfs.0.StorageVolName xx \
    --StorageConfs.0.StorageVolPath xx \
    --ImgRepo xx \
    --EnvConf.0.Value xx \
    --EnvConf.0.Key xx \
    --Description xx \
    --JdkVersion xx \
    --ContainerPort 1 \
    --LogOutputConf.ClsLogTopicId xx \
    --LogOutputConf.ClsLogsetName xx \
    --LogOutputConf.OutputType xx \
    --CpuSpec 0.0 \
    --DeployMode xx \
    --SecurityGroupIds xx \
    --SourceChannel 0 \
    --DeployVersion xx \
    --InitPodNum 1 \
    --VersionDesc xx \
    --MemorySpec 0.0 \
    --LogConfs xx \
    --PkgName xx \
    --StorageMountConfs.0.VolumeName xx \
    --StorageMountConfs.0.MountPath xx \
    --SettingConfs.0.ConfigDataName xx \
    --SettingConfs.0.MountedPath xx \
    --EsInfo.MinAliveInstances 0 \
    --EsInfo.EsStrategy 0 \
    --EsInfo.VersionId xx \
    --EsInfo.Threshold 1 \
    --EsInfo.MaxAliveInstances 2 \
    --ServiceId xx \
    --NamespaceId xx
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

