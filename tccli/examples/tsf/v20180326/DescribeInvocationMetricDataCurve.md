**Example 1: DescribeInvocationMetricDataCurve**



Input: 

```
tccli tsf DescribeInvocationMetricDataCurve --cli-unfold-argument  \
    --StartTime '2020-06-03 17:11:49' \
    --EndTime '2020-06-03 17:21:49' \
    --MetricDimensions.0.Name NamespaceId \
    --MetricDimensions.0.Value namespace-6a79x94v \
    --Metrics.0.Name request_count \
    --Metrics.0.Function sum
```

Output: 
```
{
    "Response": {
        "Result": [
            {
                "MetricName": "cpu",
                "MetricFunction": "findOne",
                "MetricDataPoints": [
                    {
                        "Key": "time",
                        "Value": "60",
                        "Tag": "time"
                    }
                ]
            }
        ],
        "RequestId": "f1183607-d21b-dde1-d99c-94643d32c62e"
    }
}
```

