**Example 1: DescribeIntegrationStatisticsInstanceTrend**



Input: 

```
tccli wedata DescribeIntegrationStatisticsInstanceTrend --cli-unfold-argument  \
    --QueryDate 2024-01-01 \
    --TaskType 0 \
    --ProjectId 14324123 \
    --ExecutorGroupId 509e340a1cba617b679bd4b5001
```

Output: 
```
{
    "Response": {
        "TrendsData": [
            {
                "StatisticName": [
                    "a",
                    "b"
                ],
                "StatisticValue": [
                    2,
                    3
                ],
                "StatisticType": "FAILED"
            }
        ],
        "RequestId": "as1cs2c123asyi23bh213cc"
    }
}
```

