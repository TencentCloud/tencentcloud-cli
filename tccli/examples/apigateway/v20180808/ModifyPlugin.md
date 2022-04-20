**Example 1: ModifyPlugin**



Input: 

```
tccli apigateway ModifyPlugin --cli-unfold-argument  \
    --PluginName newplugin \
    --PluginId plugin-3datbg1f \
    --Description 'Modify a plugin' \
    --PluginData {"type":"white_list","blocks":"172.3.1.4"}
```

Output: 
```
{
    "Response": {
        "Result": true,
        "RequestId": "bb85842c-c0d2-4543-8f4d-396a193babe8"
    }
}
```

**Example 2: 修改缓存插件**



Input: 

```
tccli apigateway ModifyPlugin --cli-unfold-argument  \
    --PluginName newplugin \
    --PluginId plugin-pbboebt1 \
    --Description modify_cache_plugin \
    --PluginData {"cache_key_params":[{"parameter":"param1","position":"header"},{"parameter":"param2","position":"query"},{"parameter":"param3","position":"path"}],"cacheable_methods":["GET","POST"],"cacheable_response_codes":[200,301,404],"cache_control":false,"ttl":300}
```

Output: 
```
{
    "Response": {
        "Result": true,
        "RequestId": "ab85842c-c0d2-4543-8f4d-396a193babe8"
    }
}
```

