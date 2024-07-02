**Example 1: 创建角色**

创建角色

Input: 

```
tccli tdmq CreateRole --cli-unfold-argument  \
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

