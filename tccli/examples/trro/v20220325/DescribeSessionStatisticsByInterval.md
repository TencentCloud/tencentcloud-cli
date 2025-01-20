**Example 1: 示例**



Input: 

```
tccli trro DescribeSessionStatisticsByInterval --cli-unfold-argument  \
    --ProjectId abcdefg \
    --EndTime 1670000000 \
    --StatisticInterval hour \
    --DeviceId dev2 \
    --StartTime 0
```

Output: 
```
{
    "Response": {
        "RequestId": "abcdefg-774e-4756-9f5b-8faa55ae1e5b",
        "SessionStatistics": [
            {
                "ActiveFieldDeviceNum": 1,
                "ActiveRemoteDeviceNum": 0,
                "SessionNum": 1,
                "StartTime": 1661151600,
                "EndTime": 1661152600,
                "TotalDuration": 20,
                "NotBadSessionRatio": 50
            },
            {
                "ActiveFieldDeviceNum": 1,
                "ActiveRemoteDeviceNum": 0,
                "SessionNum": 2,
                "StartTime": 1661162400,
                "EndTime": 1661152600,
                "TotalDuration": 20,
                "NotBadSessionRatio": 10
            },
            {
                "ActiveFieldDeviceNum": 1,
                "ActiveRemoteDeviceNum": 1,
                "SessionNum": 4,
                "StartTime": 1661166000,
                "EndTime": 1661176000,
                "TotalDuration": 604,
                "NotBadSessionRatio": 20
            },
            {
                "ActiveFieldDeviceNum": 1,
                "ActiveRemoteDeviceNum": 0,
                "SessionNum": 1,
                "StartTime": 1661166000,
                "EndTime": 1661176000,
                "TotalDuration": 10,
                "NotBadSessionRatio": 30
            }
        ]
    }
}
```

