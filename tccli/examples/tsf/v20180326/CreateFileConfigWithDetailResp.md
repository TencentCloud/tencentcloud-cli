**Example 1: 创建文件配置项**

为应用创建文件配置

Input: 

```
tccli tsf CreateFileConfigWithDetailResp --cli-unfold-argument  \
    --ConfigName app_config \
    --ConfigVersion v1.0 \
    --ConfigFileName config.txt \
    --ConfigFileValue config=enabled \
    --ApplicationId application-yx8m24ga \
    --ConfigFilePath /root/app
```

Output: 
```
{
    "Response": {
        "RequestId": "a7d2e82d-0bf1-4e44-b296-ccf60bcdbb3c",
        "Result": {
            "ApplicationId": "application-yx8m24ga",
            "ApplicationName": null,
            "ConfigFileCode": "UTF-8",
            "ConfigFileName": "config.txt",
            "ConfigFilePath": "/root/app",
            "ConfigFileValue": "config=enabled",
            "ConfigFileValueLength": 14,
            "ConfigId": "dcfg-f-yq75blda",
            "ConfigName": "app_config",
            "ConfigPostCmd": "",
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

