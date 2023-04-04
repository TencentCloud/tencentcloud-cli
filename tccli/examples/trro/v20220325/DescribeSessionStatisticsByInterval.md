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
                "TotalDuration": 0
            },
            {
                "ActiveFieldDeviceNum": 1,
                "ActiveRemoteDeviceNum": 0,
                "SessionNum": 2,
                "TotalDuration": 0
            },
            {
                "ActiveFieldDeviceNum": 1,
                "ActiveRemoteDeviceNum": 1,
                "SessionNum": 4,
                "TotalDuration": 604
            },
            {
                "ActiveFieldDeviceNum": 1,
                "ActiveRemoteDeviceNum": 0,
                "SessionNum": 1,
                "TotalDuration": 0
            }
        ]
    }
}
```

