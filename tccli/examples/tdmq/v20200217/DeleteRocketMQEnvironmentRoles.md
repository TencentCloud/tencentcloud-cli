**Example 1: 删除环境角色授权**

删除环境角色授权

Input: 

```
tccli tdmq DeleteRocketMQEnvironmentRoles --cli-unfold-argument  \
    --EnvironmentId abc \
    --RoleNames abc \
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

