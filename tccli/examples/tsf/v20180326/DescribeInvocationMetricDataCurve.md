**Example 1: DescribeInvocationMetricDataCurve**



Input: 

```
tccli tsf DescribeInvocationMetricDataCurve --cli-unfold-argument  \
    --StartTime '2020-06-03 17:11:49' \
    --EndTime '2020-06-03 17:21:49' \
    --MetricDimensions.0.Name NamespaceId \
    --MetricDimensions.0.Value test \
    --Metrics.0.Name request_count \
    --Metrics.0.Function sum
```

Output: 
```
{
    "Response": {
        "RequestId": "868d5e4f-0839-49a1-927e-5d275edc7bbe",
        "Result": [
            {
                "MetricName": "request_count",
                "MetricFunction": "sum",
                "MetricDataPoints": [
                    {}
                ]
            }
        ]
    }
}
```

