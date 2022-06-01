**Example 1: 获取默认证书**



Input: 

```
tccli teo DescribeDefaultCertificates --cli-unfold-argument  \
    --ZoneId zone-xxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "xxxx-xxxxx-xxxx",
        "TotalCount": 1,
        "CertInfo": [
            {
                "CertId": "EO-xxxx",
                "CommonName": "test.com",
                "SubjectAltName": [
                    "*.test.com",
                    "test.com"
                ],
                "Type": "default",
                "Alias": "默认证书",
                "EffectiveTime": "2014-08-03T12:00:00+08:00",
                "ExpireTime": "2014-08-03T12:00:00+08:00",
                "Status": "deployed"
            }
        ]
    }
}
```

