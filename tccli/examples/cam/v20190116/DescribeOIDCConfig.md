**Example 1: 获取OIDC配置**



Input: 

```
tccli cam DescribeOIDCConfig --cli-unfold-argument  \
    --Name testName
```

Output: 
```
{
    "Response": {
        "AutoRotateKey": 1,
        "ClientId": [
            "61adcf00620c31e3ddbc9546"
        ],
        "Description": "OIDC 联合身份",
        "IdentityKey": "eyJrZXlzIjpbeyJrdHkiOiJSU0EiLCJ1c2UiOiJzaWciLCJraWQiOiI3S2Mz************************************************************NG1SOHEzSHhON3ZZMmVLOWFKZkI2c0NnUGhVNXRXZFhtWnJRMW9JIn1dfQ==",
        "IdentityUrl": "https://xxx.qq.cn/oidc",
        "Name": "testName",
        "ProviderType": 11,
        "Status": 11,
        "RequestId": "1df46551-65d8-4df2-8ad4-89fe28aa4740"
    }
}
```

