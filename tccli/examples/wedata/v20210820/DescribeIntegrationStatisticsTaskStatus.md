**Example 1: DescribeIntegrationStatisticsTaskStatus**



Input: 

```
tccli wedata DescribeIntegrationStatisticsTaskStatus --cli-unfold-argument  \
    --QueryDate 2022-01-01 \
    --TaskType 201 \
    --ProjectId 11022568003970304 \
    --ExecutorGroupId 14323212
```

Output: 
```
{
    "Response": {
        "StatusData": "{\"running\":0}",
        "RequestId": "as1cs2c123asyi23bh213cc"
    }
}
```

