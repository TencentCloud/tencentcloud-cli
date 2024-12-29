**Example 1: 获取证书详情**



Input: 

```
tccli live DescribeLiveCert --cli-unfold-argument  \
    --CertId 1000
```

Output: 
```
{
    "Response": {
        "CertInfo": {
            "CertId": 1000,
            "CertName": "testName",
            "Description": "testDesc",
            "CreateTime": "2018-11-30T15:50:12Z",
            "HttpsCrt": "gfdsfsdfdsfdsfdsfsdfsd",
            "CertType": 0,
            "CertExpireTime": "2018-12-30T15:50:12Z",
            "DomainList": [
                "5000.livepush.play.com"
            ]
        },
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

