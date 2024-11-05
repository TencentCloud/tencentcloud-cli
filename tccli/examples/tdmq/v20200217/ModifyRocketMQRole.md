**Example 1: 修改角色**



Input: 

```
tccli tdmq ModifyRocketMQRole --cli-unfold-argument  \
    --RoleName test_role_name \
    --Remark 修改角色 \
    --ClusterId rocketmq-2p9vx3ax9jxg
```

Output: 
```
{
    "Response": {
        "RoleName": "test_role_name",
        "Remark": "修改角色",
        "RequestId": "23ca1a58-0388-4d2d-8465-653a53addda7"
    }
}
```

