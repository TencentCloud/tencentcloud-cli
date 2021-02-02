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
        "RequestId": "6d0a1dc1-2782-4456-8f30-901f59f46242",
        "Status": "ok",
        "ManagerFirstName": "xx",
        "ManagerPhone": "xx",
        "ManagerPosition": "xx",
        "ManagerLastName": "xx",
        "ManagerMail": "xx",
        "ContactFirstName": "xx",
        "ContactPhone": "xx",
        "ContactPosition": "xx",
        "ContactLastName": "xx",
        "ContactMail": "xx",
        "ManagerDepartment": "xx",
        "CompanyInfo": {
            "CompanyCity": "xx",
            "CompanyId": 0,
            "CompanyAddress": "xx",
            "CompanyName": "xx",
            "CompanyCountry": "xx",
            "CompanyProvince": "xx",
            "CompanyPhone": "xx"
        },
        "VerifyTime": "xx",
        "ExpireTime": "xx",
        "CompanyId": 0,
        "ManagerId": 23,
        "CreateTime": "xx"
    }
}
```

