**Example 1: 查询spark应用的运行任务实例列表**



Input: 

```
tccli dlc DescribeSparkAppTasks --cli-unfold-argument  \
    --JobId batch_133e005d-6486-4517-8ea7-b6b97b183a6b \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Tasks": [
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

