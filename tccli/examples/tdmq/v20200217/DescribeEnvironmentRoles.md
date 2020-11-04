**Example 1: 获取环境角色列表**



Input: 

```
tccli tdmq DescribeEnvironmentRoles --cli-unfold-argument  \
    --EnvironmentId default
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "EnvironmentRoleSets": [
            {
                "EnvironmentId": "default",
                "RoleName": "test_role",
                "Permissions": [
                    "produce",
                    "consume"
                ],
                "RoleDescribe": "Remark1",
                "CreateTime": "2020-08-03 19:46:37",
                "UpdateTime": "2020-08-04 15:59:29"
            }
        ],
        "RequestId": "gggxxxx"
    }
}
```

