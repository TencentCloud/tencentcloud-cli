**Example 1: 查询错误事件**



Input: 

```
tccli rum DescribeTDEMMetricDistribution --cli-unfold-argument  \
    --AppId 1 \
    --StartTime 1710000000000 \
    --EndTime 1710086400000 \
    --EventType js_error \
    --Metrics count \
    --GroupBy os
```

Output: 
```
{
    "Response": {
        "Total": 0,
        "RequestId": "0ebcf212-a711-4685-9721-1dbd3be27be0"
    }
}
```

