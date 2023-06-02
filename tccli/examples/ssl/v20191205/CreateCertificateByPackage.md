**Example 1: 使用权益点创建证书**

使用权益点创建证书

Input: 

```
tccli ssl CreateCertificateByPackage --cli-unfold-argument  \
    --PackageIds xx123 \
    --Tags.0.TagKey xx123 \
    --Tags.0.TagValue xx123 \
    --ProjectId 1 \
    --RenewAlgorithmParam xx123 \
    --RenewKeyPass xx123 \
    --Period 1 \
    --OldCertificateId xx123 \
    --ProductPid 1 \
    --RenewGenCsrMethod xx123 \
    --RenewCsr xx123 \
    --DomainCount xx123 \
    --RenewAlgorithmType xx123 \
    --VerifyType DNS
```

Output: 
```
{
    "Response": {
        "CertificateId": "xx123",
        "RequestId": "xx123",
        "CertificateIds": [
            "xx123"
        ]
    }
}
```

