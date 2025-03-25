**Example 1: 创建IAP的OIDC配置**

创建IAP的OIDC配置

Input: 

```
tccli iap CreateIAPUserOIDCConfig --cli-unfold-argument  \
    --IdentityUrl https://accounts.g**gle.com \
    --ClientId 47***4801-pu***e7tj.apps.g**gleusercontent.com \
    --AuthorizationEndpoint https://accounts.g**gle.com/o/oauth2/v2/auth \
    --ResponseType id_token \
    --ResponseMode form_post \
    --MappingFiled email \
    --IdentityKey ewogICAgImtleXMiOiBb*******gICBdCn0= \
    --Scope openid email profile \
    --Description idp name
```

Output: 
```
{
    "Response": {
        "RequestId": "3ccecfc6-14a0-4aaa-bcf4-0d5b77835bfb"
    }
}
```

