**Example 1: 使用非对称密钥验签**



Input: 

```
tccli kms VerifyByAsymmetricKey --cli-unfold-argument  \
    --Algorithm SM2DSA \
    --Message Zsfw9GLu7dnR8tRr3BDk4kFnxIdc8veiKX2gK49LqOA%3D \
    --KeyId 6cdf26d1-44ff-11eb-841c-5254006d0810 \
    --MessageType DIGEST \
    --SignatureValue MEUCIQDeO1wB%2F5dEfprulvh9Zw06UJylDt9R8MQY5qRMjzhXJgIgPKO2kKicFKemwOft8SgniUA692ORrqVEabS3kcbPL8U%3D
```

Output: 
```
{
    "Response": {
        "RequestId": "3e634985-c311-4790-953a-44990f7bec6b",
        "SignatureValid": true
    }
}
```

