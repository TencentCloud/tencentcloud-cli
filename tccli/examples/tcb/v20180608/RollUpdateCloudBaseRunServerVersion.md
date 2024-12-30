**Example 1: 示例**

滚动更新

Input: 

```
tccli tcb RollUpdateCloudBaseRunServerVersion --cli-unfold-argument  \
    --EnvId  \
    --VersionName  \
    --UploadType  \
    --RepositoryType  \
    --FlowRatio 0 \
    --DockerfilePath  \
    --BuildDir  \
    --Cpu  \
    --Mem  \
    --MinNum  \
    --MaxNum  \
    --PolicyType  \
    --PolicyThreshold  \
    --EnvParams  \
    --ContainerPort 0 \
    --ServerName  \
    --Repository  \
    --Branch  \
    --VersionRemark  \
    --PackageName  \
    --PackageVersion  \
    --ImageInfo.RepositoryName  \
    --ImageInfo.IsPublic True \
    --ImageInfo.TagName  \
    --ImageInfo.ServerAddr  \
    --ImageInfo.ImageUrl  \
    --CodeDetail.Name.Name  \
    --CodeDetail.Name.FullName  \
    --CodeDetail.Url  \
    --IsRebuild True \
    --InitialDelaySeconds 0 \
    --MountVolumeInfo.0.Name  \
    --MountVolumeInfo.0.MountPath  \
    --MountVolumeInfo.0.ReadOnly True \
    --MountVolumeInfo.0.NfsVolumes.0.Server  \
    --MountVolumeInfo.0.NfsVolumes.0.Path  \
    --MountVolumeInfo.0.NfsVolumes.0.ReadOnly True \
    --MountVolumeInfo.0.NfsVolumes.0.SecretName  \
    --MountVolumeInfo.0.NfsVolumes.0.EnableEmptyDirVolume True \
    --Rollback True \
    --SnapshotName  \
    --CustomLogs  \
    --EnableUnion True \
    --OperatorRemark  \
    --ServerPath  \
    --IsUpdateCls True \
    --PolicyDetail.0.PolicyType  \
    --PolicyDetail.0.PolicyThreshold 0
```

Output: 
```
{
    "Response": {
        "Result": "succ",
        "VersionName": "version",
        "RunId": "",
        "RequestId": "sdfasfaf"
    }
}
```

