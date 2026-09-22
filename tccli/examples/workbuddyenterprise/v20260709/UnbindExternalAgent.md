**Example 1: 解除外部 Agent 与 Agent 的绑定**



Input: 

```
tccli workbuddyenterprise UnbindExternalAgent --cli-unfold-argument  \
    --AgentId 736918300000000001 \
    --A2AAgentId a2a-agent-001 \
    --BindingId 5001 \
    --VersionId 2087791755109965825
```

Output: 
```
{
    "Response": {
        "Status": "UNBOUND",
        "RequestId": "3c6d138e-1234-5678-9abc-def012345678"
    }
}
```

