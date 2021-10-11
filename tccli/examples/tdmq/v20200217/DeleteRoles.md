**Example 1: 删除角色**



Input: 

```
tccli tdmq DeleteRoles --cli-unfold-argument  \
    --RoleNames test_role_1 test_role_2
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

