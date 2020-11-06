**Example 1: 请求示例**



Input: 

```
tccli live DescribeLiveCerts --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "CertInfoSet": [
            {
                "CertId": 1000,
                "CertName": "testName",
                "Description": "testDesc",
                "CreateTime": "2018-11-30T15:50:12Z",
                "HttpsCrt": "xxx",
                "CertType": 0,
                "CertExpireTime": "2018-12-30T15:50:12Z",
                "DomainList": [
                    "5000.livepush.play.com"
                ]
            }
        ],
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

