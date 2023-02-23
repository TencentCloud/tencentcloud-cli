**Example 1: demo**

demo

Input: 

```
tccli tsf DescribeInvocationMetricDataDimension --cli-unfold-argument  \
    --StartTime xx \
    --DimensionName xx \
    --Limit 0 \
    --SearchWord xx \
    --Offset 0 \
    --EndTime xx \
    --MetricDimensionValues.0.Name xx \
    --MetricDimensionValues.0.Value xx
```

Output: 
```
{
    "Response": {
        "Result": {
            "Content": [
                "xx"
            ],
            "TotalCount": 0
        },
        "RequestId": "xx"
    }
}
```

