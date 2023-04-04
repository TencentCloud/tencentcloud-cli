**Example 1: 示例1**



Input: 

```
tccli trro DescribeDeviceSessionList --cli-unfold-argument  \
    --PageNumber 1 \
    --PageSize 10 \
    --ProjectId abcdefg \
    --DeviceId dev2 \
    --StartTime 0 \
    --EndTime 1670000000
```

Output: 
```
{
    "Response": {
        "DeviceSessionList": [
            {
                "EndTime": 1650000060,
                "FieldDeviceId": "dev2",
                "Quality": "good",
                "RemoteDeviceId": "dev2",
                "Resolution": "1920*1080",
                "SessionId": "abcdefg-50f7-4c60-9c89-e7076c8529a9-0",
                "StartTime": 1650000000
            }
        ],
        "RequestId": "abcdefg-186d-4dc5-9a36-6849446dd921",
        "Total": 1,
        "Num": 1
    }
}
```

