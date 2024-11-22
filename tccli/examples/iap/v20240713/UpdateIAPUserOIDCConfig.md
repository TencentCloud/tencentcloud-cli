**Example 1: 修改IAP的OIDC配置**

修改IAP的OIDC配置

Input: 

```
tccli iap UpdateIAPUserOIDCConfig --cli-unfold-argument  \
    --IdentityUrl https://accounts.g**gle.com \
    --ClientId 47***01-pu***mvj4lj1de7tj.apps.g**gleusercontent.com \
    --AuthorizationEndpoint https://accounts.g**gle.com/o/oauth2/v2/auth \
    --ResponseType id_token \
    --ResponseMode form_post \
    --MappingFiled email \
    --IdentityKey ewogICAgImtle***xkd09GTHVVRUJkdyIKICAgICAgICB9CiAgICBdCn0= \
    --Scope openid email profile \
    --Description 1
```

Output: 
```
{
    "Response": {
        "RequestId": "b83e3152-6d18-4617-986d-ff4c666750ed"
    }
}
```

