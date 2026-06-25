**Example 1: 查看审计日志topsql**

查询最近1分钟的审计日志topsql 列表

Input: 

```
tccli dbbrain DescribeDBAuditLogTopSqls --cli-unfold-argument  \
    --StartTime 2026-06-24T11:58:50+08:00 \
    --EndTime 2026-06-24T11:59:50+08:00 \
    --Product mysql \
    --InstanceId cdb-h6b22q74 \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TopSqls": [
            {
                "AffectRows": 0,
                "AffectRowsAvg": 0,
                "AffectRowsMax": 0,
                "AffectRowsMin": 0,
                "CheckRows": 21,
                "CheckRowsAvg": 1,
                "CheckRowsMax": 1,
                "CheckRowsMin": 1,
                "CpuTime": 0.00157,
                "CpuTimeAvg": 0.32343,
                "CpuTimeMax": 0.000125,
                "CpuTimeMin": 0.000416,
                "DB": "",
                "ExecTimes": 21,
                "IoWaitTime": 0,
                "IoWaitTimeAvg": 0,
                "IoWaitTimeMax": 0,
                "IoWaitTimeMin": 0,
                "Latency": 0.13,
                "LatencyAvg": 0.006173,
                "LatencyMax": 0.00774,
                "LatencyMin": 0.00401,
                "LockWaitTime": 0,
                "LockWaitTimeAvg": 0,
                "LockWaitTimeMax": 0,
                "LockWaitTimeMin": 0,
                "QueryTimeRatio": "29.0",
                "SentRows": 21,
                "SentRowsAvg": 1,
                "SqlTemplate": "select @@max_allowed_packet",
                "SqlTemplateId": "3978247360646555614",
                "SqlText": null,
                "SqlType": "Select",
                "TableName": ""
            }
        ],
        "TotalCount": 15,
        "RequestId": "aec7ce88-cc46-4dfe-9e07-12867a2912e7"
    }
}
```

