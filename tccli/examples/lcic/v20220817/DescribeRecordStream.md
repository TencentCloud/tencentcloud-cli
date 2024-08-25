**Example 1: DescribeRecordStream**

获取流信息

Input: 

```
tccli lcic DescribeRecordStream --cli-unfold-argument  \
    --SdkAppId 1 \
    --RoomId 1
```

Output: 
```
{
    "Response": {
        "ClassId": 3211258275,
        "ClassType": 2,
        "RequestId": "6a0cd621-e6df-46a5-8ce8-29800e49679d",
        "SchoolId": 39233193,
        "StreamInfo": [
            {
                "Duration": 224,
                "FileFormat": "mp4",
                "RecordSize": 14966923,
                "RecordUrl": "https://20910970.vod2.myqcloud.com/6cac6e5evodcq100915970/adcjfhbshgahd87/f0.mp4",
                "Role": "main",
                "StartTime": 1721099743,
                "StopTime": 1721099964,
                "UserId": "2TW2Kv091028NAmYkCQlsrT1lXgk",
                "VideoId": "125312342212911616"
            }
        ]
    }
}
```

