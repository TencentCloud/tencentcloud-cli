**Example 1: 创建角色**



Input: 

```
tccli tdmq CreateRocketMQRole --cli-unfold-argument  \
    --RoleName test_role_name \
    --Remark 测试角色 \
    --ClusterId rocketmq-2p9vx3ax9jxg
```

Output: 
```
{
    "Response": {
        "RoleName": "test_role_name",
        "Token": "eyJrZXlJZCI6InN1bmdvxxxxx0X3JvbGVfMyJ9.dbHR8m6gc4L4vZUrodhW_O9bDulZQ6lraNswNLtcUcY",
        "Remark": "测试角色",
        "RequestId": "23ca1a58-0388-4d2d-8465-653a53addda7"
    }
}
```

