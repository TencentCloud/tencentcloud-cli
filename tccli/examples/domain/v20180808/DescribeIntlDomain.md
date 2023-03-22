**Example 1: 查询域名信息**



Input: 

```
tccli domain DescribeIntlDomain --cli-unfold-argument  \
    --DomainId 0
```

Output: 
```
{
    "Response": {
        "DomainInfo": {
            "Status": "xx",
            "IsPremium": false,
            "DomainId": "xx",
            "CanRenewYears": 0,
            "DomainName": "xx",
            "RegistrarType": "xx",
            "ModifyStatus": "xx",
            "DnsModifyStatus": "xx",
            "TemplateId": "xx",
            "WhoisPrivacy": 0,
            "DomainStatus": [
                ""
            ],
            "Uin": "xx",
            "AutoRenew": 3,
            "ExpirationDate": "xx",
            "Dns": [
                "f1g1ns1.dnspod.net"
            ],
            "ExpireMessage": 3,
            "DnsStatus": 3,
            "ContactInfo": {
                "Province": "xx",
                "City": "xx",
                "OrganizationName": "xx",
                "FirstName": "xx",
                "RegistrantType": "xx",
                "Country": "xx",
                "CompanyName": "xx",
                "RegistrantName": "xx",
                "Telephone": "xx",
                "ZipCode": "xx",
                "Street": "xx",
                "LastName": "xx",
                "Email": "xx"
            },
            "SupportDnssec": true,
            "CreationDate": "xx"
        },
        "RequestId": "xx"
    }
}
```

