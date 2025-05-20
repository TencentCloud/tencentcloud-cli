**Example 1: 获取硬盘分区使用图**



Input: 

```
tccli lighthouse DescribeGraphData --cli-unfold-argument  \
    --Module lighthouse, \
    --Namespace qce/cvm, \
    --MetricName disk_usage, \
    --UnInstanceID lhins-20109vr5, \
    --UUID 105047cf-0190-496f-806f-017064cc9971,
```

Output: 
```
{
    "Response": {
        "EndTime": "2021-03-19T18:11:21+08:00",
        "MetricName": "disk_usage",
        "Partitions": [],
        "Period": 0,
        "RequestId": "a61a15bc-0228-4661-9957-f893ddadc7b6",
        "StartTime": "2021-03-19T17:11:21+08:00"
    }
}
```

