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
            "VideoUrl": "http://cos.ap-guangzhou.myqcloud.com/iot-video-recodgb-125687/0001.mp4",
            "RecordTaskId": "task01",
            "RecordId": "1611732169_1611732269",
            "SceneId": 0,
            "StartTime": 0,
            "RecordStatus": 0,
            "RecordPlanId": "plan-7fqulsjc",
            "EndTime": 0,
            "WarnId": 0
        },
        "TotalCount": 1752,
        "RequestId": "d3d6f466-f2c2-44df-b78b-383ba717a3d8",
        "RecordList": [
            {
                "EventId": 1,
                "VideoUrl": "http://cos.ap-guangzhou.myqcloud.com/iot-video-recodgb-125687/0001.mp4",
                "RecordTaskId": "task01",
                "RecordId": "1611732169_1611732269",
                "SceneId": 0,
                "StartTime": 1639470612,
                "RecordStatus": 1,
                "RecordPlanId": "plan-7fqulsjc",
                "EndTime": 0,
                "WarnId": 0
            },
            {
                "EventId": 1,
                "VideoUrl": "http://cos.ap-guangzhou.myqcloud.com/iot-video-recodgb-125687/0001.mp4",
                "RecordTaskId": "task01",
                "RecordId": "1611732169_1611732269",
                "SceneId": 0,
                "StartTime": 1639470009,
                "RecordPlanId": "plan-7fqulsjc",
                "RecordStatus": 0,
                "EndTime": 1639470609,
                "WarnId": 0
            }
        ]
    }
}
```

