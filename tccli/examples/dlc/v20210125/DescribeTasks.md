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
                "Error": "xx",
                "UiUrl": "xx",
                "CanDownload": true,
                "DataSet": "xx",
                "State": 2,
                "DataAmount": 1024,
                "SparkJobId": "xx",
                "Percentage": 100,
                "SQLType": "xx",
                "SparkJobFile": "xx",
                "RowAffectInfo": "xx",
                "InputConf": "xx",
                "DataEngineId": "xx",
                "UpdateTime": "xx",
                "SparkJobName": "xx",
                "TaskType": "xx",
                "ProgressDetail": "xx",
                "InputType": "xx",
                "UserAlias": "xx",
                "DataNumber": 100,
                "ResultExpired": true,
                "OutputPath": "xx",
                "DataEngineName": "xx",
                "OperateUin": "xx",
                "OutputMessage": "xx",
                "CreateTime": "xx",
                "UsedTime": 60000,
                "DatabaseName": "xx",
                "SQL": "xx",
                "Id": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

