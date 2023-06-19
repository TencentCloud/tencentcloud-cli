**Example 1: 设置表格分布式索引**

设置表格分布式索引

Input: 

```
tccli tcaplusdb SetTableIndex --cli-unfold-argument  \
    --ClusterId 5674209986 \
    --SelectedTables.0.TableInstanceId tcaplus-1f224454 \
    --SelectedTables.0.TableGroupId 101 \
    --SelectedTables.0.TableName tb_example \
    --SelectedTables.0.TableIdlType PROTO \
    --SelectedTables.0.TableType GENERIC \
    --SelectedTables.0.ShardNum 3 \
    --SelectedTables.0.SelectedFields.0.FieldName name \
    --SelectedTables.0.SelectedFields.0.IsPrimaryKey Yes \
    --SelectedTables.0.SelectedFields.0.FieldType string \
    --SelectedTables.0.SelectedFields.0.FieldSize 64 \
    --SelectedTables.0.SelectedFields.1.FieldName id \
    --SelectedTables.0.SelectedFields.1.IsPrimaryKey No \
    --SelectedTables.0.SelectedFields.1.FieldType int32 \
    --SelectedTables.0.SelectedFields.1.FieldSize 4
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "TableResults": [
            {
                "TableInstanceId": "abc",
                "TaskId": "abc",
                "TableName": "abc",
                "TableType": "abc",
                "TableIdlType": "abc",
                "TableGroupId": "abc",
                "Error": {
                    "Code": "abc",
                    "Message": "abc"
                },
                "TaskIds": [
                    "abc"
                ],
                "ApplicationId": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

