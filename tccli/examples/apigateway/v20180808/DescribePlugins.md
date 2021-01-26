**Example 1: DescribePlugins**



Input: 

```
tccli apigateway DescribePlugins --cli-unfold-argument  \
    --PluginIds Plugin-23sdcda \
    --PluginName myplugin \
    --PluginType IPControl
```

Output: 
```
{
    "Response": {
        "Result": {
            "TotalCount": 1,
            "PluginSet": [
                {
                    "PluginId": "Plugin-23sdcda",
                    "PluginName": "myplugin",
                    "PluginType": "IPControl",
                    "Description": "my first plugin",
                    "PluginData": "{\"unit\":\"MINUTE\",\"apiDefault\":20}",
                    "ModifiedTime": "2020-09-22T00:00:00+00:00",
                    "CreatedTime": "2020-09-22T00:00:00+00:00"
                }
            ]
        },
        "RequestId": "bb85842c-c0d2-4543-8f4d-396a193babe8"
    }
}
```

