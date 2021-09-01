**Example 1: 查询配置汇总列表**



Input: 

```
tccli tsf DescribeConfigSummary --cli-unfold-argument  \
    --Offset 0 \
    --Limit 20 \
    --SearchWord driver
```

Output: 
```
{
    "Response": {
        "RequestId": "2b151339-278f-47ed-b5fe-a86273a203de",
        "Result": {
            "TotalCount": 3,
            "Content": [
                {
                    "ConfigId": null,
                    "ConfigName": "dev-driverapi-config",
                    "ConfigVersion": null,
                    "ConfigVersionDesc": null,
                    "ConfigValue": null,
                    "CreationTime": null,
                    "LastUpdateTime": "2019-04-16 12:38:45",
                    "ConfigVersionCount": 2,
                    "ApplicationId": "application-maegorqv",
                    "ApplicationName": "gactravel_dev_driverapi",
                    "DeleteFlag": null,
                    "ConfigType": null
                },
                {
                    "ConfigId": null,
                    "ConfigName": "ruqi_travel_driverapi",
                    "ConfigVersion": null,
                    "ConfigVersionDesc": null,
                    "ConfigValue": null,
                    "CreationTime": null,
                    "LastUpdateTime": "2019-04-16 12:29:55",
                    "ConfigVersionCount": 3,
                    "ApplicationId": "application-ov6mxrka",
                    "ApplicationName": "ruqi_travel_driverapi",
                    "DeleteFlag": null,
                    "ConfigType": null
                },
                {
                    "ConfigId": null,
                    "ConfigName": "test-driverapi-config",
                    "ConfigVersion": null,
                    "ConfigVersionDesc": null,
                    "ConfigValue": null,
                    "CreationTime": null,
                    "LastUpdateTime": "2019-04-23 11:16:26",
                    "ConfigVersionCount": 2,
                    "ApplicationId": "application-jy9w6lka",
                    "ApplicationName": "ruqitest_travel_driverapi",
                    "DeleteFlag": null,
                    "ConfigType": null
                }
            ]
        }
    }
}
```

