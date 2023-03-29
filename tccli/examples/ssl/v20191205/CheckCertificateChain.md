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
            "abc"
        ],
        "RequestId": "abc"
    }
}
```

