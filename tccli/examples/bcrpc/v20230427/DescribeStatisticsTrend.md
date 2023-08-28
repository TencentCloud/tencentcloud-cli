**Example 1: 查询请求统计趋势**



Input: 

```
tccli bcrpc DescribeStatisticsTrend --cli-unfold-argument  \
    --ApplicationName abc \
    --Chain abc \
    --Network abc \
    --PeriodType 0 \
    --StartTime abc \
    --EndTime abc
```

Output: 
```
{
    "Response": {
        "TotalRequest": 0,
        "AverageRequest": "ab",
        "CreditUsage": 0,
        "RequestList": [
            {
                "Time": "abc",
                "Value": "abc"
            }
        ],
        "AverageRequestList": [
            {
                "Time": "abc",
                "Value": "abc"
            }
        ],
        "UsageList": [
            {
                "Time": "abc",
                "Value": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

