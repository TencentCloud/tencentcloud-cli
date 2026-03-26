**Example 1: 查询身份源列表**



Input: 

```
tccli tcb GetProviders --cli-unfold-argument  \
    --EnvId env-123
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "AutoSignUpWithProviderUser": "TRUE",
                "Config": {
                    "AuthorizationEndpoint": "https://accounts.google.com/o/oauth2/v2/auth",
                    "ClientId": "example",
                    "ClientSecret": "example",
                    "Issuer": "",
                    "JwksUri": "",
                    "RedirectUri": "",
                    "RequestParametersMap": {
                        "RegisterUserType": "externalUser"
                    },
                    "ResponseParametersMap": {
                        "Email": "email",
                        "Groups": "groups",
                        "Name": "name",
                        "PhoneNumber": "phone_number",
                        "Picture": "picture",
                        "Sub": "sub",
                        "Username": "username"
                    },
                    "ResponseType": "",
                    "SamlMetadata": "",
                    "Scope": "email openid profile",
                    "SignoutEndpoint": "",
                    "TokenEndpoint": "https://oauth2.googleapis.com/token",
                    "TokenEndpointAuthMethod": "CLIENT_SECRET_BASIC",
                    "UserinfoEndpoint": "https://www.googleapis.com/oauth2/v3/userinfo"
                },
                "Description": {
                    "Localized": [],
                    "Message": ""
                },
                "Homepage": "",
                "Id": "google",
                "Name": {
                    "Localized": [],
                    "Message": "Google"
                },
                "On": "TRUE",
                "Picture": "https://qcloudimg.tencent-cloud.cn/raw/f9131c00dcbcbccd5899a449d68da3ba.png",
                "ProviderType": "OAUTH",
                "TransparentMode": "FALSE"
            }
        ],
        "Total": 1,
        "RequestId": "490fbbcb-c5e3-4037-b851-099e636768cc"
    }
}
```

