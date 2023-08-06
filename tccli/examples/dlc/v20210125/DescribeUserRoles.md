**Example 1: 列举用户角色信息**



Input: 

```
tccli dlc DescribeUserRoles --cli-unfold-argument  \
    --Fuzzy 1 \
    --Limit 0 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "UserRoles": [
            {
                "RoleId": 0,
                "AppId": "1234",
                "Uin": "1234",
                "ModifyTime": 1650424290,
                "Arn": "11",
                "Desc": "test role"
            }
        ],
        "RequestId": "2ae4707a-9f72-44aa-9fd4-65cb739d6301"
    }
}
```

**Example 2: test**



Input: 

```
tccli dlc DescribeUserRoles --cli-unfold-argument  \
    --Limit 0 \
    --Offset 0 \
    --Fuzzy abc \
    --SortBy abc \
    --Sorting abc
```

Output: 
```
{
    "Response": {
        "Total": 0,
        "UserRoles": [
            {
                "RoleId": 0,
                "AppId": "abc",
                "Uin": "abc",
                "Arn": "abc",
                "ModifyTime": 0,
                "Desc": "abc",
                "RoleName": "abc",
                "Creator": "abc",
                "CosPermissionList": [
                    {
                        "CosPath": "abc",
                        "Permissions": [
                            "abc"
                        ]
                    }
                ],
                "PermissionJson": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

