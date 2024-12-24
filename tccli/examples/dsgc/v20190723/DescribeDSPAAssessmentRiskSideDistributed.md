**Example 1: 示例**

查询风险面的分布详情

Input: 

```
tccli dsgc DescribeDSPAAssessmentRiskSideDistributed --cli-unfold-argument  \
    --DspaId dspa-001 \
    --TemplateId 1
```

Output: 
```
{
    "Response": {
        "RiskSideDistributed": [
            {
                "AssessmentRiskSide": {
                    "Key": "风险面1",
                    "Value": 3
                },
                "AssessmentRisk": [
                    {
                        "Key": "风险类型1",
                        "Value": 2
                    }
                ]
            }
        ],
        "RequestId": "test-001"
    }
}
```

