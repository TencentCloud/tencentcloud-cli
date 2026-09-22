**Example 1: 修改 Agent 路由配置**



Input: 

```
tccli workbuddyenterprise ModifyAgentRouting --cli-unfold-argument  \
    --AgentId 736918300000000001 \
    --RoutingSet.0.VersionId 2087791755109965825 \
    --RoutingSet.0.Weight 0.8 \
    --RoutingSet.1.VersionId 2087791755109965826 \
    --RoutingSet.1.Weight 0.2
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
                "Weight": 0.8
            },
            {
                "VersionId": "2087791755109965826",
                "Weight": 0.2
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
        "AccountId": "1438693592234206274",
        "RequestId": "3c6d138e-1234-5678-9abc-def012345678"
    }
}
```

