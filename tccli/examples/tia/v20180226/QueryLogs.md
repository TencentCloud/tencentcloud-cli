**Example 1: 显示某个训练任务的日志**



Input: 

```
tccli tia QueryLogs --cli-unfold-argument  \
    --JobName test-job \
    --Cluster ap-beijing \
    --StartTime 2018-04-26+10%3A00%3A00 \
    --EndTime 2018-04-26+11%3A00%3A00 \
    --Limit 2
```

Output: 
```
{
    "Response": {
        "Logs": [
            {
                "Log": "logs...",
                "Time": "2018-04-26T10:00:00.000000000Z",
                "ContainerName": "tensorflow",
                "PodId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                "PodName": "xxxxxx",
                "Namespace": "1000000000"
            },
            {
                "Log": "logs...",
                "Time": "2018-04-26T10:00:00.000000000Z",
                "ContainerName": "tensorflow",
                "PodId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                "PodName": "xxxxxx",
                "Namespace": "1000000000"
            }
        ],
        "RequestId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        "Context": "xxxxxxxxxx",
        "Listover": true
    }
}
```

