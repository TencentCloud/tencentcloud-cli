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
            "AssociatedInstanceIds": [],
            "CreatedTime": null,
            "KeyId": "lhkp-hfenegt1",
            "KeyName": "test_create_1",
            "PrivateKey": "xxxxxx",
            "PublicKey": "xxxxxx"
        },
        "RequestId": "02dc35eb-06f0-477f-9b06-c980bc56c18d"
    }
}
```

