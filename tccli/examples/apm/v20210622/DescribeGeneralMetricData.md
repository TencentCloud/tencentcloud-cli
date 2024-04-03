**Example 1: 查询1分钟聚合粒度的runtime_metric指标数据示例**

该示例查询实例为apm-ylTJfTSbn，按照service.name（服务名）为维度过滤，以service.name（服务名）进行聚合，查找开始时间-终止时间内以一分钟为聚合粒度的service_gc_full_count（Full GC）的指标数据。

Input: 

```
tccli apm DescribeGeneralMetricData --cli-unfold-argument  \
    --Filters.0.Key service.name \
    --Filters.0.Value tapm-api-ap-beijing \
    --ViewName runtime_metric \
    --InstanceId apm-ylTJfTSbn \
    --Period 60 \
    --Metrics service_gc_full_count \
    --StartTime 1652666416 \
    --EndTime 1652667616 \
    --GroupBy service.name
```

Output: 
```
{
    "Response": {
        "Records": [
            {
                "Tags": [
                    {
                        "Key": "service.name",
                        "Value": "java-order-service"
                    }
                ],
                "MetricName": "service_gc_full_count",
                "MetricNameCN": "full GC",
                "TimeSerial": [
                    1656428160,
                    1656428220,
                    1656428280,
                    1656428340,
                    1656428400,
                    1656428460,
                    1656428520,
                    1656428580,
                    1656428640,
                    1656428700,
                    1656428760,
                    1656428820,
                    1656428880
                ],
                "DataSerial": [
                    0.016666666666666666,
                    0,
                    0.016666666666666666,
                    0,
                    0.016666666666666666,
                    0.016666666666666666,
                    0,
                    0.016666666666666666,
                    0,
                    0.016666666666666666,
                    0.016666666666666666,
                    0,
                    0.016666666666666666
                ]
            }
        ],
        "RequestId": "test-test-test"
    }
}
```

**Example 2: 查询1分钟聚合粒度的service_metric指标数据示例**

该示例查询实例为apm-ylTJfTSbn，按照service.name（服务名）、span.kind（客户端/服务端视角）为维度过滤，以service.name（服务名）进行聚合，查找开始时间-终止时间内以一分钟为聚合粒度的service_request_count（总请求）、service_duration（平均响应时间）、service_error_req_rate（平均错误率）、service_slow_call_count（慢调用）、service_error_request_count（异常数量）的指标数据。

Input: 

```
tccli apm DescribeGeneralMetricData --cli-unfold-argument  \
    --Filters.0.Key service.name \
    --Filters.0.Value tapm-api-ap-beijing \
    --Filters.1.Key span.kind \
    --Filters.1.Value client \
    --ViewName service_metric \
    --InstanceId apm-ylTJfTSbn \
    --Period 60 \
    --Metrics service_request_count service_duration service_error_req_rate service_slow_call_count service_error_request_count \
    --StartTime 1652666416 \
    --EndTime 1652667616 \
    --GroupBy service.name span.kind
```

Output: 
```
{
    "Response": {
        "Records": [
            {
                "Tags": [
                    {
                        "Key": "service.name",
                        "Value": "java-order-service"
                    },
                    {
                        "Key": "span.kind",
                        "Value": "client"
                    }
                ],
                "MetricName": "service_request_count",
                "MetricNameCN": "总请求数",
                "TimeSerial": [
                    1656428160,
                    1656428220,
                    1656428280,
                    1656428340,
                    1656428400,
                    1656428460,
                    1656428520,
                    1656428580,
                    1656428640,
                    1656428700,
                    1656428760,
                    1656428820,
                    1656428880
                ],
                "DataSerial": [
                    10372,
                    10578,
                    10430,
                    10486,
                    10393,
                    10509,
                    10556,
                    10443,
                    10560,
                    10491,
                    10417,
                    10507,
                    10447
                ]
            },
            {
                "Tags": [
                    {
                        "Key": "service.name",
                        "Value": "java-order-service"
                    },
                    {
                        "Key": "span.kind",
                        "Value": "client"
                    }
                ],
                "MetricName": "service_duration",
                "MetricNameCN": "平均响应时间",
                "TimeSerial": [
                    1656428160,
                    1656428220,
                    1656428280,
                    1656428340,
                    1656428400,
                    1656428460,
                    1656428520,
                    1656428580,
                    1656428640,
                    1656428700,
                    1656428760,
                    1656428820,
                    1656428880
                ],
                "DataSerial": [
                    68.27933527571001,
                    75.1680976742024,
                    73.70498622754624,
                    74.37902912946632,
                    75.79610287066045,
                    77.2206395084234,
                    69.26122643544272,
                    69.63079755913704,
                    65.73752328654751,
                    76.56275573601707,
                    70.60296113316045,
                    71.30283125911086,
                    70.25328283510882
                ]
            },
            {
                "Tags": [
                    {
                        "Key": "service.name",
                        "Value": "java-order-service"
                    },
                    {
                        "Key": "span.kind",
                        "Value": "client"
                    }
                ],
                "MetricName": "service_error_req_rate",
                "MetricNameCN": "平均错误率",
                "TimeSerial": [
                    1656428160,
                    1656428220,
                    1656428280,
                    1656428340,
                    1656428400,
                    1656428460,
                    1656428520,
                    1656428580,
                    1656428640,
                    1656428700,
                    1656428760,
                    1656428820,
                    1656428880
                ],
                "DataSerial": [
                    1.3594292325491708,
                    1.0115333711476648,
                    1.2655800575263663,
                    1.077627312607286,
                    1.1738670258828057,
                    1.1704253497002568,
                    1.1841606669192877,
                    1.0916403332375753,
                    1.0700757575757576,
                    0.9246020398436755,
                    1.12316405875012,
                    1.1040258875035691,
                    1.206087872116397
                ]
            },
            {
                "Tags": [
                    {
                        "Key": "service.name",
                        "Value": "java-order-service"
                    },
                    {
                        "Key": "span.kind",
                        "Value": "client"
                    }
                ],
                "MetricName": "service_slow_call_count",
                "MetricNameCN": "慢调用",
                "TimeSerial": [
                    1656428160,
                    1656428220,
                    1656428280,
                    1656428340,
                    1656428400,
                    1656428460,
                    1656428520,
                    1656428580,
                    1656428640,
                    1656428700,
                    1656428760,
                    1656428820,
                    1656428880
                ],
                "DataSerial": [
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0
                ]
            },
            {
                "Tags": [
                    {
                        "Key": "service.name",
                        "Value": "java-order-service"
                    },
                    {
                        "Key": "span.kind",
                        "Value": "client"
                    }
                ],
                "MetricName": "service_error_request_count",
                "MetricNameCN": "错误数",
                "TimeSerial": [
                    1656428160,
                    1656428220,
                    1656428280,
                    1656428340,
                    1656428400,
                    1656428460,
                    1656428520,
                    1656428580,
                    1656428640,
                    1656428700,
                    1656428760,
                    1656428820,
                    1656428880
                ],
                "DataSerial": [
                    141,
                    107,
                    132,
                    113,
                    122,
                    123,
                    125,
                    114,
                    113,
                    97,
                    117,
                    116,
                    126
                ]
            }
        ],
        "RequestId": "test-test-test"
    }
}
```

**Example 3: 查询起始到终止时间内统计service_metric指标数据示例**

该示例查询实例为apm-ylTJfTSbn，按照service.name（服务名）、span.kind（客户端/服务端视角）为维度过滤，以service.name（服务名）进行聚合，查找开始时间-终止时间内的service_request_count（总请求）、service_duration（平均响应时间）、service_error_req_rate（平均错误率）、service_slow_call_count（慢调用）、service_error_request_count（异常数量）的指标数据。

Input: 

```
tccli apm DescribeGeneralMetricData --cli-unfold-argument  \
    --Filters.0.Key service.name \
    --Filters.0.Value tapm-api-ap-beijing \
    --Filters.1.Key span.kind \
    --Filters.1.Value client \
    --ViewName service_metric \
    --InstanceId apm-ylTJfTSbn \
    --Period 0 \
    --Metrics service_request_count service_duration service_error_req_rate service_slow_call_count service_error_request_count \
    --StartTime 1652666416 \
    --EndTime 1652667616 \
    --GroupBy service.name span.kind
```

Output: 
```
{
    "Response": {
        "Records": [
            {
                "Tags": [
                    {
                        "Key": "span.kind",
                        "Value": "client"
                    },
                    {
                        "Key": "service.name",
                        "Value": "java-order-service"
                    }
                ],
                "MetricName": "service_request_count",
                "MetricNameCN": "总请求数",
                "TimeSerial": null,
                "DataSerial": [
                    630381
                ]
            },
            {
                "Tags": [
                    {
                        "Key": "span.kind",
                        "Value": "client"
                    },
                    {
                        "Key": "service.name",
                        "Value": "java-order-service"
                    }
                ],
                "MetricName": "service_duration",
                "MetricNameCN": "平均响应时间",
                "TimeSerial": null,
                "DataSerial": [
                    72.44506470564654
                ]
            },
            {
                "Tags": [
                    {
                        "Key": "span.kind",
                        "Value": "client"
                    },
                    {
                        "Key": "service.name",
                        "Value": "java-order-service"
                    }
                ],
                "MetricName": "service_error_req_rate",
                "MetricNameCN": "平均错误率",
                "TimeSerial": null,
                "DataSerial": [
                    1.1464495281425042
                ]
            },
            {
                "Tags": [
                    {
                        "Key": "span.kind",
                        "Value": "client"
                    },
                    {
                        "Key": "service.name",
                        "Value": "java-order-service"
                    }
                ],
                "MetricName": "service_slow_call_count",
                "MetricNameCN": "慢调用",
                "TimeSerial": null,
                "DataSerial": [
                    0
                ]
            },
            {
                "Tags": [
                    {
                        "Key": "span.kind",
                        "Value": "client"
                    },
                    {
                        "Key": "service.name",
                        "Value": "java-order-service"
                    }
                ],
                "MetricName": "service_error_request_count",
                "MetricNameCN": "错误数",
                "TimeSerial": null,
                "DataSerial": [
                    7227
                ]
            }
        ],
        "RequestId": "test-test-test"
    }
}
```

**Example 4: 查询1分钟聚合粒度的sql_metric的service_slow_sql_count（慢调用sql）指标数据示例**

该示例查询实例为apm-ylTJfTSbn，按照service.name（服务名）为维度过滤，以service.name（服务名）进行聚合，查找开始时间-终止时间内以一分钟为聚合粒度的service_slow_sql_count（慢sql）的指标数据。

Input: 

```
tccli apm DescribeGeneralMetricData --cli-unfold-argument  \
    --Filters.0.Key service.name \
    --Filters.0.Value tapm-api-ap-beijing \
    --ViewName sql_metric \
    --InstanceId apm-ylTJfTSbn \
    --Period 60 \
    --Metrics service_slow_sql_count \
    --StartTime 1652666416 \
    --EndTime 1652667616 \
    --GroupBy service.name
```

Output: 
```
{
    "Response": {
        "Records": [
            {
                "Tags": [
                    {
                        "Key": "service.name",
                        "Value": "java-order-service"
                    }
                ],
                "MetricName": "service_slow_sql_count",
                "MetricNameCN": "",
                "TimeSerial": [
                    1656428160,
                    1656428220,
                    1656428280,
                    1656428340,
                    1656428400,
                    1656428460,
                    1656428520,
                    1656428580,
                    1656428640,
                    1656428700,
                    1656428760,
                    1656428820,
                    1656428880
                ],
                "DataSerial": [
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0
                ]
            }
        ],
        "RequestId": "test-test-test"
    }
}
```

**Example 5: 查询起始到终止时间内统计sql_metric的sql_duration_avg（耗时时间）指标数据示例**

该示例查询实例为apm-ylTJfTSbn，按照db.instance（数据库名称）、（db.ip）数据库实例ip为维度过滤，以service.name（服务名）、db.statement（sql语句）为维度进行聚合，查找开始时间-终止时间内top5的sql_duration_avg（耗时（ms））的指标数据。

Input: 

```
tccli apm DescribeGeneralMetricData --cli-unfold-argument  \
    --Filters.0.Key db.instance \
    --Filters.0.Value mock_project_db \
    --Filters.1.Key db.ip \
    --Filters.1.Value 9.147.18.42 \
    --ViewName sql_metric \
    --InstanceId apm-ylTJfTSbn \
    --Metrics sql_duration_avg \
    --StartTime 1652666416 \
    --EndTime 1652667616 \
    --GroupBy service.name db.statement \
    --OrderBy.Key sql_duration_avg \
    --OrderBy.Value desc \
    --PageSize 5
```

Output: 
```
{
    "Response": {
        "Records": [
            {
                "Tags": [
                    {
                        "Key": "db.statement",
                        "Value": "select * om un_exist_table limit 1"
                    },
                    {
                        "Key": "service.name",
                        "Value": "java-order-service"
                    }
                ],
                "MetricName": "sql_duration_avg",
                "MetricNameCN": "平均响应时间",
                "TimeSerial": null,
                "DataSerial": [
                    29.883333333333333
                ]
            },
            {
                "Tags": [
                    {
                        "Key": "db.statement",
                        "Value": "select * om un_exist_table limit 1"
                    },
                    {
                        "Key": "service.name",
                        "Value": "java-user-service"
                    }
                ],
                "MetricName": "sql_duration_avg",
                "MetricNameCN": "平均响应时间",
                "TimeSerial": null,
                "DataSerial": [
                    26.170082239670673
                ]
            },
            {
                "Tags": [
                    {
                        "Key": "db.statement",
                        "Value": "select * from un_exist_table limit 1"
                    },
                    {
                        "Key": "service.name",
                        "Value": "java-market-service"
                    }
                ],
                "MetricName": "sql_duration_avg",
                "MetricNameCN": "平均响应时间",
                "TimeSerial": null,
                "DataSerial": [
                    25.654237574773983
                ]
            },
            {
                "Tags": [
                    {
                        "Key": "db.statement",
                        "Value": "select * from mock_project_userinfo where id = ? limit 1"
                    },
                    {
                        "Key": "service.name",
                        "Value": "java-order-service"
                    }
                ],
                "MetricName": "sql_duration_avg",
                "MetricNameCN": "平均响应时间",
                "TimeSerial": null,
                "DataSerial": [
                    24.333649579223025
                ]
            },
            {
                "Tags": [
                    {
                        "Key": "db.statement",
                        "Value": "select * from un_exist_table limit 1"
                    },
                    {
                        "Key": "service.name",
                        "Value": "java-user-service"
                    }
                ],
                "MetricName": "sql_duration_avg",
                "MetricNameCN": "平均响应时间",
                "TimeSerial": null,
                "DataSerial": [
                    22.785741520925463
                ]
            }
        ],
        "RequestId": "test-test-test"
    }
}
```

