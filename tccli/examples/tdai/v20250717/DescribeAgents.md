**Example 1: 查询智能体列表**



Input: 

```
tccli tdai DescribeAgents --cli-unfold-argument  \
    --AgentId agt-xpcn2t3e \
    --AgentName sqlAgent测试 \
    --AgentInternalName aid \
    --AgentStatus normal \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "AgentId": "agt-xpcn2t3e",
                "AgentName": "sqlAgent测试",
                "AgentInternalName": "aid",
                "AgentStatus": "normal",
                "DefaultVersion": "v1.0.0",
                "AgentType": "chat",
                "Description": "风险SQL治理Agent",
                "Creator": "calvinliao",
                "CreateTime": "2025-05-27 20:43:51",
                "Updater": "calvinliao",
                "UpdateTime": "2025-05-27 20:44:17"
            }
        ],
        "RequestId": "d8007300-6b36-5418-f3aa-257d7b263031",
        "TotalCount": 1
    }
}
```

