**Example 1: 示例**

滚动更新

Input: 

```
tccli tcb RollUpdateCloudBaseRunServerVersion --cli-unfold-argument  \
    --EnvId abc \
    --VersionName abc \
    --UploadType abc \
    --RepositoryType abc \
    --FlowRatio 0 \
    --DockerfilePath abc \
    --BuildDir abc \
    --Cpu abc \
    --Mem abc \
    --MinNum abc \
    --MaxNum abc \
    --PolicyType abc \
    --PolicyThreshold abc \
    --EnvParams abc \
    --ContainerPort 0 \
    --ServerName abc \
    --Repository abc \
    --Branch abc \
    --VersionRemark abc \
    --PackageName abc \
    --PackageVersion abc \
    --ImageInfo.RepositoryName abc \
    --ImageInfo.IsPublic True \
    --ImageInfo.TagName abc \
    --ImageInfo.ServerAddr abc \
    --ImageInfo.ImageUrl abc \
    --CodeDetail.Name.Name abc \
    --CodeDetail.Name.FullName abc \
    --CodeDetail.Url abc \
    --IsRebuild True \
    --InitialDelaySeconds 0 \
    --MountVolumeInfo.0.Name abc \
    --MountVolumeInfo.0.MountPath abc \
    --MountVolumeInfo.0.ReadOnly True \
    --MountVolumeInfo.0.NfsVolumes.0.Server abc \
    --MountVolumeInfo.0.NfsVolumes.0.Path abc \
    --MountVolumeInfo.0.NfsVolumes.0.ReadOnly True \
    --MountVolumeInfo.0.NfsVolumes.0.SecretName abc \
    --MountVolumeInfo.0.NfsVolumes.0.EnableEmptyDirVolume True \
    --Rollback True \
    --SnapshotName abc \
    --CustomLogs abc \
    --EnableUnion True \
    --OperatorRemark abc \
    --ServerPath abc \
    --IsUpdateCls True \
    --PolicyDetail.0.PolicyType abc \
    --PolicyDetail.0.PolicyThreshold 0
```

Output: 
```
{
    "Response": {
        "Result": "abc",
        "VersionName": "abc",
        "RunId": "abc",
        "RequestId": "abc"
    }
}
```

