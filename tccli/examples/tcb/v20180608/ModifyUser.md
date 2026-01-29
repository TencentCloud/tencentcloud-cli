**Example 1: 更新用户信息**



Input: 

```
tccli tcb ModifyUser --cli-unfold-argument  \
    --EnvId testenv-123 \
    --Uid 1 \
    --Name test_user_01 \
    --Type internalUser \
    --Password test123@ \
    --UserStatus ACTIVE \
    --NickName test_user_01 \
    --Phone 18xxxx9078 \
    --Email example@qq.com \
    --AvatarUrl https://example.avatat \
    --Description 测试账号
```

Output: 
```
{
    "Response": {
        "Data": {
            "Success": true
        },
        "RequestId": "76c0ca0f-4cf2-4f89-80b9-cdbf9ab7dd77"
    }
}
```

