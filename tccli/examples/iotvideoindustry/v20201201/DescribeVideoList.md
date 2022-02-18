**Example 1: 查询录像文件列表**



Input: 

```
tccli iotvideoindustry DescribeVideoList --cli-unfold-argument  \
    --ChannelId 99576636581320000330_99576636581320000330 \
    --Limit 2 \
    --DeviceId 99576636581320000330_99576636581320000330 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "VideoList": {
            "EventId": 0,
            "VideoUrl": "xx",
            "RecordTaskId": "xx",
            "RecordId": "xx",
            "SceneId": 0,
            "StartTime": 0,
            "RecordStatus": 0,
            "RecordPlanId": "xx",
            "EndTime": 0,
            "WarnId": 0
        },
        "TotalCount": 1752,
        "RequestId": "xx",
        "RecordList": [
            {
                "EventId": 1,
                "VideoUrl": "xx",
                "RecordTaskId": "xx",
                "RecordId": "xx",
                "SceneId": 0,
                "StartTime": 1639470612,
                "RecordStatus": 1,
                "RecordPlanId": "xx",
                "EndTime": 0,
                "WarnId": 0
            },
            {
                "EventId": 1,
                "VideoUrl": "xx",
                "RecordTaskId": "xx",
                "RecordId": "xx",
                "SceneId": 0,
                "StartTime": 1639470009,
                "RecordPlanId": "xx",
                "RecordStatus": 0,
                "EndTime": 1639470609,
                "WarnId": 0
            }
        ]
    }
}
```

