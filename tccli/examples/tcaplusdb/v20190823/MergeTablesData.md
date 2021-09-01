**Example 1: 合并指定表格**



Input: 

```
tccli tcaplusdb MergeTablesData --cli-unfold-argument  \
    --IsOnlyCompare False \
    --SelectedTables.0.MergeTables.DstTableClusterId xx \
    --SelectedTables.0.MergeTables.DstTableName xx \
    --SelectedTables.0.MergeTables.SrcTableGroupId xx \
    --SelectedTables.0.MergeTables.SrcTableInstanceId xx \
    --SelectedTables.0.MergeTables.SrcTableName xx \
    --SelectedTables.0.MergeTables.SrcTableClusterId xx \
    --SelectedTables.0.MergeTables.DstTableGroupId xx \
    --SelectedTables.0.MergeTables.DstTableInstanceId xx \
    --SelectedTables.0.CheckIndex False
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

