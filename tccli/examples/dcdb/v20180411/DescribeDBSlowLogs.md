**Example 1: 无**



Input: 

```
tccli dcdb DescribeDBSlowLogs --cli-unfold-argument  \
    --ShardId shard-ngbrea6b \
    --InstanceId dcdbt-21dfpcv1 \
    --Limit 10 \
    --StartTime 2022-03-22 00:00:00 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Data": [],
        "LockTimeSum": 0,
        "QueryCount": 0,
        "QueryTimeSum": 0,
        "RequestId": "6e9bf5de-8d17-4848-915d-aee0047909eb",
        "Total": 0
    }
}
```

