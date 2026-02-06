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
                "TableInstanceId": "tcaplus-0xm12ck1",
                "TableName": "tb_test",
                "TableGroupId": "1",
                "Tags": [
                    {
                        "TagKey": "tkey",
                        "TagValue": "tvalue"
                    }
                ],
                "Error": {
                    "Code": "",
                    "Message": ""
                }
            }
        ],
        "RequestId": "1921341-214214"
    }
}
```

