**Example 1: DescribeIntegrationStatisticsTaskStatusTrend**



Input: 

```
tccli wedata DescribeIntegrationStatisticsTaskStatusTrend --cli-unfold-argument  \
    --QueryDate 2022-01-01 \
    --TaskType 201 \
    --ProjectId 13213123 \
    --ExecutorGroupId 14342131
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

