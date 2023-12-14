**Example 1: 查询域名信息**



Input: 

```
tccli domain DescribeIntlDomain --cli-unfold-argument  \
    --DomainId abc
```

Output: 
```
{
    "Response": {
        "DomainInfo": {
            "AutoRenew": 0,
            "CreationDate": "abc",
            "DomainId": "abc",
            "DnsStatus": 0,
            "DomainName": "abc",
            "DomainStatus": [
                "abc"
            ],
            "Status": "abc",
            "ExpirationDate": "abc",
            "ExpireMessage": 0,
            "IsPremium": true,
            "Dns": [
                "abc"
            ],
            "ContactInfo": {
                "City": "abc",
                "Country": "abc",
                "Email": "abc",
                "OrganizationName": "abc",
                "Province": "abc",
                "RegistrantName": "abc",
                "RegistrantType": "abc",
                "Street": "abc",
                "Telephone": "abc",
                "ZipCode": "abc",
                "FirstName": "abc",
                "LastName": "abc",
                "CompanyName": "abc"
            },
            "CanRenewYears": 0,
            "RegistrarType": "abc",
            "Uin": "abc",
            "TemplateId": "abc",
            "SupportDnssec": true,
            "WhoisPrivacy": 0,
            "ModifyStatus": "abc",
            "DnsModifyStatus": "abc"
        },
        "RequestId": "abc"
    }
}
```

