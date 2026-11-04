**Example 1: 查询角色绑定的用户**



Input: 

```
tccli tione DescribeRoleUsers --cli-unfold-argument  \
    --RoleId admin \
    --TiProjectId 1889353273052233728
```

Output: 
```
{
    "Response": {
        "RequestId": "cdc6790f-7e17-474d-89ef-994642f721e7",
        "TotalCount": 2,
        "Users": [
            {
                "CreateTime": "",
                "NickName": "user1",
                "Roles": [],
                "SubUin": "100038358153"
            },
            {
                "CreateTime": "",
                "NickName": "user2",
                "Roles": [],
                "SubUin": "100040160851"
            }
        ]
    }
}
```

