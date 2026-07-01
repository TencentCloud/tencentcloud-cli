**Example 1: 创建OIDC角色身份提供商**



Input: 

```
tccli cam CreateOIDCConfig --cli-unfold-argument  \
    --IdentityUrl https://dev-6237974.okta.com \
    --ClientId 61adcf00620c31e3ddbc9546 \
    --Name OIDC \
    --IdentityKey eyJrZXlzIjpbeyJrdHkiOiJSU0EiLCJ1c2UiOiJzaWciLCJraWQiOiI3S2Mz***********************************************************MNG1SOHEzSHhON3ZZMmVLOWFKZkI2c0NnUGhVNXRXZFhtWnJRMW9JIn1dfQ \
    --Description 修改配置信息 \
    --AutoRotateKey 1
```

Output: 
```
{
    "Response": {
        "RequestId": "92643b0c-42ad-46cb-98b8-080fa81d5a5c"
    }
}
```

