**Example 1: 使用白盒密钥进行加密**



Input: 

```
tccli kms EncryptByWhiteBox --cli-unfold-argument  \
    --KeyId 738c7598-6a69-11ef-9d7c-525400dc620c \
    --InitializationVector 3t+gDx/YmtnJuokqAg+cOw== \
    --PlainText dGVzdAo=
```

Output: 
```
{
    "Response": {
        "CipherText": "StE4p5N11zwKybR3REtaag==",
        "InitializationVector": "3t+gDx/YmtnJuokqAg+cOw==",
        "RequestId": "a77183bf-8a95-4167-bd4a-84f02df0d4da"
    }
}
```

