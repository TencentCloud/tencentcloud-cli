**Example 1: 查询统计指标概览数据**



Input: 

```
tccli iotvideoindustry DescribeStatisticSummary --cli-unfold-argument  \
    --Date 2020-12-09
```

Output: 
```
{
    "Response": {
        "RecordingDevice": 3,
        "RequestId": "d3d6f466-f2c2-44df-b78b-383ba717a3d8",
        "StorageUsage": 1.22,
        "NonRecordingDevice": 1,
        "WatchFlux": 2.21,
        "P2PFluxTotal": 1.2,
        "P2PPeakValue": 2.4,
        "LivePushTotal": 5
    }
}
```

