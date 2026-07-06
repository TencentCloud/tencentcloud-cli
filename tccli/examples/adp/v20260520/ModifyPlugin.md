**Example 1: 修改插件示例**



Input: 

```
tccli adp ModifyPlugin --cli-unfold-argument  \
    --PluginId acb14a04-a049-4a0c-bafa-9670e5d949f2 \
    --PluginVersion 2 \
    --Profile.Description 天气插件测试 \
    --Profile.IconUrl https://qidian-qbot-1251316161.cos.ap-guangzhou.myqcloud.com/public/plugin_files/%E6%8F%92%E4%BB%B6-%E9%BB%98%E8%AE%A4.png \
    --Profile.Name CAPI-Test-modify \
    --Profile.PluginClass 0 \
    --Profile.PluginKind 2 \
    --Config.MCPPluginConfig.MCPServerUrl https://uat-mcp-order-service.fxnotary.com/sse \
    --Config.MCPPluginConfig.MCPTransport 0 \
    --Config.MCPPluginConfig.PluginHeader.0.IsGlobalHidden False \
    --Config.MCPPluginConfig.PluginHeader.0.IsRequired True \
    --Config.MCPPluginConfig.PluginHeader.0.Name Authorization \
    --Config.MCPPluginConfig.PluginHeader.0.Value Bearer db4fc7ab4e3d424a9f336507e58e58ae5e606222deac46a6 \
    --Config.MCPPluginConfig.SSEReadTimeout 300 \
    --Config.MCPPluginConfig.Timeout 15 \
    --Config.MCPPluginConfig.AuthConfig.AuthType 0 \
    --UpdateMask.Paths Config.Timeout
```

Output: 
```
{
    "Response": {
        "RequestId": "04d0b5d7-31ff-4b90-a6f7-62f7133fd658"
    }
}
```

