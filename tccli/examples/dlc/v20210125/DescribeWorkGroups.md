**Example 1: 获取工作组列表**



Input: 

```
tccli dlc DescribeWorkGroups --cli-unfold-argument  \
    --Sorting xx \
    --WorkGroupId 0 \
    --Limit 0 \
    --SortBy xx \
    --Filters.0.Values xx \
    --Filters.0.Name xx \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "WorkGroupSet": [
            {
                "PolicySet": [
                    {
                        "Table": "xx",
                        "Catalog": "xx",
                        "Operation": "xx",
                        "Database": "xx"
                    }
                ],
                "WorkGroupId": 0,
                "Creator": "xx",
                "UserNum": 0,
                "WorkGroupDescription": "xx",
                "WorkGroupName": "xx",
                "UserSet": [
                    {
                        "UserDescription": "xx",
                        "UserId": "xx",
                        "CreateTime": "xx",
                        "Creator": "xx"
                    }
                ],
                "CreateTime": "xx"
            }
        ],
        "TotalCount": 0,
        "RequestId": "xx"
    }
}
```

