**Example 1: 恢复回收站中的表**

根据指定的表信息，恢复回收站中的表

Input: 

```
tccli tcaplusdb RecoverRecycleTables --cli-unfold-argument  \
    --ClusterId 5674209986 \
    --SelectedTables.0.TableIdlType xx \
    --SelectedTables.0.TableGroupId 101 \
    --SelectedTables.0.FileExtType xx \
    --SelectedTables.0.TableInstanceId tcaplus-1f224454 \
    --SelectedTables.0.Memo xx \
    --SelectedTables.0.TableName tb_example \
    --SelectedTables.0.ReservedReadQps 0 \
    --SelectedTables.0.ListElementNum 0 \
    --SelectedTables.0.ReservedVolume 0 \
    --SelectedTables.0.ReservedWriteQps 0 \
    --SelectedTables.0.FileSize 0 \
    --SelectedTables.0.FileContent xx \
    --SelectedTables.0.FileName xx \
    --SelectedTables.0.TableType xx
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

