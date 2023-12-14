**Example 1: 信息模板列表**

信息模板列表

Input: 

```
tccli domain DescribeTemplateList --cli-unfold-argument  \
    --Offset 0 \
    --Limit 20 \
    --Status InAudit \
    --Type E \
    --Keyword abc
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "TemplateSet": [
            {
                "TemplateId": "abc",
                "AuditStatus": "abc",
                "CreatedOn": "abc",
                "UpdatedOn": "abc",
                "UserUin": "abc",
                "IsDefault": "abc",
                "AuditReason": "abc",
                "CertificateInfo": {
                    "CertificateCode": "abc",
                    "CertificateType": "abc",
                    "ImgUrl": "abc",
                    "OriginImgUrl": "abc",
                    "RegistrantCertificateCode": "abc",
                    "RegistrantCertificateType": "abc",
                    "RegistrantImgUrl": "abc"
                },
                "ContactInfo": {
                    "OrganizationNameCN": "abc",
                    "OrganizationName": "abc",
                    "RegistrantNameCN": "abc",
                    "RegistrantName": "abc",
                    "ProvinceCN": "abc",
                    "Province": "abc",
                    "CityCN": "abc",
                    "City": "abc",
                    "StreetCN": "abc",
                    "Street": "abc",
                    "CountryCN": "abc",
                    "Country": "abc",
                    "Telephone": "abc",
                    "Email": "abc",
                    "ZipCode": "abc",
                    "RegistrantType": "abc"
                },
                "IsValidTemplate": 0,
                "InvalidReason": "abc",
                "IsBlack": true
            }
        ],
        "RequestId": "abc"
    }
}
```

