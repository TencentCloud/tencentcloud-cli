**Example 1: 更新沙箱工具**



Input: 

```
tccli ags UpdateSandboxTool --cli-unfold-argument  \
    --ToolId sdt-ee4ywozw \
    --Description 更新后的浏览器沙箱环境 \
    --Tags.0.Key Environment \
    --Tags.0.Value Staging \
    --Tags.1.Key Team \
    --Tags.1.Value AI-Agent \
    --Tags.2.Key Version \
    --Tags.2.Value v2.0
```

Output: 
```
{
    "Response": {
        "RequestId": "custom-request-id-456"
    }
}
```

