**Example 1: 计算资源任务概览**

查询指定计算资源下正在运行和排队中的任务概览信息

Input: 

```
tccli wedata GetComputeResourceJobsSummaries --cli-unfold-argument  \
    --WorkspaceId 17700183032157854 \
    --ResourceId res-d297d4c1
```

Output: 
```
{
    "Response": {
        "Data": {
            "Summaries": [
                {
                    "Jobs": [
                        {
                            "JobId": "job-a1b2c3d4e5f6",
                            "JobName": "spark-etl-task"
                        }
                    ],
                    "Total": 5,
                    "Status": "running"
                },
                {
                    "Jobs": [
                        {
                            "JobId": "job-m7n8p9q0r1s2",
                            "JobName": "data-sync-task"
                        }
                    ],
                    "Total": 2,
                    "Status": "in_queue"
                }
            ]
        },
        "RequestId": "1dea488b-50b7-4f68-bc8c-80a2ae04cfa1"
    }
}
```

