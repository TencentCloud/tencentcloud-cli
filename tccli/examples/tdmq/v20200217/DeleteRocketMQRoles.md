**Example 1: 删除角色**

删除角色

Input: 

```
tccli tdmq DeleteRocketMQRoles --cli-unfold-argument  \
    --RoleNames abc \
    --ClusterId abc
```

Output: 
```
{
    "Response": {
        "RoleNames": [
            "abc"
        ],
        "RequestId": "abc"
    }
}
```

