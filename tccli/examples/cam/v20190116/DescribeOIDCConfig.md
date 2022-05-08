**Example 1: 获取角色OIDC配置**



Input: 

```
tccli cam DescribeOIDCConfig --cli-unfold-argument  \
    --Name Name
```

Output: 
```
{
    "Response": {
        "Description": "Desc",
        "ProviderType": 11,
        "IdentityUrl": "https://*****.qq.cn/",
        "IdentityKey": "ewogICAgImtleXMiOiBbCiAgICAg********jenYyT0kiCiAgICAgICAgfQogICAgXQp9",
        "ClientId": [
            "61adcf0******bc9546"
        ],
        "Name": "Name",
        "Status": 11,
        "RequestId": "24366174-63dd-42ba-8073-bd6b0af0f241"
    }
}
```

