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

**Example 2: 创建缓存插件**



Input: 

```
tccli apigateway CreatePlugin --cli-unfold-argument  \
    --PluginName myCachePlugin \
    --PluginType ProxyCache \
    --Description myCachePlugin \
    --PluginData {"cache_key_params":[{"parameter":"param1","position":"header"},{"parameter":"param2","position":"query"},{"parameter":"param3","position":"path"}],"cacheable_methods":["GET","POST"],"cacheable_response_codes":[200,301,404],"cache_control":false,"ttl":300}
```

Output: 
```
{
    "Response": {
        "Result": {
            "PluginId": "plugin-pbboebt1",
            "PluginName": "myCachePlugin",
            "PluginType": "ProxyCache",
            "Description": "myCachePlugin",
            "PluginData": "{\"cache_key_params\":[{\"parameter\":\"param1\",\"position\":\"header\"},{\"parameter\":\"param2\",\"position\":\"query\"},{\"parameter\":\"param3\",\"position\":\"path\"}],\"cacheable_methods\":[\"GET\",\"POST\"],\"cacheable_response_codes\":[200,301,404],\"cache_control\":false,\"ttl\":300}",
            "CreatedTime": "2021-01-25T05:46:25Z",
            "ModifiedTime": "2021-01-25T05:46:25Z",
            "AttachedApiTotalCount": null,
            "AttachedApis": null
        },
        "RequestId": "b4ffe46b-ae2c-4ff1-911b-57fe15f3d95a"
    }
}
```

