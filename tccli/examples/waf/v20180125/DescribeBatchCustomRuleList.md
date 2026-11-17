**Example 1: 批量自定义规则列表接口**



Input: 

```
tccli waf DescribeBatchCustomRuleList --cli-unfold-argument  \
    --Offset 0 \
    --Limit 20 \
    --By update_time \
    --Order desc \
    --DataType custom-rule \
    --Filters.0.Name Status \
    --Filters.0.Values 1 \
    --Filters.0.ExactMatch True
```

Output: 
```
{
    "Response": {
        "Data": {
            "List": [
                {
                    "Id": 1101834050,
                    "ActionType": 1,
                    "Bypass": "",
                    "ExpireTime": 0,
                    "Name": "clb访问测试",
                    "Redirect": "/",
                    "SortId": 40,
                    "Status": 1,
                    "Domains": [
                        "zhenhua1020.qcloudwaf.com"
                    ],
                    "Remark": "",
                    "Strategies": [
                        {
                            "Field": "URL",
                            "Arg": "",
                            "CompareFunc": "contains",
                            "Content": "/ccc/bbb",
                            "CaseNotSensitive": 0
                        }
                    ],
                    "EventId": "",
                    "ValidStatus": 1,
                    "CreateTime": "2024-10-23 15:23:51",
                    "UpdateTime": "2024-10-23 16:17:08",
                    "JobType": "CronJob",
                    "JobDateTime": {
                        "Timed": [],
                        "Cron": [
                            {
                                "Days": [],
                                "WDays": [
                                    1,
                                    2,
                                    3,
                                    4,
                                    5
                                ],
                                "StartTime": "09:00:00",
                                "EndTime": "18:00:00"
                            }
                        ],
                        "TimeTZone": "UTC+8"
                    },
                    "CronType": "week",
                    "Label": "",
                    "PageId": "",
                    "Preview": 0
                }
            ],
            "Total": 1
        },
        "RequestId": "1547e8aa-b673-1a81-60ea-c91a2b153940"
    }
}
```

