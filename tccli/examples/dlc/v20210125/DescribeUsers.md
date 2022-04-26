**Example 1: 获取用户列表信息**



Input: 

```
tccli dlc DescribeUsers --cli-unfold-argument  \
    --Limit 10 \
    --Sorting create-time \
    --UserId 1248065439 \
    --SortBy desc \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "UserSet": [
            {
                "Creator": "1248065439",
                "PolicySet": [
                    {
                        "Table": "TableName",
                        "Catalog": "COSDataCatalog",
                        "Operation": "ALL",
                        "Database": "DatabaseName"
                    }
                ],
                "UserId": "1248065439",
                "UserType": "ADMIN",
                "UserAlias": "xxxname",
                "IsOwner": true,
                "UserDescription": "Test User",
                "WorkGroupSet": [
                    {
                        "WorkGroupId": 0,
                        "WorkGroupName": "Group1",
                        "CreateTime": "2021-07-28 16:19:32",
                        "WorkGroupDescription": "test group",
                        "Creator": "1248065439"
                    }
                ],
                "CreateTime": "2021-07-28 16:19:32"
            }
        ],
        "RequestId": "1287310-badou889lodj-1231jk12"
    }
}
```

