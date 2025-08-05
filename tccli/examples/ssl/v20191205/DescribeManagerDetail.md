**Example 1: 查询管理人详情**



Input: 

```
tccli ssl DescribeManagerDetail --cli-unfold-argument  \
    --ManagerId 23
```

Output: 
```
{
    "Response": {
        "Status": "ok",
        "ManagerFirstName": "luke",
        "ManagerMail": "luke@qq.com",
        "ContactFirstName": "luke",
        "ManagerLastName": "zhang",
        "ContactPosition": "sre",
        "ManagerPosition": "sre",
        "VerifyTime": "2023-09-11 12:00:00",
        "CreateTime": "2023-09-11 12:00:00",
        "ExpireTime": "2024-09-11 12:00:00",
        "ContactLastName": "zhang",
        "ManagerPhone": "188*******",
        "ContactPhone": "188********",
        "ContactMail": "luke@qq.com",
        "ManagerDepartment": "It",
        "CompanyInfo": {
            "CompanyName": "Tencent",
            "CompanyId": 974321,
            "CompanyCountry": "China",
            "CompanyProvince": "Guangdong",
            "CompanyCity": "Shenzhen",
            "CompanyAddress": "Street*******",
            "CompanyPhone": "021-******",
            "IdType": "IT",
            "IdNumber": "89773"
        },
        "CompanyId": 636448,
        "ManagerId": 36383,
        "StatusInfo": [
            {
                "Type": "ov",
                "Status": "active",
                "CreateTime": "2023-09-11 12:00:00",
                "ExpireTime": "2024-09-11 12:00:00",
                "ManagerPreAuditDomains": [
                    {
                        "Domain": "tencent.com",
                        "CreateTime": "2025-01-01 08:00:00",
                        "ExpireTime": "2026-01-01 08:00:00"
                    }
                ]
            }
        ],
        "RequestId": "14727a68-3b90-4408-99c9-dea6d7de9456"
    }
}
```

