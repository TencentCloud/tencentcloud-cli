**Example 1: 基于镜像创建云托管服务**



Input: 

```
tccli tcbr CreateCloudRunServer --cli-unfold-argument  \
    --ServerName nginx \
    --DeployInfo.DeployType image \
    --DeployInfo.ImageUrl nginx \
    --EnvId lowcode-9g2o448axxxxx \
    --Items.0.Key Port \
    --Items.0.IntValue 80 \
    --Items.1.Key AccessTypes \
    --Items.1.ArrayValue OA PUBLIC MINIAPP \
    --Items.2.Key InternalAccess \
    --Items.2.Value close \
    --Items.3.Key CpuSpecs \
    --Items.3.FloatValue 1 \
    --Items.4.Key MemSpecs \
    --Items.4.FloatValue 2 \
    --Items.5.Key LogPath \
    --Items.5.Value stdout \
    --Items.6.Key OperationMode \
    --Items.6.Value alwaysScale \
    --Items.7.Key MinNum \
    --Items.7.IntValue 0 \
    --Items.8.Key MaxNum \
    --Items.8.IntValue 5 \
    --Items.9.Key PolicyDetails \
    --Items.10.Key Cmd \
    --Items.11.Key EntryPoint
```

Output: 
```
{
    "Response": {
        "RequestId": "d1267757-ade0-42b5-9ea4-xxxxxxx",
        "TaskId": 0
    }
}
```

**Example 2: 基于zip包源码部署云托管服务**



Input: 

```
tccli tcbr CreateCloudRunServer --cli-unfold-argument  \
    --ServerName express \
    --DeployInfo.DeployType package \
    --DeployInfo.PackageName express.zip \
    --DeployInfo.PackageVersion 1766482739 \
    --EnvId lowcode-9g2o448axxxxx \
    --Items.0.Key Port \
    --Items.0.IntValue 3000 \
    --Items.1.Key Dockerfile \
    --Items.1.Value Dockerfile \
    --Items.2.Key AccessTypes \
    --Items.2.ArrayValue OA PUBLIC MINIAPP \
    --Items.3.Key InternalAccess \
    --Items.3.Value close \
    --Items.4.Key CpuSpecs \
    --Items.4.FloatValue 1 \
    --Items.5.Key MemSpecs \
    --Items.5.FloatValue 2 \
    --Items.6.Key LogPath \
    --Items.6.Value stdout \
    --Items.7.Key OperationMode \
    --Items.7.Value alwaysScale \
    --Items.8.Key MinNum \
    --Items.8.IntValue 0 \
    --Items.9.Key MaxNum \
    --Items.9.IntValue 5 \
    --Items.10.Key PolicyDetails \
    --Items.11.Key Cmd \
    --Items.12.Key EntryPoint
```

Output: 
```
{
    "Response": {
        "RequestId": "d1267757-ade0-42b5-9ea4-xxxxxxx",
        "TaskId": 0
    }
}
```

