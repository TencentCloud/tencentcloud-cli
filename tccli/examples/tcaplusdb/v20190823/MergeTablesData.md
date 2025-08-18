**Example 1: 合并指定表格**

合并指定表格

Input: 

```
tccli tcaplusdb MergeTablesData --cli-unfold-argument  \
    --SelectedTables.0.MergeTables.SrcTableClusterId 192342 \
    --SelectedTables.0.MergeTables.SrcTableGroupId 1 \
    --SelectedTables.0.MergeTables.SrcTableName srcname \
    --SelectedTables.0.MergeTables.DstTableClusterId 192342 \
    --SelectedTables.0.MergeTables.DstTableGroupId 2 \
    --SelectedTables.0.MergeTables.DstTableName dstname \
    --SelectedTables.0.MergeTables.SrcTableInstanceId tcaplus-13212 \
    --SelectedTables.0.MergeTables.DstTableInstanceId tcaplus-19432 \
    --SelectedTables.0.CheckIndex True \
    --IsOnlyCompare True
```

Output: 
```
{
    "Response": {
        "Results": [
            {
                "TaskId": "125124",
                "Error": {
                    "Code": "",
                    "Message": ""
                },
                "Table": {
                    "SrcTableClusterId": "192342",
                    "SrcTableGroupId": "1",
                    "SrcTableName": "srcname",
                    "DstTableClusterId": "192342",
                    "DstTableGroupId": "2",
                    "DstTableName": "dstname",
                    "SrcTableInstanceId": "tcaplus-13212",
                    "DstTableInstanceId": "tcaplus-19432"
                },
                "ApplicationId": "3232"
            }
        ],
        "RequestId": "193232-122313"
    }
}
```

