**Example 1: 更新目标**



Input: 

```
tccli eb UpdateTarget --cli-unfold-argument  \
    --EnableBatchDelivery true \
    --RuleId rule-51wvf3is \
    --BatchEventCount 32 \
    --TargetId target-ceh92ss4 \
    --EventBusId eb-ohb9x6rg \
    --BatchTimeout 43
```

Output: 
```
{
    "Response": {
        "RequestId": "72b987c9-8842-47ac-9ad6-fa2bde3e936d"
    }
}
```

