**Example 1: 通用指标列表接口**

场景2

Input: 

```
tccli apm DescribeMetricRecords --cli-unfold-argument  \
    --Filters.0.Key span.kind \
    --Filters.0.Type in \
    --Filters.0.Value server,consumer \
    --Metrics.0.MetricName duration_avg \
    --Metrics.0.Compares CompareByYesterday CompareByLastWeek \
    --GroupBy service.instance \
    --Limit 10 \
    --Offset 1 \
    --StartTime 1618361193 \
    --EndTime 1618677137 \
    --OrderBy.Key duration_avg \
    --OrderBy.Value DESC
```

Output: 
```
{
    "Response": {
        "Records": [
            {
                "Fields": [
                    {
                        "LastPeriodValue": [
                            {
                                "Key": "abc",
                                "Value": 0
                            }
                        ],
                        "CompareVal": "abc",
                        "Unit": "s",
                        "Value": 691.42,
                        "Key": "ab",
                        "CompareVals": [
                            {
                                "Value": "v1",
                                "Key": "k1"
                            },
                            {
                                "Key": "k2",
                                "Value": "v2"
                            }
                        ]
                    }
                ],
                "Tags": [
                    {
                        "Value": "v1",
                        "Key": "k1"
                    }
                ]
            }
        ],
        "RequestId": "re",
        "TotalCount": 0
    }
}
```

**Example 2: 请求参数实例**

场景一

Input: 

```
tccli apm DescribeMetricRecords --cli-unfold-argument  \
    --OrderBy.Key service_duration_avg \
    --OrderBy.Value DESC \
    --Filters.0.Type = \
    --Filters.0.Key span.kind \
    --Filters.0.Value server \
    --InstanceId apm-6xYKFXYxo \
    --BusinessName taw \
    --Metrics.0.Compare 1 \
    --Metrics.0.Compares CompareByYesterday CompareByLastWeek \
    --Metrics.0.MetricName qps \
    --Limit 10 \
    --StartTime 1618361193 \
    --Offset 22 \
    --EndTime 1618677137 \
    --PageIndex 1 \
    --PageSize 10 \
    --GroupBy service.instance
```

Output: 
```
{
    "Response": {
        "Records": [
            {
                "Fields": [
                    {
                        "CompareVal": "abc",
                        "CompareVals": [
                            {
                                "Key": "abc",
                                "Value": "abc"
                            }
                        ],
                        "Value": 0,
                        "Unit": "abc",
                        "Key": "abc",
                        "LastPeriodValue": [
                            {
                                "Key": "abc",
                                "Value": 0
                            }
                        ]
                    }
                ],
                "Tags": [
                    {
                        "Key": "abc",
                        "Value": "abc"
                    }
                ]
            }
        ],
        "TotalCount": 0,
        "RequestId": "abc"
    }
}
```

