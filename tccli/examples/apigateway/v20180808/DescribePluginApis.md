**Example 1: DescribePluginApis**



Input: 

```
tccli apigateway DescribePluginApis --cli-unfold-argument  \
    --PluginId Plugin-23sdcda
```

Output: 
```
{
    "Response": {
        "Result": {
            "TotalCount": 2,
            "AttachedApis": [
                {
                    "ServiceId": "service-jzo37opy",
                    "ServiceName": "clareplugin",
                    "ServiceDesc": "",
                    "ApiId": "api-1vkzehtw",
                    "ApiName": "mock3",
                    "ApiDesc": "",
                    "Environment": "release",
                    "AttachedTime": "2021-01-25T07:14:27Z"
                },
                {
                    "ServiceId": "service-jzo37opy",
                    "ServiceName": "clareplugin",
                    "ServiceDesc": "",
                    "ApiId": "api-buz84890",
                    "ApiName": "mock",
                    "ApiDesc": "",
                    "Environment": "release",
                    "AttachedTime": "2021-01-25T06:56:58Z"
                }
            ]
        },
        "RequestId": "f373cf5c-dddf-4263-98af-834fd0b773cf"
    }
}
```

