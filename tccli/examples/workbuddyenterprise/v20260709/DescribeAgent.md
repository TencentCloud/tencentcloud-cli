**Example 1: 查询 Agent 详情**



Input: 

```
tccli workbuddyenterprise DescribeAgent --cli-unfold-argument  \
    --AgentId 736918300000000001
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
        "ActiveSessionCount": 3,
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

