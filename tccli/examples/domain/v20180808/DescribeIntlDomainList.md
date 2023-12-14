**Example 1: 获取域名列表**



Input: 

```
tccli domain DescribeIntlDomainList --cli-unfold-argument  \
    --Offset 20 \
    --Limit 30
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "DomainSet": [
            {
                "Status": "ok",
                "IsPremium": true,
                "DomainId": "domain-dsjiokdq",
                "CanRenewYears": 0,
                "DomainName": "abc.com",
                "RegistrarType": "epp",
                "ModifyStatus": "NotModify",
                "DnsModifyStatus": "NotModify",
                "TemplateId": "temp-123456",
                "WhoisPrivacy": 0,
                "DomainStatus": [
                    "ok"
                ],
                "Uin": "111111",
                "AutoRenew": 0,
                "ExpirationDate": "2025-04-23 17:40:27",
                "Dns": [
                    "f1g1ns1.dnspod.net"
                ],
                "ExpireMessage": 0,
                "DnsStatus": 0,
                "ContactInfo": {
                    "Province": "广东省",
                    "City": "深圳市",
                    "OrganizationName": "张某某",
                    "FirstName": "zhang",
                    "RegistrantType": "I",
                    "Country": "中国",
                    "CompanyName": "张某某",
                    "RegistrantName": "张某某",
                    "Telephone": "138***8888",
                    "ZipCode": "400000",
                    "Street": " 南山一号",
                    "LastName": "moumou",
                    "Email": "12**@qq.com"
                },
                "SupportDnssec": true,
                "CreationDate": "2021-04-23 17:40:27"
            }
        ],
        "RequestId": "3c59eccc-efca-4109-1111-37e2e2bce25f"
    }
}
```

