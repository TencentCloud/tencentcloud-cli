**Example 1: 获取RocketMQ命名空间角色列表**



Input: 

```
tccli tdmq DescribeRocketMQEnvironmentRoles --cli-unfold-argument  \
    --EnvironmentId test_ns \
    --Offset 0 \
    --Limit 20 \
    --ClusterId rocketmq-2p9vx3ax9jxg \
    --RoleName test_role
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "EnvironmentRoleSets": [
            {
                "EnvironmentId": "test_ns",
                "RoleName": "test_role",
                "Permissions": [
                    "produce"
                ],
                "RoleDescribe": "测试角色",
                "CreateTime": "2020-09-22 00:00:00",
                "UpdateTime": "2020-09-22 00:00:00"
            }
        ],
        "RequestId": "23ca1a58-0388-4d2d-8465-653a53addda7"
    }
}
```

