**Example 1: 查询健康报告生成任务列表**



Input: 

```
tccli dbbrain DescribeDBDiagReportTasks --cli-unfold-argument  \
    --Product mysql \
    --StartTime 2020-09-21T00:00:00+00:00 \
    --EndTime 2020-09-22T00:00:00+00:00 \
    --Sources DAILY_INSPECTION
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Tasks": [
            {
                "AsyncRequestId": 63452,
                "Source": "DAILY_INSPECTION",
                "Progress": 100,
                "CreateTime": "2020-09-21 00:00:00",
                "StartTime": "2020-09-21 00:00:00",
                "EndTime": "2020-09-21 00:00:00",
                "InstanceInfo": {
                    "InstanceId": "cdb-c9orjpes",
                    "InstanceName": "dbbrain-test",
                    "EngineVersion": "5.7",
                    "Vip": "10.207.0.10",
                    "Vport": 3306,
                    "Product": "MySQL"
                },
                "HealthStatus": {
                    "HealthScore": 100,
                    "HealthLevel": "HEALTH",
                    "ScoreLost": 0,
                    "ScoreDetails": []
                }
            }
        ],
        "RequestId": "24665720-8c93-11eb-bee6-e98cea0e6794"
    }
}
```

