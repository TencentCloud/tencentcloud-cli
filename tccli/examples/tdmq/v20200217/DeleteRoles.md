**Example 1: 删除角色**



Input: 

```
tccli tdmq DeleteRoles --cli-unfold-argument  \
    --RoleNames abc \
    --ClusterId abc
```

Output: 
```
{
    "Response": {
        "RoleNames": [
            "test_role_1",
            "test_role_2"
        ],
        "RequestId": "gggxxxx"
    }
}
```

