**Example 1: 提取SSL证书中的可配置域名**



Input: 

```
tccli cdn DescribeCertDomains --cli-unfold-argument  \
    --Cert \u65e0
```

Output: 
```
{
    "Response": {
        "RequestId": "1abbe623-4b0e-4727-ab51-7624902d47f4",
        "Domains": [
            "test.tencentyun.com",
            "httpstest.tencentyun.com"
        ],
        "CertifiedDomains": [
            "httpstest.tencentyun.com"
        ]
    }
}
```

