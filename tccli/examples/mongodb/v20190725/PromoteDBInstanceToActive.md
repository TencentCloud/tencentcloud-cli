**Example 1: 灾备实例转正**

灾备实例转正

Input: 

```
tccli mongodb PromoteDBInstanceToActive --cli-unfold-argument  \
    --MasterId cmgo-ggh7rpz5 \
    --InstanceId cmgo-a7bb6vd7
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

