**Example 1: 创建角色**

创建角色

Input: 

```
tccli tdmq CreateRole --cli-unfold-argument  \
    --RoleName test_role_123 \
    --Remark 创建角色
```

Output: 
```
{
    "Response": {
        "RoleName": "abc",
        "Token": "abc",
        "Remark": "abc",
        "EnvironmentRoleSets": [
            {
                "EnvironmentId": "abc",
                "Permissions": [
                    "abc"
                ]
            }
        ],
        "RequestId": "abc"
    }
}
```

