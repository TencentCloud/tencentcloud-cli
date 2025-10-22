**Example 1: 修改mcp服务工具集配置**

修改mcp服务工具集配置

Input: 

```
tccli apis ModifyMcpServerToolConfig --cli-unfold-argument  \
    --InstanceID ins-9c4a1db3 \
    --ID mcp-8d5c4195 \
    --ToolConfigs.0.ToolName add-todo \
    --ToolConfigs.0.InvokeLimitConfigStatus True \
    --ToolConfigs.0.InvokeLimitConfig.Type tokenBucket \
    --ToolConfigs.0.InvokeLimitConfig.TokenBucketMaxNum 20000 \
    --ToolConfigs.0.InvokeLimitConfig.TokenBucketRate 1 \
    --ToolConfigs.0.McpSecurityRules.0.ID mr-c00eb39f \
    --ToolConfigs.0.McpSecurityRules.0.Act watch
```

Output: 
```
{
    "Response": {
        "Data": {
            "ID": "mcp-8d5c4195"
        },
        "RequestId": "93c3520a-7ecd-496d-abe5-92cf8b5a8d4d"
    }
}
```

