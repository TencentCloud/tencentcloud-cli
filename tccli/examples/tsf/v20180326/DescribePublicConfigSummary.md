**Example 1: 查询公共配置汇总列表**



Input: 

```
tccli tsf DescribePublicConfigSummary --cli-unfold-argument  \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "RequestId": "cc75758b-a2e3-4ded-a97a-c541817b4efe",
        "Result": {
            "TotalCount": 2,
            "Content": [
                {
                    "ConfigId": null,
                    "ConfigName": "global",
                    "ConfigVersion": null,
                    "ConfigVersionDesc": null,
                    "ConfigValue": null,
                    "CreationTime": null,
                    "LastUpdateTime": "2019-05-24 20:39:12",
                    "ConfigVersionCount": 6,
                    "ApplicationId": null,
                    "ApplicationName": null,
                    "DeleteFlag": null,
                    "ConfigType": null
                },
                {
                    "ConfigId": null,
                    "ConfigName": "tsf",
                    "ConfigVersion": null,
                    "ConfigVersionDesc": null,
                    "ConfigValue": null,
                    "CreationTime": null,
                    "LastUpdateTime": "2019-05-21 14:50:13",
                    "ConfigVersionCount": 4,
                    "ApplicationId": null,
                    "ApplicationName": null,
                    "DeleteFlag": null,
                    "ConfigType": null
                }
            ]
        }
    }
}
```

