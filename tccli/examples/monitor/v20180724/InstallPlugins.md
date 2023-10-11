**Example 1: 安装 Grafana 插件**



Input: 

```
tccli monitor InstallPlugins --cli-unfold-argument  \
    --InstanceId grafana-abcdefgh \
    --Plugins.0.PluginId grafana-clock-panel \
    --Plugins.0.Version 1.2.0
```

Output: 
```
{
    "Response": {
        "PluginIds": [
            "grafana-clock-panel"
        ],
        "RequestId": "requestid"
    }
}
```

