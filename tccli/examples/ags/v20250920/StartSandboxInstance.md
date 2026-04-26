**Example 1: 成功启动实例**



Input: 

```
tccli ags StartSandboxInstance --cli-unfold-argument  \
    --ToolName test-abc
```

Output: 
```
{
    "Response": {
        "Instance": {
            "AuthMode": "DEFAULT",
            "CreateTime": "2026-04-14T21:12:48+08:00",
            "CustomConfiguration": {
                "Args": [
                    "-g"
                ],
                "Command": [
                    "nginx"
                ],
                "Image": "ccr.ccs.tencentyun.com/library/nginx:alpine",
                "ImageDigest": "sha256:e7e5b7fa7a0b1ab2f59d6066092a6d35984864cc8baf2caf7c088ee409657e57",
                "ImageRegistryType": "personal",
                "Probe": {
                    "FailureThreshold": 10,
                    "HttpGet": {
                        "Path": "/",
                        "Port": 80,
                        "Scheme": "HTTP"
                    },
                    "ProbePeriodMs": 1000,
                    "ProbeTimeoutMs": 1000,
                    "ReadyTimeoutMs": 30000,
                    "SuccessThreshold": 1
                },
                "Resources": {
                    "CPU": "1",
                    "Memory": "1Gi"
                }
            },
            "ExpiresAt": "2026-04-14T22:02:46+08:00",
            "InstanceId": "f72t34xiwxop6rpcunzbs3lnlqxjscawrihz26bn",
            "NetworkMode": "PUBLIC",
            "Persistent": false,
            "Status": "RUNNING",
            "TimeoutSeconds": 3600,
            "ToolId": "sdt-m6abdmgv",
            "ToolName": "test-abc",
            "UpdateTime": "2026-04-14T21:12:48+08:00"
        },
        "RequestId": "3a2c71e2-869c-4117-9239-5362b928d568"
    }
}
```

