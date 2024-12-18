**Example 1: 获取信息模板详情**



Input: 

```
tccli domain DescribeIntlTemplate --cli-unfold-argument  \
    --TemplateId template-1000q
```

Output: 
```
{
    "Response": {
        "Template": {
            "RegistrantContact": {
                "Province": "广东",
                "City": "深圳",
                "Fax": "",
                "AddressLine": "地址",
                "FirstName": "*n",
                "CompanyName": "",
                "JobTitle": "",
                "ZipCode": "**412000",
                "AddressLineTwo": "",
                "Country": "China",
                "LastName": "*i",
                "Phone": "+86.1***55",
                "Email": "***ng@tencent.com"
            },
            "TechnicalContact": {
                "Province": "广东",
                "City": "深圳",
                "Fax": "",
                "AddressLine": "地址",
                "FirstName": "*n",
                "CompanyName": "",
                "JobTitle": "",
                "ZipCode": "**412000",
                "AddressLineTwo": "",
                "Country": "China",
                "LastName": "*i",
                "Phone": "+86.1***55",
                "Email": "***ng@tencent.com"
            },
            "AdminContact": {
                "Province": "广东",
                "City": "深圳",
                "Fax": "",
                "AddressLine": "地址",
                "FirstName": "*n",
                "CompanyName": "",
                "JobTitle": "",
                "ZipCode": "**412000",
                "AddressLineTwo": "",
                "Country": "China",
                "LastName": "*i",
                "Phone": "+86.1***55",
                "Email": "***ng@tencent.com"
            },
            "BillingContact": {
                "Province": "广东",
                "City": "深圳",
                "Fax": "",
                "AddressLine": "地址",
                "FirstName": "*n",
                "CompanyName": "",
                "JobTitle": "",
                "ZipCode": "**412000",
                "AddressLineTwo": "",
                "Country": "China",
                "LastName": "*i",
                "Phone": "+86.1***55",
                "Email": "***ng@tencent.com"
            },
            "CreatedOn": "2024-11-05 07:17:12",
            "TemplateId": "tmpl-***j",
            "TemplateType": "I",
            "UpdatedOn": "2024-11-05 07:17:12",
            "Uin": "20***97",
            "IsDefault": 0
        },
        "RequestId": "9fc66e8f-5f2c-1234-ab51-32b163d14222"
    }
}
```

**Example 2: 获取信息模板详情-错误**



Input: 

```
tccli domain DescribeIntlTemplate --cli-unfold-argument  \
    --TemplateId template-1000q
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InternalError.DescribeTemplateErr",
            "Message": "获取信息模板详情失败"
        },
        "RequestId": "2f36ac98-07f4-4fef-9124-aed4820f5d39"
    }
}
```

