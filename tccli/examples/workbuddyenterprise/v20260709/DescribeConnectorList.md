**Example 1: 查询连接器列表**

按名称模糊过滤并分页查询连接器列表，Offset/Limit 为标准分页参数

Input: 

```
tccli workbuddyenterprise DescribeConnectorList --cli-unfold-argument  \
    --Offset 0 \
    --Limit 20 \
    --Filters.0.Name Name \
    --Filters.0.Values notion
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "ConnectorSet": [
            {
                "ConnectorId": "2087791755109965900",
                "ConnectorSlug": "notion-k3x9m2",
                "ConnectorKey": "notion-k3x9m2-v2",
                "Name": "notion",
                "Description": "接入企业 Notion",
                "AvatarUrl": "https://example.com/icon.png",
                "Source": "ENTERPRISE_AGENT",
                "EnterpriseId": "100012345678",
                "Type": "MCP_SERVER",
                "ServiceUrl": "https://mcp.notion.internal/v2",
                "AuthModes": [
                    "ONEID"
                ],
                "LatestVersionNo": 2,
                "Status": "ACTIVE",
                "CreatorId": "100012345678",
                "CreatedTime": "2026-08-26T09:10:03Z",
                "ModifiedTime": "2026-08-26T11:20:44Z"
            }
        ],
        "RequestId": "3c6d138e-1234-5678-9abc-def012345678"
    }
}
```

