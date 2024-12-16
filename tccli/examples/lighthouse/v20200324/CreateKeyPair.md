**Example 1: 创建密钥对**



Input: 

```
tccli lighthouse CreateKeyPair --cli-unfold-argument  \
    --KeyName test_create_1
```

Output: 
```
{
    "Response": {
        "KeyPair": {
            "KeyId": "lhkp-hfenegt1",
            "KeyName": "test_create_1",
            "PublicKey": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC6Zx4q...",
            "AssociatedInstanceIds": [],
            "CreatedTime": null,
            "PrivateKey": "-----BEGIN RSA PRIVATE KEY-----\nMIIEowIBAAKCAQEAumc...\n-----END RSA PRIVATE KEY-----"
        },
        "RequestId": "02dc35eb-06f0-477f-9b06-c980bc56c18d"
    }
}
```

