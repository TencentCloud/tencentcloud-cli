**Example 1: success**



Input: 

```
tccli tcbr CreateCloudRunServer --cli-unfold-argument  \
    --DeployInfo.DeployType 字符串 \
    --DeployInfo.DeployRemark 字符串 \
    --DeployInfo.ImageUrl 字符串 \
    --DeployInfo.BuildPacks.UploadFilename 字符串 \
    --DeployInfo.BuildPacks.EntryPoint 字符串 \
    --DeployInfo.BuildPacks.RepoLanguage 字符串 \
    --DeployInfo.BuildPacks.BaseImage 字符串 \
    --DeployInfo.RepoInfo.Repo 字符串 \
    --DeployInfo.RepoInfo.Source 字符串 \
    --DeployInfo.RepoInfo.Branch 字符串 \
    --DeployInfo.PackageVersion 字符串 \
    --DeployInfo.PackageName 字符串 \
    --ServerName 字符串 \
    --EnvId 字符串 \
    --ServerConfig.HasDockerfile false \
    --ServerConfig.MaxNum 1 \
    --ServerConfig.BuildDir 字符串 \
    --ServerConfig.ServerName 字符串 \
    --ServerConfig.InitialDelaySeconds 1 \
    --ServerConfig.CustomLogs 字符串 \
    --ServerConfig.CreateTime 字符串 \
    --ServerConfig.Mem 1 \
    --ServerConfig.MinNum 1 \
    --ServerConfig.EnvId 字符串 \
    --ServerConfig.EnvParams 字符串 \
    --ServerConfig.Dockerfile 字符串 \
    --ServerConfig.Port 字符串
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

**Example 2: CreateCloudRunServer**



Input: 

```
tccli tcbr CreateCloudRunServer --cli-unfold-argument  \
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
        "RequestId": "xx",
        "TaskId": 0
    }
}
```

