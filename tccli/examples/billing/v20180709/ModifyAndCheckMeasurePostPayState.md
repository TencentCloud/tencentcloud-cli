**Example 1: 变更计量后付费按量计费策略并检查计量能力可用状态**

无

Input: 

```
tccli billing ModifyAndCheckMeasurePostPayState --cli-unfold-argument  \
    --ProductCode p_bsp \
    --State 1 \
    --RegionId 1 \
    --TriggerType 1 \
    --SubscriptionId bsp_test_003 \
    --Origin measure
```

Output: 
```
{
    "Response": {
        "Data": {
            "Available": true,
            "CurrentState": 1
        },
        "RequestId": "34032f2a-3ea8-4c83-b90a-1e58e7441a49"
    }
}
```

