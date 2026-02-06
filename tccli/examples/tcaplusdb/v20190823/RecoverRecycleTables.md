**Example 1: 恢复回收站中的表**

根据指定的表信息，恢复回收站中的表

Input: 

```
tccli tcaplusdb RecoverRecycleTables --cli-unfold-argument  \
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
                "TableInstanceId": "tcaplus-1f224454",
                "TaskId": "124153",
                "TableName": "abc",
                "TableType": "abc",
                "TableIdlType": "2",
                "TableGroupId": "23153",
                "Error": {
                    "Code": "",
                    "Message": ""
                },
                "TaskIds": [
                    "32626"
                ],
                "ApplicationId": "21252"
            }
        ],
        "RequestId": "154331"
    }
}
```

