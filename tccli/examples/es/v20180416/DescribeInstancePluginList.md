**Example 1: 查询实例插件列表**

查询实例插件列表

Input: 

```
tccli es DescribeInstancePluginList --cli-unfold-argument  \
    --InstanceId es-xxxxxxxx
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "PluginList": [
            {
                "PluginDesc": "1",
                "Status": 0,
                "PluginType": 0,
                "PluginVersion": "1",
                "PluginUpdateTime": "1",
                "PluginName": "1",
                "Removable": true
            }
        ],
        "RequestId": "1"
    }
}
```

