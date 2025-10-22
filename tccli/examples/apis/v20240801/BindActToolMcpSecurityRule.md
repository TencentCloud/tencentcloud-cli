**Example 1: 工具绑定处置动作mcp 安全规则**

工具绑定处置动作mcp 安全规则

Input: 

```
tccli apis BindActToolMcpSecurityRule --cli-unfold-argument  \
    --ID mr-c00eb39f \
    --InstanceID ins-9c4a1db3 \
    --Act filter \
    --ToolNames add-todo \
    --McpServerID mcp-8d5c4195
```

Output: 
```
{
    "Response": {
        "Data": {
            "ID": "mr-8d5c4195"
        },
        "RequestId": "388289da-01b2-4be6-8ba9-7b40028ac05b"
    }
}
```

