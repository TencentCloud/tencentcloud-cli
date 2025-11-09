**Example 1: 查询沙箱实例列表**



Input: 

```
tccli ags DescribeSandboxInstanceList --cli-unfold-argument  \
    --ToolId sdt-ee4ywozw \
    --Offset 0 \
    --Limit 20 \
    --Filters.0.Name Status \
    --Filters.0.Values RUNNING
```

Output: 
```
{
    "Response": {
        "InstanceSet": [
            {
                "InstanceId": "12345678123412341234123456789abc",
                "ToolId": "sdt-ee4ywozw",
                "ToolName": "my-browser-tool",
                "Status": "RUNNING",
                "TimeoutSeconds": 600,
                "ExpiresAt": "2024-01-01T10:30:00Z",
                "CreateTime": "2024-01-01T10:00:00Z",
                "UpdateTime": "2024-01-01T10:00:00Z"
            }
        ],
        "TotalCount": 1,
        "RequestId": "12345678123412341234123456789012"
    }
}
```

