**Example 1: DescribeMetricOverviewList**



Input: 

```
tccli adp DescribeMetricOverviewList --cli-unfold-argument  \
    --ResourceType 1 \
    --TimeRange.EndTime 1786463999 \
    --TimeRange.StartTime 1786377600 \
    --ViewScope.ViewType 2 \
    --ViewScope.ScopeId default_space
```

Output: 
```
{
    "Response": {
        "MetricList": [
            {
                "Key": "total_calls",
                "Mom": 0.15,
                "Unit": 2,
                "Value": 12580
            }
        ],
        "TotalCount": "12",
        "RequestId": "72c3b5b9-9c94-4fb3-9073-498bc50d0981"
    }
}
```

