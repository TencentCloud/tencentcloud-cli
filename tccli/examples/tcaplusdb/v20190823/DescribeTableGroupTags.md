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
                "ClusterId": "1989787",
                "TableGroupId": "18743",
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
        "TotalCount": 0,
        "RequestId": "198232-12431"
    }
}
```

