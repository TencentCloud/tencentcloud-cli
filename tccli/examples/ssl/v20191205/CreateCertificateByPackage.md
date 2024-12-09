**Example 1: 使用权益点创建证书**

使用权益点创建证书

Input: 

```
tccli ssl CreateCertificateByPackage --cli-unfold-argument  \
    --PackageIds Z2*******80000 \
    --Tags.0.TagKey z***j \
    --Tags.0.TagValue m****k \
    --ProjectId 1 \
    --RenewAlgorithmParam 2048 \
    --RenewKeyPass k***j \
    --Period 1 \
    --OldCertificateId Rt***9 \
    --ProductPid 1 \
    --RenewGenCsrMethod online \
    --RenewCsr CSR \
    --DomainCount 5 \
    --RenewAlgorithmType RSA \
    --VerifyType DNS
```

Output: 
```
{
    "Response": {
        "CertificateId": "T*****h",
        "RequestId": "dh7d********jdkm",
        "CertificateIds": [
            "j*****uk"
        ]
    }
}
```

