**Example 1: 修改表格标签**

修改表格标签

Input: 

```
tccli tcaplusdb ModifyTableTags --cli-unfold-argument  \
    --ClusterId 5674209986 \
    --SelectedTables.0.TableInstanceId tcaplus-0xm12ck1 \
    --SelectedTables.0.TableGroupId 1 \
    --SelectedTables.0.TableName tb_test \
    --ReplaceTags.0.TagKey test1 \
    --ReplaceTags.0.TagValue value1 \
    --DeleteTags.0.TagKey delete1
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

