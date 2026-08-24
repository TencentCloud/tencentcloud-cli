**Example 1: 创建 Deployment**



Input: 

```
tccli ags CreateDeployment --cli-unfold-argument  \
    --DeploymentName workspace-service \
    --ToolId sdt-a1b2c3d4 \
    --LifecycleConfiguration.IdleTimeoutSeconds 300 \
    --LifecycleConfiguration.IdleAction PAUSE \
    --AffinityConfiguration.Mode EXCLUSIVE
```

Output: 
```
{
    "Response": {
        "Deployment": {
            "DeploymentId": "dpl-a1b2c3d4",
            "DeploymentName": "workspace-service",
            "ToolId": "sdt-a1b2c3d4",
            "ScalingConfiguration": {
                "MinInstanceCount": 0,
                "MaxInstanceCount": 10,
                "MaxInstanceRequestConcurrency": 100
            },
            "LifecycleConfiguration": {
                "IdleTimeoutSeconds": 300,
                "IdleAction": "PAUSE"
            },
            "AffinityConfiguration": {
                "Mode": "EXCLUSIVE",
                "HeaderName": "X-Tencent-Agr-Affinity-Id"
            },
            "Status": "ACTIVE",
            "CreatedTime": "2026-08-06T08:00:00Z",
            "UpdatedTime": "2026-08-06T08:00:00Z"
        },
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

**Example 2: 创建 Deployment - 2**



Input: 

```
tccli ags CreateDeployment --cli-unfold-argument  \
    --DeploymentName hello \
    --ToolId sdt-95hq0b7k
```

Output: 
```
{
    "Response": {
        "Deployment": {
            "CreatedTime": "2026-08-18T03:08:11Z",
            "DeploymentId": "dpl-amfzcemg",
            "DeploymentName": "hello",
            "LifecycleConfiguration": {
                "IdleAction": "STOP",
                "IdleTimeoutSeconds": 300
            },
            "ScalingConfiguration": {
                "MaxInstanceCount": 10,
                "MaxInstanceRequestConcurrency": 100,
                "MinInstanceCount": 0
            },
            "Status": "ACTIVE",
            "ToolId": "sdt-95hq0b7k",
            "UpdatedTime": "2026-08-18T03:08:11Z"
        },
        "RequestId": "2fda2af5-a50e-465e-bc71-849828d9b1f2"
    }
}
```

