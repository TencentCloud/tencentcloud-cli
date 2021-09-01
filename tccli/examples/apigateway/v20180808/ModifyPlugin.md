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

