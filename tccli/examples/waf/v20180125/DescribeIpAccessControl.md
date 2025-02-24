**Example 1: IP黑白名单查询**

IP黑名单查询

Input: 

```
tccli waf DescribeIpAccessControl --cli-unfold-argument  \
    --Domain www.test.com \
    --Count 1 \
    --ActionType 42 \
    --Limit 20 \
    --OffSet 0 \
    --Sort ts_version:-1
```

Output: 
```
{
    "Response": {
        "Data": {
            "Res": [
                {
                    "Id": "66a341dd8f33c805d65f4765",
                    "RuleId": 5501526871,
                    "IpList": [
                        "113.108.77.69"
                    ],
                    "ActionType": 42,
                    "Ip": "113.108.77.69",
                    "Note": "",
                    "Source": "custom",
                    "TsVersion": 1721975261208,
                    "CreateTime": 1721975261208,
                    "ValidTs": 2019571199,
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
                    "ValidStatus": 1
                }
            ],
            "TotalCount": 1
        },
        "RequestId": "c937ce96-cf53-4df8-b288-07c6e092072d"
    }
}
```

