**Example 1: 对签名数据进行验证**



Input: 

```
tccli ess VerifyDigitalDataSign --cli-unfold-argument  \
    --PlainText 测试******23 \
    --SignValue MIAGCSqGSIb3DQE1UBg3UERzBFAiEAvMEVUnoR2hWQSNqZAuyoMquMEyiNoEGbTBKhsU0SNsYCIHBzwcKT7jSQop+jsQwtkcxNri90GoowhROnIqpb5dDBAAAAAAAA
```

Output: 
```
{
    "Response": {
        "Certificate": {
            "CommonName": "ESS*********8698",
            "IssuerCommonName": "NMGSCA TEST SM2 OCA1",
            "NotAfter": 1804749985,
            "NotBefore": 1773213985,
            "SerialNumber": "220**********959"
        },
        "VerifyResult": 1,
        "RequestId": "11fde571-5c11-477c-9973-7734f8d87c3b"
    }
}
```

