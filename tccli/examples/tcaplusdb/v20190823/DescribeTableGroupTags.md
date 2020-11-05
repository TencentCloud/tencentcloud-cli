**Example 1: Obtaining the list of tags associated with a table group**

This example shows you how to obtain the list of tags associated with a table group.

Input: 

```
tccli tcaplusdb DescribeTableGroupTags --cli-unfold-argument  \
    --ClusterId 5674209986\
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

