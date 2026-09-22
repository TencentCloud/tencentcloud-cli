**Example 1: 查询外部 Agent 列表**



Input: 

```
tccli workbuddyenterprise DescribeExternalAgentList --cli-unfold-argument  \
    --AgentId 736918300000000001 \
    --Filters.0.Name Bound \
    --Filters.0.Values BOUND \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "ExternalAgentSet": [
            {
                "A2AAgentId": "a2a-agent-001",
                "BindingId": "5001",
                "Name": "code-review-bot",
                "Description": "代码评审机器人",
                "IconUrl": "https://example.com/icon.png",
                "Endpoint": "https://a2a.example.com/server",
                "A2AVersion": "1.0",
                "A2ASkillSet": [
                    {
                        "A2ASkillId": "review",
                        "Name": "代码评审",
                        "Description": "按规范评审代码"
                    }
                ],
                "Bound": true
            }
        ],
        "RequestId": "3c6d138e-1234-5678-9abc-def012345678"
    }
}
```

