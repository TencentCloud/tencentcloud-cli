**Example 1: DescribeEdgeUnitApplications**



Input: 

```
tccli iecp DescribeEdgeUnitApplications --cli-unfold-argument  \
    --EdgeUnitId 1 \
    --Offset 0 \
    --Limit 10 \
    --Sort.0.Field StartTime \
    --Sort.0.Order DESC
```

Output: 
```
{
    "Response": {
        "RequestId": "5ebf13a2-f925-4ba7-adff-ddbc21d355e3",
        "TotalCount": 0,
        "ApplicationSet": []
    }
}
```

