**Example 1: 删除表**

删除表

Input: 

```
tccli tcaplusdb DeleteTables --cli-unfold-argument  \
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
        "RequestId": "ebc273d5-d56c-4c54-ad19-9b5a25815eed",
        "TableResults": [
            {
                "Error": null,
                "TableGroupId": "101",
                "TableIdlType": null,
                "TableInstanceId": "tcaplus-1f224454",
                "TableName": "tb_example",
                "TableType": null,
                "TaskId": "5674209986-1180",
                "TaskIds": null
            }
        ],
        "TotalCount": 1
    }
}
```

