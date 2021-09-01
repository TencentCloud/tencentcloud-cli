**Example 1: 根据时间获取回放文件列表(云端录制用)**

根据时间获取回放文件列表(云端录制用)

Input: 

```
tccli iotvideoindustry DescribeVideoList --cli-unfold-argument  \
    --DeviceId 99870353841320000007_99870353841320000007 \
    --Offset 0 \
    --Limit 10 \
    --StartTime 1616660711 \
    --EndTime 1616661017
```

Output: 
```
{
    "Response": {
        "VideoList": {
            "EventId": 1,
            "VideoUrl": "xx",
            "RecordTaskId": "xx",
            "StartTime": 1616661013,
            "RecordStatus": 0,
            "RecordPlanId": "xx",
            "EndTime": 1616661314
        },
        "TotalCount": 1,
        "RequestId": "xx",
        "RecordList": [
            {
                "EventId": 0,
                "VideoUrl": "xx",
                "RecordTaskId": "xx",
                "StartTime": 0,
                "RecordStatus": 0,
                "RecordPlanId": "xx",
                "EndTime": 0
            }
        ]
    }
}
```

