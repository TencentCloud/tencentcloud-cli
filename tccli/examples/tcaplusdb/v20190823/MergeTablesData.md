**Example 1: 合并指定表格**

合并指定表格

Input: 

```
tccli tcaplusdb MergeTablesData --cli-unfold-argument  \
    --SelectedTables.0.MergeTables.SrcTableClusterId abc \
    --SelectedTables.0.MergeTables.SrcTableGroupId abc \
    --SelectedTables.0.MergeTables.SrcTableName abc \
    --SelectedTables.0.MergeTables.DstTableClusterId abc \
    --SelectedTables.0.MergeTables.DstTableGroupId abc \
    --SelectedTables.0.MergeTables.DstTableName abc \
    --SelectedTables.0.MergeTables.SrcTableInstanceId abc \
    --SelectedTables.0.MergeTables.DstTableInstanceId abc \
    --SelectedTables.0.CheckIndex True \
    --IsOnlyCompare True
```

Output: 
```
{
    "Response": {
        "RequestId": "fdsfdsfdsfdsf",
        "Results": [
            {
                "ApplicationId": null,
                "Error": null,
                "Table": {
                    "DstTableClusterId": "3",
                    "DstTableGroupId": "2",
                    "DstTableInstanceId": "tcaplus-83c6c2d8",
                    "DstTableName": "cl_list_2",
                    "SrcTableClusterId": "3",
                    "SrcTableGroupId": "1",
                    "SrcTableInstanceId": "tcaplus-0b2c635d",
                    "SrcTableName": "cl_list"
                },
                "TaskId": "3-418"
            }
        ]
    }
}
```

