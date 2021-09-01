**Example 1: 查询拨测告警列表示例**



Input: 

```
tccli cat DescribeAlarms --cli-unfold-argument  \
    --Offset 0 \
    --Limit 2
```

Output: 
```
{
    "Response": {
        "TotalCount": 56,
        "AlarmInfos": [
            {
                "ObjId": "taskId_67093",
                "FirstOccurTime": "2019-11-30 23:10:00",
                "ObjName": "普法网官网",
                "LastOccurTime": "2019-11-30 23:40:00",
                "Status": 1,
                "Content": " 当前可用率66.67%,低于告警阈值90.0%,共有2个拨测点低于平均值,最低(广东电信:0.0%)",
                "MetricName": "avail_ratio",
                "TaskId": 67093,
                "MetricValue": "66.67%"
            },
            {
                "ObjId": "taskId_208290",
                "FirstOccurTime": "2019-11-30 22:59:00",
                "ObjName": "用户中心可用性",
                "LastOccurTime": "2019-11-30 23:01:00",
                "Status": 1,
                "Content": "近30分钟可用率73.98%,低于告警阈值75.0%,共有2个拨测点低于平均值,最低(广东电信:61.76%)",
                "MetricName": "avail_ratio_recent30",
                "TaskId": 208290,
                "MetricValue": "73.98%"
            }
        ],
        "RequestId": "efd3d558-2708-4576-8cc0-83747fb639df"
    }
}
```

