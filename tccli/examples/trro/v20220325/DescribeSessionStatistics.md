**Example 1: 示例1**



Input: 

```
tccli trro DescribeSessionStatistics --cli-unfold-argument  \
    --ProjectId abcdefg \
    --DeviceId dev2 \
    --StartTime 1670000000 \
    --EndTime 1670000000
```

Output: 
```
{
    "Response": {
        "ActiveFieldDeviceNum": 1,
        "ActiveRemoteDeviceNum": 1,
        "NotBadSessionRatio": 100,
        "RequestId": "abcdefg-1d31-47bc-8725-76124984f005",
        "SessionNum": 6,
        "TotalDuration": 604
    }
}
```

