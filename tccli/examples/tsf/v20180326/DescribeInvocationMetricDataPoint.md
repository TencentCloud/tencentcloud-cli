**Example 1: demo**



Input: 

```
tccli tsf DescribeInvocationMetricDataPoint --cli-unfold-argument  \
    --Metrics.0.Function xx \
    --Metrics.0.Name xx \
    --EndTime xx \
    --StartTime xx \
    --MetricDimensionValues.0.Name xx \
    --MetricDimensionValues.0.Value xx
```

Output: 
```
{
    "Response": {
        "Result": [
            {
                "MetricDataValue": "xx",
                "MetricFunction": "xx",
                "MetricName": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

