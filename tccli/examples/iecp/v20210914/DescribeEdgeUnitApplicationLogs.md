**Example 1: DescribeEdgeUnitApplicationLogs**



Input: 

```
tccli iecp DescribeEdgeUnitApplicationLogs --cli-unfold-argument  \
    --ApplicationId 1 \
    --EdgeUnitId 1 \
    --Limit 10 \
    --PodName Pod
```

Output: 
```
{
    "Response": {
        "RequestId": "5ebf13a2-f925-4ba7-adff-ddbc21d355e3",
        "LogSet": []
    }
}
```

