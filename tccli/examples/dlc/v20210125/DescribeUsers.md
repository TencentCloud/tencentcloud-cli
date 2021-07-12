**Example 1: 获取用户列表信息**



Input: 

```
tccli dlc DescribeUsers --cli-unfold-argument  \
    --Limit 0 \
    --Sorting xx \
    --UserId xx \
    --SortBy xx \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "UserSet": [
            {
                "Creator": "xx",
                "PolicySet": [
                    {
                        "Table": "xx",
                        "Catalog": "xx",
                        "Operation": "xx",
                        "Database": "xx"
                    }
                ],
                "UserId": "xx",
                "IsOwner": true,
                "UserDescription": "xx",
                "WorkGroupSet": [
                    {
                        "WorkGroupId": 0,
                        "WorkGroupName": "xx",
                        "CreateTime": "xx",
                        "WorkGroupDescription": "xx",
                        "Creator": "xx"
                    }
                ],
                "CreateTime": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

