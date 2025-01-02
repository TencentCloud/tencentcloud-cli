**Example 1: 获取函数预置并发详情**



Input: 

```
tccli scf GetProvisionedConcurrencyConfig --cli-unfold-argument  \
    --FunctionName functionName1 \
    --Namespace default \
    --Qualifier 1
```

Output: 
```
{
    "Response": {
        "UnallocatedConcurrencyNum": 2343,
        "Allocated": [
            {
                "Qualifier": "1",
                "AvailableProvisionedConcurrencyNum": 1,
                "AllocatedProvisionedConcurrencyNum": 1,
                "Status": "Done",
                "StatusReason": "",
                "TriggerActions": []
            },
            {
                "Qualifier": "2",
                "AvailableProvisionedConcurrencyNum": 1,
                "AllocatedProvisionedConcurrencyNum": 1,
                "Status": "Done",
                "StatusReason": "",
                "TriggerActions": [
                    {
                        "TriggerName": "timer-1",
                        "ProvisionedType": "Default",
                        "TriggerProvisionedConcurrencyNum": 1,
                        "TriggerCronConfig": "30 42 15 20 12 * 2024"
                    }
                ]
            }
        ],
        "RequestId": "dsdsfsdf-b246-4fe5-812a-f77f1275471a"
    }
}
```

