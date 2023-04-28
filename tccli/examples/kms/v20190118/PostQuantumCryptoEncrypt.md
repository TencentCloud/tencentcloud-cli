**Example 1: 使用后量子密码算法密钥进行数据加密**

使用后量子密码算法密钥进行数据加密。

Input: 

```
tccli kms PostQuantumCryptoEncrypt --cli-unfold-argument  \
    --KeyId abc \
    --PlainText abc
```

Output: 
```
{
    "Response": {
        "CiphertextBlob": "abc",
        "KeyId": "abc",
        "RequestId": "abc"
    }
}
```

