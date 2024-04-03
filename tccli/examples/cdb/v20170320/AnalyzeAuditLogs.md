**Example 1: 审计日志聚合统计**

审计日志聚合统计

Input: 

```
tccli cdb AnalyzeAuditLogs --cli-unfold-argument  \
    --InstanceId cdb-r9bpb9gs \
    --StartTime 2023-02-16 00:00:20 \
    --EndTime 2023-02-16 00:10:20 \
    --AggregationConditions.0.AggregationField host \
    --AggregationConditions.0.Offset 0 \
    --AggregationConditions.0.Limit 3 \
    --AggregationConditions.1.AggregationField sqlType \
    --AggregationConditions.1.Offset 3 \
    --AggregationConditions.1.Limit 3
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "AggregationField": "host",
                "Buckets": [
                    {
                        "Count": 89,
                        "Key": "100.122.76.176"
                    },
                    {
                        "Count": 10,
                        "Key": "9.71.156.179"
                    },
                    {
                        "Count": 1,
                        "Key": "10.0.6.6"
                    }
                ]
            },
            {
                "AggregationField": "sqlType",
                "Buckets": [
                    {
                        "Count": 13,
                        "Key": "LOGOUT"
                    },
                    {
                        "Count": 5,
                        "Key": "CREATE"
                    },
                    {
                        "Count": 2,
                        "Key": "INSERT"
                    }
                ]
            }
        ],
        "RequestId": "0000000000000-00000-014",
        "TotalCount": 100
    }
}
```

**Example 2: 先过滤后聚合审计日志**

先过滤后聚合审计日志

Input: 

```
tccli cdb AnalyzeAuditLogs --cli-unfold-argument  \
    --InstanceId cdb-r9bpb9gs \
    --StartTime 2023-02-16 00:00:00 \
    --EndTime 2023-02-17 00:00:00 \
    --AuditLogFilter.SqlTypes create \
    --AggregationConditions.0.AggregationField host \
    --AggregationConditions.0.Offset 0 \
    --AggregationConditions.0.Limit 3
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "AggregationField": "host",
                "Buckets": [
                    {
                        "Count": 3,
                        "Key": "100.122.76.176"
                    },
                    {
                        "Count": 2,
                        "Key": "9.71.156.179"
                    }
                ]
            }
        ],
        "RequestId": "0000000000000-00000-015",
        "TotalCount": 5
    }
}
```

