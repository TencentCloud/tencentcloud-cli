**Example 1: 请求参数示例**

场景1

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
                        "CompareVal": "",
                        "CompareVals": [
                            {
                                "Key": "CompareByYesterday",
                                "Value": "1%"
                            }
                        ],
                        "Value": 0,
                        "Unit": "",
                        "Key": "service_duration_avg",
                        "LastPeriodValue": [
                            {
                                "Key": "CompareByYesterday",
                                "Value": 71308388
                            }
                        ]
                    }
                ],
                "Tags": [
                    {
                        "Key": "service.name",
                        "Value": "java-order-demo"
                    }
                ]
            }
        ],
        "TotalCount": 0,
        "RequestId": "test-test-test"
    }
}
```

**Example 2: 通用指标列表接口**

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
    --InstanceId apm-CVfliqa8U \
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
                                "Key": "CompareByYesterday",
                                "Value": 71308388
                            }
                        ],
                        "CompareVal": "CompareByYesterday",
                        "Unit": "s",
                        "Value": 691.42,
                        "Key": "duration_avg",
                        "CompareVals": [
                            {
                                "Value": "CompareByYesterday",
                                "Key": "2%"
                            },
                            {
                                "Key": "CompareByLastWeek",
                                "Value": "-1%"
                            }
                        ]
                    }
                ],
                "Tags": [
                    {
                        "Value": "service.name",
                        "Key": "java-order-demo"
                    }
                ]
            }
        ],
        "RequestId": "test-test-test",
        "TotalCount": 0
    }
}
```

