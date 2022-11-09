**Example 1: DescribeAvailablePluginApis**



Input: 

```
tccli apigateway DescribePluginsByApi --cli-unfold-argument  \
    --ApiId api-fa23vfd \
    --EnvironmentName release \
    --ServiceId service-o5as3moe
```

Output: 
```
{
    "Response": {
        "Result": {
            "TotalCount": 1,
            "PluginSummary": [
                {
                    "PluginId": "plugin-9l0d4sdf",
                    "PluginName": "onlyname",
                    "PluginType": "IPControl",
                    "Description": "modifyDesc",
                    "PluginData": "{\"blocks\":\"1.1.1.1\",\"type\":\"black_list\"}",
                    "Environment": "release",
                    "AttachedTime": "2021-01-25T06:56:58Z"
                }
            ]
        },
        "RequestId": "4effd8e7-abd0-4f95-a881-301d68d9985e"
    }
}
```

