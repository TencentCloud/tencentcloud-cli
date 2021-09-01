**Example 1: DescribePlugin**



Input: 

```
tccli apigateway DescribePlugin --cli-unfold-argument  \
    --PluginId plugin-5xzwu9vh
```

Output: 
```
{
    "Response": {
        "Result": {
            "PluginId": "plugin-5xzwu9vh",
            "PluginName": "mynewplugins",
            "PluginType": "IPControl",
            "Description": "newmodify",
            "PluginData": "{\"blocks\":\"1.1.1.1\",\"type\":\"black_list\"}",
            "CreatedTime": "2021-01-26T03:00:34Z",
            "ModifiedTime": "2021-01-26T04:14:01Z",
            "AttachedApiTotalCount": 1,
            "AttachedApis": [
                {
                    "ServiceId": "service-2mvp5cwi",
                    "ServiceName": "clarescftest2",
                    "ServiceDesc": "",
                    "ApiId": "api-6wn5mmfq",
                    "ApiName": "eee",
                    "ApiDesc": "",
                    "Environment": "release",
                    "AttachedTime": "2021-01-26T04:17:41Z"
                }
            ]
        },
        "RequestId": "d1f768f4-ef4f-49e7-8117-4e12f720e355"
    }
}
```

