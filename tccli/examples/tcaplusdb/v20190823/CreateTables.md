**Example 1: 批量创建表**

批量创建表

Input: 

```
tccli tcaplusdb CreateTables --cli-unfold-argument  \
    --ResourceTags.0.TagKey xx \
    --ResourceTags.0.TagValue xx \
    --ClusterId 22762983670 \
    --IdlFiles.0.FileExtType proto \
    --IdlFiles.0.FileType PROTO \
    --IdlFiles.0.FileName table_test_2_modify \
    --IdlFiles.0.FileSize 0 \
    --IdlFiles.0.FileContent xx \
    --IdlFiles.0.FileId 0 \
    --SelectedTables.0.TableIdlType PROTO \
    --SelectedTables.0.TableGroupId 2 \
    --SelectedTables.0.FileExtType xx \
    --SelectedTables.0.TableInstanceId xx \
    --SelectedTables.0.Memo test \
    --SelectedTables.0.TableName PLAYERONLINECNT \
    --SelectedTables.0.ReservedReadQps 0 \
    --SelectedTables.0.ListElementNum 0 \
    --SelectedTables.0.ReservedVolume 0 \
    --SelectedTables.0.ReservedWriteQps 0 \
    --SelectedTables.0.FileSize 0 \
    --SelectedTables.0.FileContent xx \
    --SelectedTables.0.FileName xx \
    --SelectedTables.0.TableType GENERIC
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "TableResults": [
            {
                "TableIdlType": "TDR",
                "TableInstanceId": "tcaplus-c6187008",
                "TableName": "PLAYERONLINECNT",
                "TableGroupId": "2",
                "TaskId": "22762983670-144",
                "TableType": "GENERIC"
            }
        ],
        "RequestId": "8cEcE3E8-2fE2-6d4b-5E34-Fdc01E35f2C6"
    }
}
```

