**Example 1: 质量评分趋势**

质量评分趋势

Input: 

```
tccli wedata DescribeQualityScoreTrend --cli-unfold-argument  \
    --StatisticsStartDate 1679414400 \
    --StatisticsEndDate 1679414400 \
    --ProjectId 1 \
    --DatasourceId 123
```

Output: 
```
{
    "Response": {
        "RequestId": "8f440fef-24c6-4f5c-a58e-7e0aa7aa19d7",
        "Data": {
            "AverageScore": 0.0,
            "DailyScoreList": [
                {
                    "StatisticsDate": 0,
                    "Score": 0.0
                }
            ]
        }
    }
}
```

