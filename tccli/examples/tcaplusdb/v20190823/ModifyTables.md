**Example 1: 修改表结构**

修改表结构

Input: 

```
tccli tcaplusdb ModifyTables --cli-unfold-argument  \
    --ClusterId 5674209986 \
    --IdlFiles.0.FileExtType proto \
    --IdlFiles.0.FileType PROTO \
    --IdlFiles.0.FileName tb_example_modify \
    --IdlFiles.0.FileSize 0 \
    --IdlFiles.0.FileContent xx \
    --IdlFiles.0.FileId 0 \
    --SelectedTables.0.TableIdlType PROTO \
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
        "RequestId": "007a279d-fd19-452c-842e-46a804e8564b",
        "TableResults": [
            {
                "Error": null,
                "TableGroupId": "101",
                "TableIdlType": "PROTO",
                "TableInstanceId": "tcaplus-1f224454",
                "TableName": "tb_example",
                "TableType": "GENERIC",
                "TaskId": "5674209986-1200",
                "TaskIds": null
            }
        ],
        "TotalCount": 1
    }
}
```

