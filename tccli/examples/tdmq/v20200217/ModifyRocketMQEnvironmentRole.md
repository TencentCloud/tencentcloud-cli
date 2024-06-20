**Example 1: 修改RocketMQ环境角色授权**

修改RocketMQ环境角色授权


Input: 

```
tccli tdmq ModifyRocketMQEnvironmentRole --cli-unfold-argument  \
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

