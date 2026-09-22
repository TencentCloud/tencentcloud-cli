**Example 1: 查询专家列表**



Input: 

```
tccli workbuddyenterprise DescribeExpertList --cli-unfold-argument  \
    --Source CUSTOM \
    --Offset 0 \
    --Limit 20 \
    --Filters.0.Name Keyword \
    --Filters.0.Values 数据库
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "ExpertSet": [
            {
                "Source": "CUSTOM",
                "ExpertId": "expert-001",
                "DisplayName": "数据库优化专家",
                "Description": "SQL 优化与索引设计",
                "Icon": "https://example.com/icon/db-optimization.png",
                "ExpertVersion": "1.0.1",
                "Enabled": true,
                "DownloadUrl": "https://cos.example.com/signed-url",
                "ModifiedTime": "2026-07-25T09:15:00Z"
            }
        ],
        "Counts": {
            "Builtin": 6,
            "Custom": 1,
            "Total": 7
        },
        "RequestId": "3c6d138e-1234-5678-9abc-def012345678"
    }
}
```

