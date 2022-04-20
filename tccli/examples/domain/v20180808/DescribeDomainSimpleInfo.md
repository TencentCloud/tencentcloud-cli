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
            "RegistrantType": "xx",
            "DomainId": "xx",
            "OrganizationName": "xx",
            "DomainName": "xx",
            "RegistrarType": "xx",
            "RegistrantName": "xx",
            "OrganizationNameCN": "xx",
            "LockEndTime": "xx",
            "DomainStatus": [
                "ok"
            ],
            "BuyStatus": "xx",
            "RegistrantNameCN": "xx",
            "RealNameAuditStatus": "xx",
            "ExpirationDate": "xx",
            "LockTransfer": true,
            "NameServer": [
                "f1g1ns1.dnspod.net",
                "f1g1ns2.dnspod.net"
            ],
            "CreationDate": "xx",
            "RealNameAuditUnpassReason": "xx",
            "DomainNameAuditStatus": "xx",
            "DomainNameAuditUnpassReason": "xx"
        },
        "RequestId": "xx",
        "Uin": "xx"
    }
}
```

