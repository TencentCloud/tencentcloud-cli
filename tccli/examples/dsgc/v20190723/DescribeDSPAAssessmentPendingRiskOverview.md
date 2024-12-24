**Example 1: 查询待处理风险统计数**



Input: 

```
tccli dsgc DescribeDSPAAssessmentPendingRiskOverview --cli-unfold-argument  \
    --DspaId dspa-2mlc8asd \
    --TemplateId 2
```

Output: 
```
{
    "Response": {
        "AffectedAssetCount": 0,
        "WeekRatio": 0,
        "PendingRiskCount": 0,
        "RequestId": "2b0de1a7-b984-490b-b616-bbc67668e76a"
    }
}
```

