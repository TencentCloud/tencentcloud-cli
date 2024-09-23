**Example 1: 为权限配置修改自定义策略**

为权限配置修改自定义策略

Input: 

```
tccli organization UpdateCustomPolicyForRoleConfiguration --cli-unfold-argument  \
    --ZoneId z-fdk3o32kqw \
    --RoleConfigurationId rc-sin23wj29s \
    --CustomPolicyName test \
    --NewCustomPolicyDocument {"statement":{"action":["name/cvm:*","name/vpc:*","name/cos:*","name/cmqtopic:*","name/cmqqueue:*"],"effect":"allow","resource":"*"},"version":"2.0"}
```

Output: 
```
{
    "Response": {
        "RequestId": "e297543a-80de-4039-83c8-9d324545"
    }
}
```

