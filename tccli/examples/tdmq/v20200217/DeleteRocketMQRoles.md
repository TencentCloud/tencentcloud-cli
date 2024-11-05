**Example 1: 删除角色**



Input: 

```
tccli tdmq DeleteRocketMQRoles --cli-unfold-argument  \
    --RoleNames test_role_name \
    --ClusterId rocketmq-2p9vx3ax9jxg
```

Output: 
```
{
    "Response": {
        "RoleNames": [
            "test_role_name"
        ],
        "RequestId": "23ca1a58-0388-4d2d-8465-653a53addda7"
    }
}
```

