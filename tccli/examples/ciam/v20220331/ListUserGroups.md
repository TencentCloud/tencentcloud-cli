**Example 1: 查询用户组列表**



Input: 

```
tccli ciam ListUserGroups --cli-unfold-argument  \
    --UserStoreId xx \
    --Pageable.PageNumber 0 \
    --Pageable.PageSize 0 \
    --Filters.0.Values xx \
    --Filters.0.Key xx \
    --Filters.0.Logic True
```

Output: 
```
{
    "Response": {
        "Content": [
            {
                "UserStoreId": "xx",
                "DisplayName": "xx",
                "Description": "xx",
                "UserGroupId": "xx",
                "TenantId": "xx"
            }
        ],
        "Total": 0,
        "Pageable": {
            "PageNumber": 0,
            "PageSize": 0
        },
        "RequestId": "xx"
    }
}
```

