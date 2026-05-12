**Example 1: 查询Dspm风险详情**



Input: 

```
tccli csip DescribeDspmRiskDetail --cli-unfold-argument  \
    --RiskId f7966e40-e20f-4540-9927-d34fb6cc4747 \
    --Filter.Limit 100 \
    --Filter.Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "cf839eee-b651-4ff3-9b49-173f9f55733f"
    }
}
```

