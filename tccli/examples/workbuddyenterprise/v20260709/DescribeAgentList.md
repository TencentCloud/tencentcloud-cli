**Example 1: 查询 Agent 列表**

按名称模糊过滤并按创建时间倒序查询 Agent 列表

Input: 

```
tccli workbuddyenterprise DescribeAgentList --cli-unfold-argument  \
    --Offset 0 \
    --Limit 20 \
    --Filters.0.Name AgentName \
    --Filters.0.Values 数据分析 \
    --Filters.0.ExactMatch False \
    --SortBy created_at \
    --SortDirection DESC
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "AgentSet": [
            {
                "AgentId": "736918300000000001",
                "AgentName": "数据分析助手",
                "Description": "负责每日运营数据的汇总与分析",
                "AvatarUrl": "https://example.com/avatar/agent-001.png",
                "CreatedTime": "2026-06-01T09:00:00Z",
                "ModifiedTime": "2026-09-10T15:20:00Z",
                "A2AEnabled": true,
                "A2AEndpoint": "https://a2a.example.workbuddy.com/agents/736918300000000001/.well-known/agent-card.json",
                "A2AStatus": "REGISTERED",
                "PublicApiEnabled": true,
                "PublicApiUrl": "https://736918300000000001-tc-nanjing.example-workbuddy.com",
                "CreatorUin": "100012345678",
                "AccountId": "1438693592234206274",
                "SessionCount": 42,
                "Model": "hunyuan-turbos-latest",
                "LatestVersionId": "2087791755109965825",
                "LatestVersionName": "prod-3"
            }
        ],
        "RequestId": "3c6d138e-1234-5678-9abc-def012345678"
    }
}
```

