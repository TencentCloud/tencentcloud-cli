**Example 1: 插件绑定API**



Input: 

```
tccli tsf BindPlugin --cli-unfold-argument  \
    --PluginInstanceList.0.PluginId pgn-spzs5mv5 \
    --PluginInstanceList.0.ScopeType api \
    --PluginInstanceList.0.ScopeValue api-dvdv4i8i
```

Output: 
```
{
    "Response": {
        "RequestId": "5d996e5507e42d5970cd2e25ed5267a",
        "Result": true
    }
}
```

