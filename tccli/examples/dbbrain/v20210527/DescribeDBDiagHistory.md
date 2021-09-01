**Example 1: 获取实例诊断事件列表**



Input: 

```
tccli dbbrain DescribeDBDiagHistory --cli-unfold-argument  \
    --StartTime '2019-01-01 00:00:00' \
    --EndTime '2019-01-01 01:00:00' \
    --InstanceId cdb-test
```

Output: 
```
{
    "Response": {
        "RequestId": "ed279d8b-a9d9-48d6-9429-e0fde000994a",
        "Events": [
            {
                "DiagType": "行锁",
                "StartTime": "2019-01-01 00:00:20",
                "EndTime": "2019-01-01 00:00:30",
                "InstanceId": "cdb-test",
                "Region": "ap-beijing",
                "Metric": "",
                "EventId": 5,
                "Severity": 4,
                "Outline": "监控指标 \"innodb_row_lock_waits\" 告警，当前值 131",
                "DiagItem": "更新语句等待行锁"
            }
        ]
    }
}
```

