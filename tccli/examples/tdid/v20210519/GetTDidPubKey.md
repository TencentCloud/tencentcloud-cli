**Example 1: 查询DID标识的认证公钥**

查询DID标识的认证公钥列表

Input: 

```
tccli tdid GetTDidPubKey --cli-unfold-argument  \
    --Did did:tdid:w1:0xcb04e621e21236f7bb39f4dd03b2a485b1009ba9 \
    --DAPId 1
```

Output: 
```
{
    "Response": {
        "AuthPublicKeyList": [
            "-----BEGIN PUBLIC KEY-----\r\nMFkwEwYHKoZIzj0CAQYIKoEcz1UBgi0DQgAEbV9OaLigX26ulDAfpeMxVYBb3VK27RdqZlEIniHf62DqCdXwL0V9Jj3C+8EkDH3ZWDoIwWPj6x6javrkEDi0PQ==\r\n-----END PUBLIC KEY-----"
        ],
        "RequestId": "75c5d57a-731e-44a1-aa19-9bd031b02021"
    }
}
```

