**Example 1: success**



Input: 

```
tccli tcbr CreateCloudRunServer --cli-unfold-argument  \
    --EnvId env-sdfsdfdf \
    --ServerName server-sdfsdf \
    --DeployInfo.DeployType package \
    --DeployInfo.ImageUrl  \
    --DeployInfo.PackageName redis \
    --DeployInfo.PackageVersion 234234 \
    --DeployInfo.DeployRemark remark \
    --DeployInfo.RepoInfo.Source source \
    --DeployInfo.RepoInfo.Repo repo \
    --DeployInfo.RepoInfo.Branch main \
    --DeployInfo.BuildPacks.BaseImage  \
    --DeployInfo.BuildPacks.EntryPoint  \
    --DeployInfo.BuildPacks.RepoLanguage  \
    --DeployInfo.BuildPacks.UploadFilename  \
    --DeployInfo.ReleaseType FULL \
    --ServerConfig.EnvId env-sdfsdf \
    --ServerConfig.ServerName server-sdfsf \
    --ServerConfig.OpenAccessTypes OA \
    --ServerConfig.Cpu 0 \
    --ServerConfig.Mem 0 \
    --ServerConfig.MinNum 1 \
    --ServerConfig.MaxNum 1 \
    --ServerConfig.PolicyDetails.0.PolicyType cpu \
    --ServerConfig.PolicyDetails.0.PolicyThreshold 60 \
    --ServerConfig.CustomLogs  \
    --ServerConfig.EnvParams  \
    --ServerConfig.InitialDelaySeconds 1 \
    --ServerConfig.CreateTime 2022-12-12 12:00:00 \
    --ServerConfig.Port 0 \
    --ServerConfig.HasDockerfile True \
    --ServerConfig.Dockerfile Dockerfile \
    --ServerConfig.BuildDir  \
    --ServerConfig.LogType none \
    --ServerConfig.LogSetId  \
    --ServerConfig.LogTopicId  \
    --ServerConfig.LogParseType  \
    --ServerConfig.Tag 
```

Output: 
```
{
    "Response": {
        "RequestId": "d1267757-ade0-42b5-9ea4-42229a580acd",
        "TaskId": 0
    }
}
```

