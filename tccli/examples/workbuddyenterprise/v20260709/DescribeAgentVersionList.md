**Example 1: 查询 Agent 版本列表**



Input: 

```
tccli workbuddyenterprise DescribeAgentVersionList --cli-unfold-argument  \
    --AgentId 736918300000000001 \
    --Offset 0 \
    --Limit 20 \
    --Filters.0.Name VersionType \
    --Filters.0.Values PROD
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "AgentVersionSet": [
            {
                "VersionId": "2087791755109965825",
                "VersionName": "prod-3",
                "VersionType": "PROD",
                "Model": "hunyuan-turbos-latest",
                "SandboxTemplateId": "sbt-001",
                "Status": "ENABLED",
                "SessionCount": 42,
                "CreatedTime": "2026-08-01T10:00:00Z",
                "ModifiedTime": "2026-08-10T15:30:00Z"
            }
        ],
        "RequestId": "3c6d138e-1234-5678-9abc-def012345678"
    }
}
```

