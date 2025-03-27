**Example 1: 获取prometheus集成指标**



Input: 

```
tccli monitor DescribePrometheusIntegrationMetrics --cli-unfold-argument  \
    --IntegrationCode qcloud
```

Output: 
```
{
    "Response": {
        "IntegrationMetricSet": [
            {
                "Group": "cdb",
                "Metrics": [
                    {
                        "MetricName": "qce_cdb_abortedclients_sum",
                        "Name": "异常关闭的客户端连接数",
                        "MetricType": "",
                        "Unit": "Count",
                        "Description": "由于客户端在没有正确关闭连接的情况下死亡而中止的连接数"
                    }
                ]
            }
        ],
        "RequestId": "sjwbr-sjhrbgfrb"
    }
}
```

