**Example 1: 示例**

创建版本

Input: 

```
tccli tcb CreateCloudBaseRunServerVersion --cli-unfold-argument  \
    --EnvId abc \
    --UploadType abc \
    --RepositoryType abc \
    --FlowRatio 0 \
    --DockerfilePath abc \
    --BuildDir abc \
    --Cpu 0 \
    --Mem 0 \
    --MinNum 0 \
    --MaxNum 0 \
    --PolicyType abc \
    --PolicyThreshold 0 \
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
    --ImageSecretInfo.RegistryServer abc \
    --ImageSecretInfo.UserName abc \
    --ImageSecretInfo.Password abc \
    --ImageSecretInfo.Email abc \
    --ImagePullSecret abc \
    --CustomLogs abc \
    --InitialDelaySeconds 0 \
    --MountVolumeInfo.0.Name abc \
    --MountVolumeInfo.0.MountPath abc \
    --MountVolumeInfo.0.ReadOnly True \
    --MountVolumeInfo.0.NfsVolumes.0.Server abc \
    --MountVolumeInfo.0.NfsVolumes.0.Path abc \
    --MountVolumeInfo.0.NfsVolumes.0.ReadOnly True \
    --MountVolumeInfo.0.NfsVolumes.0.SecretName abc \
    --MountVolumeInfo.0.NfsVolumes.0.EnableEmptyDirVolume True \
    --AccessType 0 \
    --EsInfo.Id 0 \
    --EsInfo.SecretName abc \
    --EsInfo.Ip abc \
    --EsInfo.Port 0 \
    --EsInfo.Index abc \
    --EsInfo.Account abc \
    --EsInfo.Password abc \
    --EnableUnion True \
    --OperatorRemark abc \
    --ServerPath abc \
    --ImageReuseKey abc \
    --SidecarSpecs.0.ContainerImage abc \
    --SidecarSpecs.0.ContainerPort 0 \
    --SidecarSpecs.0.ContainerName abc \
    --SidecarSpecs.0.EnvVar abc \
    --SidecarSpecs.0.InitialDelaySeconds 0 \
    --SidecarSpecs.0.Cpu 0 \
    --SidecarSpecs.0.Mem 0 \
    --SidecarSpecs.0.Security.Capabilities.Add abc \
    --SidecarSpecs.0.Security.Capabilities.Drop abc \
    --SidecarSpecs.0.VolumeMountInfos.0.Name abc \
    --SidecarSpecs.0.VolumeMountInfos.0.MountPath abc \
    --SidecarSpecs.0.VolumeMountInfos.0.ReadOnly True \
    --SidecarSpecs.0.VolumeMountInfos.0.NfsVolumes.0.Server abc \
    --SidecarSpecs.0.VolumeMountInfos.0.NfsVolumes.0.Path abc \
    --SidecarSpecs.0.VolumeMountInfos.0.NfsVolumes.0.ReadOnly True \
    --SidecarSpecs.0.VolumeMountInfos.0.NfsVolumes.0.SecretName abc \
    --SidecarSpecs.0.VolumeMountInfos.0.NfsVolumes.0.EnableEmptyDirVolume True \
    --Security.Capabilities.Add abc \
    --Security.Capabilities.Drop abc \
    --ServiceVolumes.0.Name abc \
    --ServiceVolumes.0.NFS.Server abc \
    --ServiceVolumes.0.NFS.Path abc \
    --ServiceVolumes.0.NFS.ReadOnly True \
    --ServiceVolumes.0.NFS.SecretName abc \
    --ServiceVolumes.0.NFS.EnableEmptyDirVolume True \
    --ServiceVolumes.0.SecretName abc \
    --ServiceVolumes.0.EnableEmptyDirVolume True \
    --ServiceVolumes.0.EmptyDir.EnableEmptyDirVolume True \
    --ServiceVolumes.0.EmptyDir.Medium abc \
    --ServiceVolumes.0.EmptyDir.SizeLimit abc \
    --IsCreateJnsGw 0 \
    --ServiceVolumeMounts.0.Name abc \
    --ServiceVolumeMounts.0.MountPath abc \
    --ServiceVolumeMounts.0.ReadOnly True \
    --ServiceVolumeMounts.0.SubPath abc \
    --ServiceVolumeMounts.0.MountPropagation abc \
    --HasDockerfile 0 \
    --BaseImage abc \
    --EntryPoint abc \
    --RepoLanguage abc \
    --UploadFilename abc \
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

