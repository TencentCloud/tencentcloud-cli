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
        "RecordUrl": "xx",
        "Name": "xx",
        "AudioQuality": 1,
        "MaxMicNumber": 1,
        "SubType": "xx",
        "SdkAppId": 1,
        "RequestId": "xx",
        "StartTime": 1,
        "TeacherId": "xx",
        "Assistants": [
            "xx"
        ],
        "EndTime": 1,
        "Resolution": 1,
        "DisableRecord": 1
    }
}
```

