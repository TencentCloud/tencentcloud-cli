**Example 1: 查询员工**

不带过滤条件查询员工

Input: 

```
tccli essbasic ChannelDescribeEmployees --cli-unfold-argument  \
    --Agent.ProxyOrganizationOpenId test \
    --Agent.ProxyOperator.OpenId test \
    --Agent.AppId test \
    --Filters.0.Values  \
    --Filters.0.Key  \
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
                "Mobile": "123testtest4567",
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

