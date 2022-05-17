**Example 1: 查询起始到终止时间内统计指标数据示例**

该示例查询实例为apm-ylTJfTSbn，按照service.name（服务名）、span.kind（客户端/服务端视角）为维度过滤，以service.name（服务名）进行聚合，查找开始时间-终止时间内的service_request_count（总请求）、service_duration（平均响应时间）的指标数据。

Input: 

```
tccli apm DescribeGeneralMetricData --cli-unfold-argument  \
    --Filters.0.Key service.name \
    --Filters.0.Value tapm-api-ap-beijing \
    --ViewName service_metric \
    --InstanceId apm-iIPwOX7Ln \
    --Period 0 \
    --Metrics service_request_count \
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
                "MetricName": "service_request_count",
                "MetricNameCN": "总请求数",
                "TimeSerial": null,
                "DataSerial": [
                    1193137
                ]
            },
            {
                "Tags": [
                    {
                        "Key": "service.name",
                        "Value": "java-order-service"
                    }
                ],
                "MetricName": "service_duration",
                "MetricNameCN": "平均响应时间",
                "TimeSerial": null,
                "DataSerial": [
                    58.888715069029146
                ]
            }
        ],
        "RequestId": "test-test-test"
    }
}
```

**Example 2: 查询1分钟聚合粒度的指标数据示例**

该示例查询实例为apm-ylTJfTSbn，按照service.name（服务名）、span.kind（客户端/服务端视角）为维度过滤，以service.name（服务名）进行聚合，查找开始时间-终止时间内以一分钟为聚合粒度的service_request_count（总请求）、service_duration（平均响应时间）的指标数据。

Input: 

```
tccli apm DescribeGeneralMetricData --cli-unfold-argument  \
    --Filters.0.Key service.name \
    --Filters.0.Value tapm-api-ap-beijing \
    --ViewName service_metric \
    --InstanceId apm-iIPwOX7Ln \
    --Period 60 \
    --Metrics service_request_count \
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
                "MetricName": "service_request_count",
                "MetricNameCN": "总请求数",
                "TimeSerial": null,
                "DataSerial": [
                    1193137
                ]
            },
            {
                "Tags": [
                    {
                        "Key": "service.name",
                        "Value": "java-order-service"
                    }
                ],
                "MetricName": "service_duration",
                "MetricNameCN": "平均响应时间",
                "TimeSerial": null,
                "DataSerial": [
                    58.888715069029146
                ]
            }
        ],
        "RequestId": "test-test-test"
    }
}
```

