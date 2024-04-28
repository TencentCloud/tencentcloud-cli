**Example 1: 修改模板**



Input: 

```
tccli domain ModifyTemplate --cli-unfold-argument  \
    --TemplateId 字符串 \
    --CertificateInfo.CertificateCode 字符串 \
    --CertificateInfo.CertificateType 字符串 \
    --CertificateInfo.ImgUrl 字符串 \
    --ContactInfo.OrganizationNameCN 字符串 \
    --ContactInfo.OrganizationName 字符串 \
    --ContactInfo.RegistrantNameCN 字符串 \
    --ContactInfo.RegistrantName 字符串 \
    --ContactInfo.ProvinceCN 字符串 \
    --ContactInfo.Province 字符串 \
    --ContactInfo.CityCN 字符串 \
    --ContactInfo.City 字符串 \
    --ContactInfo.StreetCN 字符串 \
    --ContactInfo.Street 字符串 \
    --ContactInfo.CountryCN 字符串 \
    --ContactInfo.Country 字符串 \
    --ContactInfo.Telephone 字符串 \
    --ContactInfo.Email 字符串 \
    --ContactInfo.ZipCode 字符串 \
    --ContactInfo.RegistrantType 字符串
```

Output: 
```
{
    "Response": {
        "RequestId": "c9308288-2016-4197-bba1-baf0a9ea0a6f",
        "Template": {
            "AuditReason": "",
            "IsValidTemplate": 1,
            "UpdatedOn": "2020-07-30 16:44:04",
            "AuditStatus": "InAudit",
            "CreatedOn": "2020-07-30 16:44:04",
            "InvalidReason": "",
            "CertificateInfo": {
                "CertificateType": "YYZZ",
                "CertificateCode": "441900000553075",
                "ImgUrl": "https://wss-10039692.cos.ap-shanghai.myqcloudXj"
            },
            "TemplateId": "tmpl-3mm9fxug",
            "UserUin": "1213059621",
            "ContactInfo": {
                "Province": "shen zhen shi",
                "RegistrantType": "E",
                "OrganizationName": "niubihonghong",
                "OrganizationNameCN": "牛逼哄哄",
                "Country": "CN",
                "RegistrantName": "niubihonghong",
                "ZipCode": "100011",
                "Email": "1213059621@qq.com",
                "City": "nan shan qu",
                "RegistrantNameCN": "牛逼哄哄",
                "StreetCN": "万利达大厦",
                "Street": "wanlidadasha",
                "ProvinceCN": "深圳市",
                "CountryCN": "中国",
                "CityCN": "南山区",
                "Telephone": "13600147752"
            },
            "IsDefault": "no"
        }
    }
}
```

