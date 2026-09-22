**Example 1: 把外部 Agent 绑定到指定 Agent**



Input: 

```
tccli workbuddyenterprise BindExternalAgent --cli-unfold-argument  \
    --AgentId 736918300000000001 \
    --A2AAgentId a2a-agent-001 \
    --VersionId 2087791755109965825
```

Output: 
```
{
    "Response": {
        "Status": "BOUND",
        "RequestId": "3c6d138e-1234-5678-9abc-def012345678"
    }
}
```

