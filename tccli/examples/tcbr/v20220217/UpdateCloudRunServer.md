**Example 1: 通过镜像更新云托管服务**



Input: 

```
tccli tcbr UpdateCloudRunServer --cli-unfold-argument  \
    --ServerName nginx \
    --DeployInfo.DeployType image \
    --DeployInfo.ImageUrl nginx \
    --DeployInfo.ReleaseType FULL \
    --EnvId lowcode-9g2o448afxxxxxx \
    --Items.0.Key HasDockerfile \
    --Items.0.BoolValue True
```

Output: 
```
{
    "Response": {
        "EnvId": "lowcode-9g2o448afxxxxxx",
        "TaskId": 0,
        "RequestId": "f205956f-7eee-4846-b4c4-xxxxxxx"
    }
}
```

**Example 2: 通过源码更新云托管服务**



Input: 

```
tccli tcbr UpdateCloudRunServer --cli-unfold-argument  \
    --ServerName express \
    --DeployInfo.DeployType package \
    --DeployInfo.PackageName express.zip \
    --DeployInfo.PackageVersion 1766483290 \
    --DeployInfo.ReleaseType FULL \
    --EnvId lowcode-9g2o448afxxxxxx \
    --Items.0.Key HasDockerfile \
    --Items.0.BoolValue True
```

Output: 
```
{
    "Response": {
        "EnvId": "lowcode-9g2o448afxxxxxx",
        "TaskId": 0,
        "RequestId": "f205956f-7eee-4846-b4c4-xxxxxxx"
    }
}
```

