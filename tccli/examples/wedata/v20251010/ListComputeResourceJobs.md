**Example 1: 查询计算资源任务列表**



Input: 

```
tccli wedata ListComputeResourceJobs --cli-unfold-argument  \
    --WorkspaceId 17663856806379896 \
    --ResourceId res_001 \
    --Page.PageNumber 1 \
    --Page.PageSize 10 \
    --Keywords task_001 \
    --JobStatus RUNNING PENDING \
    --OrderFields.0.Name CreateTime \
    --OrderFields.0.Direction DESC \
    --Filters.0.Name JobType \
    --Filters.0.Values sql pyspark
```

Output: 
```
{
    "Response": {
        "Data": {
            "Jobs": [
                {
                    "ResourceType": 1,
                    "JobId": "job_001",
                    "JobName": "my-sql-job",
                    "JobStatus": "RUNNING",
                    "InstanceId": "inst_001",
                    "CreateTime": "1738953600000",
                    "Runtime": "120",
                    "SourceName": "DataStudio",
                    "ObjectName": "target_table",
                    "TriggerType": "manual",
                    "JobType": "sql",
                    "Operator": "user001",
                    "SQL": "SELECT * FROM test_table LIMIT 100",
                    "UsedCU": 4,
                    "ExecutionId": "exec_001"
                }
            ],
            "Page": {
                "PageNumber": 1,
                "PageSize": 10,
                "TotalCount": 1,
                "TotalPageNumber": 1
            }
        },
        "RequestId": "5a678494-1b3c-43d1-b897-8748beb25f6d"
    }
}
```

