**Example 1: 查询数据**



Input: 

```
tccli gpm DescribeData --cli-unfold-argument  \
    --MatchCode match-v87jcr87 \
    --StartTime 1600741736 \
    --EndTime 1601000936 \
    --TimeType 2
```

Output: 
```
{
    "Response": {
        "OverviewData": {
            "AverageSec": 1.91,
            "FailPercent": 2.86,
            "SuccessPercent": 22.86,
            "TimeoutPercent": 40,
            "TotalTimes": "35"
        },
        "RequestId": "024cba11-2f69-40ac-ac14-bbd31b210159",
        "TrendData": {
            "CancelList": [
                "0",
                "0",
                "0"
            ],
            "FailList": [
                "0",
                "0",
                "0"
            ],
            "SuccessList": [
                "0",
                "2",
                "0"
            ],
            "TimeList": [
                "1601103600",
                "1601107200",
                "1601110800",
                "1601362800"
            ],
            "TimeoutList": [
                "0",
                "1",
                "0",
                "0"
            ],
            "TotalList": [
                "0",
                "3",
                "0",
                "0"
            ]
        }
    }
}
```

