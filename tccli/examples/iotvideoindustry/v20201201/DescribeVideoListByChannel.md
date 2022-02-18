**Example 1: 获取录制文件列表**



Input: 

```
tccli iotvideoindustry DescribeVideoListByChannel --cli-unfold-argument  \
    --Limit 10 \
    --ChannelId 99576636581320000330_99576636581320000330 \
    --Type 1 \
    --DeviceId 99576636581320000330_99576636581320000330 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "5830fae4-3a4c-4d88-9b46-ce9f0c62f7d1",
        "TotalCount": 94,
        "VideoList": [
            {
                "RecordId": "",
                "RecordTaskId": "20211214707e9bd48a3c443c922fce4fca3676ab",
                "RecordPlanId": "plan-fyw1k9l5",
                "StartTime": 1639467009,
                "EndTime": 1639467609,
                "EventId": 1,
                "VideoUrl": "https://1304886180.vod2.myqcloud.com/cac4da69vodcq1304886180/af1a6a2b387702292619211604/f0.mp4",
                "RecordStatus": 0,
                "SceneId": 0,
                "WarnId": 0
            },
            {
                "RecordId": "",
                "RecordTaskId": "20211214707e9bd48a3c443c922fce4fca3676ab",
                "RecordPlanId": "plan-fyw1k9l5",
                "StartTime": 1639466409,
                "EndTime": 1639467009,
                "EventId": 1,
                "VideoUrl": "https://1304886180.vod2.myqcloud.com/cac4da69vodcq1304886180/e6c89beb387702292620245731/f0.mp4",
                "RecordStatus": 0,
                "SceneId": 0,
                "WarnId": 0
            },
            {
                "RecordId": "",
                "RecordTaskId": "20211214707e9bd48a3c443c922fce4fca3676ab",
                "RecordPlanId": "plan-fyw1k9l5",
                "StartTime": 1639465809,
                "EndTime": 1639466409,
                "EventId": 1,
                "VideoUrl": "https://1304886180.vod2.myqcloud.com/cac4da69vodcq1304886180/af0c9fad387702292619209122/f0.mp4",
                "RecordStatus": 0,
                "SceneId": 0,
                "WarnId": 0
            },
            {
                "RecordId": "",
                "RecordTaskId": "20211214707e9bd48a3c443c922fce4fca3676ab",
                "RecordPlanId": "plan-fyw1k9l5",
                "StartTime": 1639465209,
                "EndTime": 1639465809,
                "EventId": 1,
                "VideoUrl": "https://1304886180.vod2.myqcloud.com/cac4da69vodcq1304886180/66ca6a0c387702292618411154/f0.mp4",
                "RecordStatus": 0,
                "SceneId": 0,
                "WarnId": 0
            },
            {
                "RecordId": "",
                "RecordTaskId": "20211214707e9bd48a3c443c922fce4fca3676ab",
                "RecordPlanId": "plan-fyw1k9l5",
                "StartTime": 1639464609,
                "EndTime": 1639465209,
                "EventId": 1,
                "VideoUrl": "https://1304886180.vod2.myqcloud.com/cac4da69vodcq1304886180/70b296fd387702292618896352/f0.mp4",
                "RecordStatus": 0,
                "SceneId": 0,
                "WarnId": 0
            },
            {
                "RecordId": "",
                "RecordTaskId": "20211214707e9bd48a3c443c922fce4fca3676ab",
                "RecordPlanId": "plan-fyw1k9l5",
                "StartTime": 1639464009,
                "EndTime": 1639464609,
                "EventId": 1,
                "VideoUrl": "https://1304886180.vod2.myqcloud.com/cac4da69vodcq1304886180/25676513387702292617900591/f0.mp4",
                "RecordStatus": 0,
                "SceneId": 0,
                "WarnId": 0
            },
            {
                "RecordId": "",
                "RecordTaskId": "20211214707e9bd48a3c443c922fce4fca3676ab",
                "RecordPlanId": "plan-fyw1k9l5",
                "StartTime": 1639463409,
                "EndTime": 1639464009,
                "EventId": 1,
                "VideoUrl": "https://1304886180.vod2.myqcloud.com/cac4da69vodcq1304886180/5fbc368f387702292618107605/f0.mp4",
                "RecordStatus": 0,
                "SceneId": 0,
                "WarnId": 0
            },
            {
                "RecordId": "",
                "RecordTaskId": "20211214707e9bd48a3c443c922fce4fca3676ab",
                "RecordPlanId": "plan-fyw1k9l5",
                "StartTime": 1639462809,
                "EndTime": 1639463409,
                "EventId": 1,
                "VideoUrl": "https://1304886180.vod2.myqcloud.com/cac4da69vodcq1304886180/5fbb9e94387702292618106395/f0.mp4",
                "RecordStatus": 0,
                "SceneId": 0,
                "WarnId": 0
            },
            {
                "RecordId": "",
                "RecordTaskId": "20211214707e9bd48a3c443c922fce4fca3676ab",
                "RecordPlanId": "plan-fyw1k9l5",
                "StartTime": 1639462209,
                "EndTime": 1639462809,
                "EventId": 1,
                "VideoUrl": "https://1304886180.vod2.myqcloud.com/cac4da69vodcq1304886180/5fbb090a387702292618105143/f0.mp4",
                "RecordStatus": 0,
                "SceneId": 0,
                "WarnId": 0
            },
            {
                "RecordId": "",
                "RecordTaskId": "20211214707e9bd48a3c443c922fce4fca3676ab",
                "RecordPlanId": "plan-fyw1k9l5",
                "StartTime": 1639461609,
                "EndTime": 1639462209,
                "EventId": 1,
                "VideoUrl": "https://1304886180.vod2.myqcloud.com/cac4da69vodcq1304886180/8b748b6b387702292615903411/f0.mp4",
                "RecordStatus": 0,
                "SceneId": 0,
                "WarnId": 0
            }
        ]
    }
}
```

