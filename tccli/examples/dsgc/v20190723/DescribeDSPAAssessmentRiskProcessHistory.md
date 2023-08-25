**Example 1: xx**

xx

Input: 

```
tccli dsgc DescribeDSPAAssessmentRiskProcessHistory --cli-unfold-argument  \
    --DspaId abc \
    --RiskId 0
```

Output: 
```
{
    "Response": {
        "ProcessHistory": [
            {
                "Time": "abc",
                "Status": 0,
                "Handler": "abc",
                "Note": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

