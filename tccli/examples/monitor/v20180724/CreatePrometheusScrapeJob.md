**Example 1: 创建 Prometheus 抓取任务**



Input: 

```
tccli monitor CreatePrometheusScrapeJob --cli-unfold-argument  \
    --InstanceId prom-abcd1234 \
    --AgentId agent-abcd1234 \
    --Config job_name: demo-config
honor_timestamps: true
metrics_path: /metrics
scheme: http
static_configs:
- targets:
  - localhost:8080
```

Output: 
```
{
    "Response": {
        "JobId": "job-xxfs",
        "RequestId": "3e0dff9d-9ed5-47c3-beb2-a42c1d69e1cc"
    }
}
```

