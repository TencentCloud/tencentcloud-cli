**Example 1: 查询员工列表**

查询员工列表

Input: 

```
tccli ess DescribeIntegrationEmployees --cli-unfold-argument  \
    --Operator.UserId 11234********************678901 \
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
                    "DepartmentId": "dp**********************155f2",
                    "DepartmentName": "**企业"
                },
                "DisplayName": "**",
                "Email": "",
                "Mobile": "123****4567",
                "OpenId": "",
                "Roles": [
                    {
                        "RoleId": "ea4ab3******************a6902",
                        "RoleName": "法人"
                    },
                    {
                        "RoleId": "4fcbf3******************ea6c63",
                        "RoleName": "超级管理员"
                    },
                    {
                        "RoleId": "9b7d******************cf8e9",
                        "RoleName": "业务员"
                    },
                    {
                        "RoleId": "4dff1******************10b",
                        "RoleName": "企业员工"
                    }
                ],
                "UserId": "yDRt******************BKpnZs",
                "Verified": true,
                "VerifiedOn": 1658114065
            }
        ],
        "Limit": 20,
        "Offset": 0,
        "RequestId": "s1663******************195",
        "TotalCount": 1
    }
}
```

**Example 2: 根据企微账号查询员工**

根据企微账号查询员工

Input: 

```
tccli ess DescribeIntegrationEmployees --cli-unfold-argument  \
    --Operator.UserId 11234********************678901 \
    --Filters.0.Key UserWeWorkOpenId \
    --Filters.0.Values fxxxxxxxf \
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
                    "DepartmentId": "dp**********************155f2",
                    "DepartmentName": "**企业"
                },
                "DisplayName": "**",
                "Email": "",
                "Mobile": "123****4567",
                "OpenId": "",
                "Roles": [
                    {
                        "RoleId": "ea4ab3******************a6902",
                        "RoleName": "法人"
                    },
                    {
                        "RoleId": "4fcbf3******************ea6c63",
                        "RoleName": "超级管理员"
                    },
                    {
                        "RoleId": "9b7d******************cf8e9",
                        "RoleName": "业务员"
                    },
                    {
                        "RoleId": "4dff1******************10b",
                        "RoleName": "企业员工"
                    }
                ],
                "UserId": "yDRt******************BKpnZs",
                "Verified": true,
                "VerifiedOn": 1658114065,
                "WeworkOpenId": "fxxxxxxxf"
            }
        ],
        "Limit": 20,
        "Offset": 0,
        "RequestId": "s1663******************195",
        "TotalCount": 1
    }
}
```

