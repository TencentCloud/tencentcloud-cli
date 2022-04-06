**Example 1: 添加用户OIDC配置**



Input: 

```
tccli cam CreateUserOIDCConfig --cli-unfold-argument  \
    --ResponseType id_token \
    --IdentityUrl https://tencent.auth***.cn/ \
    --ResponseMode form_post \
    --Description 测试 \
    --IdentityKey ewogICAgImtleXMiOiBbCi****** \
    --ClientId 61adcf00620c31e3*** \
    --MappingFiled sub \
    --AuthorizationEndpoint https://tencent.auth**.cn \
    --Scope openidScope.1
```

Output: 
```
{
    "Response": {
        "RequestId": "8a70d447-3c04-43c0-94ca-db899d4d05ac"
    }
}
```

