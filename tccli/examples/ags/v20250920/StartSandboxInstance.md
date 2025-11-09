**Example 1: 启动沙箱实例**



Input: 

```
tccli ags StartSandboxInstance --cli-unfold-argument  \
    --ToolId sdt-ee4ywozw \
    --Timeout 10m \
    --ClientToken instance-token-456
```

Output: 
```
{
    "Response": {
        "Instance": {
            "InstanceId": "12345678123412341234123456789abc",
            "ToolId": "sdt-ee4ywozw",
            "ToolName": "my-browser-tool",
            "Status": "RUNNING",
            "TimeoutSeconds": 600,
            "ExpiresAt": "2024-01-01T10:30:00Z",
            "CreateTime": "2024-01-01T10:00:00Z",
            "UpdateTime": "2024-01-01T10:00:00Z"
        },
        "RequestId": "12345678123412341234123456789012"
    }
}
```

