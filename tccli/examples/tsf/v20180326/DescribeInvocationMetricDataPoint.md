**Example 1: demo**



Input: 

```
tccli tsf DescribeInvocationMetricDataPoint --cli-unfold-argument  \
    --StartTime 2019-11-23 09:22:33 \
    --EndTime 2019-11-23 09:24:33 \
    --MetricDimensionValues.0.Name namespace \
    --MetricDimensionValues.0.Value namespace-6a79x94v \
    --Metrics.0.Name name-mock \
    --Metrics.0.Function func-mock \
    --Kind SERVER
```

Output: 
```
{
    "Response": {
        "Result": [
            {
                "MetricName": "name-mock",
                "MetricFunction": "func-mock",
                "MetricDataValue": "namespace-6a79x94v",
                "DailyPercent": 0
            }
        ],
        "RequestId": "96561cf1-738a-47d6-943b-dec7ebbccabe"
    }
}
```

