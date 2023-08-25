**Example 1: 风险项处理趋势统计**

风险项处理趋势统计

Input: 

```
tccli dsgc DescribeDSPAAssessmentRiskDealedTrend --cli-unfold-argument  \
    --DspaId dspa-97538993 \
    --StartTime 2022-09-01 \
    --EndTime 2022-09-03
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "Date": "09-01",
                "Unhandled": 0,
                "Handled": 0
            },
            {
                "Date": "09-02",
                "Unhandled": 0,
                "Handled": 0
            },
            {
                "Date": "09-03",
                "Unhandled": 0,
                "Handled": 0
            }
        ],
        "RequestId": "128009ac-7df4-0530-cc92-52f0d945e191"
    }
}
```

**Example 2: xx**

xx

Input: 

```
tccli dsgc DescribeDSPAAssessmentRiskDealedTrend --cli-unfold-argument  \
    --DspaId abc \
    --StartTime abc \
    --EndTime abc \
    --TemplateId abc
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "Date": "abc",
                "Unhandled": 1,
                "Handled": 1,
                "NewDiscoveryHandled": 1
            }
        ],
        "RequestId": "abc"
    }
}
```

