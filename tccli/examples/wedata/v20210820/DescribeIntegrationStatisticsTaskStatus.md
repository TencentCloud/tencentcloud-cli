**Example 1: DescribeIntegrationStatisticsTaskStatus**



Input: 

```
tccli wedata DescribeIntegrationStatisticsTaskStatus --cli-unfold-argument  \
    --QueryDate abc \
    --TaskType 0 \
    --ProjectId abc \
    --ExecutorGroupId abc
```

Output: 
```
{
    "Response": {
        "StatusData": "{\"running\":0}",
        "RequestId": "abc"
    }
}
```

