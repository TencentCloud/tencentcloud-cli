**Example 1: 获取SSH密钥对凭据明文**

获取SSH密钥对凭据明文

Input: 

```
tccli ssm GetSSHKeyPairValue --cli-unfold-argument  \
    --SecretName test2-sshkey-secret
```

Output: 
```
{
    "Response": {
        "PrivateKey": "-----BEGIN RSA PRIVATE KEY-----\nMIIEowIBAAKC***********NEuTGXFT8sLJ\n-----END RSA PRIVATE KEY-----",
        "ProjectID": 0,
        "PublicKey": "ssh-rsa AAAA********H5TD4ab skey-e0vbh2ts",
        "RequestId": "9f436a38-ced1-45f0-9b51-946958b90244",
        "SSHKeyDescription": "created by ssm",
        "SSHKeyID": "skey-e0vbh2ts",
        "SSHKeyName": "test2_key"
    }
}
```

