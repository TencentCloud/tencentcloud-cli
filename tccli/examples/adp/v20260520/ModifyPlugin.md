**Example 1: 修改插件示例**



Input: 

```
tccli adp ModifyPlugin --cli-unfold-argument  \
    --PluginId 6ec78f78-23fb-49db-8e53-76921e1e3918 \
    --PluginVersion 4 \
    --Profile.Description 天气插件测试 \
    --Profile.IconUrl https://qidian-qbot-1251316161.cos.ap-guangzhou.myqcloud.com/public/plugin_files/%E6%8F%92%E4%BB%B6-%E9%BB%98%E8%AE%A4.png \
    --Profile.Name CAPI-Test-modify \
    --Profile.PluginClass 0 \
    --Profile.PluginKind 2 \
    --Config.MCPPluginConfig.MCPServerUrl https://******************************.com/sse \
    --Config.MCPPluginConfig.MCPTransport 0 \
    --Config.MCPPluginConfig.PluginHeader.0.IsGlobalHidden False \
    --Config.MCPPluginConfig.PluginHeader.0.IsRequired True \
    --Config.MCPPluginConfig.PluginHeader.0.Name Authorization \
    --Config.MCPPluginConfig.PluginHeader.0.Value Bearer ************************************************ \
    --Config.MCPPluginConfig.SSEReadTimeout 300 \
    --Config.MCPPluginConfig.Timeout 15 \
    --Config.MCPPluginConfig.AuthConfig.AuthType 0 \
    --UpdateMask.Paths Config.Timeout \
    --LoginUin 6000005624511 \
    --LoginSubAccountUin 6000005624511
```

Output: 
```
{
    "Response": {
        "RequestId": "9814760b-4166-4571-bf83-856aed7ccade"
    }
}
```

