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
                "FirstName": "abc",
                "LastName": "abc",
                "CompanyName": "abc",
                "JobTitle": "abc",
                "Country": "abc",
                "Province": "abc",
                "City": "abc",
                "AddressLine": "abc",
                "AddressLineTwo": "abc",
                "ZipCode": "abc",
                "Email": "abc",
                "Phone": "abc",
                "Fax": "abc"
            },
            "AdminContact": {
                "FirstName": "abc",
                "LastName": "abc",
                "CompanyName": "abc",
                "JobTitle": "abc",
                "Country": "abc",
                "Province": "abc",
                "City": "abc",
                "AddressLine": "abc",
                "AddressLineTwo": "abc",
                "ZipCode": "abc",
                "Email": "abc",
                "Phone": "abc",
                "Fax": "abc"
            },
            "TechnicalContact": {
                "FirstName": "abc",
                "LastName": "abc",
                "CompanyName": "abc",
                "JobTitle": "abc",
                "Country": "abc",
                "Province": "abc",
                "City": "abc",
                "AddressLine": "abc",
                "AddressLineTwo": "abc",
                "ZipCode": "abc",
                "Email": "abc",
                "Phone": "abc",
                "Fax": "abc"
            },
            "BillingContact": {
                "FirstName": "abc",
                "LastName": "abc",
                "CompanyName": "abc",
                "JobTitle": "abc",
                "Country": "abc",
                "Province": "abc",
                "City": "abc",
                "AddressLine": "abc",
                "AddressLineTwo": "abc",
                "ZipCode": "abc",
                "Email": "abc",
                "Phone": "abc",
                "Fax": "abc"
            },
            "CreatedOn": "2020-09-22 00:00:00",
            "TemplateId": "abc",
            "TemplateType": "abc",
            "UpdatedOn": "2020-09-22 00:00:00",
            "Uin": "abc",
            "IsDefault": 0
        },
        "RequestId": "abc"
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

