**Example 1: 导入密钥对**



Input: 

```
tccli cvm ImportKeyPair --cli-unfold-argument  \
    --ProjectId 0 \
    --KeyName operation_key \
    --PublicKey ssh-rsa XXXXXXXXXXXX== skey_45071
```

Output: 
```
{
    "Response": {
        "KeyId": "skey-4e5ty7i8",
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7"
    }
}
```

