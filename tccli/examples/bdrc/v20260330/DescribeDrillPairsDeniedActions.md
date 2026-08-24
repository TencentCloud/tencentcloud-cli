**Example 1: 查询演练操作掩码**



Input: 

```
tccli bdrc DescribeDrillPairsDeniedActions --cli-unfold-argument  \
    --DrillPairType INSTANCE \
    --DrillPairIds drillpair-p50csne5
```

Output: 
```
{
    "Response": {
        "DrillPairDeniedActionSet": [
            {
                "DeniedActions": [],
                "DrillPairId": "drillpair-p50csne5"
            }
        ],
        "RequestId": "55237331-f650-4023-bc60-2a091c6c9201"
    }
}
```

