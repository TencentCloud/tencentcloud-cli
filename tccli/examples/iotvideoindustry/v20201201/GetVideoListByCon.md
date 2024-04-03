**Example 1: 查询指定设备某天的录制情况**



Input: 

```
tccli iotvideoindustry GetVideoListByCon --cli-unfold-argument  \
    --DeviceId xxxxx \
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
                "RecordTaskId": "xxxxxx",
                "RecordPlanId": "plan-xxxxx",
                "StartTime": 1608603764,
                "EndTime": 0,
                "EventId": 1,
                "VideoUrl": "",
                "RecordStatus": 1
            }
        ]
    }
}
```

**Example 2: 查询指定设备最近一天的录像情况**



Input: 

```
tccli iotvideoindustry GetVideoListByCon --cli-unfold-argument  \
    --DeviceId xxxxx \
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
                "RecordTaskId": "xxxxxx",
                "RecordPlanId": "plan-xxxxx",
                "StartTime": 1608603764,
                "EndTime": 0,
                "VideoUrl": "",
                "RecordStatus": 1
            }
        ]
    }
}
```

