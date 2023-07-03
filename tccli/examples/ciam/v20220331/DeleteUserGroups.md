**Example 1: 批量删除用户组**



Input: 

```
tccli ciam DeleteUserGroups --cli-unfold-argument  \
    --UserGroupIds xxx \
    --UserStoreId xxx
```

Output: 
```
{
    "Response": {
        "UserGroupDeletedInfo": {
            "AppAssociatedUserGroupIds": [
                {
                    "ApplicationName": "xx",
                    "ApplicationId": "xx",
                    "UserGroupId": "xx"
                }
            ]
        },
        "RequestId": "xx"
    }
}
```

