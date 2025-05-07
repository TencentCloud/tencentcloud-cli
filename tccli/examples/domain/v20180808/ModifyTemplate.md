**Example 1: 修改模板**



Input: 

```
tccli domain ModifyTemplate --cli-unfold-argument  \
    --TemplateId tmpl-3mm9fxug \
    --CertificateInfo.CertificateCode 4****075 \
    --CertificateInfo.CertificateType YYZZ \
    --CertificateInfo.ImgUrl image.jpg \
    --ContactInfo.OrganizationNameCN 企业名 \
    --ContactInfo.OrganizationName qiyeming \
    --ContactInfo.RegistrantNameCN 张三 \
    --ContactInfo.RegistrantName zhangsan \
    --ContactInfo.ProvinceCN *市 \
    --ContactInfo.Province 'shen zhen shi' \
    --ContactInfo.CityCN *区 \
    --ContactInfo.City 'nan shan qu' \
    --ContactInfo.StreetCN *大厦 \
    --ContactInfo.Street *sha \
    --ContactInfo.CountryCN 中国 \
    --ContactInfo.Country CN \
    --ContactInfo.Telephone 字13****2 \
    --ContactInfo.Email 121****@qq.com \
    --ContactInfo.ZipCode 100011 \
    --ContactInfo.RegistrantType E
```

Output: 
```
{
    "Response": {
        "RequestId": "c9308288-****-baf0a9ea0a6f",
        "Template": {
            "IsBlack": false,
            "AuditReason": "",
            "IsValidTemplate": 1,
            "UpdatedOn": "2020-07-30 16:44:04",
            "AuditStatus": "InAudit",
            "CreatedOn": "2020-07-30 16:44:04",
            "InvalidReason": "",
            "CertificateInfo": {
                "CertificateType": "YYZZ",
                "CertificateCode": "4****075",
                "ImgUrl": "image.jpg",
                "OriginImgUrl": "image.jpg",
                "RegistrantCertificateType": "",
                "RegistrantCertificateCode": "",
                "RegistrantImgUrl": ""
            },
            "TemplateId": "tmpl-3mm9fxug",
            "UserUin": "1213059621",
            "ContactInfo": {
                "Province": "shen zhen shi",
                "RegistrantType": "E",
                "OrganizationName": "qiyeming",
                "OrganizationNameCN": "企业名",
                "Country": "CN",
                "RegistrantName": "zhangsan",
                "ZipCode": "100011",
                "Email": "121****@qq.com",
                "City": "nan shan qu",
                "RegistrantNameCN": "张三",
                "StreetCN": "*大厦",
                "Street": "*sha",
                "ProvinceCN": "*市",
                "CountryCN": "中国",
                "CityCN": "*区",
                "Telephone": "13****2"
            },
            "IsDefault": "no"
        }
    }
}
```

