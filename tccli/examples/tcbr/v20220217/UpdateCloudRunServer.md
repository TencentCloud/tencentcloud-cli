**Example 1: UpdateCloudRunServer**



Input: 

```
tccli tcbr UpdateCloudRunServer --cli-unfold-argument  \
    --ServerName xx \
    --EnvId xx \
    --ServerConfig.EnvId xx \
    --ServerConfig.MaxNum 1 \
    --ServerConfig.BuildDir xx \
    --ServerConfig.Mem 0.0 \
    --ServerConfig.ServerName xx \
    --ServerConfig.InitialDelaySeconds 1 \
    --ServerConfig.CustomLogs xx \
    --ServerConfig.CreateTime xx \
    --ServerConfig.MinNum 1 \
    --ServerConfig.HasDockerfile True \
    --ServerConfig.EnvParams xx \
    --ServerConfig.Dockerfile xx \
    --ServerConfig.Port xx \
    --ServerConfig.Cpu 0.0 \
    --DeployInfo.DeployType xx \
    --DeployInfo.DeployRemark xx \
    --DeployInfo.ImageUrl xx \
    --DeployInfo.BuildPacks.UploadFilename xx \
    --DeployInfo.BuildPacks.EntryPoint xx \
    --DeployInfo.BuildPacks.RepoLanguage xx \
    --DeployInfo.BuildPacks.BaseImage xx \
    --DeployInfo.RepoInfo.Repo xx \
    --DeployInfo.RepoInfo.Source xx \
    --DeployInfo.RepoInfo.Branch xx \
    --DeployInfo.PackageVersion xx \
    --DeployInfo.PackageName xx
```

Output: 
```
{
    "Response": {
        "EnvId": "xx",
        "RequestId": "xx",
        "TaskId": 0
    }
}
```

