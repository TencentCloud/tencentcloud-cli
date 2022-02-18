**Example 1: 查询实例可恢复的时间范围**



Input: 

```
tccli postgres DescribeAvailableRecoveryTime --cli-unfold-argument  \
    --DBInstanceId postgres-apzvwncr
```

Output: 
```
{
    "Response": {
        "RequestId": "08fdf411-5d39-44f2-8e1d-a58ee60b237d",
        "RecoveryBeginTime": "2021-12-24 03:41:50",
        "RecoveryEndTime": "2021-12-25 17:43:27"
    }
}
```

