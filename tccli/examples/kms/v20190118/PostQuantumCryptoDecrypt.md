**Example 1: 使用后量子密码算法解密**

使用后量子密码算法解密。

Input: 

```
tccli kms PostQuantumCryptoDecrypt --cli-unfold-argument  \
    --CiphertextBlob Ade234dasdeEWdGVzdCUyMHBsYWlJJlIHL \
    --EncryptionPublicKey -----BEGIN PUBLIC KEY----- MFkwEwYHKoZIzj0CAQYI******VWhjH2dhziiH/NWCkk3FjIhjIwqjmnWhmUTg== -----END PUBLIC KEY-----  \
    --EncryptionAlgorithm SM2
```

Output: 
```
{
    "Response": {
        "KeyId": "23e80852-1e38-11e9-b129-5cb9019b4b01",
        "PlainText": "dGVzdCUyMHBsYWluJTIwdGV4dA==",
        "RequestId": "cc8f9b3c-620d-4a25-9fb5-decd94357bd8"
    }
}
```

