**Example 1: 对证书链进行检查**

对证书链完整性进行检查

Input: 

```
tccli ssl CheckCertificateChain --cli-unfold-argument  \
    --CertificateChain -----BEGIN CERTIFICATE-----MIIFrDCCBJSgAwIBA.................BJSgAwIBA-----END CERTIFICATE-----
-----BEGIN CERTIFICATE-----MIIErjCCA5agAwIB.................DCCBJSg-----END CERTIFICATE-----
```

Output: 
```
{
    "Response": {
        "IsValid": true,
        "IsTrustedCA": true,
        "Chains": [
            "m.d****.com",
            "TrustAsia RSA DV TLS CA G2",
            "AAA Certificate Services"
        ],
        "RequestId": "14727a68-3b90-4408-99c9-dea6d7de9456"
    }
}
```

