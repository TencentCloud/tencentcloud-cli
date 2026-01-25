**Example 1: 获取接口分析列表明细数据**

场景描述：查看某个具体服务在一段时间内的流量趋势、耗时变化趋势。通常用于前端绘制折线图。
关键配置：
* ViewName: 查询 service_metric（基础性能指标）视图。
* Metrics: 返回 request_count（请求量）数据。
* Filters: 指定span.kind（调用角色）、service.name（应用名称）、operation（接口）查询条件。
* GroupBy: 未指定，代表不需要按照特定的维度进行聚合。
* Period: 设置为 1，表示按时间切片聚合。
请求参数示例：查询应用 apm-test 下特定接口POST /mall/test在指定时间段内的每分钟请求数趋势。

Input: 

```
tccli apm DescribeGeneralMetricData --cli-unfold-argument  \
    --InstanceId apm-instanceKey \
    --ViewName service_metric \
    --Metrics request_count \
    --Filters.0.Key span.kind \
    --Filters.0.Value server \
    --Filters.1.Key service.name \
    --Filters.1.Value apm-test \
    --Filters.2.Key operation \
    --Filters.2.Value POST /mall/test \
    --StartTime 1768377000 \
    --EndTime 1768377900 \
    --Period 1
```

Output: 
```
{
    "Response": {
        "Records": [
            {
                "MetricName": "service_request_count_sum",
                "MetricNameCN": "总请求数",
                "Tags": [
                    {
                        "Key": "service.name",
                        "Value": "apm-test"
                    }
                ],
                "TimeSerial": [
                    1768377000,
                    1768377060,
                    1768377120
                ],
                "DataSerial": [
                    1,
                    null,
                    1
                ]
            }
        ],
        "RequestId": "4d62d7d5-e4b7-491b-874e-3563968f1626"
    }
}
```

**Example 2: 获取接口分析列表数据**

场景描述：查看一段时间内，各个接口的请求总量，或者查看平均响应时间、p99、最大响应时间、错误率等指标。
关键配置：
* ViewName: 查询 service_metric（基础性能指标）视图。
* Metrics: 返回 request_count（请求量）数据。
* Filters: 指定span.kind（调用角色）、service.name（应用名称）查询条件。
* GroupBy: 按 operation（接口名）聚合。
* Period: 设置为 0，表示不按时间切片，计算整个时间范围内的汇总值。
请求参数示例：查询服务 apm-test 下所有接口在指定时间段内的请求总数，并按接口名分组展示。

Input: 

```
tccli apm DescribeGeneralMetricData --cli-unfold-argument  \
    --InstanceId apm-instanceKey \
    --ViewName service_metric \
    --Metrics request_count \
    --Filters.0.Key span.kind \
    --Filters.0.Value server \
    --Filters.1.Key service.name \
    --Filters.1.Value apm-test \
    --GroupBy operation \
    --StartTime 1768377000 \
    --EndTime 1768377900 \
    --Period 0
```

Output: 
```
{
    "Response": {
        "Records": [
            {
                "MetricName": "service_request_count_sum",
                "MetricNameCN": "总请求数",
                "Tags": [
                    {
                        "Key": "operation",
                        "Value": "GET /mall/test"
                    }
                ],
                "TimeSerial": [],
                "DataSerial": [
                    18
                ]
            }
        ],
        "RequestId": "bfcc1a20-b6ff-455b-8fab-1d9883f4f629"
    }
}
```

