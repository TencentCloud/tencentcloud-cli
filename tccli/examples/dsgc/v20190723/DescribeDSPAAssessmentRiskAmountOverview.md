**Example 1: 示例**

风险概览页风险数量和受影响资产数概览统计

Input: 

```
tccli dsgc DescribeDSPAAssessmentRiskAmountOverview --cli-unfold-argument  \
    --DspaId dspa-a1b2c3d4 \
    --TemplateId 2
```

Output: 
```
{
    "Response": {
        "TotalRiskCount": 0,
        "TotalAffectedAssetCount": 0,
        "RequestId": "e298a8a2-e620-4cc5-9b85-4f0e22d273bf"
    }
}
```

