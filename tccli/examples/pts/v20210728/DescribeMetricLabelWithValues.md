**Example 1: 查询指标所有的label及values值**

查询指标所有的label及values值

Input: 

```
tccli pts DescribeMetricLabelWithValues --cli-unfold-argument  \
    --JobId job-jbn1pvne \
    --ScenarioId scenario-frfvrab4 \
    --ProjectId project-c9drst6a
```

Output: 
```
{
    "Response": {
        "MetricLabelWithValuesSet": [
            {
                "MetricName": "pts_engine_req_total",
                "LabelValuesSet": [
                    {
                        "LabelName": "service",
                        "LabelValues": [
                            "http://httpbin.org/get",
                            "http://www.baidu.com"
                        ]
                    },
                    {
                        "LabelName": "status",
                        "LabelValues": [
                            "200",
                            "502"
                        ]
                    },
                    {
                        "LabelName": "result",
                        "LabelValues": [
                            "502 Bad Gateway",
                            "ok"
                        ]
                    },
                    {
                        "LabelName": "method",
                        "LabelValues": [
                            "GET"
                        ]
                    },
                    {
                        "LabelName": "proto",
                        "LabelValues": [
                            "HTTP/1.1"
                        ]
                    },
                    {
                        "LabelName": "region",
                        "LabelValues": [
                            "ap-shanghai"
                        ]
                    }
                ]
            },
            {
                "MetricName": "pts_engine_req_duration_seconds",
                "LabelValuesSet": [
                    {
                        "LabelName": "service",
                        "LabelValues": [
                            "http://httpbin.org/get",
                            "http://www.baidu.com"
                        ]
                    },
                    {
                        "LabelName": "status",
                        "LabelValues": [
                            "200",
                            "502"
                        ]
                    },
                    {
                        "LabelName": "result",
                        "LabelValues": [
                            "502 Bad Gateway",
                            "ok"
                        ]
                    },
                    {
                        "LabelName": "method",
                        "LabelValues": [
                            "GET"
                        ]
                    },
                    {
                        "LabelName": "proto",
                        "LabelValues": [
                            "HTTP/1.1"
                        ]
                    },
                    {
                        "LabelName": "region",
                        "LabelValues": [
                            "ap-shanghai"
                        ]
                    }
                ]
            },
            {
                "MetricName": "pts_engine_checks_total",
                "LabelValuesSet": [
                    {
                        "LabelName": "check",
                        "LabelValues": [
                            "body.args.name1 equals value1",
                            "status is 200"
                        ]
                    },
                    {
                        "LabelName": "result",
                        "LabelValues": [
                            "ok"
                        ]
                    },
                    {
                        "LabelName": "region",
                        "LabelValues": [
                            "ap-shanghai"
                        ]
                    }
                ]
            },
            {
                "MetricName": "pts_engine_num_vus",
                "LabelValuesSet": []
            },
            {
                "MetricName": "pts_engine_send_bytes_total",
                "LabelValuesSet": []
            },
            {
                "MetricName": "pts_engine_receive_bytes_total",
                "LabelValuesSet": []
            },
            {
                "MetricName": "pts_engine_iterations_total",
                "LabelValuesSet": []
            },
            {
                "MetricName": "pts_engine_iterations_duration_seconds",
                "LabelValuesSet": []
            },
            {
                "MetricName": "pts_engine_req_send_duration_seconds",
                "LabelValuesSet": [
                    {
                        "LabelName": "service",
                        "LabelValues": [
                            "http://httpbin.org/get",
                            "http://www.baidu.com"
                        ]
                    },
                    {
                        "LabelName": "status",
                        "LabelValues": [
                            "200",
                            "502"
                        ]
                    },
                    {
                        "LabelName": "result",
                        "LabelValues": [
                            "502 Bad Gateway",
                            "ok"
                        ]
                    },
                    {
                        "LabelName": "method",
                        "LabelValues": [
                            "GET"
                        ]
                    },
                    {
                        "LabelName": "proto",
                        "LabelValues": [
                            "HTTP/1.1"
                        ]
                    },
                    {
                        "LabelName": "region",
                        "LabelValues": [
                            "ap-shanghai"
                        ]
                    }
                ]
            },
            {
                "MetricName": "pts_engine_req_wait_duration_seconds",
                "LabelValuesSet": [
                    {
                        "LabelName": "service",
                        "LabelValues": [
                            "http://httpbin.org/get",
                            "http://www.baidu.com"
                        ]
                    },
                    {
                        "LabelName": "status",
                        "LabelValues": [
                            "200",
                            "502"
                        ]
                    },
                    {
                        "LabelName": "result",
                        "LabelValues": [
                            "502 Bad Gateway",
                            "ok"
                        ]
                    },
                    {
                        "LabelName": "method",
                        "LabelValues": [
                            "GET"
                        ]
                    },
                    {
                        "LabelName": "proto",
                        "LabelValues": [
                            "HTTP/1.1"
                        ]
                    },
                    {
                        "LabelName": "region",
                        "LabelValues": [
                            "ap-shanghai"
                        ]
                    }
                ]
            },
            {
                "MetricName": "pts_engine_req_receive_duration_seconds",
                "LabelValuesSet": [
                    {
                        "LabelName": "service",
                        "LabelValues": [
                            "http://httpbin.org/get",
                            "http://www.baidu.com"
                        ]
                    },
                    {
                        "LabelName": "status",
                        "LabelValues": [
                            "200",
                            "502"
                        ]
                    },
                    {
                        "LabelName": "result",
                        "LabelValues": [
                            "502 Bad Gateway",
                            "ok"
                        ]
                    },
                    {
                        "LabelName": "method",
                        "LabelValues": [
                            "GET"
                        ]
                    },
                    {
                        "LabelName": "proto",
                        "LabelValues": [
                            "HTTP/1.1"
                        ]
                    },
                    {
                        "LabelName": "region",
                        "LabelValues": [
                            "ap-shanghai"
                        ]
                    }
                ]
            },
            {
                "MetricName": "pts_engine_req_block_duration_seconds",
                "LabelValuesSet": [
                    {
                        "LabelName": "service",
                        "LabelValues": [
                            "http://httpbin.org/get",
                            "http://www.baidu.com"
                        ]
                    },
                    {
                        "LabelName": "status",
                        "LabelValues": [
                            "200",
                            "502"
                        ]
                    },
                    {
                        "LabelName": "result",
                        "LabelValues": [
                            "502 Bad Gateway",
                            "ok"
                        ]
                    },
                    {
                        "LabelName": "method",
                        "LabelValues": [
                            "GET"
                        ]
                    },
                    {
                        "LabelName": "proto",
                        "LabelValues": [
                            "HTTP/1.1"
                        ]
                    },
                    {
                        "LabelName": "region",
                        "LabelValues": [
                            "ap-shanghai"
                        ]
                    }
                ]
            },
            {
                "MetricName": "pts_engine_req_connect_duration_seconds",
                "LabelValuesSet": [
                    {
                        "LabelName": "service",
                        "LabelValues": [
                            "http://httpbin.org/get",
                            "http://www.baidu.com"
                        ]
                    },
                    {
                        "LabelName": "status",
                        "LabelValues": [
                            "200",
                            "502"
                        ]
                    },
                    {
                        "LabelName": "result",
                        "LabelValues": [
                            "502 Bad Gateway",
                            "ok"
                        ]
                    },
                    {
                        "LabelName": "method",
                        "LabelValues": [
                            "GET"
                        ]
                    },
                    {
                        "LabelName": "proto",
                        "LabelValues": [
                            "HTTP/1.1"
                        ]
                    },
                    {
                        "LabelName": "region",
                        "LabelValues": [
                            "ap-shanghai"
                        ]
                    }
                ]
            },
            {
                "MetricName": "pts_engine_req_tls_handshake_duration_seconds",
                "LabelValuesSet": [
                    {
                        "LabelName": "service",
                        "LabelValues": [
                            "http://httpbin.org/get",
                            "http://www.baidu.com"
                        ]
                    },
                    {
                        "LabelName": "status",
                        "LabelValues": [
                            "200",
                            "502"
                        ]
                    },
                    {
                        "LabelName": "result",
                        "LabelValues": [
                            "502 Bad Gateway",
                            "ok"
                        ]
                    },
                    {
                        "LabelName": "method",
                        "LabelValues": [
                            "GET"
                        ]
                    },
                    {
                        "LabelName": "proto",
                        "LabelValues": [
                            "HTTP/1.1"
                        ]
                    },
                    {
                        "LabelName": "region",
                        "LabelValues": [
                            "ap-shanghai"
                        ]
                    }
                ]
            }
        ],
        "RequestId": "xx"
    }
}
```

