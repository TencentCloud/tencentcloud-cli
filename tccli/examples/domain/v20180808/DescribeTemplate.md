**Example 1: 获取模板信息**



Input: 

```
tccli domain DescribeTemplate --cli-unfold-argument  \
    --TemplateId 模板ID
```

Output: 
```
{
    "Response": {
        "RequestId": "0c209d0e-f244-435f-8222-d86741c3edbd",
        "Template": {
            "AuditReason": "",
            "ContactInfo": {
                "Province": "hu nan sheng",
                "RegistrantType": "I",
                "OrganizationName": "yan zheng org name",
                "OrganizationNameCN": "验证的企业名称",
                "Country": "CN",
                "RegistrantName": "registrant name",
                "ZipCode": "425000",
                "Telephone": "155*********",
                "City": "ce shi",
                "RegistrantNameCN": "注册人名称",
                "StreetCN": "咸嘉湖街道",
                "Street": "xian jia hu jie dao",
                "ProvinceCN": "湖南省",
                "CityCN": "长沙市",
                "CountryCN": "中国",
                "Email": "dnspod@dnspod.com"
            },
            "UpdatedOn": "2020-07-28 13:33:55",
            "AuditStatus": "InAudit",
            "IsBlack": false,
            "CreatedOn": "2020-07-28 12:50:23",
            "UserUin": "12334********",
            "IsDefault": "no",
            "TemplateId": "tmpl-dgmgwpe2",
            "InvalidReason": "",
            "IsValidTemplate": 1,
            "CertificateInfo": {
                "CertificateType": "SFZ",
                "CertificateCode": "12345679",
                "ImgUrl": "https://image.com/******",
                "OriginImgUrl": "https://tencentyun.com/******",
                "RegistrantCertificateCode": "12345679",
                "RegistrantCertificateType": "SFZ",
                "RegistrantImgUrl": "https://image.com/******"
            }
        }
    }
}
```

