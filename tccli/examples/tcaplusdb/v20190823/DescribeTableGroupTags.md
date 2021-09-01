**Example 1: 获取表格组关联的标签列表**

获取表格组关联的标签列表

Input: 

```
tccli tcaplusdb DescribeTableGroupTags --cli-unfold-argument  \
    --ClusterId 5674209986 \
    --TableGroupIds 1
```

Output: 
```
{
    "Response": {
        "RequestId": "abd7111a-62d4-4bbb-a781-3646040e9530",
        "TotalCount": 1,
        "Rows": [
            {
                "ClusterId": "5674209986",
                "TableGroupId": "1",
                "Tags": {
                    "TagKey": "test1",
                    "TagValue": "value1"
                }
            }
        ]
    }
}
```

