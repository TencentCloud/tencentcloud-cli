**Example 1: 修改 Deployment**



Input: 

```
tccli ags ModifyDeployment --cli-unfold-argument  \
    --DeploymentId dpl-amfzcemg \
    --LifecycleConfiguration.IdleTimeoutSeconds 30 \
    --LifecycleConfiguration.IdleAction STOP
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
                "IdleTimeoutSeconds": 30
            },
            "ScalingConfiguration": {
                "MaxInstanceCount": 10,
                "MaxInstanceRequestConcurrency": 100,
                "MinInstanceCount": 0
            },
            "Status": "ACTIVE",
            "ToolId": "sdt-95hq0b7k",
            "UpdatedTime": "2026-08-18T03:10:42Z"
        },
        "RequestId": "c24cd623-f7f2-47b2-a5be-e25987405d6d"
    }
}
```

