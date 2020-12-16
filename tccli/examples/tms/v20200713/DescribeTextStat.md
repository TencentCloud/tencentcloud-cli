**Example 1: 控制台识别统计**



Input: 

```
tccli tms DescribeTextStat --cli-unfold-argument  \
    --AuditType 1 \
    --Filters.0.Name xxx \
    --Filters.0.Values xxx
```

Output: 
```
{
    "Response": {
        "TrendCount": [
            {
                "TotalHour": 0,
                "EvilHour": 0,
                "TotalCount": 0,
                "EvilCount": 0,
                "PassCount": 0,
                "Date": "xx",
                "PassHour": 0,
                "SuspectHour": 0,
                "SuspectCount": 0
            }
        ],
        "Overview": {
            "TotalHour": 0,
            "EvilHour": 0,
            "TotalCount": 0,
            "EvilCount": 0,
            "PassCount": 0,
            "PassHour": 0,
            "SuspectHour": 0,
            "SuspectCount": 0
        },
        "RequestId": "xx",
        "EvilCount": [
            {
                "Count": 0,
                "EvilType": "xx"
            }
        ]
    }
}
```

