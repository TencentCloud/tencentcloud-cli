**Example 1: 示例**



Input: 

```
tccli tcb CreateCloudBaseRunServerVersion --cli-unfold-argument  \
    --MaxNum 0 \
    --Branch xx \
    --PackageName xx \
    --MountVolumeInfo.0.ReadOnly True \
    --MountVolumeInfo.0.MountPath xx \
    --MountVolumeInfo.0.Name xx \
    --MountVolumeInfo.0.NfsVolumes.0.Path xx \
    --MountVolumeInfo.0.NfsVolumes.0.ReadOnly True \
    --MountVolumeInfo.0.NfsVolumes.0.Server xx \
    --ImageInfo.ImageUrl xx \
    --ImageInfo.RepositoryName xx \
    --ImageInfo.IsPublic True \
    --ImageInfo.ServerAddr xx \
    --ImageInfo.TagName xx \
    --EnvParams xx \
    --AddIntranetDns True \
    --BuildDir xx \
    --Repository xx \
    --Mem 0.0 \
    --UploadType xx \
    --RepositoryType xx \
    --InitialDelaySeconds 0 \
    --AccessType 0 \
    --CustomLogs xx \
    --FlowRatio 0 \
    --MinNum 0 \
    --VersionRemark xx \
    --ContainerPort 0 \
    --DockerfilePath xx \
    --EnvId xx \
    --ImageSecretInfo.UserName xx \
    --ImageSecretInfo.RegistryServer xx \
    --ImageSecretInfo.Password xx \
    --ImageSecretInfo.Email xx \
    --ServerName xx \
    --EnableUnion True \
    --PackageVersion xx \
    --Cpu 0.0 \
    --ImagePullSecret xx \
    --CodeDetail.Url xx \
    --CodeDetail.Name.FullName xx \
    --CodeDetail.Name.Name xx \
    --PolicyThreshold 0 \
    --EsInfo.Index xx \
    --EsInfo.Account xx \
    --EsInfo.Ip xx \
    --EsInfo.Id 0 \
    --EsInfo.SecretName xx \
    --EsInfo.Password xx \
    --EsInfo.Port 0 \
    --PolicyType xx
```

Output: 
```
{
    "Response": {
        "Result": "xx",
        "VersionName": "xx",
        "RequestId": "xx"
    }
}
```

