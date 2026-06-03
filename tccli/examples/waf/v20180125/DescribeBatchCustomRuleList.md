**Example 1: 批量自定义规则列表接口**



Input: 

```
tccli waf DescribeBatchCustomRuleList --cli-unfold-argument  \
    --Offset 0 \
    --Limit 0 \
    --By abc \
    --Order abc \
    --DataType abc \
    --Filters.0.Name abc \
    --Filters.0.Values abc \
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
                    "JobType": "TimedJob",
                    "JobDateTime": {
                        "Timed": [
                            {
                                "StartDateTime": 0,
                                "EndDateTime": 0
                            }
                        ],
                        "Cron": null,
                        "TimeTZone": "UTC+8"
                    },
                    "CronType": "-",
                    "Label": "",
                    "PageId": ""
                }
            ],
            "Total": 1
        },
        "RequestId": "1547e8aa-b673-1a81-60ea-c91a2b153940"
    }
}
```

