**Example 1: 获取表格标签**

获取表格标签

Input: 

```
tccli tcaplusdb DescribeTableTags --cli-unfold-argument  \
    --ClusterId 5674209986 \
    --SelectedTables.0.TableInstanceId tcaplus-0xm12ck1 \
    --SelectedTables.0.TableGroupId 1 \
    --SelectedTables.0.TableName tb_test
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "Rows": [
            {
                "TableInstanceId": "abc",
                "TableName": "abc",
                "TableGroupId": "abc",
                "Tags": [
                    {
                        "TagKey": "abc",
                        "TagValue": "abc"
                    }
                ],
                "Error": {
                    "Code": "abc",
                    "Message": "abc"
                }
            }
        ],
        "RequestId": "abc"
    }
}
```

