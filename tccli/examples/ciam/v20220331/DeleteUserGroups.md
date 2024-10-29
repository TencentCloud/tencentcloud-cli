**Example 1: 批量删除用户组**



Input: 

```
tccli ciam DeleteUserGroups --cli-unfold-argument  \
    --UserGroupIds 6cd22e51****************f6f7cb81 \
    --UserStoreId 2c3aca3b****************a7efe88e
```

Output: 
```
{
    "Response": {
        "UserGroupDeletedInfo": {
            "ErrorMessage": "error message",
            "AppAssociatedUserGroupIds": [
                {
                    "UserGroupId": "6cd22e51****************f6f7cb81",
                    "ApplicationId": "17c29b8c****************c0228c48",
                    "ApplicationName": "应用1"
                }
            ]
        },
        "RequestId": "e2e9e8aa********************9ab34c6e"
    }
}
```

