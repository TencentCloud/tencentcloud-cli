**Example 1: 启动沙箱实例**



Input: 

```
tccli ags StartSandboxInstance --cli-unfold-argument  \
    --ToolName test_tool
```

Output: 
```
{
    "Response": {
        "Instance": {
            "AuthMode": "DEFAULT",
            "CreateTime": "2026-08-06T08:10:44+08:00",
            "CustomConfiguration": {
                "Args": [
                    "-c"
                ],
                "Command": [
                    "/bin/bash"
                ],
                "Image": "ccr.ccs.tencentyun.com/******************:2.19-alpine-with-envd",
                "ImageDigest": "sha256:8c14af9fd97819411ea7368c8c9b85823085c8abf911675cfa16c5475d1b627c",
                "ImageRegistryType": "personal",
                "Ports": [
                    {
                        "Name": "http",
                        "Port": 8080,
                        "Protocol": "TCP"
                    }
                ],
                "Probe": {
                    "FailureThreshold": 10,
                    "HttpGet": {
                        "Path": "/health",
                        "Port": 49983,
                        "Scheme": "HTTP"
                    },
                    "ProbePeriodMs": 3000,
                    "ProbeTimeoutMs": 1000,
                    "ReadyTimeoutMs": 30000,
                    "SuccessThreshold": 1
                },
                "Resources": {
                    "CPU": "1000m",
                    "Memory": "500Mi",
                    "Storage": "1024Mi"
                }
            },
            "ExpiresAt": "2026-08-06T08:15:40+08:00",
            "InstanceId": "v4bstpofq5tkvgsaywzkscssvoftz4q4mh6c5jdr",
            "NetworkMode": "PUBLIC",
            "Persistent": false,
            "Status": "RUNNING",
            "TimeoutSeconds": 300,
            "ToolId": "sdt-********",
            "ToolName": "test_tool",
            "UpdateTime": "2026-08-06T08:10:44+08:00"
        },
        "RequestId": "2fb58122-4e85-4640-b0ed-16af015e0bae"
    }
}
```

