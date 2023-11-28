**Example 1: 示例**



Input: 

```
tccli dsgc DescribeDSPAAssessmentProcessingRiskOverview --cli-unfold-argument  \
    --DspaId abc \
    --TemplateId 2
```

Output: 
```
{
    "Response": {
        "ProcessingRiskCount": 0,
        "AffectedAssetCount": 0,
        "WeekRatio": 0,
        "RequestId": "abc"
    }
}
```

