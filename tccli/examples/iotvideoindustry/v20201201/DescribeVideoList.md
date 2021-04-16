**Example 1: 根据时间获取回放文件列表(云端录制用)**

根据时间获取回放文件列表(云端录制用)

Input: 

```
tccli iotvideoindustry DescribeVideoList --cli-unfold-argument  \
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
            "VideoUrl": "http://1258344699.vod2.myqcloud.com/1b875455vodcq1258344699/32dcdd5d5285890815979923365/f0.mp4",
            "RecordTaskId": "20210325-dced0113e4384a0da0d832cc260d9d7c",
            "StartTime": 1616661013,
            "RecordStatus": 0,
            "RecordPlanId": "plan-5sio5j9m",
            "EndTime": 1616661314
        },
        "TotalCount": 1,
        "RequestId": "xx"
    }
}
```

