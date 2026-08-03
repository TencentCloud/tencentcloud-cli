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

**Example 2: 创建并关联访问策略的沙箱工具**

创建沙箱工具时关联两条访问策略。

Input: 

```
tccli ags CreateSandboxTool --cli-unfold-argument  \
    --ToolName browser-policy-sandbox \
    --ToolType browser \
    --NetworkConfiguration.NetworkMode PUBLIC \
    --ClientToken create-tool-with-access-policy-example
```

Output: 
```
{
    "Response": {
        "ToolId": "sdt-policy123",
        "RequestId": "req-create-tool-policy-example"
    }
}
```

