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
        "Status": "xx",
        "ManagerFirstName": "xx",
        "ManagerMail": "xx",
        "ContactPhone": "xx",
        "ContactMail": "xx",
        "CompanyId": 0,
        "ManagerPosition": "xx",
        "ContactPosition": "xx",
        "ManagerLastName": "xx",
        "VerifyTime": "xx",
        "ManagerId": 23,
        "ExpireTime": "xx",
        "ContactLastName": "xx",
        "ContactFirstName": "xx",
        "StatusInfo": [
            {}
        ],
        "RequestId": "xx",
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
        "ManagerPhone": "xx",
        "CreateTime": "xx"
    }
}
```

