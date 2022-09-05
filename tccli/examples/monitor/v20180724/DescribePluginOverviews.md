**Example 1: 列出所有可安装的 Grafana 插件**



Input: 

```
tccli monitor DescribePluginOverviews --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "PluginSet": [
            {
                "PluginId": "grafana-piechart-panel",
                "Version": "1.6.1"
            },
            {
                "PluginId": "grafana-clock-panel",
                "Version": "1.1.1"
            }
        ],
        "RequestId": "zdrpp6r5pl7m349e6o9nc2g525pyxn92"
    }
}
```

