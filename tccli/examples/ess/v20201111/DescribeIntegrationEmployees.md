**Example 1: 测试**



Input: 

```
tccli ess DescribeIntegrationEmployees --cli-unfold-argument  \
    --Operator.ProxyIp  \
    --Operator.ClientIp 0.0.0.1 \
    --Operator.UserId yDRttUUgygquy98pUuO4zjEyE8Z79prN \
    --Operator.Channel  \
    --Operator.OpenId  \
    --Limit 20 \
    --Filters.0.Values  \
    --Filters.0.Key  \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Employees": [
            {
                "CreatedOn": 1658287617,
                "Department": {
                    "DepartmentId": "dp-bd8d1f999c3a4ddaa13d24b83ac3e56c",
                    "DepartmentName": "桂欣测试企业1"
                },
                "DisplayName": "桂欣",
                "Email": "",
                "Mobile": "178****7061",
                "OpenId": "",
                "Roles": [
                    {
                        "RoleId": "d70ec603439cbb813366a2f5f7e9a9a3",
                        "RoleName": "法人"
                    },
                    {
                        "RoleId": "f3040a928cf65729706007db2e406804",
                        "RoleName": "超级管理员"
                    },
                    {
                        "RoleId": "yDRttUUgygquxwuwUuO4zjEBLES6f52M",
                        "RoleName": "test"
                    }
                ],
                "UserId": "yDRttUUgygquy98pUuO4zjEyE8Z79prN",
                "Verified": true,
                "VerifiedOn": 1658287612
            }
        ],
        "Limit": 20,
        "Offset": 0,
        "RequestId": "affa7552-089f-407d-aa5a-3920f357e877",
        "TotalCount": 1
    }
}
```

**Example 2: 查询员工信息**



Input: 

```
tccli ess DescribeIntegrationEmployees --cli-unfold-argument  \
    --Operator.Channel string \
    --Operator.ClientIp 1.1.1.1 \
    --Operator.OpenId 321654 \
    --Operator.ProxyIp 2.2.2.2 \
    --Operator.UserId 11234567890123456789012345678901 \
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
                    "DepartmentId": "dp-8a801d515bb4455f9d820e2aed8155f2",
                    "DepartmentName": "**企业"
                },
                "DisplayName": "**",
                "Email": "",
                "Mobile": "123****4567",
                "OpenId": "",
                "Roles": [
                    {
                        "RoleId": "ea4ab302e702ed48e80dd388e6da6902",
                        "RoleName": "法人"
                    },
                    {
                        "RoleId": "4fcbf3624c0818e32cadf77e30ea6c63",
                        "RoleName": "超级管理员"
                    },
                    {
                        "RoleId": "9b7dcf74abf12192e306b57c9fecf8e9",
                        "RoleName": "业务员"
                    },
                    {
                        "RoleId": "4dff1ceaa8158d917aaf746fc061010b",
                        "RoleName": "企业员工"
                    }
                ],
                "UserId": "yDRtvUUgygqbmbn4UuO4zjESsMBKpnZs",
                "Verified": true,
                "VerifiedOn": 1658114065
            }
        ],
        "Limit": 20,
        "Offset": 0,
        "RequestId": "s1663579381697576195",
        "TotalCount": 1
    }
}
```

