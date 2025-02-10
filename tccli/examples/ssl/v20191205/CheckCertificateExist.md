**Example 1: 查询证书内容是否存在**



Input: 

```
tccli ssl CheckCertificateExist --cli-unfold-argument  \
    --CertificatePublicKey -----BEGIN CERTIFICATE-----
MIIFGDCCBACgAwIBAgISBPCgHOEnsbZ/-----END CERTIFICATE-----
```

Output: 
```
{
    "Response": {
        "RepeatCertId": "GswyCokt",
        "RequestId": "f85b93a5-9040-49e4-865e-bd47cb35794a"
    }
}
```

