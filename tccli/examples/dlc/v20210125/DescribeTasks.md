**Example 1: 查询任务列表**



Input: 

```
tccli dlc DescribeTasks --cli-unfold-argument  \
    --Limit 20 \
    --Offset 0 \
    --Filters.0.Name task-id \
    --Filters.0.Values 4ad30ca9-8b0e-499f-b4e1-d6e43ba0e564
```

Output: 
```
{
    "Response": {
        "RequestId": "7b1b3bb1-6174-49ea-a97e-bb141d32c1b0",
        "TaskList": [
            {
                "Id": "4ad30ca9-8b0e-499f-b4e1-d6e43ba0e564",
                "DatabaseName": "testdb",
                "SQLType": "DQL",
                "SQL": "SELECT * FROM `test`.`table1` LIMIT 10",
                "DataAmount": 0,
                "UsedTime": 0,
                "OutputPath": "cosn://rickyhu-1301312708/test2/DLCQueryResults/2021/09/01/4ad30ca9-8b0e-499f-b4e1-d6e43ba0e564/",
                "RowAffectInfo": "",
                "ResultExpired": false,
                "State": 1,
                "CreateTime": "1630496032942",
                "DataSet": "",
                "Error": "",
                "OutputMessage": "",
                "Percentage": 0,
                "TaskType": "SQLTask",
                "ProgressDetail": ""
            }
        ],
        "TotalCount": 1
    }
}
```

**Example 2: 任务列表展示**



Input: 

```
tccli dlc DescribeTasks --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "5b68c82f-d946-4ea9-8336-2f56ff5dd199",
        "TaskList": [],
        "TotalCount": 0
    }
}
```

