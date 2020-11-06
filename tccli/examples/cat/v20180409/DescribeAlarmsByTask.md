**Example 1: 按任务查询拨测告警列表示例**



Input: 

```
tccli cat DescribeAlarmsByTask --cli-unfold-argument  \
    --Offset 0 \
    --Limit 2 \
    --BeginTime '2019-12-11 00:04:24' \
    --EndTime '2019-12-12 00:04:24' \
    --TaskId 260409
```

Output: 
```
{
    "Response": {
        "AlarmInfos": [
            {
                "ObjId": "taskId_260409",
                "FirstOccurTime": "2019-12-11 23:23:00",
                "ObjName": "贴吧云签到",
                "LastOccurTime": "2019-12-11 23:28:25",
                "Status": 3,
                "Content": "近10分钟可用率0.0%,低于或等于告警阈值10.0%,请检查您的服务是否正常",
                "MetricName": "avail_ratio_recent10",
                "TaskId": 260409,
                "MetricValue": "0.0%"
            }
        ],
        "FaultTimeSpec": "5分5秒",
        "FaultRatio": 0.3762,
        "RequestId": "62116e8d-94da-401c-9d38-145d92ce1f43"
    }
}
```

