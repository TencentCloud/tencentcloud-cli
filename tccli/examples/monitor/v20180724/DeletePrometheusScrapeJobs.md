**Example 1: 删除 Prometheus 抓取任务**

删除 Prometheus 抓取任务

Input: 

```
tccli monitor DeletePrometheusScrapeJobs --cli-unfold-argument  \
    --InstanceId prom-evrh1x32 \
    --AgentId agent-hod16m3f \
    --JobIds job-afeiig0x
```

Output: 
```
{
    "Response": {
        "RequestId": "3e0dff9d-9ed5-47c3-beb2-a42c1d69e1cc"
    }
}
```

