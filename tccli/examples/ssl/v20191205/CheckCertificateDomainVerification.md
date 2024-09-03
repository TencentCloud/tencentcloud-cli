**Example 1: 检查证书域名验证**



Input: 

```
tccli ssl CheckCertificateDomainVerification --cli-unfold-argument  \
    --CertificateId xx
```

Output: 
```
{
    "Response": {
        "VerificationResults": [
            {
                "Domain": "xx",
                "CheckValue": [
                    "xx"
                ],
                "LocalCheckFailReason": "xx",
                "LocalCheck": 0,
                "CaCheck": 0,
                "Frequently": true,
                "VerifyType": "xx",
                "Issued": true
            }
        ],
        "RequestId": "xx"
    }
}
```

