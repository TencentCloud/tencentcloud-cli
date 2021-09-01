**Example 1: CreatePlugin**



Input: 

```
tccli apigateway CreatePlugin --cli-unfold-argument  \
    --PluginName mytestPlugin \
    --PluginType IPControl \
    --Description IPControl \
    --PluginData {"blocks":"1.1.1.12","type":"black_list"}
```

Output: 
```
{
    "Response": {
        "Result": {
            "PluginId": "plugin-qrboebt1",
            "PluginName": "mytestPlugin",
            "PluginType": "IPControl",
            "Description": "IPControl",
            "PluginData": "{\"blocks\":\"1.1.1.12\",\"type\":\"black_list\"}",
            "CreatedTime": "2021-01-25T05:46:25Z",
            "ModifiedTime": "2021-01-25T05:46:25Z",
            "AttachedApiTotalCount": null,
            "AttachedApis": null
        },
        "RequestId": "b4ffe46b-ae2c-4ff1-911b-57fe15f3d95b"
    }
}
```

