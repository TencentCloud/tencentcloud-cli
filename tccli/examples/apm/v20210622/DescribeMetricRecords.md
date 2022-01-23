**Example 1: 通用指标列表接口**



Input: 

```
tccli apm DescribeMetricRecords --cli-unfold-argument  \
    --Filters.0.Key span.kind \
    --Filters.0.Type = \
    --Filters.0.Value SPAN_KIND_SERVER \
    --Metrics.0.MetricName service_duration_avg \
    --Metrics.0.Compare 1 \
    --Metrics.1.MetricName request_count_sum \
    --GroupBy operation service.component \
    --Limit 10 \
    --Offset 1 \
    --StartTime 1618361193 \
    --EndTime 1618677137 \
    --OrderBy.Key service_duration_avg \
    --OrderBy.Value DESC
```

Output: 
```
{
    "Response": {
        "Records": [
            {
                "Tags": [
                    {
                        "Key": "operation",
                        "Value": "/DescribeAlarmList"
                    },
                    {
                        "Key": "service.component",
                        "Value": "HTTP"
                    }
                ],
                "Fields": [
                    {
                        "Key": "service_duration_avg",
                        "Value": 0.02383373177662466,
                        "CompareVal": -0.004148131882911392
                    },
                    {
                        "Key": "request_count_sum",
                        "Value": 31184,
                        "CompareVal": 0
                    }
                ]
            },
            {
                "Tags": [
                    {
                        "Key": "operation",
                        "Value": "/collector.CollectorService/PostSpans"
                    },
                    {
                        "Key": "service.component",
                        "Value": "gRPC"
                    }
                ],
                "Fields": [
                    {
                        "Key": "service_duration_avg",
                        "Value": 18.811467216411906,
                        "CompareVal": 0.17306355798699288
                    },
                    {
                        "Key": "request_count_sum",
                        "Value": 4986,
                        "CompareVal": 0
                    }
                ]
            },
            {
                "Tags": [
                    {
                        "Key": "operation",
                        "Value": "/notify.Notify/SendAlert"
                    },
                    {
                        "Key": "service.component",
                        "Value": "gRPC"
                    }
                ],
                "Fields": [
                    {
                        "Key": "service_duration_avg",
                        "Value": 9.486143798828124,
                        "CompareVal": 0.4454246545216073
                    },
                    {
                        "Key": "request_count_sum",
                        "Value": 4111,
                        "CompareVal": 0
                    }
                ]
            },
            {
                "Tags": [
                    {
                        "Key": "operation",
                        "Value": "HTTP GET"
                    },
                    {
                        "Key": "service.component",
                        "Value": "net/http"
                    }
                ],
                "Fields": [
                    {
                        "Key": "service_duration_avg",
                        "Value": 14.46367618133845,
                        "CompareVal": 1
                    },
                    {
                        "Key": "request_count_sum",
                        "Value": 8345,
                        "CompareVal": 0
                    }
                ]
            },
            {
                "Tags": [
                    {
                        "Key": "operation",
                        "Value": "HTTP POST"
                    },
                    {
                        "Key": "service.component",
                        "Value": "net/http"
                    }
                ],
                "Fields": [
                    {
                        "Key": "service_duration_avg",
                        "Value": 12.396896973135917,
                        "CompareVal": 0.1693196368191666
                    },
                    {
                        "Key": "request_count_sum",
                        "Value": 15094,
                        "CompareVal": 0
                    }
                ]
            },
            {
                "Tags": [
                    {
                        "Key": "operation",
                        "Value": "http_server_root"
                    },
                    {
                        "Key": "service.component",
                        "Value": "net/http"
                    }
                ],
                "Fields": [
                    {
                        "Key": "service_duration_avg",
                        "Value": 68.29158163921177,
                        "CompareVal": -0.05762747632987753
                    },
                    {
                        "Key": "request_count_sum",
                        "Value": 104642033,
                        "CompareVal": 0
                    }
                ]
            },
            {
                "Tags": [
                    {
                        "Key": "service.component",
                        "Value": "httpserverv3"
                    },
                    {
                        "Key": "operation",
                        "Value": "Ping"
                    }
                ],
                "Fields": [
                    {
                        "Key": "service_duration_avg",
                        "Value": 0.4196629148780232,
                        "CompareVal": 1
                    },
                    {
                        "Key": "request_count_sum",
                        "Value": 10182,
                        "CompareVal": 0
                    }
                ]
            },
            {
                "Tags": [
                    {
                        "Key": "operation",
                        "Value": "microServer_cdbwan"
                    },
                    {
                        "Key": "service.component",
                        "Value": "httpserverv3"
                    }
                ],
                "Fields": [
                    {
                        "Key": "service_duration_avg",
                        "Value": 3.6889778198423007,
                        "CompareVal": 0.15496546525321617
                    },
                    {
                        "Key": "request_count_sum",
                        "Value": 191205,
                        "CompareVal": 0
                    }
                ]
            }
        ],
        "RequestId": "fyy3-g7ujmxbouxshy3plmkmhlnmdbfh"
    }
}
```

**Example 2: 请求参数实例**



Input: 

```
tccli apm DescribeMetricRecords --cli-unfold-argument  \
    --OrderBy.Key service_duration_avg \
    --OrderBy.Value DESC \
    --Filters.0.Type  \
    --Filters.0.Key span.kind \
    --Filters.0.Value server \
    --InstanceId apm-6xYKFXYxo \
    --BusinessName taw \
    --Metrics.0.Compare 1 \
    --Metrics.0.Compares 1 \
    --Metrics.0.MetricName qps \
    --Limit 10 \
    --StartTime 1618361193 \
    --Offset 22 \
    --EndTime 1618677137 \
    --GroupBy operation
```

Output: 
```
{
    "Response": {
        "Records": [],
        "RequestId": "5809b2da-cfd8-499c-8897-7dfee822a8cb"
    }
}
```

