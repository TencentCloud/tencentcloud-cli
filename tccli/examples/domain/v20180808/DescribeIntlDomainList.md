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
                "Status": "xx",
                "IsPremium": true,
                "DomainId": "xx",
                "CanRenewYears": 0,
                "DomainName": "xx",
                "RegistrarType": "xx",
                "ModifyStatus": "xx",
                "DnsModifyStatus": "xx",
                "TemplateId": "xx",
                "WhoisPrivacy": 0,
                "DomainStatus": [
                    "xx"
                ],
                "Uin": "xx",
                "AutoRenew": 0,
                "ExpirationDate": "xx",
                "Dns": [
                    "xx"
                ],
                "ExpireMessage": 0,
                "DnsStatus": 0,
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
            }
        ],
        "RequestId": "xx"
    }
}
```

