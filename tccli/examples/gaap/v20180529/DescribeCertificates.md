**Example 1: 查询服务器证书信息**



Input: 

```
tccli gaap DescribeCertificates --cli-unfold-argument  \
    --CertificateType 2 \
    --Limit 1 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 19,
        "RequestId": "35d85baa-eeb8-4eb5-96a9-b6d27f4ff92c",
        "CertificateSet": [
            {
                "CertificateId": "cert-8k1l0pat",
                "SubjectCN": "lagameft01.xyz",
                "CertificateAlias": "test",
                "CertificateName": "test",
                "BeginTime": 1554134400,
                "CertificateType": 2,
                "EndTime": 1585713600,
                "CreateTime": 1564557014,
                "IssuerCN": "TrustAsia TLS RSA CA"
            }
        ]
    }
}
```

