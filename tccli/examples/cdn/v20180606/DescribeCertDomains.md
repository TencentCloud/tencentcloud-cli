**Example 1: Getting configurable domain names in an SSL certificate**



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

