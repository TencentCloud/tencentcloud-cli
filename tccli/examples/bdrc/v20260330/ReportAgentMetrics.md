**Example 1: 上报agent机器指标信息**



Input: 

```
tccli bdrc ReportAgentMetrics --cli-unfold-argument  \
    --InstanceId br-agent-3b7dfe41-6bd2-6ff8-4cde-eb5d71398c4a \
    --CvmInstanceId ins-aznn0ilo \
    --AgentIp 172.16.0.2 \
    --Metrics.0.MetricName system_cpu_usage_percent \
    --Metrics.0.Value 5.00000000002 \
    --Metrics.0.Timestamp 1781071201698 \
    --Metrics.0.Labels "{\"IP\":\"172.16.0.2\",\"UIN\":\"700002687914\",\"cvm_instance_id\":\"ins-aznn0ilo\",\"instance_id\":\"br-agent-3b7dfe41-6bd2-6ff8-4cde-eb5d71398c4a\",\"label\":\"\"}"
```

Output: 
```
{
    "Response": {
        "AcceptedCount": 1,
        "InstanceId": "br-agent-3b7dfe41-6bd2-6ff8-4cde-eb5d71398c4a",
        "RequestId": "73e066a3-673b-4913-bf36-740c9e6f5f27"
    }
}
```

