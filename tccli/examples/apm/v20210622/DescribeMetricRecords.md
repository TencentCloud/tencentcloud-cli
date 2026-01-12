**Example 1: 查询每个服务实例的平均响应时间**



Input: 

```
tccli apm DescribeMetricRecords --cli-unfold-argument  \
    --InstanceId apm-eDyXPD6FF \
    --Metrics.0.MetricName duration_avg \
    --Metrics.0.Compares CompareByYesterday \
    --StartTime 1768200720 \
    --EndTime 1768201620 \
    --GroupBy service.instance \
    --Filters.0.Type in \
    --Filters.0.Key span.kind \
    --Filters.0.Value server,consumer
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
                                "Value": "1.1%"
                            }
                        ],
                        "Key": "duration_avg",
                        "LastPeriodValue": [
                            {
                                "Key": "CompareByYesterday",
                                "Value": 837.1754975463576
                            }
                        ],
                        "NameCN": "平均响应时间",
                        "NameEN": "Average Response Time",
                        "Unit": "ms",
                        "Value": 846.6
                    }
                ],
                "Tags": [
                    {
                        "Key": "service.instance",
                        "Value": "10.244.3.220"
                    },
                    {
                        "Key": "color",
                        "Value": "green"
                    }
                ]
            },
            {
                "Fields": [
                    {
                        "CompareVal": "",
                        "CompareVals": [
                            {
                                "Key": "CompareByYesterday",
                                "Value": "-12.0%"
                            }
                        ],
                        "Key": "duration_avg",
                        "LastPeriodValue": [
                            {
                                "Key": "CompareByYesterday",
                                "Value": 321.9870221880734
                            }
                        ],
                        "NameCN": "平均响应时间",
                        "NameEN": "Average Response Time",
                        "Unit": "ms",
                        "Value": 283.3
                    }
                ],
                "Tags": [
                    {
                        "Key": "service.instance",
                        "Value": "10.244.3.226"
                    },
                    {
                        "Key": "color",
                        "Value": "green"
                    }
                ]
            },
            {
                "Fields": [
                    {
                        "CompareVal": "",
                        "CompareVals": [
                            {
                                "Key": "CompareByYesterday",
                                "Value": "100%"
                            }
                        ],
                        "Key": "duration_avg",
                        "LastPeriodValue": [
                            {
                                "Key": "CompareByYesterday",
                                "Value": 0
                            }
                        ],
                        "NameCN": "平均响应时间",
                        "NameEN": "Average Response Time",
                        "Unit": "ms",
                        "Value": 1608.8
                    }
                ],
                "Tags": [
                    {
                        "Key": "service.instance",
                        "Value": ""
                    },
                    {
                        "Key": "color",
                        "Value": "green"
                    }
                ]
            }
        ],
        "RequestId": "8d1d6400-8852-498b-aeca-de9fb14774da",
        "TotalCount": 3
    }
}
```

**Example 2: 查询特定应用每个接口的错误请求数**



Input: 

```
tccli apm DescribeMetricRecords --cli-unfold-argument  \
    --InstanceId apm-eDyXPD6FF \
    --Metrics.0.MetricName err_error_request_count \
    --Metrics.0.Compares CompareByYesterday \
    --StartTime 1768183020 \
    --EndTime 1768183920 \
    --GroupBy operation \
    --Filters.0.Type = \
    --Filters.0.Key service.name \
    --Filters.0.Value java-gateway-service \
    --OrderBy.Key err_error_request_count \
    --OrderBy.Value desc \
    --Limit 10 \
    --Offset 0
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
                                "Value": "0"
                            }
                        ],
                        "Key": "err_error_request_count",
                        "LastPeriodValue": [
                            {
                                "Key": "CompareByYesterday",
                                "Value": 15
                            }
                        ],
                        "NameCN": "错误数",
                        "NameEN": "Error Count",
                        "Unit": "个",
                        "Value": 15
                    }
                ],
                "Tags": [
                    {
                        "Key": "operation",
                        "Value": "GET mock-security-service-route"
                    }
                ]
            },
            {
                "Fields": [
                    {
                        "CompareVal": "",
                        "CompareVals": [
                            {
                                "Key": "CompareByYesterday",
                                "Value": "0"
                            }
                        ],
                        "Key": "err_error_request_count",
                        "LastPeriodValue": [
                            {
                                "Key": "CompareByYesterday",
                                "Value": 15
                            }
                        ],
                        "NameCN": "错误数",
                        "NameEN": "Error Count",
                        "Unit": "个",
                        "Value": 15
                    }
                ],
                "Tags": [
                    {
                        "Key": "operation",
                        "Value": "FilteringWebHandler.handle"
                    }
                ]
            }
        ],
        "RequestId": "05301a08-7c8b-41cd-889b-a6386238e82b",
        "TotalCount": 2
    }
}
```

