**Example 1: 查询管理人列表**



Input: 

```
tccli ssl DescribeManagers --cli-unfold-argument  \
    --Offset 0 \
    --ManagerName xx \
    --Limit 0 \
    --CompanyId 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Managers": [
            {
                "Status": "xx",
                "ManagerFirstName": "xx",
                "ManagerPhone": "xx",
                "ManagerLastName": "xx",
                "SubmitAuditTime": "xx",
                "CertCount": 2,
                "ManagerPosition": "xx",
                "VerifyTime": "xx",
                "ManagerId": 22,
                "ExpireTime": "xx",
                "ManagerMail": "xx",
                "StatusInfo": [
                    {}
                ],
                "DomainCount": 2,
                "ManagerDepartment": "xx",
                "CreateTime": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

