**Example 1: 创建模板**

创建模板

Input: 

```
tccli domain CreateTemplate --cli-unfold-argument  \
    --ContactInfo.Province sheng \
    --ContactInfo.OrganizationNameCN xx企业 \
    --ContactInfo.OrganizationName xx企业 \
    --ContactInfo.City abc \
    --ContactInfo.CityCN abc \
    --ContactInfo.RegistrantName 张三 \
    --ContactInfo.Telephone 13788888888 \
    --ContactInfo.ZipCode qweqwe \
    --ContactInfo.RegistrantNameCN qweqwe \
    --ContactInfo.StreetCN asdqw \
    --ContactInfo.Street sdqw \
    --ContactInfo.ProvinceCN sdw \
    --ContactInfo.Country CN \
    --ContactInfo.RegistrantType E \
    --ContactInfo.CountryCN abc \
    --ContactInfo.Email 23124@qq.com \
    --CertificateInfo.CertificateType SFZ \
    --CertificateInfo.CertificateCode 430234123 \
    --CertificateInfo.ImgUrl --
```

Output: 
```
{
    "Response": {
        "Template": {
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
        },
        "RequestId": "abc"
    }
}
```

