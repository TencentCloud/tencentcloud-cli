**Example 1: 查询处理中风险统计数**



Input: 

```
tccli dsgc DescribeDSPAAssessmentProcessingRiskOverview --cli-unfold-argument  \
    --DspaId dspa-23bnnjk5 \
    --TemplateId 2
```

Output: 
```
{
    "Response": {
        "ProcessingRiskCount": 0,
        "AffectedAssetCount": 0,
        "WeekRatio": 0,
        "RequestId": "18f6cc8f-fab5-46f9-881d-adf57580befd"
    }
}
```

