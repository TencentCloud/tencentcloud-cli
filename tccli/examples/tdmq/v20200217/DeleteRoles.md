**Example 1: 删除角色**



Input: 

```
tccli tdmq DeleteRoles --cli-unfold-argument  \
    --RoleNames test_role_1 \
    --ClusterId pulsar-xk3ne8k2qkp8
```

Output: 
```
{
    "Response": {
        "RoleNames": [
            "test_role_1"
        ],
        "RequestId": "1004f1de-6fb8-41d5-965e-3aae8c87183a"
    }
}
```

