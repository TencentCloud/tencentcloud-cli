**Example 1: DescribeIntegrationStatisticsInstanceTrend**



Input: 

```
tccli wedata DescribeIntegrationStatisticsInstanceTrend --cli-unfold-argument  \
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

