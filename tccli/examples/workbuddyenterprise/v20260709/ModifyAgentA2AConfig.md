**Example 1: 修改 Agent 的 A2A 配置**



Input: 

```
tccli workbuddyenterprise ModifyAgentA2AConfig --cli-unfold-argument  \
    --AgentId 736918300000000001 \
    --A2AEnabled True \
    --A2ASkillSet.0.A2ASkillId faq \
    --A2ASkillSet.0.Name 常见问答 \
    --A2ASkillSet.0.Description 客户常见问题解答
```

Output: 
```
{
    "Response": {
        "AgentId": "736918300000000001",
        "AgentName": "客服助手",
        "Description": "自动回复客户问题",
        "AvatarUrl": "https://cos.example.com/avatar.png",
        "IsDebug": false,
        "RoutingSet": [
            {
                "VersionId": "2087791755109965825",
                "Weight": 1.0
            }
        ],
        "CreatedTime": "2026-08-01T10:00:00Z",
        "ModifiedTime": "2026-08-10T15:30:00Z",
        "A2AConfig": {
            "A2AEnabled": true,
            "A2APublicRef": "a2a://workbuddy/736918300000000001",
            "A2AEndpoint": "https://a2a.example.com/card/736918300000000001",
            "A2AStatus": "REGISTERED"
        },
        "RequestId": "3c6d138e-1234-5678-9abc-def012345678"
    }
}
```

