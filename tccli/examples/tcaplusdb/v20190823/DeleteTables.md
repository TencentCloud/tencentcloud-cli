**Example 1: 删除表**

删除表

Input: 

```
tccli tcaplusdb DeleteTables --cli-unfold-argument  \
    --ClusterId 5674209986 \
    --SelectedTables.0.TableInstanceId tcaplus-1f224454 \
    --SelectedTables.0.TableGroupId 101 \
    --SelectedTables.0.TableName tb_example
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "TableResults": [
            {
                "TableInstanceId": "56755",
                "TaskId": "5675",
                "TableName": "abc",
                "TableType": "1",
                "TableIdlType": "1",
                "TableGroupId": "23121",
                "Error": {
                    "Code": "",
                    "Message": ""
                },
                "TaskIds": [
                    "657567"
                ],
                "ApplicationId": "57657"
            }
        ],
        "RequestId": "576567"
    }
}
```

