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
                "Aggregations": [
                    {
                        "Aggregation": "Rate",
                        "Legend": "请求RPS",
                        "Unit": "reqs/s"
                    },
                    {
                        "Aggregation": "MaxRateOverTime",
                        "Legend": "请求RPS峰值",
                        "Unit": "reqs/s"
                    },
                    {
                        "Aggregation": "Count",
                        "Legend": "请求总数",
                        "Unit": "reqs"
                    },
                    {
                        "Aggregation": "ErrorPercentage",
                        "Legend": "请求失败率",
                        "Unit": "%"
                    },
                    {
                        "Aggregation": "ErrorPercentageByResult",
                        "Legend": "请求失败率(结果码）",
                        "Unit": "%"
                    }
                ],
                "Alias": "RequestsCount",
                "Description": "请求数量",
                "InnerMetric": false,
                "Metric": "pts_engine_req_total",
                "MetricType": "counter",
                "Unit": "reqs"
            },
            {
                "Aggregations": [
                    {
                        "Aggregation": "Percentiles",
                        "Legend": "响应时间Percentiles",
                        "Unit": "s"
                    },
                    {
                        "Aggregation": "Timings",
                        "Legend": "各阶段平均耗时分布",
                        "Unit": "s"
                    },
                    {
                        "Aggregation": "Avg",
                        "Legend": "平均响应时间",
                        "Unit": "s"
                    },
                    {
                        "Aggregation": "P50",
                        "Legend": "响应时间P50",
                        "Unit": "s"
                    },
                    {
                        "Aggregation": "P90",
                        "Legend": "响应时间P90",
                        "Unit": "s"
                    },
                    {
                        "Aggregation": "P95",
                        "Legend": "响应时间P95",
                        "Unit": "s"
                    },
                    {
                        "Aggregation": "P99",
                        "Legend": "响应时间P99",
                        "Unit": "s"
                    }
                ],
                "Alias": "RequestDuration",
                "Description": "请求响应时间",
                "InnerMetric": false,
                "Metric": "pts_engine_req_duration_seconds",
                "MetricType": "histogram",
                "Unit": "s"
            },
            {
                "Aggregations": [
                    {
                        "Aggregation": "Rate",
                        "Legend": "检查点RPS",
                        "Unit": "checks/s"
                    },
                    {
                        "Aggregation": "Count",
                        "Legend": "检查点总数",
                        "Unit": "checks"
                    },
                    {
                        "Aggregation": "ErrorPercentage",
                        "Legend": "检查点错误率",
                        "Unit": "%"
                    }
                ],
                "Alias": "ChecksCount",
                "Description": "检查点数量",
                "InnerMetric": false,
                "Metric": "pts_engine_checks_total",
                "MetricType": "counter",
                "Unit": "checks"
            },
            {
                "Aggregations": [
                    {
                        "Aggregation": "Gauge",
                        "Legend": "并发数",
                        "Unit": "VUs"
                    },
                    {
                        "Aggregation": "MaxOverTime",
                        "Legend": "并发数峰值",
                        "Unit": "VUs"
                    }
                ],
                "Alias": "NumberVirtualUsers",
                "Description": "并发用户数",
                "InnerMetric": false,
                "Metric": "pts_engine_num_vus",
                "MetricType": "gauge",
                "Unit": "VUs"
            },
            {
                "Aggregations": [
                    {
                        "Aggregation": "Rate",
                        "Legend": "发送速率",
                        "Unit": "bytes/s"
                    },
                    {
                        "Aggregation": "Count",
                        "Legend": "发送总数",
                        "Unit": "bytes"
                    },
                    {
                        "Aggregation": "UsagePercentage",
                        "Legend": "出口带宽使用率",
                        "Unit": "%"
                    }
                ],
                "Alias": "SendBytesCount",
                "Description": "发送字节数",
                "InnerMetric": false,
                "Metric": "pts_engine_send_bytes_total",
                "MetricType": "counter",
                "Unit": "bytes"
            },
            {
                "Aggregations": [
                    {
                        "Aggregation": "Rate",
                        "Legend": "接收速率",
                        "Unit": "bytes/s"
                    },
                    {
                        "Aggregation": "Count",
                        "Legend": "接收总数",
                        "Unit": "bytes"
                    },
                    {
                        "Aggregation": "UsagePercentage",
                        "Legend": "入口带宽使用率",
                        "Unit": "%"
                    }
                ],
                "Alias": "ReceiveBytesCount",
                "Description": "接收字节数",
                "InnerMetric": false,
                "Metric": "pts_engine_receive_bytes_total",
                "MetricType": "counter",
                "Unit": "bytes"
            },
            {
                "Aggregations": [
                    {
                        "Aggregation": "Rate",
                        "Legend": "场景执行TPS",
                        "Unit": "iters/s"
                    },
                    {
                        "Aggregation": "Count",
                        "Legend": "场景执行总数",
                        "Unit": "iters"
                    }
                ],
                "Alias": "IterationsCount",
                "Description": "场景迭代数",
                "InnerMetric": false,
                "Metric": "pts_engine_iterations_total",
                "MetricType": "counter",
                "Unit": "iters"
            },
            {
                "Aggregations": [
                    {
                        "Aggregation": "Rate",
                        "Legend": "已发送请求RPS",
                        "Unit": "reqs/s"
                    },
                    {
                        "Aggregation": "Count",
                        "Legend": "已发送请求总数",
                        "Unit": "reqs"
                    }
                ],
                "Alias": "RequestSentCount",
                "Description": "已发送请求数量",
                "InnerMetric": false,
                "Metric": "pts_engine_req_sent_total",
                "MetricType": "counter",
                "Unit": "reqs"
            },
            {
                "Aggregations": [
                    {
                        "Aggregation": "Percentiles",
                        "Legend": "场景执行Percentiles",
                        "Unit": "s"
                    },
                    {
                        "Aggregation": "Avg",
                        "Legend": "场景执行平均耗时",
                        "Unit": "s"
                    },
                    {
                        "Aggregation": "P50",
                        "Legend": "场景执行P50",
                        "Unit": "s"
                    },
                    {
                        "Aggregation": "P90",
                        "Legend": "场景执行P90",
                        "Unit": "s"
                    },
                    {
                        "Aggregation": "P95",
                        "Legend": "场景执行P95",
                        "Unit": "s"
                    },
                    {
                        "Aggregation": "P99",
                        "Legend": "场景执行P99",
                        "Unit": "s"
                    }
                ],
                "Alias": "IterationDuration",
                "Description": "场景执行耗时",
                "InnerMetric": false,
                "Metric": "pts_engine_iterations_duration_seconds",
                "MetricType": "histogram",
                "Unit": "s"
            },
            {
                "Aggregations": [
                    {
                        "Aggregation": "Percentiles",
                        "Legend": "发送耗时Percentiles",
                        "Unit": "s"
                    },
                    {
                        "Aggregation": "Avg",
                        "Legend": "发送请求平均耗时",
                        "Unit": "s"
                    },
                    {
                        "Aggregation": "P50",
                        "Legend": "发送耗时P50",
                        "Unit": "s"
                    },
                    {
                        "Aggregation": "P90",
                        "Legend": "发送耗时P90",
                        "Unit": "s"
                    },
                    {
                        "Aggregation": "P95",
                        "Legend": "发送耗时P95",
                        "Unit": ""
                    },
                    {
                        "Aggregation": "P99",
                        "Legend": "发送耗时P99",
                        "Unit": "s"
                    }
                ],
                "Alias": "RequestSendingDuration",
                "Description": "发送请求阶段耗时",
                "InnerMetric": false,
                "Metric": "pts_engine_req_send_duration_seconds",
                "MetricType": "histogram",
                "Unit": "s"
            },
            {
                "Aggregations": [
                    {
                        "Aggregation": "Percentiles",
                        "Legend": "等待响应Percentiles",
                        "Unit": "s"
                    },
                    {
                        "Aggregation": "Avg",
                        "Legend": "等待响应平均耗时",
                        "Unit": "s"
                    },
                    {
                        "Aggregation": "P50",
                        "Legend": "等待响应P50",
                        "Unit": "s"
                    },
                    {
                        "Aggregation": "P90",
                        "Legend": "等待响应P90",
                        "Unit": "s"
                    },
                    {
                        "Aggregation": "P95",
                        "Legend": "等待响应P95",
                        "Unit": "s"
                    },
                    {
                        "Aggregation": "P99",
                        "Legend": "等待响应P99",
                        "Unit": "s"
                    }
                ],
                "Alias": "RequestWaitingDuration",
                "Description": "等待响应阶段耗时",
                "InnerMetric": false,
                "Metric": "pts_engine_req_wait_duration_seconds",
                "MetricType": "histogram",
                "Unit": "s"
            },
            {
                "Aggregations": [
                    {
                        "Aggregation": "Percentiles",
                        "Legend": "下载响应体Percentiles",
                        "Unit": "s"
                    },
                    {
                        "Aggregation": "Avg",
                        "Legend": "下载响应体平均耗时",
                        "Unit": "s"
                    },
                    {
                        "Aggregation": "P50",
                        "Legend": "下载响应体P50",
                        "Unit": "s"
                    },
                    {
                        "Aggregation": "P90",
                        "Legend": "下载响应体P90",
                        "Unit": "s"
                    },
                    {
                        "Aggregation": "P95",
                        "Legend": "下载响应体P95",
                        "Unit": "s"
                    },
                    {
                        "Aggregation": "P99",
                        "Legend": "下载响应体P99",
                        "Unit": "s"
                    }
                ],
                "Alias": "RequestReceivingDuration",
                "Description": "下载响应体耗时",
                "InnerMetric": false,
                "Metric": "pts_engine_req_receive_duration_seconds",
                "MetricType": "histogram",
                "Unit": "s"
            },
            {
                "Aggregations": [
                    {
                        "Aggregation": "Percentiles",
                        "Legend": "等待连接Percentiles",
                        "Unit": "s"
                    },
                    {
                        "Aggregation": "Avg",
                        "Legend": "等待连接平均耗时",
                        "Unit": "s"
                    },
                    {
                        "Aggregation": "P50",
                        "Legend": "等待连接P50",
                        "Unit": "s"
                    },
                    {
                        "Aggregation": "P90",
                        "Legend": "等待连接P90",
                        "Unit": "s"
                    },
                    {
                        "Aggregation": "P95",
                        "Legend": "等待连接P95",
                        "Unit": "s"
                    },
                    {
                        "Aggregation": "P99",
                        "Legend": "等待连接P99",
                        "Unit": "s"
                    }
                ],
                "Alias": "RequestBlockingDuration",
                "Description": "等待连接耗时",
                "InnerMetric": false,
                "Metric": "pts_engine_req_block_duration_seconds",
                "MetricType": "histogram",
                "Unit": "s"
            },
            {
                "Aggregations": [
                    {
                        "Aggregation": "Percentiles",
                        "Legend": "建立连接Percentiles",
                        "Unit": "s"
                    },
                    {
                        "Aggregation": "Avg",
                        "Legend": "建立连接平均耗时",
                        "Unit": "s"
                    },
                    {
                        "Aggregation": "P50",
                        "Legend": "建立连接P50",
                        "Unit": "s"
                    },
                    {
                        "Aggregation": "P90",
                        "Legend": "建立连接P90",
                        "Unit": "s"
                    },
                    {
                        "Aggregation": "P95",
                        "Legend": "建立连接P95",
                        "Unit": "s"
                    },
                    {
                        "Aggregation": "P99",
                        "Legend": "建立连接P99",
                        "Unit": "s"
                    }
                ],
                "Alias": "RequestConnectingDuration",
                "Description": "建立连接耗时",
                "InnerMetric": false,
                "Metric": "pts_engine_req_connect_duration_seconds",
                "MetricType": "histogram",
                "Unit": "s"
            },
            {
                "Aggregations": [
                    {
                        "Aggregation": "Percentiles",
                        "Legend": "TLS握手Percentiles",
                        "Unit": "s"
                    },
                    {
                        "Aggregation": "Avg",
                        "Legend": "TLS握手平均耗时",
                        "Unit": "s"
                    },
                    {
                        "Aggregation": "P50",
                        "Legend": "TLS握手P50",
                        "Unit": "s"
                    },
                    {
                        "Aggregation": "P90",
                        "Legend": "TLS握手P90",
                        "Unit": "s"
                    },
                    {
                        "Aggregation": "P95",
                        "Legend": "TLS握手P95",
                        "Unit": "s"
                    },
                    {
                        "Aggregation": "P99",
                        "Legend": "TLS握手P99",
                        "Unit": "s"
                    }
                ],
                "Alias": "RequestHandshakingDuration",
                "Description": "TLS握手耗时",
                "InnerMetric": false,
                "Metric": "pts_engine_req_tls_handshake_duration_seconds",
                "MetricType": "histogram",
                "Unit": "s"
            },
            {
                "Aggregations": [
                    {
                        "Aggregation": "Max",
                        "Legend": "最大响应时间",
                        "Unit": "s"
                    }
                ],
                "Alias": "RequestMaxDuration",
                "Description": "请求最大响应时间",
                "InnerMetric": true,
                "Metric": "pts_engine_req_max_duration_seconds",
                "MetricType": "gauge",
                "Unit": "s"
            },
            {
                "Aggregations": [
                    {
                        "Aggregation": "Min",
                        "Legend": "最小响应时间",
                        "Unit": "s"
                    }
                ],
                "Alias": "RequestMinDuration",
                "Description": "请求最小响应时间",
                "InnerMetric": true,
                "Metric": "pts_engine_req_min_duration_seconds",
                "MetricType": "gauge",
                "Unit": "s"
            },
            {
                "Aggregations": [
                    {
                        "Aggregation": "UsagePercentage",
                        "Legend": "CPU使用率",
                        "Unit": "%"
                    }
                ],
                "Alias": "ContainerCPUUsageCount",
                "Description": "施压机 CPU 使用量",
                "InnerMetric": true,
                "Metric": "container_cpu_usage_seconds_total",
                "MetricType": "counter",
                "Unit": "s"
            },
            {
                "Aggregations": [
                    {
                        "Aggregation": "UsagePercentage",
                        "Legend": "内存使用率",
                        "Unit": "%"
                    }
                ],
                "Alias": "ContainerMemUsage",
                "Description": "施压机内存使用量",
                "InnerMetric": true,
                "Metric": "container_memory_usage_bytes",
                "MetricType": "gauge",
                "Unit": "bytes"
            },
            {
                "Aggregations": [
                    {
                        "Aggregation": "Rate",
                        "Legend": "发送速率",
                        "Unit": "bytes/s"
                    },
                    {
                        "Aggregation": "Count",
                        "Legend": "发送总数",
                        "Unit": "bytes"
                    }
                ],
                "Alias": "ContainerNetworkSendCount",
                "Description": "施压机发送字节数",
                "InnerMetric": true,
                "Metric": "container_network_transmit_bytes_total",
                "MetricType": "counter",
                "Unit": "bytes"
            },
            {
                "Aggregations": [
                    {
                        "Aggregation": "Rate",
                        "Legend": "接收速率",
                        "Unit": "bytes/s"
                    },
                    {
                        "Aggregation": "Count",
                        "Legend": "接收总数",
                        "Unit": "bytes"
                    }
                ],
                "Alias": "ContainerNetworkReceiveCount",
                "Description": "施压机接收字节数",
                "InnerMetric": true,
                "Metric": "container_network_receive_bytes_total",
                "MetricType": "counter",
                "Unit": "bytes"
            }
        ],
        "RequestId": "50233a27-a7c0-4e3e-b598-bf213373aa99"
    }
}
```

