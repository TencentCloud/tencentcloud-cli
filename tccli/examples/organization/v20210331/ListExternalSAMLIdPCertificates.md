**Example 1: 查询SAML签名证书列表**

查询SAML签名证书列表

Input: 

```
tccli organization ListExternalSAMLIdPCertificates --cli-unfold-argument  \
    --ZoneId z-xj239dj23***
```

Output: 
```
{
    "Response": {
        "TotalCounts": 20,
        "SAMLIdPCertificates": [
            {
                "SerialNumber": "1347934239****",
                "Issuer": "5.6.54.22.1.9.1=#dj39dj39e3w9rm3e2e3****,CN=dev-xxxxxx,OU=SSOProvider,O=Okta",
                "Version": "1",
                "CertificateId": "idp-c-2jd8923je29****",
                "PublicKey": "nMIIBtjCCAVugAwIBAgITBmyf1XSXNmY****",
                "SignatureAlgorithm": "SHA256withRSA",
                "NotAfter": "2030-06-23 07:04:37",
                "NotBefore": "2010-06-23 07:04:37",
                "Subject": "5.6.54.22.1.9.1=#dj39dj39e3w9rm3e2e3****,CN=dev-xxxxxx,OU=SSOProvider,O=Okta",
                "X509Certificate": "nMIIBtjCCAVugAwIBAgITBmyf1XSXNmY****"
            }
        ],
        "RequestId": "2ccd7ed1-24b4-4882-8f4a-5580b430bce7"
    }
}
```

