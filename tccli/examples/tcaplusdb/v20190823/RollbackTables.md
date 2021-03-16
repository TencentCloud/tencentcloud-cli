**Example 1: 表格按主键回档**

表格按主键回档

Input: 

```
tccli tcaplusdb RollbackTables --cli-unfold-argument  \
    --RollbackTime 2019-08-29 10:00:00 \
    --ClusterId 5674209986 \
    --Mode xx \
    --SelectedTables.0.TableIdlType PROTO \
    --SelectedTables.0.TableGroupId 101 \
    --SelectedTables.0.FileExtType txt \
    --SelectedTables.0.TableInstanceId tcaplus-1f224454 \
    --SelectedTables.0.Memo xx \
    --SelectedTables.0.TableName tb_example \
    --SelectedTables.0.ReservedReadQps 0 \
    --SelectedTables.0.ListElementNum 0 \
    --SelectedTables.0.ReservedVolume 0 \
    --SelectedTables.0.ReservedWriteQps 0 \
    --SelectedTables.0.FileSize 0 \
    --SelectedTables.0.FileContent uin%20name%0A1%20calvin%0A2%20jacob%0A3%20matthew%0A%0A \
    --SelectedTables.0.FileName tb_example_key1 \
    --SelectedTables.0.TableType xx
```

Output: 
```
{
    "Response": {
        "RequestId": "128a5622-0de1-41ed-9850-483944f11370",
        "TableResults": [
            {
                "Error": null,
                "FileId": "604",
                "TableGroupId": "101",
                "SuccKeyNum": 3,
                "TableIdlType": "PROTO",
                "TableInstanceId": "tcaplus-1f224454",
                "TableName": "tb_example",
                "TableType": null,
                "TaskId": "5674209986-1212",
                "TaskIds": null,
                "TotalKeyNum": 3
            }
        ],
        "TotalCount": 1
    }
}
```

