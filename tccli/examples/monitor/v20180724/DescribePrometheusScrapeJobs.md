**Example 1: 列出 Prometheus 抓取任务**

查询 Prometheus 抓取任务列表

Input: 

```
tccli monitor DescribePrometheusScrapeJobs --cli-unfold-argument  \
    --InstanceId prom-evrh1x32 \
    --AgentId agent-hod16m43
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "RequestId": "5fa8c92-3072-4f46-8553-4cb82c30943c",
        "ScrapeJobSet": [
            {
                "AgentId": "agent-hod16m43",
                "Config": "job_name: static\nhonor_timestamps: true\nmetrics_path: /metrics\nscheme: http\nfollow_redirects: true\nstatic_configs:\n- targets:\n  - localhost:9090\n",
                "Name": "node-exporter",
                "JobId": "job-afeiig0k"
            }
        ]
    }
}
```

