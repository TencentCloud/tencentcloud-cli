**Example 1: 风险数量概览统计**

风险数量概览统计

Input: 

```
tccli dsgc DescribeDSPAAssessmentRiskOverview --cli-unfold-argument  \
    --DspaId dspa-92aabacd
```

Output: 
```
{
    "Response": {
        "TotalCount": 6,
        "HighRiskCount": 1,
        "HighRiskWeekRatio": 0,
        "HighRiskDayRatio": 0,
        "RequestId": "128009ac-7df4-0530-cc92-52f0d945e191"
    }
}
```

