**Example 1: 获取角色列表**



Input: 

```
tccli tdmq DescribeRocketMQRoles --cli-unfold-argument  \
    --RoleName test_role_name \
    --Offset 0 \
    --Limit 20 \
    --ClusterId rocketmq-2p9vx3ax9jxg \
    --Filters.0.Name RoleName \
    --Filters.0.Values test_role_name
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RoleSets": [
            {
                "RoleName": "test_role_name",
                "Token": "eyJrZXlJZCI6InN1bmdvxxxxx0X3JvbGVfMyJ9.dbHR8m6gc4L4vZUrodhW_O9bDulZQ6lraNswNLtcUcY",
                "Remark": "测试角色",
                "CreateTime": "2020-09-22 00:00:00",
                "UpdateTime": "2020-09-22 00:00:00"
            }
        ],
        "RequestId": "23ca1a58-0388-4d2d-8465-653a53addda7"
    }
}
```

