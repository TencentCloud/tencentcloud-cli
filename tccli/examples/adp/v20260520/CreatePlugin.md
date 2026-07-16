**Example 1: 创建插件**



Input: 

```
tccli adp CreatePlugin --cli-unfold-argument  \
    --Profile.Description 天气插件测试 \
    --Profile.IconUrl https://qidian-qbot-1251316161.cos.ap-guangzhou.myqcloud.com/public/plugin_files/%E6%8F%92%E4%BB%B6-%E9%BB%98%E8%AE%A4.png \
    --Profile.Name CAPI-Test-modify \
    --Profile.PluginClass 0 \
    --Profile.PluginKind 2 \
    --Config.MCPPluginConfig.MCPServerUrl https://*******************************com/sse \
    --Config.MCPPluginConfig.MCPTransport 0 \
    --Config.MCPPluginConfig.PluginHeader.0.IsGlobalHidden False \
    --Config.MCPPluginConfig.PluginHeader.0.IsRequired True \
    --Config.MCPPluginConfig.PluginHeader.0.Name Authorization \
    --Config.MCPPluginConfig.PluginHeader.0.Value Bearer ************************************************ \
    --Config.MCPPluginConfig.SSEReadTimeout 300 \
    --Config.MCPPluginConfig.Timeout 15 \
    --Config.MCPPluginConfig.AuthConfig.AuthType 0 \
    --SpaceId default_space \
    --LoginUin 6000005624511 \
    --LoginSubAccountUin 6000005624511
```

Output: 
```
{
    "Response": {
        "PluginId": "230ae967-f8fe-421d-96db-5e38c0ab4506",
        "RequestId": "bd90f649-fe4c-4723-b92b-95f20152dea8"
    }
}
```

