**Example 1: 创建公共配置项**

创建公共配置项

Input: 

```
tccli tsf CreatePublicConfigWithDetailResp --cli-unfold-argument  \
    --ConfigName app-config \
    --ConfigVersion v1 \
    --ConfigVersionDesc This is desc \
    --ConfigValue config: enabled \
    --ConfigType public \
    --EncodeWithBase64 True
```

Output: 
```
{
    "Response": {
        "RequestId": "354e3865-d1ae-4cde-8de6-a50732fd00e5",
        "Result": {
            "ApplicationId": null,
            "ApplicationName": null,
            "ConfigId": "dcfg-p-vkj5dnky",
            "ConfigName": "app-config",
            "ConfigType": "public",
            "ConfigValue": "config: enabled",
            "ConfigVersion": "v1",
            "ConfigVersionCount": null,
            "ConfigVersionDesc": "This is desc",
            "CreationTime": null,
            "DeleteFlag": null,
            "LastUpdateTime": null
        }
    }
}
```

