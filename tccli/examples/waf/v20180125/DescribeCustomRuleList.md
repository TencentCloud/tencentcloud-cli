**Example 1: 获取访问控制规则列表**



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
        "RequestId": "6a638b80-87db-458d-9dd8-461bb38d960a",
        "RuleList": [
            {
                "ActionType": "1",
                "Bypass": "cc",
                "CreateTime": "2024-07-29T18:55:42+08:00",
                "ExpireTime": "0",
                "Name": "rulename",
                "Redirect": "/redirect_url",
                "RuleId": "1101205922",
                "SortId": "50",
                "Status": "1",
                "Strategies": [
                    {
                        "Field": "COOKIE",
                        "CompareFunc": "eq",
                        "Content": "cookie_value",
                        "Arg": "cookie_key",
                        "CaseNotSensitive": 0
                    }
                ],
                "EventId": "1101",
                "ValidStatus": 1,
                "ModifyTime": "2024-08-28T18:54:25+08:00",
                "Source": "custom",
                "JobType": "TimedJob",
                "JobDateTime": {
                    "Timed": [
                        {
                            "StartDateTime": 0,
                            "EndDateTime": 0
                        }
                    ],
                    "Cron": [],
                    "TimeTZone": "UTC+8"
                },
                "CronType": "week",
                "Label": "label",
                "PageId": "1101",
                "Domain": "www.testwaf.com"
            }
        ],
        "TotalCount": "1"
    }
}
```

