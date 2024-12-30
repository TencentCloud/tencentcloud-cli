**Example 1: 查询指定设备某天的录制情况**



Input: 

```
tccli iotvideoindustry GetVideoListByCon --cli-unfold-argument  \
    --DeviceId 99870353841320000007_99870353841320000007 \
    --Date 2020-12-12 \
    --Offset 0 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "RequestId": "d3d6f466-f2c2-44df-b78b-383ba717a3d8",
        "TotalCount": 1,
        "VideoList": [
            {
                "RecordTaskId": "fyw1k9l5",
                "RecordPlanId": "plan-fyw1k9l5",
                "StartTime": 1608603764,
                "EndTime": 0,
                "EventId": 1,
                "VideoUrl": "",
                "RecordStatus": 1,
                "SceneId": 234354,
                "WarnId": "834",
                "RecordId": "1611732169_1611732269"
            }
        ]
    }
}
```

**Example 2: 查询指定设备最近一天的录像情况**



Input: 

```
tccli iotvideoindustry GetVideoListByCon --cli-unfold-argument  \
    --DeviceId 99870353841320000007_99870353841320000007 \
    --LatestDay 1 \
    --Offset 0 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "RequestId": "d3d6f466-f2c2-44df-b78b-383ba717a3d8",
        "TotalCount": 1,
        "VideoList": [
            {
                "RecordTaskId": "fyw1k9l5",
                "RecordPlanId": "plan-fyw1k9l5",
                "StartTime": 1608603764,
                "EndTime": 0,
                "EventId": 1,
                "VideoUrl": "",
                "RecordStatus": 1,
                "SceneId": 234354,
                "WarnId": "834",
                "RecordId": "1611732169_1611732269"
            }
        ]
    }
}
```

