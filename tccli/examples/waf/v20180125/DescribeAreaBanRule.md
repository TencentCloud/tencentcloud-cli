**Example 1: 获取地域封禁规则**



Input: 

```
tccli waf DescribeAreaBanRule --cli-unfold-argument  \
    --Domain www.testwaf.com
```

Output: 
```
{
    "Response": {
        "Data": {
            "Status": 1,
            "Source": "custom",
            "Areas": [
                {
                    "Country": "中国",
                    "Region": "广东",
                    "City": "深圳"
                }
            ],
            "JobType": "Timed",
            "JobDateTime": {
                "Timed": [
                    {
                        "StartDateTime": 1711618518,
                        "EndDateTime": 1711919518
                    }
                ],
                "Cron": [],
                "TimeTZone": "UTC+8"
            },
            "Lang": "cn"
        },
        "RequestId": "9b02bf9e-c89c-42c3-9ae1-685f968fa02d"
    }
}
```

