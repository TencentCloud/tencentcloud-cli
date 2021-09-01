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
            "NameServer": [
                "f1g1ns1.dnspod.net",
                "f1g1ns2.dnspod.net"
            ],
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
            "DomainNameAuditStatus": "Approved",
            "LockTransfer": true,
            "LockEndTime": "2021-12-28 18:00:00"
        },
        "RequestId": "1b76dd88-64d0-4bd1-9cb8-c20de11c3686",
        "Uin": "1111"
    }
}
```

