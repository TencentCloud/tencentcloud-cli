**Example 1: 返回**



Input: 

```
tccli ssl HostCertificate --cli-unfold-argument  \
    --ResourceType CDN \
    --CertificateId ahsgjahs
```

Output: 
```
{
    "Response": {
        "CertHostingInfo": {
            "CertId": "lw0LEZmv",
            "ResourceType": "CDN,CLB",
            "RenewCertId": null,
            "CreateTime": "2021-05-16T09:06:24.000000Z"
        },
        "RequestId": "5ca56-1eca6-5678-9754-2bda0"
    }
}
```

