**Example 1: UpdateCloudRunServer**



Input: 

```
tccli tcbr UpdateCloudRunServer --cli-unfold-argument  \
    --EnvId env-sdsdf \
    --ServerName server-sdfsdf \
    --DeployInfo.DeployType package \
    --DeployInfo.ImageUrl  \
    --DeployInfo.PackageName redis \
    --DeployInfo.PackageVersion 12324 \
    --DeployInfo.DeployRemark remark \
    --DeployInfo.RepoInfo.Source source \
    --DeployInfo.RepoInfo.Repo repo \
    --DeployInfo.RepoInfo.Branch main \
    --DeployInfo.BuildPacks.BaseImage  \
    --DeployInfo.BuildPacks.EntryPoint  \
    --DeployInfo.BuildPacks.RepoLanguage  \
    --DeployInfo.BuildPacks.UploadFilename  \
    --DeployInfo.ReleaseType FULL \
    --ServerConfig.EnvId env-sdfafa \
    --ServerConfig.ServerName server-sdfafd \
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
    --ServerConfig.CreateTime 2024-12-12 12:22:00 \
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
        "EnvId": "env-sdfsfddf",
        "TaskId": 0,
        "RequestId": "sdfjlskdflkf"
    }
}
```

