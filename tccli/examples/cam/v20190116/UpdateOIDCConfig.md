**Example 1: 修改配置信息**



Input: 

```
tccli cam UpdateOIDCConfig --cli-unfold-argument  \
    --IdentityUrl https://dev-6237974.okta.com \
    --ClientId 61adcf00620c31e3ddbc9546 \
    --Name oidc \
    --IdentityKey eyJrZXlzIjpbeyJrdHkiOiJSU0EiLCJ1c2UiOiJzaWciLCJraWQiOiI3S2Mz***********************************************************MNG1SOHEzSHhON3ZZMmVLOWFKZkI2c0NnUGhVNXRXZFhtWnJRMW9JIn1dfQ \
    --Description 修改配置信息 \
    --AutoRotateKey 1
```

Output: 
```
{
    "Response": {
        "RequestId": "68bedb22-0c9d-4f83-9509-f79249ef7fd2"
    }
}
```

