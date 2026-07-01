**Example 1: ExecuteAgentApi**



Input: 

```
tccli dataagent ExecuteAgentApi --cli-unfold-argument  \
    --RequestPath /api/agents \
    --RequestData agentType=builtin \
    --RequestType get
```

Output: 
```
{
    "Response": {
        "AgentData": "data too long, just for show",
        "ErrorMsg": "success",
        "RequestPath": "/api/agents",
        "RequestId": "a8dbf68c-e822-47cf-bea6-a4927bf692c1"
    }
}
```

