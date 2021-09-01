**Example 1: 获取SSH密钥对凭据明文**

获取SSH密钥对凭据明文

Input: 

```
tccli ssm GetSSHKeyPairValue --cli-unfold-argument  \
    --SecretName xx
```

Output: 
```
{
    "Response": {
        "SSHKeyID": "xx",
        "ProjectID": 0,
        "PrivateKey": "xx",
        "PublicKey": "xx",
        "RequestId": "xx",
        "SSHKeyName": "xx",
        "SSHKeyDescription": "xx"
    }
}
```

