**Example 1: 查询实例声明的访问策略**

返回实例自己声明的访问策略，不包含 Tool 与 Instance 合并后的内部结果。

Input: 

```
tccli ags DescribeSandboxInstanceList --cli-unfold-argument  \
    --InstanceIds ins-policy123
```

Output: 
```
{
    "Response": {
        "InstanceSet": [
            {
                "InstanceId": "ins-policy123",
                "ToolId": "sdt-policy123",
                "ToolName": "browser-policy-sandbox",
                "Status": "RUNNING"
            }
        ],
        "TotalCount": 1,
        "RequestId": "req-describe-instance-policy-example"
    }
}
```

**Example 2: 查询沙箱实例列表**



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

