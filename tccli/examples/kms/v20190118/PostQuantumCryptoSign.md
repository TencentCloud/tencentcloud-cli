**Example 1: 后量子密码算法签名**

后量子密码算法签名。

Input: 

```
tccli kms PostQuantumCryptoSign --cli-unfold-argument  \
    --Message abc \
    --KeyId abc
```

Output: 
```
{
    "Response": {
        "Signature": "abc",
        "RequestId": "abc"
    }
}
```

