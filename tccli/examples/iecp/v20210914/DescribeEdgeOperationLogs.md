**Example 1: DescribeEdgeOperationLogs**



Input: 

```
tccli iecp DescribeEdgeOperationLogs --cli-unfold-argument  \
    --BeginTime 2021-01-01 00:00:00 \
    --EndTime 2021-01-02 00:00:00 \
    --Offset 0 \
    --Limit 10 \
    --Sort.0.Field OPERATETIME \
    --Sort.0.Order DESC
```

Output: 
```
{
    "Response": {
        "RequestId": "5ebf13a2-f925-4ba7-adff-ddbc21d355e3",
        "TotalCount": 0,
        "OperationLogSet": []
    }
}
```

