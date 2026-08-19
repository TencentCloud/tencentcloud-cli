**Example 1: 云资源配置检查报告风险统计**



Input: 

```
tccli csip DescribeCFGRiskReportStatistics --cli-unfold-argument  \
    --MemberId mem-68b8*8*a65***000 \
    --StandardIDs 3
```

Output: 
```
{
    "Response": {
        "TotalAssetCount": 1439,
        "TotalRiskCount": 2833,
        "TotalRuleCount": 34,
        "RequestId": "b2f369df-c79f-494d-9a50-27a793cf0a1c"
    }
}
```

