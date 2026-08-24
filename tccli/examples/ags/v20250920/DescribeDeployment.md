**Example 1: 查询 Deployment**



Input: 

```
tccli ags DescribeDeployment --cli-unfold-argument  \
    --DeploymentId dpl-a1b2c3d4
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

