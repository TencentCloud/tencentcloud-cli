**Example 1: 非对称密钥签名**



Input: 

```
tccli kms SignByAsymmetricKey --cli-unfold-argument  \
    --Algorithm SM2DSA \
    --Message Zsfw9GLu7dnR8tRr3BDk4kFnxIdc8veiKX2gK49LqOA%3D \
    --KeyId 6cdf26d1-44ff-11eb-841c-5254006d0810 \
    --MessageType DIGEST
```

Output: 
```
{
    "Response": {
        "RequestId": "e86d6131-2830-4e1c-9d03-d421affd646c",
        "Signature": "MEUCICr/JCV52BqGvI0iYxdZ1eL8zzJjx39mWNv2ZWdLOMvRAiEApO6os3Wj0Tg302fbTBr02IxHO1aCr0Zr41t4hi6yTG8="
    }
}
```

