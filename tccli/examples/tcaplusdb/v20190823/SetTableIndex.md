**Example 1: 设置表格分布式索引**

设置表格分布式索引

Input: 

```
tccli tcaplusdb SetTableIndex --cli-unfold-argument  \
    --ClusterId 5674209986 \
    --SelectedTables.0.ShardNum 1 \
    --SelectedTables.0.TableIdlType PROTO \
    --SelectedTables.0.TableGroupId 101 \
    --SelectedTables.0.TableInstanceId tcaplus-1f224454 \
    --SelectedTables.0.TableName tb_example \
    --SelectedTables.0.TableType GENERIC \
    --SelectedTables.0.SelectedFields.0.IsPrimaryKey No \
    --SelectedTables.0.SelectedFields.0.FieldName id \
    --SelectedTables.0.SelectedFields.0.FieldType int32 \
    --SelectedTables.0.SelectedFields.0.FieldSize 0 \
    --SelectedTables.0.SelectedFields.1.IsPrimaryKey Yes \
    --SelectedTables.0.SelectedFields.1.FieldName name \
    --SelectedTables.0.SelectedFields.1.FieldType string \
    --SelectedTables.0.SelectedFields.1.FieldSize 0
```

Output: 
```
{
    "Response": {
        "RequestId": "122bb375-7464-4536-a3c5-8ddbdd6f4ce4",
        "TableResults": [
            {
                "Error": null,
                "TableGroupId": "101",
                "TableIdlType": null,
                "TableInstanceId": "tcaplus-1f224454",
                "TableName": "tb_example",
                "TableType": null,
                "TaskId": "5674209986-1199",
                "TaskIds": null
            }
        ],
        "TotalCount": 1
    }
}
```

