**Example 1: 使用后量子密码算法解密**

使用后量子密码算法解密。

Input: 

```
tccli kms PostQuantumCryptoDecrypt --cli-unfold-argument  \
    --CiphertextBlob abc \
    --EncryptionPublicKey abc \
    --EncryptionAlgorithm abc
```

Output: 
```
{
    "Response": {
        "KeyId": "abc",
        "PlainText": "abc",
        "RequestId": "abc"
    }
}
```

