**Example 1: 查询员工**



Input: 

```
tccli essbasic ChannelDescribeEmployees --cli-unfold-argument  \
    --Operator.ProxyIp  \
    --Operator.ClientIp 0.0.0.1 \
    --Operator.Channel  \
    --Operator.OpenId ******* \
    --Limit 20 \
    --Agent.ProxyAppId xx \
    --Agent.ProxyOrganizationOpenId xx \
    --Agent.ProxyOperator.OpenId xx \
    --Agent.ProxyOperator.ClientIp xx \
    --Agent.ProxyOperator.CustomUserId xx \
    --Agent.ProxyOperator.ProxyIp xx \
    --Agent.ProxyOperator.Channel xx \
    --Agent.ProxyOrganizationId xx \
    --Agent.AppId xx \
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

**Example 2: 测试**



Input: 

```
tccli essbasic ChannelDescribeEmployees --cli-unfold-argument  \
    --Operator.OpenId test1_*****_test1 \
    --Limit 20 \
    --Agent.ProxyAppId ************************ \
    --Agent.AppId 7************************c \
    --Agent.ProxyOrganizationOpenId test1_************_organization1 \
    --Agent.ProxyOperator.OpenId test1_********_test1 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Employees": [
            {
                "CreatedOn": 1658299333,
                "Department": {
                    "DepartmentId": "",
                    "DepartmentName": ""
                },
                "DisplayName": "",
                "Email": "",
                "Mobile": "",
                "OpenId": "",
                "Roles": [],
                "UserId": "",
                "Verified": false,
                "VerifiedOn": 0
            },
            {
                "CreatedOn": 1635494541,
                "Department": {
                    "DepartmentId": "",
                    "DepartmentName": ""
                },
                "DisplayName": "张**",
                "Email": "",
                "Mobile": "1*********0",
                "OpenId": "",
                "Roles": [
                    {
                        "RoleId": "f****************7",
                        "RoleName": "超级管理员"
                    }
                ],
                "UserId": "y***************************N",
                "Verified": true,
                "VerifiedOn": 1635494912
            },
            {
                "CreatedOn": 1661504311,
                "Department": {
                    "DepartmentId": "",
                    "DepartmentName": ""
                },
                "DisplayName": "袁媛",
                "Email": "",
                "Mobile": "17600909519",
                "OpenId": "",
                "Roles": [
                    {
                        "RoleId": "y*********************P",
                        "RoleName": "普通经办员"
                    }
                ],
                "UserId": "y**********************W",
                "Verified": true,
                "VerifiedOn": 1661504471
            },
            {
                "CreatedOn": 1663652732,
                "Department": {
                    "DepartmentId": "",
                    "DepartmentName": ""
                },
                "DisplayName": "陈**",
                "Email": "",
                "Mobile": "13627110845",
                "OpenId": "",
                "Roles": [],
                "UserId": "y***************************I",
                "Verified": true,
                "VerifiedOn": 1663652820
            }
        ],
        "Limit": 20,
        "Offset": 0,
        "RequestId": "5ff98c9f-db0c-4d20-8399-40290a5e4115",
        "TotalCount": 4
    }
}
```

