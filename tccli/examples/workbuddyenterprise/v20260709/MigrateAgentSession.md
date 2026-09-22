**Example 1: 迁移 Agent 会话**



Input: 

```
tccli workbuddyenterprise MigrateAgentSession --cli-unfold-argument  \
    --SessionId sess-9f3c1a2b7d4e \
    --AgentId 736918300000000001 \
    --TargetVersionId 2087791755109965825
```

Output: 
```
{
    "Response": {
        "SessionId": "sess-9f3c1a2b7d4e",
        "Status": "ACTIVE",
        "RequestId": "3c6d138e-1234-5678-9abc-def012345678"
    }
}
```

