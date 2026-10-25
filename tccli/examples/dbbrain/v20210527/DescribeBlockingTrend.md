**Example 1: 查询阻塞趋势**

查询阻塞趋势（LockCount 表示这段时间内的锁采样上报次数）

Input: 

```
tccli dbbrain DescribeBlockingTrend --cli-unfold-argument  \
    --InstanceId mssql-qte20qje \
    --Product sqlserver \
    --StartTime 2026-10-19 20:15:00 \
    --EndTime 2026-10-19 20:16:00
```

Output: 
```
{
    "Response": {
        "DataPoints": [
            {
                "EndTime": "2026-10-19 20:15:01",
                "LockCount": 0,
                "MonitorLoopCount": 0,
                "StartTime": "2026-10-19 20:15:00"
            }
        ],
        "Granularity": "SECONDS",
        "GranularityMs": 1000,
        "RequestId": "d1afd140-7145-4bbe-800f-072853992d04"
    }
}
```

