**Example 1: 请求示例**



Input: 

```
tccli live DescribeLiveDomainCert --cli-unfold-argument  \
    --DomainName 5000.liveplay.myqcloud.com
```

Output: 
```
{
    "Response": {
        "DomainCertInfo": {
            "CertId": 1000,
            "CertName": "tName",
            "Description": "tDesc",
            "CreateTime": "2018-11-30T15:50:12Z",
            "HttpsCrt": "fsgfdsfsdfdsfd",
            "CertType": 0,
            "CertExpireTime": "2018-12-30T15:50:12Z",
            "DomainName": "5000.livepush.play.com",
            "Status": 1,
            "CertDomains": [
                "*.play.com"
            ],
            "CloudCertId": "sfrsfvdf"
        },
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

