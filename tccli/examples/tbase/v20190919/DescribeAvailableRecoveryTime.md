**Example 1: TbaseV2获取回档时间**



Input: 

```
tccli tbase DescribeAvailableRecoveryTime --cli-unfold-argument  \
    --InstanceId tdpg-751k9fi1
```

Output: 
```
{
    "Response": {
        "RecoveryStatus": "init",
        "EndTime": "2025-07-21 12:00:00",
        "RequestId": "123e4567-e89b-12d3-a456-426614174000",
        "StartTime": "2025-07-21 10:00:00",
        "RecoveryTaskId": 12345
    }
}
```

