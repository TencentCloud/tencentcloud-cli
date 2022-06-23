**Example 1: 列出 Prometheus 抓取任务**



Input: 

```
tccli monitor DescribePrometheusScrapeJobs --cli-unfold-argument  \
    --InstanceId xx \
    --AgentId xx
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "RequestId": "xx",
        "ScrapeJobSet": [
            {
                "AgentId": "xx",
                "Config": "xx",
                "Name": "xx",
                "JobId": "xx"
            }
        ]
    }
}
```

