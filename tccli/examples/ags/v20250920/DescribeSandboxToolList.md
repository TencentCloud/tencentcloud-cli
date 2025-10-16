**Example 1: 查询沙箱工具列表**



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

