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
        "RequestId": "xx",
        "Template": {
            "RegistrantContact": {
                "Province": "xx",
                "City": "xx",
                "Fax": "xx",
                "AddressLine": "xx",
                "FirstName": "xx",
                "CompanyName": "xx",
                "JobTitle": "xx",
                "ZipCode": "xx",
                "AddressLineTwo": "xx",
                "Country": "xx",
                "LastName": "xx",
                "Phone": "xx",
                "Email": "xx"
            },
            "TechnicalContact": {
                "Province": "xx",
                "City": "xx",
                "Fax": "xx",
                "AddressLine": "xx",
                "FirstName": "xx",
                "CompanyName": "xx",
                "JobTitle": "xx",
                "ZipCode": "xx",
                "AddressLineTwo": "xx",
                "Country": "xx",
                "LastName": "xx",
                "Phone": "xx",
                "Email": "xx"
            },
            "CreatedOn": "2020-09-22 00:00:00",
            "AdminContact": {
                "Province": "xx",
                "City": "xx",
                "Fax": "xx",
                "AddressLine": "xx",
                "FirstName": "xx",
                "CompanyName": "xx",
                "JobTitle": "xx",
                "ZipCode": "xx",
                "AddressLineTwo": "xx",
                "Country": "xx",
                "LastName": "xx",
                "Phone": "xx",
                "Email": "xx"
            },
            "Uin": "xx",
            "TemplateId": "xx",
            "BillingContact": {
                "Province": "xx",
                "City": "xx",
                "Fax": "xx",
                "AddressLine": "xx",
                "FirstName": "xx",
                "CompanyName": "xx",
                "JobTitle": "xx",
                "ZipCode": "xx",
                "AddressLineTwo": "xx",
                "Country": "xx",
                "LastName": "xx",
                "Phone": "xx",
                "Email": "xx"
            },
            "UpdatedOn": "2020-09-22 00:00:00",
            "IsDefault": 0
        }
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
        "RequestId": "2f36ac98-07f4-4fef-9124-aed4820f5d39"
    }
}
```

