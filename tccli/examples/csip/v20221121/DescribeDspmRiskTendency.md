**Example 1: 查询Dspm风险趋势**



Input: 

```
tccli csip DescribeDspmRiskTendency --cli-unfold-argument  \
    --StartDate 2025-03-01 \
    --EndDate 2025-03-03
```

Output: 
```
{
    "Response": {
        "RiskTendencySet": [],
        "RequestId": "cf839eee-b651-4ff3-9b49-173f9f55733f"
    }
}
```

