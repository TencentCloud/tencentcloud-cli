**Example 1: 查询计量后付费按量计费策略**

无

Input: 

```
tccli billing DescribeMeasurePostPayState --cli-unfold-argument  \
    --ProductCode p_bsp \
    --SubscriptionId bsp100570
```

Output: 
```
{
    "Response": {
        "Data": {
            "State": 1
        },
        "RequestId": "d252bea5-dfb9-45b8-85b3-fcbcc0405094"
    }
}
```

