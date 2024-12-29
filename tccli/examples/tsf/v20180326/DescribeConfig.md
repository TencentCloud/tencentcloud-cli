**Example 1: 查询配置**



Input: 

```
tccli tsf DescribeConfig --cli-unfold-argument  \
    --ConfigId dcfg-vzk36owv
```

Output: 
```
{
    "Response": {
        "RequestId": "60bd18bd-50bb-4e4c-af76-8f1c938b103a",
        "Result": {
            "ApplicationId": "application-5yr26r9a",
            "ApplicationName": "amp-consumer",
            "ConfigId": "dcfg-vzk36owv",
            "ConfigName": "config_app",
            "ConfigType": "application",
            "ConfigValue": "config: enabled",
            "ConfigVersion": "v1",
            "ConfigVersionCount": 1,
            "ConfigVersionDesc": "This is desc",
            "CreationTime": "2024-12-24 18:04:02",
            "DeleteFlag": true,
            "LastUpdateTime": "2024-12-24 18:04:02"
        }
    }
}
```

