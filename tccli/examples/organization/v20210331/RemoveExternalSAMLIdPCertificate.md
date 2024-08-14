**Example 1: 移除SAML签名证书**

移除SAML签名证书

Input: 

```
tccli organization RemoveExternalSAMLIdPCertificate --cli-unfold-argument  \
    --ZoneId z-2js923necd*** \
    --CertificateId idp-c-2jd8923je29****
```

Output: 
```
{
    "Response": {
        "RequestId": "2ccd7ed1-24b4-4882-8f4a-5580b430bce7"
    }
}
```

