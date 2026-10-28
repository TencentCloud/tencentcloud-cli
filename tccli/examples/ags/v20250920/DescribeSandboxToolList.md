**Example 1: 按访问策略查询沙箱工具**

按关联的访问策略 ID 反向查询沙箱工具。

Input: 

```
tccli ags DescribeSandboxToolList --cli-unfold-argument  \
    --Filters.0.Name access-policy-id \
    --Filters.0.Values ap-2j6p7q8r \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "SandboxToolSet": [
            {
                "ToolId": "sdt-policy123",
                "ToolName": "browser-policy-sandbox",
                "ToolType": "browser",
                "Status": "ACTIVE",
                "Description": "浏览器沙箱环境",
                "Tags": []
            }
        ],
        "TotalCount": 1,
        "RequestId": "req-describe-tool-policy-example"
    }
}
```

**Example 2: 查询沙箱工具入口配置**

返回 Tool 当前声明的 L1 入口上限。

Input: 

```
tccli ags DescribeSandboxToolList --cli-unfold-argument  \
    --ToolIds sdt-k4m8q2vz
```

Output: 
```
{
    "Response": {
        "SandboxToolSet": [
            {
                "ToolId": "sdt-k4m8q2vz",
                "ToolName": "private-browser-sandbox",
                "ToolType": "browser",
                "Status": "ACTIVE",
                "Description": "私网浏览器沙箱",
                "Tags": []
            }
        ],
        "TotalCount": 1,
        "RequestId": "0d58d01d-67d3-466e-84e2-a4375c728b9c"
    }
}
```

**Example 3: 查询沙箱工具列表**



Input: 

```
tccli ags DescribeSandboxToolList --cli-unfold-argument  \
    --ToolIds sdt-ee4ywozw sdt-another123
```

Output: 
```
{
    "Response": {
        "SandboxToolSet": [
            {
                "ToolId": "sdt-ee4ywozw",
                "ToolName": "browser-sandbox",
                "ToolType": "browser",
                "Status": "ACTIVE",
                "Description": "浏览器沙箱环境",
                "Tags": [],
                "CreateTime": "2024-01-15T10:30:00Z",
                "UpdateTime": "2024-01-15T10:30:00Z"
            }
        ],
        "TotalCount": 1,
        "RequestId": "custom-request-id-123"
    }
}
```

