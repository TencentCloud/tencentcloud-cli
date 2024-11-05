**Example 1: 修改RocketMQ环境角色授权**



Input: 

```
tccli tdmq ModifyRocketMQEnvironmentRole --cli-unfold-argument  \
    --EnvironmentId test_namespace \
    --RoleName test_role_name \
    --Permissions produce \
    --ClusterId rocketmq-2p9vx3ax9jxg
```

Output: 
```
{
    "Response": {
        "RequestId": "23ca1a58-0388-4d2d-8465-653a53addda7"
    }
}
```

