**Example 1: 修改规则执行顺序**



Input: 

```
tccli cfw ModifySequenceRules --cli-unfold-argument  \
    --Data.0.Id 36114 \
    --Data.0.OrderIndex 8 \
    --Data.0.NewOrderIndex 7 \
    --Data.1.Id 36068 \
    --Data.1.OrderIndex 7 \
    --Data.1.NewOrderIndex 8 \
    --EdgeId  \
    --Direction 1 \
    --Area 
```

Output: 
```
{
    "Response": {
        "Status": 0,
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

