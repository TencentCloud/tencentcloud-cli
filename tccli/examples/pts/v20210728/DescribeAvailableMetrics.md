**Example 1: 查询系统支持的指标**



Input: 

```
tccli pts DescribeAvailableMetrics --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "MetricSet": [
            {
                "Alias": "RequestsCount",
                "Description": "请求数量",
                "Metric": "pts_engine_req_total",
                "MetricType": "counter",
                "Unit": "reqs",
                "Aggregations": [
                    {
                        "Aggregation": "Rate",
                        "Legend": "请求RPS"
                    },
                    {
                        "Aggregation": "Count",
                        "Legend": "请求总数"
                    },
                    {
                        "Aggregation": "ErrorPercentage",
                        "Legend": "请求失败率"
                    }
                ],
                "InnerMetric": false
            },
            {
                "Alias": "RequestDuration",
                "Description": "请求响应时间",
                "Metric": "pts_engine_req_duration_seconds",
                "MetricType": "histogram",
                "Unit": "s",
                "Aggregations": [
                    {
                        "Aggregation": "Percentiles",
                        "Legend": "响应时间Percentiles"
                    },
                    {
                        "Aggregation": "Timings",
                        "Legend": "各阶段平均耗时分布"
                    },
                    {
                        "Aggregation": "Avg",
                        "Legend": "平均响应时间"
                    },
                    {
                        "Aggregation": "P50",
                        "Legend": "响应时间P50"
                    },
                    {
                        "Aggregation": "P90",
                        "Legend": "响应时间P90"
                    },
                    {
                        "Aggregation": "P95",
                        "Legend": "响应时间P95"
                    }
                ],
                "InnerMetric": false
            },
            {
                "Alias": "ChecksCount",
                "Description": "检查点数量",
                "Metric": "pts_engine_checks_total",
                "MetricType": "counter",
                "Unit": "checks",
                "Aggregations": [
                    {
                        "Aggregation": "Rate",
                        "Legend": "检查点RPS"
                    },
                    {
                        "Aggregation": "Count",
                        "Legend": "检查点总数"
                    }
                ],
                "InnerMetric": false
            },
            {
                "Alias": "NumberVirtualUsers",
                "Description": "并发用户数",
                "Metric": "pts_engine_num_vus",
                "MetricType": "gauge",
                "Unit": "s",
                "Aggregations": [
                    {
                        "Aggregation": "Gauge",
                        "Legend": "并发数"
                    }
                ],
                "InnerMetric": false
            },
            {
                "Alias": "SendBytesCount",
                "Description": "发送字节数",
                "Metric": "pts_engine_send_bytes_total",
                "MetricType": "counter",
                "Unit": "bytes",
                "Aggregations": [
                    {
                        "Aggregation": "Rate",
                        "Legend": "发送速率"
                    },
                    {
                        "Aggregation": "Count",
                        "Legend": "发送总数"
                    }
                ],
                "InnerMetric": false
            },
            {
                "Alias": "ReceiveBytesCount",
                "Description": "接收字节数",
                "Metric": "pts_engine_receive_bytes_total",
                "MetricType": "counter",
                "Unit": "bytes",
                "Aggregations": [
                    {
                        "Aggregation": "Rate",
                        "Legend": "接收速率"
                    },
                    {
                        "Aggregation": "Count",
                        "Legend": "接收总数"
                    }
                ],
                "InnerMetric": false
            },
            {
                "Alias": "IterationsCount",
                "Description": "场景迭代数",
                "Metric": "pts_engine_iterations_total",
                "MetricType": "counter",
                "Unit": "iters",
                "Aggregations": [
                    {
                        "Aggregation": "Rate",
                        "Legend": "场景执行TPS"
                    },
                    {
                        "Aggregation": "Count",
                        "Legend": "场景执行总数"
                    }
                ],
                "InnerMetric": false
            },
            {
                "Alias": "IterationDuration",
                "Description": "场景执行耗时",
                "Metric": "pts_engine_iterations_duration_seconds",
                "MetricType": "histogram",
                "Unit": "s",
                "Aggregations": [
                    {
                        "Aggregation": "Percentiles",
                        "Legend": "场景执行Percentiles"
                    },
                    {
                        "Aggregation": "Avg",
                        "Legend": "场景执行平均耗时"
                    },
                    {
                        "Aggregation": "P50",
                        "Legend": "场景执行P50"
                    },
                    {
                        "Aggregation": "P90",
                        "Legend": "场景执行P90"
                    },
                    {
                        "Aggregation": "P95",
                        "Legend": "场景执行P95"
                    }
                ],
                "InnerMetric": false
            },
            {
                "Alias": "RequestSendingDuration",
                "Description": "发送请求阶段耗时",
                "Metric": "pts_engine_req_send_duration_seconds",
                "MetricType": "histogram",
                "Unit": "s",
                "Aggregations": [
                    {
                        "Aggregation": "Percentiles",
                        "Legend": "发送耗时Percentiles"
                    },
                    {
                        "Aggregation": "Avg",
                        "Legend": "发送请求平均耗时"
                    },
                    {
                        "Aggregation": "P50",
                        "Legend": "发送耗时P50"
                    },
                    {
                        "Aggregation": "P90",
                        "Legend": "发送耗时P90"
                    },
                    {
                        "Aggregation": "P95",
                        "Legend": "发送耗时P95"
                    }
                ],
                "InnerMetric": false
            },
            {
                "Alias": "RequestWaitingDuration",
                "Description": "等待响应阶段耗时",
                "Metric": "pts_engine_req_wait_duration_seconds",
                "MetricType": "histogram",
                "Unit": "s",
                "Aggregations": [
                    {
                        "Aggregation": "Percentiles",
                        "Legend": "等待响应Percentiles"
                    },
                    {
                        "Aggregation": "Avg",
                        "Legend": "等待响应平均耗时"
                    },
                    {
                        "Aggregation": "P50",
                        "Legend": "等待响应P50"
                    },
                    {
                        "Aggregation": "P90",
                        "Legend": "等待响应P90"
                    },
                    {
                        "Aggregation": "P95",
                        "Legend": "等待响应P95"
                    }
                ],
                "InnerMetric": false
            },
            {
                "Alias": "RequestReceivingDuration",
                "Description": "下载响应体耗时",
                "Metric": "pts_engine_req_receive_duration_seconds",
                "MetricType": "histogram",
                "Unit": "s",
                "Aggregations": [
                    {
                        "Aggregation": "Percentiles",
                        "Legend": "下载响应体Percentiles"
                    },
                    {
                        "Aggregation": "Avg",
                        "Legend": "下载响应体平均耗时"
                    },
                    {
                        "Aggregation": "P50",
                        "Legend": "下载响应体P50"
                    },
                    {
                        "Aggregation": "P90",
                        "Legend": "下载响应体P90"
                    },
                    {
                        "Aggregation": "P95",
                        "Legend": "下载响应体P95"
                    }
                ],
                "InnerMetric": false
            },
            {
                "Alias": "RequestBlockingDuration",
                "Description": "等待连接耗时",
                "Metric": "pts_engine_req_block_duration_seconds",
                "MetricType": "histogram",
                "Unit": "s",
                "Aggregations": [
                    {
                        "Aggregation": "Percentiles",
                        "Legend": "等待连接Percentiles"
                    },
                    {
                        "Aggregation": "Avg",
                        "Legend": "等待连接平均耗时"
                    },
                    {
                        "Aggregation": "P50",
                        "Legend": "等待连接P50"
                    },
                    {
                        "Aggregation": "P90",
                        "Legend": "等待连接P90"
                    },
                    {
                        "Aggregation": "P95",
                        "Legend": "等待连接P95"
                    }
                ],
                "InnerMetric": false
            },
            {
                "Alias": "RequestConnectingDuration",
                "Description": "建立连接耗时",
                "Metric": "pts_engine_req_connect_duration_seconds",
                "MetricType": "histogram",
                "Unit": "s",
                "Aggregations": [
                    {
                        "Aggregation": "Percentiles",
                        "Legend": "建立连接Percentiles"
                    },
                    {
                        "Aggregation": "Avg",
                        "Legend": "建立连接平均耗时"
                    },
                    {
                        "Aggregation": "P50",
                        "Legend": "建立连接P50"
                    },
                    {
                        "Aggregation": "P90",
                        "Legend": "建立连接P90"
                    },
                    {
                        "Aggregation": "P95",
                        "Legend": "建立连接P95"
                    }
                ],
                "InnerMetric": false
            },
            {
                "Alias": "RequestHandshakingDuration",
                "Description": "TLS握手耗时",
                "Metric": "pts_engine_req_tls_handshake_duration_seconds",
                "MetricType": "histogram",
                "Unit": "s",
                "Aggregations": [
                    {
                        "Aggregation": "Percentiles",
                        "Legend": "TLS握手Percentiles"
                    },
                    {
                        "Aggregation": "Avg",
                        "Legend": "TLS握手平均耗时"
                    },
                    {
                        "Aggregation": "P50",
                        "Legend": "TLS握手P50"
                    },
                    {
                        "Aggregation": "P90",
                        "Legend": "TLS握手P90"
                    },
                    {
                        "Aggregation": "P95",
                        "Legend": "TLS握手P95"
                    }
                ],
                "InnerMetric": false
            },
            {
                "Alias": "RequestMaxDuration",
                "Description": "请求最大响应时间",
                "Metric": "pts_engine_req_max_duration_seconds",
                "MetricType": "gauge",
                "Unit": "s",
                "Aggregations": [
                    {
                        "Aggregation": "Max",
                        "Legend": "最大响应时间"
                    }
                ],
                "InnerMetric": true
            },
            {
                "Alias": "RequestMinDuration",
                "Description": "请求最小响应时间",
                "Metric": "pts_engine_req_min_duration_seconds",
                "MetricType": "gauge",
                "Unit": "s",
                "Aggregations": [
                    {
                        "Aggregation": "Min",
                        "Legend": "最小响应时间"
                    }
                ],
                "InnerMetric": true
            }
        ],
        "RequestId": "mzs29tyki4uxl-9pp6thbjeldh34a4xd"
    }
}
```

