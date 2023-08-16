**Example 1: AttachPlugin**

连接插件

Input: 

```
tccli apigateway AttachPlugin --cli-unfold-argument  \
    --ServiceId Service-3fasdgrg \
    --PluginId Plugin-3datbg1f \
    --EnvironmentName release \
    --ApiIds api-gesv1rfa api-9ads3g
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

