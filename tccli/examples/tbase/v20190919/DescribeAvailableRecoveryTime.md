**Example 1: TbaseV2获取回档时间**



Input: 

```
tccli tbase DescribeAvailableRecoveryTime --cli-unfold-argument  \
    --InstanceId xx
```

Output: 
```
{
    "Response": {
        "RecoveryStatus": "xx",
        "EndTime": "xx",
        "RequestId": "xx",
        "StartTime": "xx",
        "RecoveryTaskId": 0
    }
}
```

