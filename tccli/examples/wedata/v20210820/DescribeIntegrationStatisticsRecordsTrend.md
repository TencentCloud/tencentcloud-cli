**Example 1: DescribeIntegrationStatisticsRecordsTrend**



Input: 

```
tccli wedata DescribeIntegrationStatisticsRecordsTrend --cli-unfold-argument  \
    --QueryDate 2022-01-01 \
    --TaskType 201 \
    --ProjectId 1
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
                "StatisticType": "typeA"
            }
        ],
        "RequestId": "as1cs2c123asyi23bh213cc"
    }
}
```

