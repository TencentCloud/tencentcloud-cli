**Example 1: 查询慢日志数据**



Input: 

```
tccli tdmysql DescribeSlowLogs --cli-unfold-argument  \
    --InstanceId tdsql3-535ae7e5 \
    --StartTime 2024-06-18 21:50:00 \
    --EndTime 2024-06-25 21:54:00
```

Output: 
```
{
    "Response": {
        "Items": [],
        "RequestId": "3c2ebf73-d02e-4a39-a2c1-6b365d096f71",
        "TotalCount": 0
    }
}
```

