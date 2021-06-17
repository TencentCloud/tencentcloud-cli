**Example 1: 查询使用计划使用量**



Input: 

```
tccli market GetUsagePlanUsageAmount --cli-unfold-argument  \
    --InstanceId 123456789
```

Output: 
```
{
    "Response": {
        "MaxRequestNum": 1000,
        "InUseRequestNum": 500,
        "RemainingRequestNum": 500,
        "RequestId": "xx"
    }
}
```

