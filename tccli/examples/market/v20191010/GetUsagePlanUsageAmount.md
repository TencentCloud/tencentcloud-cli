**Example 1: 查询使用计划使用量**



Input: 

```
tccli market GetUsagePlanUsageAmount --cli-unfold-argument  \
    --InstanceId 45419893
```

Output: 
```
{
    "Response": {
        "MaxRequestNum": 1000,
        "InUseRequestNum": 500,
        "RemainingRequestNum": 500,
        "RequestId": "f598b754-b814-47e7-9052-5848cf9a8862"
    }
}
```

