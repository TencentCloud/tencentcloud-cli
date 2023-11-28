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

