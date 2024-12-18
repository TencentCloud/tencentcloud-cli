**Example 1: 信息模板列表**

信息模板列表

Input: 

```
tccli domain DescribeTemplateList --cli-unfold-argument  \
    --Offset 0 \
    --Limit 20 \
    --Status InAudit \
    --Type E \
    --Keyword search_name
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "TemplateSet": [
            {
                "AuditReason": "",
                "ContactInfo": {
                    "Province": "hu nan sheng",
                    "RegistrantType": "I",
                    "OrganizationName": "org name",
                    "OrganizationNameCN": "企业名称",
                    "Country": "CN",
                    "RegistrantName": "shi ming name",
                    "ZipCode": "425000",
                    "Telephone": "155*********",
                    "City": "ce shi",
                    "RegistrantNameCN": "实名人",
                    "StreetCN": "咸嘉湖街道",
                    "Street": "xian jia hu jie dao",
                    "ProvinceCN": "湖南省",
                    "CityCN": "长沙市",
                    "CountryCN": "中国",
                    "Email": "**d@dnspod.com"
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
        ],
        "RequestId": "skdwd-eoffew-dwdwq-dwdw"
    }
}
```

