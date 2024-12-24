**Example 1: 创建模板**

创建模板

Input: 

```
tccli domain CreateTemplate --cli-unfold-argument  \
    --ContactInfo.Province sheng \
    --ContactInfo.OrganizationNameCN xx企业 \
    --ContactInfo.OrganizationName xx企业 \
    --ContactInfo.City shang hai \
    --ContactInfo.CityCN 上海 \
    --ContactInfo.RegistrantName 张三 \
    --ContactInfo.Telephone 1***88 \
    --ContactInfo.ZipCode qweqwe \
    --ContactInfo.RegistrantNameCN qweqwe \
    --ContactInfo.StreetCN asdqw \
    --ContactInfo.Street sdqw \
    --ContactInfo.ProvinceCN sdw \
    --ContactInfo.Country CN \
    --ContactInfo.RegistrantType E \
    --ContactInfo.CountryCN 上海 \
    --ContactInfo.Email **@qq.com \
    --CertificateInfo.CertificateType SFZ \
    --CertificateInfo.CertificateCode 430234123 \
    --CertificateInfo.ImgUrl --
```

Output: 
```
{
    "Response": {
        "RequestId": "ca29ee8d-3034-1234-9060-699a971e9f5f",
        "Template": {
            "AuditReason": "",
            "IsValidTemplate": 1,
            "UpdatedOn": "2024-12-18 12:23:28",
            "AuditStatus": "InAudit",
            "CreatedOn": "2024-12-18 12:23:28",
            "IsBlack": false,
            "InvalidReason": "",
            "CertificateInfo": {
                "OriginImgUrl": "https://domain-***.com/1000***3.jpg",
                "CertificateCode": "***56",
                "RegistrantCertificateCode": "",
                "RegistrantImgUrl": "",
                "RegistrantCertificateType": "",
                "CertificateType": "SFZ",
                "ImgUrl": "https://domain-***.com/1000***3.jpg"
            },
            "TemplateId": "tmpl-***u",
            "UserUin": "***07",
            "ContactInfo": {
                "Province": "shang hai shi",
                "RegistrantType": "I",
                "OrganizationName": "*u",
                "OrganizationNameCN": "*名",
                "Country": "CN",
                "RegistrantName": "*名",
                "ZipCode": "***1",
                "Email": "*@qq.com",
                "City": "shang hai shi",
                "RegistrantNameCN": "*名",
                "StreetCN": "***117号",
                "Street": "***1117 Hao",
                "ProvinceCN": "上海市",
                "CountryCN": "中国",
                "CityCN": "上海市",
                "Telephone": "***29"
            },
            "IsDefault": "no"
        }
    }
}
```

