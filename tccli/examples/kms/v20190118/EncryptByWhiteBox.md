**Example 1: 使用白盒密钥进行加密**



Input: 

```
tccli kms EncryptByWhiteBox --cli-unfold-argument  \
    --KeyId 244dab8c-6dad-11ea-80c6-5254006d0810 \
    --PlainText UGxhaW5UZXh0
```

Output: 
```
{
    "Response": {
        "RequestId": "4b3be01e-117a-43f5-aa34-dd5034efe3dd",
        "InitializationVector": "BQbVImt3p_xr8VQebZaXGQ==",
        "CipherText": "ZKHH2la4DpwlkwjANQ5hgw=="
    }
}
```

