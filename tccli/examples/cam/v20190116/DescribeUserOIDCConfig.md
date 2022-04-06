**Example 1: 获取用户OIDC配置**



Input: 

```
tccli cam DescribeUserOIDCConfig --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Description": "描述信息",
        "ProviderType": 12,
        "IdentityUrl": "https://tencent.auth**.cn/",
        "IdentityKey": "ewogICAgImtleXMiOiBbC****",
        "ClientId": "61adcf00620c31e3d***",
        "AuthorizationEndpoint": "https://tencent.auth**.cn",
        "Scope": [
            "openid",
            "email"
        ],
        "ResponseType": "id_token",
        "ResponseMode": "form_post",
        "MappingFiled": "sub",
        "Status": 11,
        "RequestId": "e00eaca1-57b4-49e7-978d-648c5f1b9bd3"
    }
}
```

