**Example 1: 使用后量子密码算法密钥进行数据加密**

使用后量子密码算法密钥进行数据加密。

Input: 

```
tccli kms PostQuantumCryptoEncrypt --cli-unfold-argument  \
    --KeyId 23e80852-1e38-11e9-b129-5cb9019b4b01 \
    --PlainText dGVzdAo=
```

Output: 
```
{
    "Response": {
        "CiphertextBlob": "ZHNhZHNpbzEyMW5uaz1qb2lqMm***********TIxbWExcwo=",
        "KeyId": "23e80852-1e38-11e9-b129-5cb9019b4b01",
        "RequestId": "403150d4-1736-4e61-9259-d70bb7799620"
    }
}
```

