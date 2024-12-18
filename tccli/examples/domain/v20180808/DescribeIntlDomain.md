**Example 1: 查询域名信息**



Input: 

```
tccli domain DescribeIntlDomain --cli-unfold-argument  \
    --DomainId domain-eowerfeq
```

Output: 
```
{
    "Response": {
        "DomainInfo": {
            "AutoRenew": 1,
            "CreationDate": "2024-11-21",
            "DnsStatus": 1,
            "DomainId": "domain-***8vq",
            "DomainName": "**j.com",
            "DomainStatus": [
                "ok"
            ],
            "Status": "ok",
            "ExpirationDate": "2025-11-21",
            "ExpireMessage": 1,
            "IsPremium": false,
            "Dns": [
                "a.dnspod.com",
                "b.dnspod.com",
                "c.dnspod.com"
            ],
            "CanRenewYears": 9,
            "RegistrarType": "aceville",
            "Uin": "***347",
            "TemplateId": "tmpl-****f",
            "SupportDnssec": false,
            "WhoisPrivacy": 0,
            "ModifyStatus": "",
            "DnsModifyStatus": "",
            "ContactInfo": {
                "City": "***e",
                "Country": "US",
                "Email": "***5@comcast.net",
                "OrganizationName": "***",
                "Province": "IN",
                "RegistrantName": "**ny",
                "RegistrantType": "E",
                "Street": "** Ct",
                "Telephone": "+1.61**",
                "ZipCode": "**02",
                "FirstName": "**h",
                "LastName": "**ny",
                "CompanyName": "**re"
            }
        },
        "RequestId": "6d7bef38-fc4d-1234-978b-fb48b5f4daa3"
    }
}
```

