**Example 1: 创建RocketMQ环境角色授权**



Input: 

```
tccli tdmq CreateRocketMQEnvironmentRole --cli-unfold-argument  \
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

