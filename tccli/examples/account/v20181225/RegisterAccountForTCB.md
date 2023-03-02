**Example 1: TCB注册云账号**



Input: 

```
tccli account RegisterAccountForTCB --cli-unfold-argument  \
    --RegisterData.AppID  wx3fcd6d0f9dd497a1 \
    --RegisterData.AuthInfo.ID 1234 \
    --RegisterData.AuthInfo.PrincipalName test \
    --RegisterData.AuthInfo.Type 0 \
    --RegisterData.Email 1@qq.com \
    --RegisterData.Nickname test \
    --RegisterData.Phone 12345678901 \
    --RegisterData.Username  gh_56f03c56dc39 \
    --Type la
```

Output: 
```
{
    "Response": {
        "Uin": 600000561806,
        "IsBind": 0,
        "RequestId": "b3d63aa7-8a8e-45af-902e-7835efbd24b7"
    }
}
```

