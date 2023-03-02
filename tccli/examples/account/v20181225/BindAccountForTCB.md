**Example 1: 绑定TCB账号**



Input: 

```
tccli account BindAccountForTCB --cli-unfold-argument  \
    --AccountData.AppID  wx3fcd6d0f9dd497a1 \
    --AccountData.AuthInfo.ID 1234 \
    --AccountData.AuthInfo.PrincipalName test \
    --AccountData.AuthInfo.Type 0 \
    --AccountData.Email 1@qq.com \
    --AccountData.Nickname test \
    --AccountData.Phone 12345678901 \
    --AccountData.Username  gh_56f03c56dc39 \
    --AccountData.CountryCode 86 \
    --Type la \
    --BindUin 100000546547
```

Output: 
```
{
    "Response": {
        "RequestId": "3e2bda45-8d95-4061-af86-3f54dfe953a5"
    }
}
```

