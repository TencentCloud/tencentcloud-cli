**Example 1: DescribeInvocationMetricDataCurve**



Input: 

```
tccli tsf DescribeInvocationMetricScatterPlot --cli-unfold-argument  \
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
        "Result": {
            "EndTime": 0,
            "StartTime": 0,
            "Period": 0,
            "DataPoints": [
                {
                    "Points": [
                        {
                            "Values": [
                                0
                            ]
                        }
                    ],
                    "MetricName": "namespaceId",
                    "PointKeys": [
                        "time"
                    ]
                }
            ]
        },
        "RequestId": "96561cf1-738a-47d6-943b-dec7ebbccabe"
    }
}
```

