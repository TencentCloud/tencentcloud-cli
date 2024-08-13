**Example 1: 添加SAML签名证书**

添加SAML签名证书

Input: 

```
tccli organization AddExternalSAMLIdPCertificate --cli-unfold-argument  \
    --ZoneId z-dsj3ieme \
    --X509Certificate nMIIBtjCCAVugAwIBAgITBmyf1XSXNmY*****
```

Output: 
```
{
    "Response": {
        "CertificateId": "idp-c-2jd8923je29****",
        "RequestId": "2ccd7ed1-24b4-4882-8f4a-5580b430bce7"
    }
}
```

