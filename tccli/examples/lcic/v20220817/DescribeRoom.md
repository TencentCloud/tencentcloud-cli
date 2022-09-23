**Example 1: 房间信息**



Input: 

```
tccli lcic DescribeRoom --cli-unfold-argument  \
    --RoomId 1
```

Output: 
```
{
    "Response": {
        "AutoMic": 1,
        "EndTime": 1,
        "Name": "xx",
        "AudioQuality": 1,
        "Resolution": 1,
        "MaxMicNumber": 1,
        "SubType": "xx",
        "RequestId": "213das",
        "SdkAppId": 1,
        "TeacherId": "xx",
        "StartTime": 1,
        "DisableRecord": 1,
        "Assistants": [
            "xx"
        ]
    }
}
```

