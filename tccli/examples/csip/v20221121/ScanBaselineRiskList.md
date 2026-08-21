**Example 1: 检测具体风险**

检测具体风险

Input: 

```
tccli csip ScanBaselineRiskList --cli-unfold-argument  \
    --PolicyType SELF \
    --PolicyID 2 \
    --CategoryID 2 \
    --ParentCategoryID 2012 \
    --RiskIDList risk-id2 \
    --ItemID 2 \
    --MemberId mem-************95752f66e429
```

Output: 
```
{
    "Response": {
        "RequestId": "a39c2f2a-49ba-4982-bdf7-561ff527d0bd"
    }
}
```

