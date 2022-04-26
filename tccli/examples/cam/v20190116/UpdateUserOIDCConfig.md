**Example 1: 修改用户OIDC配置**



Input: 

```
tccli cam UpdateUserOIDCConfig --cli-unfold-argument  \
    --ResponseType id_token \
    --IdentityUrl https://tencent.auth**.com \
    --ResponseMode form_post \
    --Description 描述 \
    --IdentityKey key \
    --ClientId cbaefefes9823*** \
    --MappingFiled sub \
    --AuthorizationEndpoint https://tencent.auth**.com \
    --Scope email
```

Output: 
```
{
    "Response": {
        "RequestId": "10a20884-070e-48a8-aa40-9ed295a33ea2"
    }
}
```

