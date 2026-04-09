**Example 1: 启动沙箱实例**



Input: 

```
tccli ags StartSandboxInstance --cli-unfold-argument  \
    --ToolId sdt-m1v36fnp \
    --Timeout 10m
```

Output: 
```
{
    "Response": {
        "Instance": {
            "CreateTime": "2026-04-09T15:56:22+08:00",
            "ExpiresAt": "2026-04-09T16:06:22+08:00",
            "InstanceId": "6k56rm47ciif3kzljg655rsyuauboyggnqqxv6l6",
            "NetworkMode": "PUBLIC",
            "Status": "RUNNING",
            "TimeoutSeconds": 600,
            "ToolId": "sdt-m1v36fnp",
            "ToolName": "e2e-ops-test-8bdd5d61",
            "UpdateTime": "2026-04-09T15:56:22+08:00"
        },
        "RequestId": "d8856bc9-f668-4837-aeaf-c2747bca46f3"
    }
}
```

