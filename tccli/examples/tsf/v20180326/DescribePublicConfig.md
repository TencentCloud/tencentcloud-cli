**Example 1: 查询公共配置（单条）**



Input: 

```
tccli tsf DescribePublicConfig --cli-unfold-argument  \
    --ConfigId dcfg-p-vkj5dnky
```

Output: 
```
{
    "Response": {
        "RequestId": "8a143a46-4f13-4c9e-b536-9225ab88a55e",
        "Result": {
            "ApplicationId": null,
            "ApplicationName": null,
            "ConfigId": "dcfg-p-vkj5dnky",
            "ConfigName": "app-config",
            "ConfigType": null,
            "ConfigValue": "config: enabled",
            "ConfigVersion": "v1",
            "ConfigVersionCount": null,
            "ConfigVersionDesc": "This is desc",
            "CreationTime": "2024-12-20 19:16:10",
            "DeleteFlag": true,
            "LastUpdateTime": null
        }
    }
}
```

