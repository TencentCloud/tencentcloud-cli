**Example 1: 风险级别趋势统计**

风险级别趋势统计

Input: 

```
tccli dsgc DescribeDSPAAssessmentRiskLevelTrend --cli-unfold-argument  \
    --DspaId dspa-92aabacd \
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
                "High": 0,
                "Medium": 0,
                "Low": 0,
                "Total": 0
            },
            {
                "Date": "09-02",
                "High": 0,
                "Medium": 0,
                "Low": 0,
                "Total": 0
            },
            {
                "Date": "09-03",
                "High": 0,
                "Medium": 0,
                "Low": 0,
                "Total": 0
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
tccli dsgc DescribeDSPAAssessmentRiskLevelTrend --cli-unfold-argument  \
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
                "High": 1,
                "Medium": 1,
                "Low": 1,
                "Total": 1
            }
        ],
        "RequestId": "abc"
    }
}
```

