**Example 1: 查询用户组列表**



Input: 

```
tccli ciam ListUserGroups --cli-unfold-argument  \
    --UserStoreId 6cd22e51****************f6f7cb81 \
    --Pageable.PageSize 10 \
    --Pageable.PageNumber 5 \
    --Filters.0.Key condition \
    --Filters.0.Values 1 \
    --Filters.0.Logic True
```

Output: 
```
{
    "Response": {
        "Content": [
            {
                "UserGroupId": "6cd22e51****************f6f7cb81",
                "DisplayName": "用户组1",
                "Description": "包含了一组用户",
                "UserStoreId": "2c3aca3b****************a7efe88e",
                "TenantId": "tenantId",
                "CreatedDate": 1651073285427,
                "LastModifyDate": 1651073285306
            }
        ],
        "Total": 100,
        "Pageable": {
            "PageSize": 10,
            "PageNumber": 5
        },
        "RequestId": "e2e9e8aa********************9ab34c6e"
    }
}
```

