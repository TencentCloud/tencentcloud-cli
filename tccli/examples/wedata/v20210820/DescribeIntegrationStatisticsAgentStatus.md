**Example 1: DescribeIntegrationStatisticsAgentStatus**



Input: 

```
tccli wedata DescribeIntegrationStatisticsAgentStatus --cli-unfold-argument  \
    --QueryDate abc \
    --TaskType 0 \
    --ProjectId abc \
    --ExecutorGroupId abc
```

Output: 
```
{
    "Response": {
        "StatusData": "abc",
        "RequestId": "abc"
    }
}
```

