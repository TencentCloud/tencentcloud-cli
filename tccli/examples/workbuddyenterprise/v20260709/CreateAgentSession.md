**Example 1: 创建 Agent 会话**



Input: 

```
tccli workbuddyenterprise CreateAgentSession --cli-unfold-argument  \
    --AgentId 736918300000000001 \
    --VersionId 2087791755109965825
```

Output: 
```
{
    "Response": {
        "SessionId": "sess-9f3c1a2b7d4e",
        "EndpointSet": [
            {
                "EndpointType": "PUBLIC",
                "Url": "https://736918300000000001-tc-nanjing.example-workbuddy.com"
            }
        ],
        "RequestId": "3c6d138e-1234-5678-9abc-def012345678"
    }
}
```

