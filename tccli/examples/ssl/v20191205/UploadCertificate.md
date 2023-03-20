**Example 1: 上传证书**

上传证书

Input: 

```
tccli ssl UploadCertificate --cli-unfold-argument  \
    --CertificatePublicKey CertificateContent
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

