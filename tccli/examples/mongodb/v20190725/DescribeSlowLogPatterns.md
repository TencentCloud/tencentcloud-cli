**Example 1: 查询数据库慢日志统计信息**



Input: 

```
tccli mongodb DescribeSlowLogPatterns --cli-unfold-argument  \
    --InstanceId cmgo-a3bm93hf \
    --StartTime '2020-04-20 00:00:00' \
    --EndTime '2020-04-20 22:00:00' \
    --SlowMS 100 \
    --Offset 0 \
    --Limit 100
```

Output: 
```
{
    "Response": {
        "Count": 2,
        "RequestId": "895de939-f726-4cb0-bb02-3890289479e3",
        "SlowLogPatterns": [
            {
                "AverageTime": 699,
                "MaxTime": 5335,
                "Pattern": "admin.$cmd.command",
                "Total": 12
            },
            {
                "AverageTime": 271,
                "MaxTime": 423,
                "Pattern": "local.system.replset.command",
                "Total": 8
            }
        ]
    }
}
```

