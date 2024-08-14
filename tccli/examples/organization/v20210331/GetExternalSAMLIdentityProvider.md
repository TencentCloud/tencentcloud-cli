**Example 1: 查询SAML身份提供商配置信息**

查询SAML身份提供商配置信息

Input: 

```
tccli organization GetExternalSAMLIdentityProvider --cli-unfold-argument  \
    --ZoneId z-dm239d****
```

Output: 
```
{
    "Response": {
        "SAMLIdentityProviderConfiguration": {
            "EntityId": "http://www.okta.com/2jd83ne9m*****",
            "SSOStatus": "Enabled",
            "EncodedMetadataDocument": "PD94bWwgdmVyc2lvbj0iMS4wIj8+CjxFbnRpdHlEZXNjcmlwdG9yIHhtbG5zPSJ1cm46b2FzaXM6bmFtZXM6dGM6U0FNTDoydpbi5jb20vc2FtbC9tZXRhZGF0YS8xN2NkYjEyOC03N**********",
            "CertificateIds": [
                "idp-c-2jd8923je29****"
            ],
            "LoginUrl": "https://dev-xxxxxx.okta.com/app/dev-xxxxxx_cloudssodemo_1/2jd83ne9m****/sso/saml",
            "CreateTime": "2024-01-01 12:12:12",
            "UpdateTime": "2024-01-01 12:12:12"
        },
        "RequestId": "2ccd7ed1-24b4-4882-8f4a-5580b430bce7"
    }
}
```

