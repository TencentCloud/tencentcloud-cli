**Example 1: 修改角色OIDC配置**



Input: 

```
tccli cam UpdateOIDCConfig --cli-unfold-argument  \
    --IdentityKey ewogICAgImtleXMiOiBbCiAgICAgICAgewogIC************klJbUpsLV9jenYyT0kiCiAgICAgICAgfQogICAgXQp9 \
    --IdentityUrl https://test.qq.cn/ \
    --Name test-oidc \
    --ClientId 61adcf0*****9546 \
    --Description Desc
```

Output: 
```
{
    "Response": {
        "RequestId": "59b8efa4-cdd3-46dd-b9e7-0925aa1bee74"
    }
}
```

