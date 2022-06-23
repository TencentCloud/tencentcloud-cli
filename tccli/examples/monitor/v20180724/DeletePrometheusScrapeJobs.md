**Example 1: 删除 Prometheus 抓取任务**



Input: 

```
tccli monitor DeletePrometheusScrapeJobs --cli-unfold-argument  \
    --InstanceId xx \
    --AgentId xx \
    --JobIds xx
```

Output: 
```
{
    "Response": {
        "RequestId": "3e0dff9d-9ed5-47c3-beb2-a42c1d69e1cc"
    }
}
```

