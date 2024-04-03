**Example 1: 上传证书CA证书**

上传证书根证书

Input: 

```
tccli ssl UploadCertificate --cli-unfold-argument  \
    --CertificatePublicKey -----BEGIN CERTIFICATE-----
xxxxxxxxxxxxxxxxxxx
-----END CERTIFICATE----- \
    --Alias 上传CA证书 \
    --ProjectId 12345 \
    --Repeatable False \
    --CertificateType CA \
    --Tags.0.TagKey key1 \
    --Tags.0.TagValue value1 \
    --Tags.1.TagKey key2 \
    --Tags.1.TagValue value2
```

Output: 
```
{
    "Response": {
        "CertificateId": "a92b1Z1i",
        "RepeatCertId": "",
        "RequestId": "7ef2d2bb-f609-4e3d-a35c-04a5d3ac633b"
    }
}
```

**Example 2: 上传服务端证书**

上传服务端证书

Input: 

```
tccli ssl UploadCertificate --cli-unfold-argument  \
    --CertificatePublicKey -----BEGIN CERTIFICATE-----
xxxxxxxxxxxxxxxxxxx
-----END CERTIFICATE----- \
    --CertificatePrivateKey -----BEGIN RSA PRIVATE KEY-----
xxxxxxxxxxxxxxxxxxxxxxxx
-----END RSA PRIVATE KEY----- \
    --Alias 上传证书 \
    --ProjectId 12345 \
    --Repeatable False \
    --CertificateType SVR \
    --Tags.0.TagKey key1 \
    --Tags.0.TagValue value1 \
    --Tags.1.TagKey key2 \
    --Tags.1.TagValue value2
```

Output: 
```
{
    "Response": {
        "CertificateId": "DSAuy46E",
        "RepeatCertId": "DSAuy46E",
        "RequestId": "6d69e2d8-2c31-40d2-a244-9f86ffb20cd0"
    }
}
```

