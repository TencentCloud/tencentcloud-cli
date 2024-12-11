**Example 1: success**



Input: 

```
tccli tcbr CreateCloudRunServer --cli-unfold-argument  \
    --EnvId abc \
    --ServerName abc \
    --DeployInfo.DeployType abc \
    --DeployInfo.ImageUrl abc \
    --DeployInfo.PackageName abc \
    --DeployInfo.PackageVersion abc \
    --DeployInfo.DeployRemark abc \
    --DeployInfo.RepoInfo.Source abc \
    --DeployInfo.RepoInfo.Repo abc \
    --DeployInfo.RepoInfo.Branch abc \
    --DeployInfo.BuildPacks.BaseImage abc \
    --DeployInfo.BuildPacks.EntryPoint abc \
    --DeployInfo.BuildPacks.RepoLanguage abc \
    --DeployInfo.BuildPacks.UploadFilename abc \
    --DeployInfo.ReleaseType abc \
    --ServerConfig.EnvId abc \
    --ServerConfig.ServerName abc \
    --ServerConfig.OpenAccessTypes abc \
    --ServerConfig.Cpu 0 \
    --ServerConfig.Mem 0 \
    --ServerConfig.MinNum 1 \
    --ServerConfig.MaxNum 1 \
    --ServerConfig.PolicyDetails.0.PolicyType abc \
    --ServerConfig.PolicyDetails.0.PolicyThreshold 1 \
    --ServerConfig.CustomLogs abc \
    --ServerConfig.EnvParams abc \
    --ServerConfig.InitialDelaySeconds 1 \
    --ServerConfig.CreateTime abc \
    --ServerConfig.Port 0 \
    --ServerConfig.HasDockerfile True \
    --ServerConfig.Dockerfile abc \
    --ServerConfig.BuildDir abc \
    --ServerConfig.LogType abc \
    --ServerConfig.LogSetId abc \
    --ServerConfig.LogTopicId abc \
    --ServerConfig.LogParseType abc \
    --ServerConfig.Tag abc
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
    --EnvId abc \
    --ServerName abc \
    --DeployInfo.DeployType abc \
    --DeployInfo.ImageUrl abc \
    --DeployInfo.PackageName abc \
    --DeployInfo.PackageVersion abc \
    --DeployInfo.DeployRemark abc \
    --DeployInfo.RepoInfo.Source abc \
    --DeployInfo.RepoInfo.Repo abc \
    --DeployInfo.RepoInfo.Branch abc \
    --DeployInfo.BuildPacks.BaseImage abc \
    --DeployInfo.BuildPacks.EntryPoint abc \
    --DeployInfo.BuildPacks.RepoLanguage abc \
    --DeployInfo.BuildPacks.UploadFilename abc \
    --DeployInfo.ReleaseType abc \
    --ServerConfig.EnvId abc \
    --ServerConfig.ServerName abc \
    --ServerConfig.OpenAccessTypes abc \
    --ServerConfig.Cpu 0 \
    --ServerConfig.Mem 0 \
    --ServerConfig.MinNum 1 \
    --ServerConfig.MaxNum 1 \
    --ServerConfig.PolicyDetails.0.PolicyType abc \
    --ServerConfig.PolicyDetails.0.PolicyThreshold 1 \
    --ServerConfig.CustomLogs abc \
    --ServerConfig.EnvParams abc \
    --ServerConfig.InitialDelaySeconds 1 \
    --ServerConfig.CreateTime abc \
    --ServerConfig.Port 0 \
    --ServerConfig.HasDockerfile True \
    --ServerConfig.Dockerfile abc \
    --ServerConfig.BuildDir abc \
    --ServerConfig.LogType abc \
    --ServerConfig.LogSetId abc \
    --ServerConfig.LogTopicId abc \
    --ServerConfig.LogParseType abc \
    --ServerConfig.Tag abc
```

Output: 
```
{
    "Response": {
        "TaskId": 0,
        "RequestId": "abc"
    }
}
```

