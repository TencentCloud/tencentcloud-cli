**Example 1: 安装 Grafana 插件**



Input: 

```
tccli monitor InstallPlugins --cli-unfold-argument  \
    --InstanceId grafana-abcdefgh \
    --Plugins.0.PluginId grafana-clock-panel \
    --Plugins.0.Version xx
```

Output: 
```
{
    "Response": {
        "PluginIds": [
            "xx"
        ],
        "RequestId": "xx"
    }
}
```

