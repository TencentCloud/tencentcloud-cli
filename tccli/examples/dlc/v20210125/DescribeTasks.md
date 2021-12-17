**Example 1: 任务列表展示**



Input: 

```
tccli dlc DescribeTasks --cli-unfold-argument  \
    --Sorting desc \
    --Filters.0.Values e386471f-139a-4e59-877f-50ece8135b99 \
    --Filters.0.Name task-id \
    --Filters.1.Values e386471f-139a-4e59-877f-50ece8135b98 \
    --Filters.1.Name task-id \
    --Limit 10 \
    --SortBy create-time \
    --StartTime 2019-01-21 00:00:00 \
    --Offset 0 \
    --EndTime 2019-01-22 00:00:00 \
    --DataEngineName shared_presto
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "TaskList": [
            {
                "CanDownload": true,
                "DataSet": "{'Schema':['name','age'],'Data':[{'name':'29','age':'Michael'}]}",
                "State": 2,
                "DataAmount": 1024,
                "Percentage": 100,
                "SQLType": "DDL",
                "RowAffectInfo": "500 rows selected (0.077 seconds)",
                "InputConf": "[{'Key':'paths','Value':'lakefs://20000003366d155f79a522c8349496'}]",
                "DataEngineId": "resource-1gghpd1t",
                "UpdateTime": "1611646962000",
                "TaskType": "presto",
                "ProgressDetail": "[{'jobId':1,'stages':[{'stageId':1,'numTasks':3,'numActiveTasks'}]}]",
                "InputType": "local",
                "DataNumber": 100,
                "ResultExpired": true,
                "OutputPath": "cosn://test-bucket-123434324234/result/",
                "DataEngineName": "shared_presto",
                "Error": "****",
                "OperateUin": "****",
                "OutputMessage": "****",
                "CreateTime": "1611646962000",
                "UsedTime": 60000,
                "DatabaseName": "database1",
                "SQL": "U0VMRUNUICogRlJPTSBgdGVzdGA7",
                "Id": "89570c65-49de-4bbd-ac0a-a67c724fc80f"
            }
        ],
        "RequestId": "b577857e-041f-46c7-b5cf-4b3d3f50bc51"
    }
}
```

