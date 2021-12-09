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
                "Qualifier": "xx",
                "AvailableProvisionedConcurrencyNum": 1,
                "StatusReason": "xx",
                "AllocatedProvisionedConcurrencyNum": 1,
                "TriggerActions": [
                    {
                        "TriggerProvisionedConcurrencyNum": 1,
                        "TriggerCronConfig": "xx",
                        "TriggerName": "xx"
                    }
                ]
            }
        ],
        "RequestId": "xx"
    }
}
```

