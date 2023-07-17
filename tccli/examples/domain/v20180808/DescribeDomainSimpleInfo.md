**Example 1: 域名详情**



Input: 

```
tccli domain DescribeDomainSimpleInfo --cli-unfold-argument  \
    --DomainName test.cn
```

Output: 
```
{
    "Response": {
        "DomainInfo": {
            "RegistrantType": "E",
            "DomainId": "domain-1234abcd",
            "OrganizationName": "tencent cloud",
            "ExpirationDate": "2018-08-08",
            "DomainName": "cloud.tencent.com",
            "RegistrarType": "qcloud",
            "LockEndTime": "",
            "OrganizationNameCN": "腾讯云",
            "RegistrantName": "tencent",
            "DomainStatus": [
                "ok"
            ],
            "BuyStatus": "ok",
            "RegistrantNameCN": "腾讯云",
            "RealNameAuditStatus": "Approved",
            "DomainNameAuditStatus": "Approved",
            "LockTransfer": false,
            "NameServer": [
                "ns2.qq.com",
                "ns4.qq.com",
                "ns3.qq.com",
                "ns1.qq.com"
            ],
            "CreationDate": "2018-08-08",
            "RealNameAuditUnpassReason": "",
            "DomainNameAuditUnpassReason": ""
        },
        "RequestId": "88888888-8888-8888-8888-888888888888",
        "Uin": "100000000001"
    }
}
```

