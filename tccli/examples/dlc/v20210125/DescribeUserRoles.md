**Example 1: test**



Input: 

```
tccli dlc DescribeUserRoles --cli-unfold-argument  \
    --Limit 0 \
    --Offset 0 \
    --Fuzzy roleName \
    --SortBy modify_time \
    --Sorting desc
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "UserRoles": [
            {
                "RoleId": 110,
                "AppId": "125****421",
                "Uin": "1000*****740",
                "Arn": "***roleName/***cos02",
                "ModifyTime": 0,
                "Desc": "test_arn",
                "RoleName": "NULL",
                "Creator": "1000*****356",
                "CosPermissionList": [
                    {
                        "CosPath": "cosn://***",
                        "Permissions": [
                            "read"
                        ]
                    }
                ],
                "PermissionJson": "deny"
            }
        ],
        "RequestId": "490e0b63-ae1a-4faf-a689-a5cde719cdc3"
    }
}
```

