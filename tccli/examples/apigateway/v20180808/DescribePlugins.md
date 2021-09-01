**Example 1: DescribePlugins**



Input: 

```
tccli apigateway DescribePlugins --cli-unfold-argument  \
    --PluginIds plugin-2nuhovb7 \
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
                    "PluginId": "plugin-2nuhovb7",
                    "PluginName": "myplugin",
                    "PluginType": "IPControl",
                    "Description": "IPControl",
                    "PluginData": "{\"blocks\":\"1.1.1.12\",\"type\":\"black_list\"}",
                    "CreatedTime": "2021-01-25T10:15:21Z",
                    "ModifiedTime": "2021-01-25T10:15:21Z",
                    "AttachedApiTotalCount": 1,
                    "AttachedApis": [
                        {
                            "ServiceId": "service-jzo37opy",
                            "ServiceName": "clareplugin",
                            "ServiceDesc": "",
                            "ApiId": "api-buz84890",
                            "ApiName": "mock",
                            "ApiDesc": "",
                            "Environment": "release",
                            "AttachedTime": "2021-01-25T12:50:32Z"
                        }
                    ]
                }
            ]
        },
        "RequestId": "e2cc60e0-c1d9-4b11-97f9-d772ab3b0b6c"
    }
}
```

