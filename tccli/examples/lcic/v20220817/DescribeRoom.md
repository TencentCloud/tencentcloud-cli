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

**Example 2: 示例**

获取房间信息

Input: 

```
tccli lcic DescribeRoom --cli-unfold-argument  \
    --RoomId 331450358
```

Output: 
```
{
    "Response": {
        "Assistants": [],
        "AudioQuality": 0,
        "AutoMic": 0,
        "DisableRecord": 0,
        "EnableDirectControl": 0,
        "EndTime": 1687943391,
        "GroupId": "",
        "InteractionMode": 1,
        "IsGradingRequiredPostClass": 0,
        "MaxMicNumber": 2,
        "Name": "测试1",
        "RecordUrl": "",
        "RequestId": "a8dea9b9-5172-4c01-a53d-5a53437f7fdf",
        "Resolution": 1,
        "RoomType": 1,
        "SdkAppId": 3923193,
        "StartTime": 1687943339,
        "Status": 0,
        "SubType": "video",
        "TeacherId": "2O2bjPEXxStIac3NC9kfH3mHeBC",
        "VideoOrientation": 1
    }
}
```

