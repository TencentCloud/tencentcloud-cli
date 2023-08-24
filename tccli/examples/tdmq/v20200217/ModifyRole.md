**Example 1: 更新角色**

更新角色

Input: 

```
tccli tdmq ModifyRole --cli-unfold-argument  \
    --RoleName abc \
    --Remark abc \
    --ClusterId abc \
    --EnvironmentRoleSets.0.EnvironmentId abc \
    --EnvironmentRoleSets.0.Permissions abc \
    --UnbindAllEnvironment True
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

