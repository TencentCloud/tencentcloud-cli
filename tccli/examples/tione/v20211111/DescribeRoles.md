**Example 1: 查询角色列表**



Input: 

```
tccli tione DescribeRoles --cli-unfold-argument  \
    --TiProjectId 1889353273052233728
```

Output: 
```
{
    "Response": {
        "RequestId": "eb976db7-c2ad-40d9-b1f1-407887eeab4b",
        "Roles": [
            {
                "CreateTime": "",
                "Description": "",
                "RoleId": "admin",
                "RoleName": "管理员",
                "RoleType": "SYSTEM",
                "UserCount": 0
            },
            {
                "CreateTime": "",
                "Description": "",
                "RoleId": "developer",
                "RoleName": "开发人员",
                "RoleType": "SYSTEM",
                "UserCount": 0
            },
            {
                "CreateTime": "2025-12-04T19:50:50+08",
                "Description": "",
                "RoleId": "role-1467545446382887168",
                "RoleName": "test_数据权限",
                "RoleType": "CUSTOM",
                "UserCount": 0
            }
        ],
        "TotalCount": 3
    }
}
```

