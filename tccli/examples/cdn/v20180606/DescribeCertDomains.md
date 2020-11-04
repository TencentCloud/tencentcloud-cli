**Example 1: 提取SSL证书中的可配置域名**



Input: 

```
tccli cdn DescribeCertDomains --cli-unfold-argument  \
    --Cert XXXXX
```

Output: 
```
{
    "Response": {
        "RequestId": "xxxxx-xxxxx-xxxxx-xxxxx-xxxxx",
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

