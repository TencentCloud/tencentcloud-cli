**Example 1: 添加谷歌认证源**

添加谷歌认证源

Input: 

```
tccli tcb AddProvider --cli-unfold-argument  \
    --EnvId env-123 \
    --Name.Message 谷歌 \
    --ProviderType OAUTH \
    --Id google \
    --Picture https://qcloudimg.tencent-cloud.cn/raw/f3c2d4c33223231e42135df51723a59c.svg \
    --Config.ClientId example \
    --Config.ClientSecret example \
    --Config.Scope openid profile email \
    --Config.AuthorizationEndpoint https://accounts.google.com/o/oauth2/v2/auth \
    --Config.TokenEndpoint https://oauth2.googleapis.com/token \
    --Config.UserinfoEndpoint https://www.googleapis.com/oauth2/v3/userinfo \
    --Config.TokenEndpointAuthMethod CLIENT_SECRET_BASIC \
    --Config.RequestParametersMap.RegisterUserType externalUser \
    --TransparentMode FALSE \
    --Description.Message GitHub OAuth身份认证 \
    --On TRUE \
    --AutoSignInWhenEmailMatch TRUE \
    --AutoSignInWhenPhoneNumberMatch TRUE
```

Output: 
```
{
    "Response": {
        "RequestId": "7a3a7e6b-7982-4acd-bb52-206d6e57f2b7"
    }
}
```

