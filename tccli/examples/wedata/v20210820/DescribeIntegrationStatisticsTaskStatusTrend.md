**Example 1: DescribeIntegrationStatisticsTaskStatusTrend**



Input: 

```
tccli wedata DescribeIntegrationStatisticsTaskStatusTrend --cli-unfold-argument  \
    --QueryDate abc \
    --TaskType 0 \
    --ProjectId abc \
    --ExecutorGroupId abc
```

Output: 
```
{
    "Response": {
        "TrendsData": [
            {
                "StatisticName": [
                    "abc"
                ],
                "StatisticValue": [
                    0
                ],
                "StatisticType": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

