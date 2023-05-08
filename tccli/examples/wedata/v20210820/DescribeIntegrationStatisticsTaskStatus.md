**Example 1: DescribeIntegrationStatisticsTaskStatus**



Input: 

```
tccli wedata DescribeIntegrationStatisticsTaskStatus --cli-unfold-argument  \
    --QueryDate 2022-01-01 \
    --TaskType 201 \
    --ProjectId 1 \
    --ExecutorGroupId 1
```

Output: 
```
{
    "Response": {
        "StatusData": "{\"running\":0}",
        "RequestId": "xx"
    }
}
```

