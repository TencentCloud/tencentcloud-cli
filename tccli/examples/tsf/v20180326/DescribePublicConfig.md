**Example 1: 查询公共配置（单条）**



Input: 

```
tccli tsf DescribePublicConfig --cli-unfold-argument  \
    --ConfigId dcfg-p-5yrl4z2y
```

Output: 
```
{
    "Response": {
        "RequestId": "0fd83b45-ec19-45ad-9874-dbda7c4e84e6",
        "Result": {
            "ConfigId": "dcfg-p-5yrl4z2y",
            "ConfigName": "test-config",
            "ConfigVersion": "1.3",
            "ConfigVersionDesc": "",
            "ConfigValue": "tsf.inventory.password.encrypt2: ENC(3M7wGw2XtFc5Y+rxOgNBLrm2spUtgodjIxa+7F3XcAo=)\r\ntsf.inventory.password.encrypt1: ENC(3M7wGw2XtFc5Y+rxOgNBLrm2spUtgodjIxa+7F3XcAo=)\r\n",
            "CreationTime": "2019-05-29 11:23:28",
            "LastUpdateTime": null,
            "ConfigVersionCount": null,
            "ApplicationId": null,
            "ApplicationName": null,
            "DeleteFlag": true,
            "ConfigType": null
        }
    }
}
```

