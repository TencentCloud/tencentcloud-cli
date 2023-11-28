**Example 1: 示例**



Input: 

```
tccli dsgc DescribeDSPAAssessmentHighRiskTop10Overview --cli-unfold-argument  \
    --DspaId abc \
    --TemplateId 1
```

Output: 
```
{
    "Response": {
        "AssetsList": [
            {
                "InstanceId": "abc",
                "AssetsName": "abc",
                "HighRiskCount": 0,
                "RiskType": "abc",
                "TotalRiskCount": 0
            }
        ],
        "RequestId": "abc"
    }
}
```

