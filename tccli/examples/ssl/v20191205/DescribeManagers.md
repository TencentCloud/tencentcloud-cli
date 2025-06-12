**Example 1: 查询管理人列表**



Input: 

```
tccli ssl DescribeManagers --cli-unfold-argument  \
    --CompanyId 89002 \
    --Offset 0 \
    --Limit 10 \
    --ManagerName luke \
    --ManagerMail luke@qq.com \
    --Status ok \
    --SearchKey luke
```

Output: 
```
{
    "Response": {
        "Managers": [
            {
                "Status": "ok",
                "ManagerFirstName": "luke",
                "ManagerLastName": "zhang",
                "ManagerPosition": "SRE",
                "ManagerPhone": "18*******99",
                "ManagerMail": "luke@qq.com",
                "ManagerDepartment": "IT",
                "CreateTime": "2021-09-11 12:00:00",
                "DomainCount": 0,
                "CertCount": 0,
                "ManagerId": 0,
                "ExpireTime": "2022-09-11 12:00:00",
                "SubmitAuditTime": "2022-08-11 12:00:00",
                "VerifyTime": "2022-09-01 12:00:00",
                "StatusInfo": [
                    {
                        "Type": "ov",
                        "Status": "active",
                        "CreateTime": "2021-09-11 12:00:00",
                        "ExpireTime": "2022-09-11 12:00:00",
                        "ManagerPreAuditDomains": []
                    }
                ]
            }
        ],
        "TotalCount": 0,
        "RequestId": "14727a68-3b90-4408-99c9-dea6d7de9456"
    }
}
```

