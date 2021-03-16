**Example 1: 修改表格标签**

修改表格标签

Input: 

```
tccli tcaplusdb ModifyTableTags --cli-unfold-argument  \
    --ReplaceTags.0.TagKey test1 \
    --ReplaceTags.0.TagValue value1 \
    --DeleteTags.0.TagKey delete1 \
    --DeleteTags.0.TagValue xx \
    --ClusterId 5674209986 \
    --SelectedTables.0.TableIdlType xx \
    --SelectedTables.0.TableGroupId 1 \
    --SelectedTables.0.FileExtType xx \
    --SelectedTables.0.TableInstanceId tcaplus-0xm12ck1 \
    --SelectedTables.0.Memo xx \
    --SelectedTables.0.TableName tb_test \
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
        "RequestId": "abd7111a-62d4-4bbb-a781-3646040e9530",
        "TotalCount": 1,
        "TableResults": [
            {
                "TableInstanceId": "tcaplus-0xm12ck1",
                "TableGroupId": "1",
                "TableName": "tb_test",
                "TaskId": "5674209986-1212"
            }
        ]
    }
}
```

