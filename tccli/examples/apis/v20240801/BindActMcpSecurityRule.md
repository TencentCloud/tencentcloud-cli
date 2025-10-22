**Example 1: 绑定处置动作mcp 安全规则**

绑定处置动作mcp 安全规则

Input: 

```
tccli apis BindActMcpSecurityRule --cli-unfold-argument  \
    --ID mr-2bdbbf32 \
    --InstanceID ins-9c4a1db3 \
    --Act watch \
    --McpServerIDs mcp-8d5c4195
```

Output: 
```
{
    "Response": {
        "Data": {
            "ID": "mr-2bdbbf32"
        },
        "RequestId": "cbe4e2a9-d2e2-4f3a-8805-019536f9169e"
    }
}
```

