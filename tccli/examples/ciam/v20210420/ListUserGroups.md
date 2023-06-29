**Example 1: 示例1**



Input: 

```
tccli ciam ListUserGroups --cli-unfold-argument  \
    --UserStoreId xx \
    --Page 0 \
    --Condition xx \
    --Size 10
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

