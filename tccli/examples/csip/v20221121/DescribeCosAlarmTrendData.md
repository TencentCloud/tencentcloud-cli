**Example 1: 每日告警新增数据**



Input: 

```
tccli csip DescribeCosAlarmTrendData --cli-unfold-argument  \
    --LastDays 30
```

Output: 
```
{
    "Response": {
        "CosAlarmTrendInfo": [
            {
                "CurrentDateStr": "2024-01-31",
                "CurrentDayCount": 23,
                "CurrentDayOverView": [
                    {
                        "PolicyType": 1,
                        "PolicyTypeName": "",
                        "PolicyCount": 10
                    }
                ]
            }
        ],
        "RequestId": "6a625df7-dea0-4ba2-9942-97303d13d23e"
    }
}
```

