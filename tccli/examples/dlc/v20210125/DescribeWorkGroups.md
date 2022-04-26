**Example 1: 获取工作组列表**



Input: 

```
tccli dlc DescribeWorkGroups --cli-unfold-argument  \
    --Sorting desc \
    --WorkGroupId 1 \
    --Limit 0 \
    --SortBy create-time \
    --Filters.0.Values workgroup-name \
    --Filters.0.Name Group1 \
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
                        "Table": "TableName",
                        "Catalog": "COSDataCatalog",
                        "Operation": "ALL",
                        "Database": "DatabaseName"
                    }
                ],
                "WorkGroupId": 1,
                "Creator": "1248065439",
                "UserNum": 1,
                "WorkGroupDescription": "test group",
                "WorkGroupName": "Group1",
                "UserSet": [
                    {
                        "UserDescription": "test user",
                        "UserAlias": "testname",
                        "UserId": "1248065439",
                        "CreateTime": "2021-07-28 16:19:32",
                        "Creator": "1248065439"
                    }
                ],
                "CreateTime": "2021-07-28 16:19:32"
            }
        ],
        "TotalCount": 1,
        "RequestId": "1287310-badou889lodj-1231jk12"
    }
}
```

