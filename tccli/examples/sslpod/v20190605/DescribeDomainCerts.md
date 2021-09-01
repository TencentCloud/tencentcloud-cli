**Example 1: 获取域名关联证书**



Input: 

```
tccli sslpod DescribeDomainCerts --cli-unfold-argument  \
    --DomainId 13076
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Hash": "xxxxxx",
                "CN": "cloud.tencent.com",
                "KeyAlgo": "RSA 2048",
                "Brand": "xxxxxx",
                "Days": 3650,
                "CertType": "xx",
                "BeginTime": "2020-01-01T00:00:00+08:00",
                "TrustStatus": "xx",
                "SANs": "xx",
                "EndTime": "2030-01-01T00:00:00+08:00",
                "Issuer": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

