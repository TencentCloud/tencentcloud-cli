**Example 1: demo**

demo

Input: 

```
tccli tsf DescribeInvocationMetricDataDimension --cli-unfold-argument  \
    --StartTime 2024-11-11 12:21:32 \
    --DimensionName applicationName \
    --Limit 0 \
    --SearchWord name \
    --Offset 0 \
    --EndTime 2024-11-11 12:26:32 \
    --MetricDimensionValues.0.Name key \
    --MetricDimensionValues.0.Value value1
```

Output: 
```
{
    "Response": {
        "Result": {
            "Content": [],
            "TotalCount": 0
        },
        "RequestId": "niw82o0-k298s7-akqo20-kx8305"
    }
}
```

