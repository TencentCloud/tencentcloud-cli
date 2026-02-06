**Example 1: 创建用户**



Input: 

```
tccli tcb CreateUser --cli-unfold-argument  \
    --EnvId test-envId \
    --Name zhangsan \
    --Uid 1001 \
    --Type internalUser \
    --Password Abc@123456 \
    --UserStatus ACTIVE \
    --NickName 张三 \
    --Phone 13800138000 \
    --Email zhangsan@example.com \
    --AvatarUrl https://example.com/avatars/zhangsan.jpg \
    --Description 研发部门员工
```

Output: 
```
{
    "Response": {
        "Data": {
            "Uid": "1001"
        },
        "RequestId": "af638232-4d1c-4e41-b959-ea3dbe5de0be"
    }
}
```

