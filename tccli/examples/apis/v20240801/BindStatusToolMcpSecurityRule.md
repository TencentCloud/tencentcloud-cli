**Example 1: 工具绑定（解绑）mcp 安全规则**

工具绑定（解绑）mcp 安全规则

Input: 

```
tccli apis BindStatusToolMcpSecurityRule --cli-unfold-argument  \
    --ID mr-c00eb39f \
    --InstanceID ins-9c4a1db3 \
    --Status close \
    --ToolNames add-todo \
    --McpServerID mcp-8d5c4195
```

Output: 
```
{
    "Response": {
        "Data": {
            "ID": "mr-c00eb39f"
        },
        "RequestId": "cb6189ab-e520-409d-b0e5-1b563c0bfe37"
    }
}
```

