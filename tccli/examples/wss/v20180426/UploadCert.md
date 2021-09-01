**Example 1: 上传证书**



Input: 

```
tccli wss UploadCert --cli-unfold-argument  \
    --Cert -----BEGIN+CERTIFICATE-----%0D%...(省略)...0%0A-----END+CERTIFICATE----- \
    --CertType SVR \
    --key -----BEGIN+RSA+PRIVATE+KEY-----%0D%...(省略)...0%0A-----END+RSA+PRIVATE+KEY----- \
    --ProjectId 1000 \
    --ModuleType ssl
```

Output: 
```
{
    "Response": {
        "Id": "9hyvgrkE",
        "RequestId": "378194e2-a873-445f-8902-23d7d4e8693e"
    }
}
```

