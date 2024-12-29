**Example 1: 查询配置汇总列表**



Input: 

```
tccli tsf DescribeConfigSummary --cli-unfold-argument  \
    --ApplicationId application-5yr26r9a \
    --SearchWord config_app \
    --Offset 0 \
    --Limit 10 \
    --OrderBy creation_time \
    --OrderType 1 \
    --ConfigTagList config_app-application-5yr26r9a \
    --DisableProgramAuthCheck True \
    --ConfigIdList dcfg-vzk36owv
```

Output: 
```
{
    "Response": {
        "RequestId": "0e8d31d3-e16a-4070-9248-cce94db7fae5",
        "Result": {
            "Content": [
                {
                    "ApplicationId": "application-5yr26r9a",
                    "ApplicationName": "amp-consumer",
                    "ConfigId": "dcfg-vzk36owv",
                    "ConfigName": "config_app",
                    "ConfigType": null,
                    "ConfigValue": null,
                    "ConfigVersion": null,
                    "ConfigVersionCount": 1,
                    "ConfigVersionDesc": null,
                    "CreationTime": null,
                    "DeleteFlag": null,
                    "LastUpdateTime": "2024-12-24 18:04:02"
                }
            ],
            "TotalCount": 1
        }
    }
}
```

