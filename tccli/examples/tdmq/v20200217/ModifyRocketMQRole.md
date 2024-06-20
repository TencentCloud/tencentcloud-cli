**Example 1: RocketMQ角色修改**

RocketMQ角色修改


Input: 

```
tccli tdmq ModifyRocketMQRole --cli-unfold-argument  \
    --RoleName abc \
    --Remark abc \
    --ClusterId abc
```

Output: 
```
{
    "Response": {
        "RoleName": "abc",
        "Remark": "abc",
        "RequestId": "abc"
    }
}
```

