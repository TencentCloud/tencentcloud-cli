**Example 1: test1**



Input: 

```
tccli waf DescribeCustomRuleList --cli-unfold-argument  \
    --Domain hzh.qcloud.com \
    --Limit 10 \
    --Offset 10
```

Output: 
```
{
    "Response": {
        "RequestId": "89d3f512-674f-4ecf-b766-90d2600fa498",
        "RuleList": [],
        "TotalCount": "1"
    }
}
```

**Example 2: 获取访问控制规则列表**



Input: 

```
tccli waf DescribeCustomRuleList --cli-unfold-argument  \
    --Domain test.qcloudwaf.com \
    --Limit 1 \
    --Filters.0.Values 1234567890 \
    --Filters.0.Name RuleID \
    --Filters.0.ExactMatch True \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "RuleList": [
            {
                "ActionType": "abc",
                "Bypass": "abc",
                "CreateTime": "abc",
                "ExpireTime": "abc",
                "Name": "abc",
                "Redirect": "abc",
                "RuleId": "abc",
                "SortId": "abc",
                "Status": "abc",
                "Strategies": [
                    {
                        "Field": "abc",
                        "CompareFunc": "abc",
                        "Content": "abc",
                        "Arg": "abc"
                    }
                ],
                "EventId": "abc",
                "ModifyTime": "abc",
                "ValidStatus": 0,
                "Source": "abc",
                "JobType": "abc",
                "JobDateTime": {
                    "Timed": [
                        {
                            "StartDateTime": 1,
                            "EndDateTime": 1
                        }
                    ],
                    "Cron": [
                        {
                            "Days": [
                                1
                            ],
                            "WDays": [
                                1
                            ],
                            "StartTime": "abc",
                            "EndTime": "abc"
                        }
                    ],
                    "TimeTZone": "abc"
                },
                "CronType": "abc",
                "Label": "abc",
                "PageId": "abc"
            }
        ],
        "TotalCount": "abc",
        "RequestId": "abc"
    }
}
```

