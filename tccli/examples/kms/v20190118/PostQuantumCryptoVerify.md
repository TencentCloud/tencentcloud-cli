**Example 1: 后量子密码算法验签**

后量子密码算法验签。

Input: 

```
tccli kms PostQuantumCryptoVerify --cli-unfold-argument  \
    --KeyId abc \
    --SignatureValue abc \
    --Message abc
```

Output: 
```
{
    "Response": {
        "SignatureValid": true,
        "RequestId": "abc"
    }
}
```

