**Example 1: xx**

xx

Input: 

```
tccli dsgc DescribeDSPAAssessmentHighRiskTop10Overview --cli-unfold-argument  \
    --DspaId abc \
    --TemplateId 0
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

