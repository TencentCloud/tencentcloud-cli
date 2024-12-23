**Example 1: 创建配置项**

为应用创建配置项

Input: 

```
tccli tsf CreateConfigWithDetailResp --cli-unfold-argument  \
    --ConfigName app-config \
    --ConfigVersion v1.0 \
    --ConfigValue config: enabled \
    --ApplicationId application-yx8m24ga
```

Output: 
```
{
    "Response": {
        "RequestId": "52fb20a9-efc0-443d-97e3-cf43478f1b0d",
        "Result": {
            "ApplicationId": "application-yx8m24ga",
            "ApplicationName": null,
            "ConfigId": "dcfg-vw83k2zv",
            "ConfigName": "app-config",
            "ConfigType": null,
            "ConfigValue": "config: enabled",
            "ConfigVersion": "v1.0",
            "ConfigVersionCount": null,
            "ConfigVersionDesc": null,
            "CreationTime": null,
            "DeleteFlag": null,
            "LastUpdateTime": null
        }
    }
}
```

