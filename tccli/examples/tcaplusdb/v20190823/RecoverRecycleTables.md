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
        "RequestId": "f19ec9d8-ecd6-41f2-9da1-712dfdbe9ef7",
        "TableResults": [
            {
                "Error": null,
                "TableGroupId": "101",
                "TableIdlType": null,
                "TableInstanceId": "tcaplus-1f224454",
                "TableName": "tb_example",
                "TableType": null,
                "TaskId": "5674209986-1198",
                "TaskIds": null
            }
        ],
        "TotalCount": 1
    }
}
```

