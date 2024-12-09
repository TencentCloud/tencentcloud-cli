**Example 1: 检查证书域名验证**



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
                "Domain": "*.umcare.cn",
                "VerifyType": "DNS",
                "LocalCheck": 1,
                "CaCheck": 1,
                "LocalCheckFailReason": "",
                "CheckValue": [],
                "Frequently": false,
                "Issued": true
            }
        ],
        "RequestId": "14727a68-3b90-4408-99c9-dea6d7de9456"
    }
}
```

