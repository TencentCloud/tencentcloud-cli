**Example 1: 查询IAP的OIDC配置**

查询IAP的OIDC配置

Input: 

```
tccli iap DescribeIAPUserOIDCConfig --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "AuthorizationEndpoint": "https://accounts.g**gle.com/o/oauth2/v2/auth",
        "ClientId": "47***01-pu1e*****7tj.apps.g**gleusercontent.com",
        "Description": "idp name",
        "IdentityKey": "ewogICAgImtletVUkttZ0I***GTHVVRUJkdyIKICAgICAgICB9CiAgICBdCn0=",
        "IdentityUrl": "https://accounts.g**gle.com",
        "MappingFiled": "email",
        "ProviderType": 13,
        "RequestId": "f87e5dab-426a-4a50-ac5b-1c08151cd6a2",
        "ResponseMode": "form_post",
        "ResponseType": "id_token",
        "Scope": [
            "openid",
            "email",
            "profile"
        ],
        "Status": 2
    }
}
```

