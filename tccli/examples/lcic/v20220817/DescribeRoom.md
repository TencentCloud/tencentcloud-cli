**Example 1: 房间信息**

获取课堂房间信息

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
        "RecordUrl": "https://example.com/test.mp4",
        "Name": "test",
        "AudioQuality": 1,
        "MaxMicNumber": 1,
        "SubType": "videodoc",
        "SdkAppId": 1,
        "RequestId": "test",
        "StartTime": 1,
        "TeacherId": "test",
        "Assistants": [
            "test"
        ],
        "EndTime": 1,
        "Resolution": 1,
        "DisableRecord": 1,
        "Status": 0,
        "EnableDirectControl": 0,
        "GroupId": "afdg"
    }
}
```

