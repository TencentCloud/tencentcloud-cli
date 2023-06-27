**Example 1: 查询表得分趋势**

查询表得分趋势

Input: 

```
tccli wedata DescribeTableScoreTrend --cli-unfold-argument  \
    --StatisticsStartDate 1679414400 \
    --StatisticsEndDate 1679414400 \
    --ProjectId 1 \
    --TableId 23f
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

