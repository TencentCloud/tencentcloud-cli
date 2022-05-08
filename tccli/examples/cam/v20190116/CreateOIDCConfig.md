**Example 1: 添加角色OIDC配置**



Input: 

```
tccli cam CreateOIDCConfig --cli-unfold-argument  \
    --IdentityKey ewogICAgImtleXMiOiBbCiAgIC***************V9jenYyT0kiCiAgICAgICAgfQogICAgXQp9 \
    --IdentityUrl https://*******.qq.cn/ \
    --Name oidc \
    --ClientId 61adcf00******ddbc9546 \
    --Description Desc
```

Output: 
```
{
    "Response": {
        "RequestId": "0d8de866-7385-4230-8f28-060a92d723ee"
    }
}
```

