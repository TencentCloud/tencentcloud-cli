**Example 1: 重颁发证书-使用原证书 CSR**



Input: 

```
tccli ssl ReplaceCertificate --cli-unfold-argument  \
    --CertificateId KPX97tim \
    --ValidType DNS \
    --CsrType Original \
    --Reason 不想要了
```

Output: 
```
{
    "Response": {
        "CertificateId": "a91hoLqo",
        "RequestId": "91afa3b6-5b67-43e1-b312-9d3b9bf0f410"
    }
}
```

**Example 2: 重颁发证书-使用在线生成 CSR**



Input: 

```
tccli ssl ReplaceCertificate --cli-unfold-argument  \
    --CertificateId KPX97tim \
    --ValidType DNS \
    --CsrType Online \
    --Reason 不想要了
```

Output: 
```
{
    "Response": {
        "CertificateId": "TfRfcXz1",
        "RequestId": "91afa3b6-5b67-43e1-b312-9d3b9bf0f410"
    }
}
```

**Example 3: 重颁发证书-使用上传 CSR**



Input: 

```
tccli ssl ReplaceCertificate --cli-unfold-argument  \
    --CertificateId KPX97tim \
    --ValidType DNS \
    --CsrType Upload \
    --CsrContent -----BEGIN CERTIFICATE REQUEST-----\nMIIBajCCARECAQAwga4xCzAJBgNVBAYTAkNOMRswGQYDVQQIDBLDp8Kmwo/DpcK7\n-----END CERTIFICATE REQUEST----- \
    --Reason 不想要了
```

Output: 
```
{
    "Response": {
        "CertificateId": "TfRfcXz1",
        "RequestId": "91afa3b6-5b67-43e1-b312-9d3b9bf0f410"
    }
}
```

