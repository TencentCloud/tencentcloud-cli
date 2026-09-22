**Example 1: 查询 Agent 会话详情**



Input: 

```
tccli workbuddyenterprise DescribeAgentSession --cli-unfold-argument  \
    --SessionId sess-9f3c1a2b7d4e
```

Output: 
```
{
    "Response": {
        "SessionId": "sess-9f3c1a2b7d4e",
        "SessionName": "7 月运营数据汇总",
        "AgentId": "736918300000000001",
        "AgentName": "数据分析助手",
        "VersionId": "2087791755109965825",
        "VersionName": "prod-3",
        "Status": "ACTIVE",
        "Creator": "100012345678",
        "Source": "CLOUD",
        "EndpointSet": [
            {
                "EndpointType": "PUBLIC",
                "Url": "https://736918300000000001-tc-nanjing.example-workbuddy.com"
            }
        ],
        "CreatedTime": "2026-07-20T10:00:00Z",
        "ModifiedTime": "2026-07-20T10:35:00Z",
        "RequestId": "3c6d138e-1234-5678-9abc-def012345678"
    }
}
```

