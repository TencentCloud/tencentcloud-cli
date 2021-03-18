**Example 1: 查询任务列表**



Input: 

```
tccli dlc DescribeTasks --cli-unfold-argument  \
    --Limit 1 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "TaskList": [
            {
                "DataSet": "xx",
                "Id": "xx",
                "DatabaseName": "xx",
                "OutputMessage": "xx",
                "SQL": "xx",
                "ResultExpired": true,
                "OutputPath": "xx",
                "State": 0,
                "UsedTime": 0,
                "DataAmount": 0,
                "Error": "xx",
                "Percentage": 0,
                "SQLType": "xx",
                "CreateTime": "xx",
                "RowAffectInfo": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

