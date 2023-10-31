**Example 1: 查询员工列表（查询已实名员工列表）**

查询已实名员工列表
1. Filter参数Key设置为"Status";
2. Filter参数Values设置为"IsVerified"，表示查询已实名员工；
3. 设置Limit和Offset参数，从首页开始，每页查询20条数据返回。

Input: 

```
tccli essbasic ChannelDescribeEmployees --cli-unfold-argument  \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --Agent.ProxyOperator.OpenId n9527 \
    --Agent.AppId yDxbWUyKxxxxxxxxxxxzjEB8mxCcDjAyF \
    --Filters.0.Key Status \
    --Filters.0.Values IsVerified \
    --Limit 20 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Employees": [
            {
                "CreatedOn": 1658114069,
                "Department": {
                    "DepartmentId": "dp-8a801d51****820e2aed8155f2",
                    "DepartmentName": "test企业"
                },
                "DisplayName": "test",
                "Email": "",
                "Mobile": "123****4567",
                "OpenId": "",
                "Roles": [
                    {
                        "RoleId": "ea4ab302****80dd388e6da6902",
                        "RoleName": "法人"
                    },
                    {
                        "RoleId": "4fcbf3624****df77e30ea6c63",
                        "RoleName": "超级管理员"
                    },
                    {
                        "RoleId": "9b7dcf74ab****b57c9fecf8e9",
                        "RoleName": "业务员"
                    },
                    {
                        "RoleId": "4dff1cea****6fc061010b",
                        "RoleName": "企业员工"
                    }
                ],
                "UserId": "yDRtvUUgygq****O4zjESsMBKpnZs",
                "Verified": true,
                "VerifiedOn": 1658114065,
                "QuiteJob": 0
            }
        ],
        "Limit": 20,
        "Offset": 0,
        "RequestId": "s16635***97576195",
        "TotalCount": 1
    }
}
```

**Example 2: 错误示例-参数不合法**

在使用此接口时，需要按照入参描述进行相应的设置，以确保参数的合法性。如果参数设置不合法，此接口将返回错误信息。
1. 将Limit参数设置为21，超过最大值20。

Input: 

```
tccli essbasic ChannelDescribeEmployees --cli-unfold-argument  \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --Agent.ProxyOperator.OpenId n9527 \
    --Agent.AppId yDxbWUyKxxxxxxxxxxxzjEB8mxCcDjAyF \
    --Filters.0.Key Status \
    --Filters.0.Values IsVerified \
    --Limit 21 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameter.ParamError",
            "Message": "参数Limit不正确"
        },
        "RequestId": "3b506b8a-xxxx-xxxx-xxxx-xxxxx9eaaadd"
    }
}
```

