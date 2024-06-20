**Example 1: 获取RocketMQ角色列表**

获取RocketMQ角色列表


Input: 

```
tccli tdmq DescribeRocketMQRoles --cli-unfold-argument  \
    --RoleName abc \
    --Offset 0 \
    --Limit 0 \
    --ClusterId abc \
    --Filters.0.Name abc \
    --Filters.0.Values abc
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "RoleSets": [
            {
                "RoleName": "abc",
                "Token": "abc",
                "Remark": "abc",
                "CreateTime": "2020-09-22 00:00:00",
                "UpdateTime": "2020-09-22 00:00:00"
            }
        ],
        "RequestId": "abc"
    }
}
```

