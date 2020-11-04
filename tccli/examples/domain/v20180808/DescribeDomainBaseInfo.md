**Example 1: 获取域名基础信息**



Input: 

```
tccli domain DescribeDomainBaseInfo --cli-unfold-argument  \
    --Domain 域名
```

Output: 
```
{
    "Response": {
        "DomainInfo": {
            "DomainId": "domain-xxxxx",
            "DomainName": "tencent.com",
            "RegistrarType": "epp",
            "DomainStatus": [
                "ok"
            ],
            "BuyStatus": "ok",
            "RealNameAuditUnpassReason": "",
            "DomainNameAuditUnpassReason": "",
            "RealNameAuditStatus": "Approved",
            "ExpirationDate": "2020-11-14",
            "CreationDate": "2019-11-14",
            "DomainNameAuditStatus": "Approved"
        },
        "RequestId": "1b76dd88-64d0-4bd1-9cb8-c20de11c3686"
    }
}
```

