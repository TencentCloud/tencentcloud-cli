**Example 1: 查询管理人列表**



Input: 

```
tccli ssl DescribeManagers --cli-unfold-argument  \
    --CompanyId 0 \
    --Offset 0 \
    --Limit 0 \
    --ManagerName abc \
    --ManagerMail abc \
    --Status abc \
    --SearchKey abc
```

Output: 
```
{
    "Response": {
        "Managers": [
            {
                "Status": "abc",
                "ManagerFirstName": "abc",
                "ManagerLastName": "abc",
                "ManagerPosition": "abc",
                "ManagerPhone": "abc",
                "ManagerMail": "abc",
                "ManagerDepartment": "abc",
                "CreateTime": "abc",
                "DomainCount": 0,
                "CertCount": 0,
                "ManagerId": 0,
                "ExpireTime": "abc",
                "SubmitAuditTime": "abc",
                "VerifyTime": "abc",
                "StatusInfo": [
                    {
                        "Type": "abc",
                        "Status": "abc",
                        "CreateTime": "abc",
                        "ExpireTime": "abc"
                    }
                ]
            }
        ],
        "TotalCount": 0,
        "RequestId": "abc"
    }
}
```

