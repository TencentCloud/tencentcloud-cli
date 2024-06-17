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
        "Rows": [
            {
                "ClusterId": "abc",
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
        "TotalCount": 0,
        "RequestId": "abc"
    }
}
```

