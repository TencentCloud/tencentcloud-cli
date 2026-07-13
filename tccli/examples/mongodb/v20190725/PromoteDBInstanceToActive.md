**Example 1: 灾备或只读实例转正**



Input: 

```
tccli mongodb PromoteDBInstanceToActive --cli-unfold-argument  \
    --MasterId cmgo-******** \
    --InstanceId cmgo-********
```

Output: 
```
{
    "Response": {
        "RequestId": "230c9c0e-a56f-4639-81ee-3cb46905c087",
        "FlowId": 10001
    }
}
```

