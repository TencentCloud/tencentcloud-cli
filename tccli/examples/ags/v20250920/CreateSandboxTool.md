**Example 1: 创建沙箱工具**



Input: 

```
tccli ags CreateSandboxTool --cli-unfold-argument  \
    --ToolName browser-sandbox \
    --ToolType browser \
    --Description 浏览器沙箱环境 \
    --DefaultTimeout 30m \
    --NetworkConfiguration.NetworkMode PUBLIC \
    --Tags.0.Key Environment \
    --Tags.0.Value Production \
    --Tags.1.Key Team \
    --Tags.1.Value AI-Agent \
    --ClientToken unique-token-123
```

Output: 
```
{
    "Response": {
        "ToolId": "sdt-ee4ywozw",
        "RequestId": "custom-request-id-123"
    }
}
```

