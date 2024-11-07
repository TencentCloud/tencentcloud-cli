**Example 1: 更新角色**

更新角色

Input: 

```
tccli tdmq ModifyRole --cli-unfold-argument  \
    --RoleName role1 \
    --Remark remarkDemo \
    --ClusterId pulsar-xk3ne8k2qkp8 \
    --EnvironmentRoleSets.0.EnvironmentId devNs \
    --EnvironmentRoleSets.0.Permissions produce \
    --UnbindAllEnvironment True
```

Output: 
```
{
    "Response": {
        "RoleName": "role1",
        "Remark": "remarkDemo",
        "RequestId": "1004f1de-6fb8-41d5-965e-3aae8c87183a"
    }
}
```

