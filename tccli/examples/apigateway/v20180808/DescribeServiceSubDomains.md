**Example 1: 查询服务自定义域名列表**



Input: 

```
tccli apigateway DescribeServiceSubDomains --cli-unfold-argument  \
    --ServiceId service-19c5fnhy
```

Output: 
```
{
    "Response": {
        "Result": {
            "TotalCount": 1,
            "DomainSet": [
                {
                    "Status": 1,
                    "CertificateId": "xx",
                    "Protocol": "xx",
                    "IsDefaultMapping": false,
                    "DomainName": "xx",
                    "IsForcedHttps": true,
                    "NetType": "xx",
                    "RegistrationStatus": true
                }
            ]
        },
        "RequestId": "xx"
    }
}
```

