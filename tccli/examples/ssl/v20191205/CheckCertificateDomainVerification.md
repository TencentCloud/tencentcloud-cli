**Example 1: 检查证书域名验证结果**



Input: 

```
tccli ssl CheckCertificateDomainVerification --cli-unfold-argument  \
    --CertificateId hehk**js
```

Output: 
```
{
    "Response": {
        "VerificationResults": [
            {
                "Domain": "ninghhuang.online",
                "VerifyType": "DNS",
                "LocalCheck": -1,
                "CaCheck": -1,
                "LocalCheckFailReason": "txt record not found",
                "CheckValue": [],
                "Frequently": false,
                "Issued": false
            }
        ],
        "RequestId": "14727a68-3b90-4408-99c9-dea6d7de9456"
    }
}
```

