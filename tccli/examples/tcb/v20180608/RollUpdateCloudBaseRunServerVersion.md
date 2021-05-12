**Example 1: 示例**



Input: 

```
tccli tcb RollUpdateCloudBaseRunServerVersion --cli-unfold-argument  \
    --MaxNum xx \
    --EnvParams xx \
    --PackageName xx \
    --MountVolumeInfo.0.ReadOnly True \
    --MountVolumeInfo.0.MountPath xx \
    --MountVolumeInfo.0.Name xx \
    --MountVolumeInfo.0.NfsVolumes.0.Path xx \
    --MountVolumeInfo.0.NfsVolumes.0.ReadOnly True \
    --MountVolumeInfo.0.NfsVolumes.0.Server xx \
    --Branch xx \
    --Rollback True \
    --BuildDir xx \
    --Repository xx \
    --Mem xx \
    --UploadType xx \
    --RepositoryType xx \
    --InitialDelaySeconds 0 \
    --CustomLogs xx \
    --FlowRatio 0 \
    --MinNum xx \
    --VersionRemark xx \
    --ContainerPort 0 \
    --DockerfilePath xx \
    --EnvId xx \
    --SnapshotName xx \
    --ServerName xx \
    --EnableUnion True \
    --PackageVersion xx \
    --Cpu xx \
    --CodeDetail.Url xx \
    --CodeDetail.Name.FullName xx \
    --CodeDetail.Name.Name xx \
    --ImageInfo.ImageUrl xx \
    --ImageInfo.RepositoryName xx \
    --ImageInfo.IsPublic True \
    --ImageInfo.ServerAddr xx \
    --ImageInfo.TagName xx \
    --PolicyThreshold xx \
    --IsRebuild True \
    --PolicyType xx \
    --VersionName xx
```

Output: 
```
{
    "Response": {
        "Result": "succ",
        "VersionName": "xxx",
        "RunId": "a123",
        "RequestId": "5620b49e-a25a-4007-84ef-03c9035c584d"
    }
}
```

