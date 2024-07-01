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
        "Status": "abc",
        "ManagerFirstName": "abc",
        "ManagerMail": "abc",
        "ContactFirstName": "abc",
        "ManagerLastName": "abc",
        "ContactPosition": "abc",
        "ManagerPosition": "abc",
        "VerifyTime": "abc",
        "CreateTime": "abc",
        "ExpireTime": "abc",
        "ContactLastName": "abc",
        "ManagerPhone": "abc",
        "ContactPhone": "abc",
        "ContactMail": "abc",
        "ManagerDepartment": "abc",
        "CompanyInfo": {
            "CompanyName": "abc",
            "CompanyId": 0,
            "CompanyCountry": "abc",
            "CompanyProvince": "abc",
            "CompanyCity": "abc",
            "CompanyAddress": "abc",
            "CompanyPhone": "abc",
            "IdType": "abc",
            "IdNumber": "abc"
        },
        "CompanyId": 0,
        "ManagerId": 0,
        "StatusInfo": [
            {
                "Type": "abc",
                "Status": "abc",
                "CreateTime": "abc",
                "ExpireTime": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

