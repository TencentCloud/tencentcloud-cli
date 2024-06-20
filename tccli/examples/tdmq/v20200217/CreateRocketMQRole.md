**Example 1: 创建RocketMQ角色**

创建RocketMQ角色


Input: 

```
tccli tdmq CreateRocketMQRole --cli-unfold-argument  \
    --RoleName abc \
    --Remark abc \
    --ClusterId abc
```

Output: 
```
{
    "Response": {
        "RoleName": "abc",
        "Token": "abc",
        "Remark": "abc",
        "RequestId": "abc"
    }
}
```

