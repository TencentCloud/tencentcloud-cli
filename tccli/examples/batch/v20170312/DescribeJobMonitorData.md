**Example 1: 查询作业实例的资源使用监控信息**



Input: 

```
tccli batch DescribeJobMonitorData --cli-unfold-argument  \
    --JobId job-1jj9noyr \
    --TaskName demo-1 \
    --TaskInstanceIndex 0 \
    --MetricName CpuUsage
```

Output: 
```
{
    "Response": {
        "RequestId": "a66adf73-110f-49b4-a173-c68c952d4428",
        "Period": 60,
        "DataPoints": {
            "Timestamps": [
                1749696420,
                1749696430,
                1749696440
            ],
            "Values": [
                0.1,
                0.2,
                0.3
            ]
        }
    }
}
```

