**Example 1: 获取函数预置并发详情**



Input: 

```
tccli scf GetProvisionedConcurrencyConfig --cli-unfold-argument  \
    --FunctionName test \
    --Qualifier 1
```

Output: 
```
{
    "Response": {
        "UnallocatedConcurrencyNum": 1,
        "Allocated": [
            {
                "Status": "xx",
                "AllocatedProvisionedConcurrencyNum": 1,
                "AvailableProvisionedConcurrencyNum": 1,
                "Qualifier": "xx",
                "StatusReason": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

