**Example 1: 修改数据检索策略**



Input: 

```
tccli cfs ModifyDataRetrieval --cli-unfold-argument  \
    --DataRetrievalId dataretrieval-72986e77 \
    --DataRetrievalName default-rule \
    --CompoundCondition from entries|where size >4096 \
    --QueryCondition path:/cfs/abc/* AND type:file AND size:>0 \
    --DayOfMonth 1 \
    --Hour 12
```

Output: 
```
{
    "Response": {
        "RequestId": "bebba10a-eb1f-492b-8a64-468ed48394f5"
    }
}
```

