**Example 1: DescribeInvocationMetricDataCurve**



Input: 

```
tccli tsf DescribeInvocationMetricScatterPlot --cli-unfold-argument  \
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
        "Result": {
            "EndTime": 0,
            "Period": 0,
            "StartTime": 0,
            "DataPoints": [
                {
                    "PointKeys": [
                        "xx"
                    ],
                    "Points": [
                        {
                            "Values": [
                                0.0
                            ]
                        }
                    ],
                    "MetricName": "xx"
                }
            ]
        },
        "RequestId": "xx"
    }
}
```

