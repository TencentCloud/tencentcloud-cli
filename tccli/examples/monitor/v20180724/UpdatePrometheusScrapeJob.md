**Example 1: 更新 Prometheus 抓取任务**



Input: 

```
tccli monitor UpdatePrometheusScrapeJob --cli-unfold-argument  \
    --JobId xx \
    --InstanceId xx \
    --AgentId xx \
    --Config job_name:xx
```

Output: 
```
{
    "Response": {
        "RequestId": "3e0dff9d-9ed5-47c3-beb2-a42c1d69e1cc"
    }
}
```

