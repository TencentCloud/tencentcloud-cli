**Example 1: 查询风险的处理历史**

查询风险的处理历史

Input: 

```
tccli dsgc DescribeDSPAAssessmentRiskProcessHistory --cli-unfold-argument  \
    --DspaId dspa-97538993 \
    --RiskId 1
```

Output: 
```
{
    "Response": {
        "ProcessHistory": [
            {
                "Time": "2023-09-20 16:16:53",
                "Status": 3,
                "Handler": "系统（最近一次扫描未发现）",
                "Note": "已处理"
            }
        ],
        "RequestId": "1f1765cf-c01a-4a93-95b2-99108f4aa04f"
    }
}
```

