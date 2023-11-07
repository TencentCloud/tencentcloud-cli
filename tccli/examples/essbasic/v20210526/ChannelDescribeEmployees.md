**Example 1: 查询已实名员工列表**

Filter参数Key设置为"Status",Values设置为"IsVerified"表示查询已实名员工

Input: 

```
tccli essbasic ChannelDescribeEmployees --cli-unfold-argument  \
    --Agent.AppId yDwhxUUckp3gl8j5UuFX33LSNozpRsbi \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --Agent.ProxyOperator.OpenId n9527 \
    --Agent.ProxyAppId  \
    --Filters.0.Key Status \
    --Filters.0.Values IsVerified \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "Employees": [
            {
                "UserId": "yDSLNUUckpossi8fUy98I4ESq4EmlpEd",
                "DisplayName": "张三",
                "Mobile": "18888888888",
                "Email": "",
                "OpenId": "n02468",
                "Roles": [
                    {
                        "RoleId": "yDSLOUUckpojqpkmUEJmzYK68ctIyPFp",
                        "RoleName": "业务员"
                    }
                ],
                "Department": {
                    "DepartmentId": "",
                    "DepartmentName": ""
                },
                "Verified": true,
                "CreatedOn": 1699087891,
                "VerifiedOn": 1699088080,
                "QuiteJob": 0
            },
            {
                "UserId": "yDwi0UUckpohyi32UEdhBFEEbigdd0Dd",
                "DisplayName": "李四",
                "Mobile": "15100000000",
                "Email": "",
                "OpenId": "n123456",
                "Roles": [
                    {
                        "RoleId": "69997f600a7c8e9accc71f4241a8a091",
                        "RoleName": "超级管理员"
                    }
                ],
                "Department": {
                    "DepartmentId": "",
                    "DepartmentName": ""
                },
                "Verified": true,
                "CreatedOn": 1698814301,
                "VerifiedOn": 1698814443,
                "QuiteJob": 0
            }
        ],
        "Offset": 0,
        "Limit": 20,
        "TotalCount": 2,
        "RequestId": "e0461ce0-455c-410b-873b-f33de95f281f"
    }
}
```

**Example 2: 查询某几个员工列表**

Filter参数Key设置为"StaffOpenId",Values设置为员工的OpenId列表

Input: 

```
tccli essbasic ChannelDescribeEmployees --cli-unfold-argument  \
    --Agent.AppId yDwhxUUckp3gl8j5UuFX33LSNozpRsbi \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --Agent.ProxyOperator.OpenId n9527 \
    --Agent.ProxyAppId  \
    --Filters.0.Key StaffOpenId \
    --Filters.0.Values n02468 n123456 \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "Employees": [
            {
                "UserId": "",
                "DisplayName": "张三",
                "Mobile": "18888888888",
                "Email": "",
                "OpenId": "n02468",
                "Roles": [],
                "Department": {
                    "DepartmentId": "",
                    "DepartmentName": ""
                },
                "Verified": false,
                "CreatedOn": 1699095474,
                "VerifiedOn": 0,
                "QuiteJob": 0
            },
            {
                "UserId": "",
                "DisplayName": "李四",
                "Mobile": "15100000000",
                "Email": "",
                "OpenId": "n123456",
                "Roles": [],
                "Department": {
                    "DepartmentId": "",
                    "DepartmentName": ""
                },
                "Verified": false,
                "CreatedOn": 1699095486,
                "VerifiedOn": 0,
                "QuiteJob": 1
            }
        ],
        "Offset": 0,
        "Limit": 20,
        "TotalCount": 2,
        "RequestId": "4ab55898-527c-47d1-a2bd-79b81471b563"
    }
}
```

