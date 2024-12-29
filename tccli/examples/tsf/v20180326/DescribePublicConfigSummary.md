**Example 1: 查询公共配置汇总列表**



Input: 

```
tccli tsf DescribePublicConfigSummary --cli-unfold-argument  \
    --SearchWord app \
    --Offset 0 \
    --Limit 10 \
    --OrderBy creation_time \
    --OrderType 1 \
    --ConfigTagList app-config \
    --DisableProgramAuthCheck True \
    --ConfigIdList dcfg-p-vkj5dnky
```

Output: 
```
{
    "Response": {
        "RequestId": "d6da2add-172a-4a4d-8f30-8abca66e314f",
        "Result": {
            "Content": [
                {
                    "ApplicationId": null,
                    "ApplicationName": null,
                    "ConfigId": "dcfg-p-vkj5dnky",
                    "ConfigName": "app-config",
                    "ConfigType": null,
                    "ConfigValue": null,
                    "ConfigVersion": null,
                    "ConfigVersionCount": 1,
                    "ConfigVersionDesc": null,
                    "CreationTime": null,
                    "DeleteFlag": null,
                    "LastUpdateTime": "2024-12-20 19:16:10"
                }
            ],
            "TotalCount": 1
        }
    }
}
```

