**Example 1: 创建RocketMQ环境角色授权**

创建RocketMQ环境角色授权

Input: 

```
tccli tdmq CreateRocketMQEnvironmentRole --cli-unfold-argument  \
    --EnvironmentId abc \
    --RoleName abc \
    --Permissions abc \
    --ClusterId abc
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

