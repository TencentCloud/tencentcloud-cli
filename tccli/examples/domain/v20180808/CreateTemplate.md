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
        "RequestId": "sdwqe-dwfq-fwqd-sdqwdf",
        "Template": {
            "AuditReason": "",
            "IsValidTemplate": 0,
            "UpdatedOn": "2020-10-16 00:00:00",
            "AuditStatus": "Approve",
            "CreatedOn": "2020-10-16 00:00:00",
            "InvalidReason": "",
            "CertificateInfo": {
                "CertificateType": "SFZ",
                "CertificateCode": "430234123",
                "ImgUrl": "--"
            },
            "TemplateId": "tmpl-sdqw12",
            "UserUin": "10001",
            "ContactInfo": {
                "Province": "sheng",
                "OrganizationNameCN": "xx企业",
                "OrganizationName": "xx企业",
                "City": "abc",
                "CityCN": "abc",
                "RegistrantName": "张三",
                "Telephone": "13788888888",
                "ZipCode": "qweqwe",
                "RegistrantNameCN": "qweqwe",
                "StreetCN": "asdqw",
                "Street": "sdqw",
                "ProvinceCN": "sdw",
                "Country": "CN",
                "RegistrantType": "E",
                "CountryCN": "abc",
                "Email": "23124@qq.com"
            },
            "IsDefault": "yes"
        }
    }
}
```

