**Example 1: 获取表格标签**

获取表格标签

Input: 

```
tccli tcaplusdb DescribeTableTags --cli-unfold-argument  \
    --ClusterId 5674209986\
    --SelectedTables.0.TableInstanceId tcaplus-0xm12ck1\
    --SelectedTables.0.TableGroupId 1\
    --SelectedTables.0.TableName tb_test
```

Output: 
```
{
    "Response": {
        "RequestId": "abd7111a-62d4-4bbb-a781-3646040e9530",
        "TotalCount": 1,
        "Rows": [
            {
                "TableInstanceId": "tcaplus-0xm12ck1",
                "TableGroupId": "1",
                "TableName": "tb_test",
                "Tags": {
                    "TagKey": "test1",
                    "TagValue": "value1"
                }
            }
        ]
    }
}
```

