**Example 1: 创建插件**



Input: 

```
tccli adp CreatePlugin --cli-unfold-argument  \
    --Profile.Description 天气插件 \
    --Profile.IconUrl https://qidian-qbot-1251316161.cos.ap-guangzhou.myqcloud.com/public/plugin_files/%E6%8F%92%E4%BB%B6-%E9%BB%98%E8%AE%A4.png \
    --Profile.Name CAPI-Test \
    --Profile.PluginClass 0 \
    --Profile.PluginKind 2 \
    --Config.MCPPluginConfig.MCPServerUrl https://uat-mcp-order-service.fxnotary.com/sse \
    --Config.MCPPluginConfig.MCPTransport 0 \
    --Config.MCPPluginConfig.PluginHeader.0.IsGlobalHidden False \
    --Config.MCPPluginConfig.PluginHeader.0.IsRequired True \
    --Config.MCPPluginConfig.PluginHeader.0.Name Authorization \
    --Config.MCPPluginConfig.PluginHeader.0.Value Bearer db4fc7ab4e3d424a9f336507e58e58ae5e606222deac46a6 \
    --Config.MCPPluginConfig.SSEReadTimeout 300 \
    --Config.MCPPluginConfig.Timeout 5 \
    --Config.MCPPluginConfig.AuthConfig.AuthType 0 \
    --SpaceId default_space
```

Output: 
```
{
    "Response": {
        "PluginId": "acb14a04-a049-4a0c-bafa-9670e5d949f2",
        "RequestId": "0bf7928a-a74c-4fe7-ab79-6e531f5329be"
    }
}
```

