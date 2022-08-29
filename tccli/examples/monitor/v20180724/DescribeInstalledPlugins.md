**Example 1: 列出已安装的插件**



Input: 

```
tccli monitor DescribeInstalledPlugins --cli-unfold-argument  \
    --InstanceId grafana-kleu3gt0
```

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
        "RequestId": "qmunlpf51noe13qp5vyvg7mq5t4t4w6u"
    }
}
```

