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
        "RequestId": "099e5c01-42b5-468a-97f8-b76af37fa8d4",
        "TemplateSet": [
            {
                "AuditReason": "注册人审核资料上传失败",
                "IsValidTemplate": 1,
                "UpdatedOn": "2020-07-20 16:05:10",
                "AuditStatus": "Reject",
                "CreatedOn": "2020-07-20 12:44:49",
                "InvalidReason": "",
                "CertificateInfo": {
                    "CertificateType": "YYZZ",
                    "CertificateCode": "888888888888888888",
                    "ImgUrl": "https://xxx.xxx.com/xxxx.jpg"
                },
                "TemplateId": "tmpl-xxxxxxxx",
                "UserUin": "88888888",
                "ContactInfo": {
                    "Province": "guang dong sheng",
                    "RegistrantType": "E",
                    "OrganizationName": "tenxungongsi",
                    "OrganizationNameCN": "tencent公司",
                    "Country": "CN",
                    "RegistrantName": "tencent Gong Si",
                    "ZipCode": "100011",
                    "Email": "tencent@qq.com",
                    "City": "shen zhen shi",
                    "RegistrantNameCN": "腾讯公司",
                    "StreetCN": "深南大道",
                    "Street": "shen nan da dao ",
                    "ProvinceCN": "广东省",
                    "CountryCN": "中国",
                    "CityCN": "深圳市",
                    "Telephone": "4009100100"
                },
                "IsDefault": "yes"
            }
        ]
    }
}
```

