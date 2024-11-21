**Example 1: 设置Okta认证配置**



Input: 

```
tccli dasb ModifyOAuthSetting --cli-unfold-argument  \
    --Enable True \
    --AuthMethod okta \
    --ClientId client-id \
    --ClientSecret client-secret \
    --CodeUrl https://some-url/oauth2/v1/authorize \
    --TokenUrl https://some-url/oauth2/v1/token \
    --UserInfoUrl https://some-url/oauth2/v1/userinfo
```

Output: 
```
{
    "Response": {
        "RequestId": "dfac9070-8b23-499e-83b2-a50e3ca059af"
    }
}
```

