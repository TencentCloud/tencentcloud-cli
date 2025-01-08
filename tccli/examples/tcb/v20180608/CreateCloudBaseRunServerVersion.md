**Example 1: 示例**

创建版本

Input: 

```
tccli tcb CreateCloudBaseRunServerVersion --cli-unfold-argument  \
    --EnvId env-sdfdf \
    --UploadType package \
    --RepositoryType  \
    --FlowRatio 0 \
    --DockerfilePath  \
    --BuildDir  \
    --Cpu 0 \
    --Mem 0 \
    --MinNum 0 \
    --MaxNum 0 \
    --PolicyType cpu \
    --PolicyThreshold 60 \
    --EnvParams  \
    --ContainerPort 0 \
    --ServerName server-1 \
    --Repository  \
    --Branch  \
    --VersionRemark remark \
    --PackageName test.zip \
    --PackageVersion 1231 \
    --ImageInfo.RepositoryName  \
    --ImageInfo.IsPublic True \
    --ImageInfo.TagName  \
    --ImageInfo.ServerAddr  \
    --ImageInfo.ImageUrl  \
    --CodeDetail.Name.Name  \
    --CodeDetail.Name.FullName  \
    --CodeDetail.Url  \
    --ImageSecretInfo.RegistryServer  \
    --ImageSecretInfo.UserName  \
    --ImageSecretInfo.Password  \
    --ImageSecretInfo.Email  \
    --ImagePullSecret  \
    --CustomLogs  \
    --InitialDelaySeconds 0 \
    --MountVolumeInfo.0.Name  \
    --MountVolumeInfo.0.MountPath  \
    --MountVolumeInfo.0.ReadOnly True \
    --MountVolumeInfo.0.NfsVolumes.0.Server  \
    --MountVolumeInfo.0.NfsVolumes.0.Path  \
    --MountVolumeInfo.0.NfsVolumes.0.ReadOnly True \
    --MountVolumeInfo.0.NfsVolumes.0.SecretName  \
    --MountVolumeInfo.0.NfsVolumes.0.EnableEmptyDirVolume True \
    --AccessType 0 \
    --EsInfo.Id 0 \
    --EsInfo.SecretName server \
    --EsInfo.Ip  \
    --EsInfo.Port 0 \
    --EsInfo.Index  \
    --EsInfo.Account  \
    --EsInfo.Password  \
    --EnableUnion True \
    --OperatorRemark remark \
    --ServerPath  \
    --ImageReuseKey  \
    --SidecarSpecs.0.ContainerImage  \
    --SidecarSpecs.0.ContainerPort 0 \
    --SidecarSpecs.0.ContainerName  \
    --SidecarSpecs.0.EnvVar  \
    --SidecarSpecs.0.InitialDelaySeconds 0 \
    --SidecarSpecs.0.Cpu 0 \
    --SidecarSpecs.0.Mem 0 \
    --SidecarSpecs.0.VolumeMountInfos.0.Name  \
    --SidecarSpecs.0.VolumeMountInfos.0.MountPath  \
    --SidecarSpecs.0.VolumeMountInfos.0.ReadOnly True \
    --SidecarSpecs.0.VolumeMountInfos.0.NfsVolumes.0.Server  \
    --SidecarSpecs.0.VolumeMountInfos.0.NfsVolumes.0.Path  \
    --SidecarSpecs.0.VolumeMountInfos.0.NfsVolumes.0.ReadOnly True \
    --SidecarSpecs.0.VolumeMountInfos.0.NfsVolumes.0.SecretName server \
    --SidecarSpecs.0.VolumeMountInfos.0.NfsVolumes.0.EnableEmptyDirVolume True \
    --ServiceVolumes.0.Name  \
    --ServiceVolumes.0.NFS.Server  \
    --ServiceVolumes.0.NFS.Path  \
    --ServiceVolumes.0.NFS.ReadOnly True \
    --ServiceVolumes.0.NFS.SecretName  \
    --ServiceVolumes.0.NFS.EnableEmptyDirVolume True \
    --ServiceVolumes.0.SecretName server \
    --ServiceVolumes.0.EnableEmptyDirVolume True \
    --ServiceVolumes.0.EmptyDir.EnableEmptyDirVolume True \
    --ServiceVolumes.0.EmptyDir.Medium  \
    --ServiceVolumes.0.EmptyDir.SizeLimit  \
    --ServiceVolumes.0.HostPath.Path  \
    --IsCreateJnsGw 0 \
    --ServiceVolumeMounts.0.Name  \
    --ServiceVolumeMounts.0.MountPath  \
    --ServiceVolumeMounts.0.ReadOnly True \
    --ServiceVolumeMounts.0.SubPath  \
    --ServiceVolumeMounts.0.MountPropagation  \
    --HasDockerfile 0 \
    --BaseImage  \
    --EntryPoint  \
    --RepoLanguage  \
    --UploadFilename  \
    --PolicyDetail.0.PolicyType cpu \
    --PolicyDetail.0.PolicyThreshold 0
```

Output: 
```
{
    "Response": {
        "Result": "",
        "VersionName": "version-001",
        "RunId": "",
        "RequestId": "sdfsdfdf"
    }
}
```

