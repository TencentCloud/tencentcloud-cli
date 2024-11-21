**Example 1: 重加密接口示例**

对密文进行重新加密。

Input: 

```
tccli kms ReEncrypt --cli-unfold-argument  \
    --CiphertextBlob M1UPpYhWviWGrfn78MLVBG1n5G2H6+pGK5u7xOmoWoCcWpxVKC1OAQujzQSLHWBE54p3Kd8Qji+7FOPN3nkQeA==-k-fKVP3WIlGpg8m9LMW4jEkQ==-k-8VyKJSv97jE/+mKGeevmUUvCXLYzWs6Zxn3PZoeBW4aPCjYX \
    --DestinationKeyId 87ff856e-973c-11ef-947b-525400d834e5 \
    --DestinationEncryptionContext {"key1":"value1"}
```

Output: 
```
{
    "Response": {
        "CiphertextBlob": "M1UPpYhWviWGrfn78MLVBG1n5G2H6+pGK5u7xOmoWoCcWpxVKC1OAQujzQSLHWBE54p3Kd8Qji+7FOPN3nkQeA==-k-XqqalxTyNKIC1rITRePFGQ==-k-8VyKJSv97jE/+mKGeevmUUvCXLYzWs6Zxn3PZoeBW4aPCjYX",
        "KeyId": "87ff856e-973c-11ef-947b-525400d834e5",
        "ReEncrypted": true,
        "RequestId": "6c3281fb-5286-49d5-8aeb-4a4424bc4271",
        "SourceKeyId": "87ff856e-973c-11ef-947b-525400d834e5"
    }
}
```

