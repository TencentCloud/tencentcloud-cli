**Example 1: 获取RocketMQ命名空间角色列表**

获取RocketMQ命名空间角色列表


Input: 

```
tccli tdmq DescribeRocketMQEnvironmentRoles --cli-unfold-argument  \
    --EnvironmentId abc \
    --Offset 0 \
    --Limit 0 \
    --ClusterId abc \
    --RoleName abc \
    --Filters.0.Name abc \
    --Filters.0.Values abc
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "EnvironmentRoleSets": [
            {
                "EnvironmentId": "abc",
                "RoleName": "abc",
                "Permissions": [
                    "abc"
                ],
                "RoleDescribe": "abc",
                "CreateTime": "2020-09-22 00:00:00",
                "UpdateTime": "2020-09-22 00:00:00"
            }
        ],
        "RequestId": "abc"
    }
}
```

