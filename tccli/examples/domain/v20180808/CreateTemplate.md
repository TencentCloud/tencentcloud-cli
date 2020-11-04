**Example 1: 创建模板**



Input: 

```
tccli domain CreateTemplate --cli-unfold-argument  \
    --ContactInfo.Province xx\
    --ContactInfo.OrganizationNameCN xx\
    --ContactInfo.OrganizationName xx\
    --ContactInfo.City xx\
    --ContactInfo.CityCN xx\
    --ContactInfo.RegistrantName xx\
    --ContactInfo.Telephone xx\
    --ContactInfo.ZipCode xx\
    --ContactInfo.RegistrantNameCN xx\
    --ContactInfo.StreetCN xx\
    --ContactInfo.Street xx\
    --ContactInfo.ProvinceCN xx\
    --ContactInfo.Country xx\
    --ContactInfo.RegistrantType xx\
    --ContactInfo.CountryCN xx\
    --ContactInfo.Email xx\
    --CertificateInfo.CertificateType xx\
    --CertificateInfo.CertificateCode xx\
    --CertificateInfo.ImgUrl xx
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "Template": {
            "AuditReason": "",
            "IsValidTemplate": 0,
            "UpdatedOn": "2020-10-16 00:00:00",
            "AuditStatus": "Approve",
            "CreatedOn": "2020-10-16 00:00:00",
            "InvalidReason": "",
            "CertificateInfo": {
                "CertificateType": "xx",
                "CertificateCode": "xx",
                "ImgUrl": "xx"
            },
            "TemplateId": "xx",
            "UserUin": "xx",
            "ContactInfo": {
                "Province": "xx",
                "OrganizationNameCN": "xx",
                "OrganizationName": "xx",
                "City": "xx",
                "CityCN": "xx",
                "RegistrantName": "xx",
                "Telephone": "xx",
                "ZipCode": "xx",
                "RegistrantNameCN": "xx",
                "StreetCN": "xx",
                "Street": "xx",
                "ProvinceCN": "xx",
                "Country": "xx",
                "RegistrantType": "xx",
                "CountryCN": "xx",
                "Email": "xx"
            },
            "IsDefault": "xx"
        }
    }
}
```

