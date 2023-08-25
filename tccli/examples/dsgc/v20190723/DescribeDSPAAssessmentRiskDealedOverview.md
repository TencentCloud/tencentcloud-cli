**Example 1: 遗留待处理概览统计**

遗留待处理&昨日完成风险处置概览统计

Input: 

```
tccli dsgc DescribeDSPAAssessmentRiskDealedOverview --cli-unfold-argument  \
    --DspaId dspa-92aabacd
```

Output: 
```
{
    "Response": {
        "TotalCount": 6,
        "YesterdayDealedCount": 1,
        "UnDealedRiskWeekRatio": 0,
        "UnDealedRiskDayRatio": 0,
        "RequestId": "128009ac-7df4-0530-cc92-52f0d945e191"
    }
}
```

