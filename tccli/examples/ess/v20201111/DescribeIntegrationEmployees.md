**Example 1: 错误示例-参数不合法**

在使用此接口时，需要按照入参描述进行相应的设置，以确保参数的合法性。如果参数设置不合法，此接口将返回错误信息。
1. 将Limit参数设置为21，超过最大值20。

Input: 

```
tccli ess DescribeIntegrationEmployees --cli-unfold-argument  \
    --Operator.UserId 11234********************678901 \
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

**Example 2: 查询员工列表（查询指定ID的员工）**

接口支持指定ID查询员工，此处以企微账号ID为例查询指定员工
1. Filter参数Key设置为"UserWeWorkOpenId";
2. Filter参数Values设置为具体的企微账号ID；
3. 设置Limit和Offset参数，从首页开始，每页查询20条数据返回。

Input: 

```
tccli ess DescribeIntegrationEmployees --cli-unfold-argument  \
    --Operator.UserId 11234********************678901 \
    --Filters.0.Key UserWeWorkOpenId \
    --Filters.0.Values axxxxxxxa \
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
                "QuiteJob": 0,
                "ReceiveOpenId": "",
                "ReceiveUserId": "",
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
                "WeworkOpenId": "axxxxxxxa"
            }
        ],
        "Limit": 20,
        "Offset": 0,
        "RequestId": "s1663******************195",
        "TotalCount": 1
    }
}
```

**Example 3: 查询员工列表（查询已实名员工列表）**

查询已实名员工列表
1. Filter参数Key设置为"Status";
2. Filter参数Values设置为"IsVerified"，表示查询已实名员工；
3. 设置Limit和Offset参数，从首页开始，每页查询20条数据返回。

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
                    "DepartmentName": "测试企业"
                },
                "DisplayName": "张三",
                "Email": "",
                "Mobile": "13300001233",
                "OpenId": "",
                "QuiteJob": 0,
                "ReceiveOpenId": "",
                "ReceiveUserId": "",
                "Roles": [
                    {
                        "RoleId": "ea4ab3******************a6902",
                        "RoleName": "法人"
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
                "WeworkOpenId": ""
            },
            {
                "CreatedOn": 1658114000,
                "Department": {
                    "DepartmentId": "dp**********************155f2",
                    "DepartmentName": "测试企业"
                },
                "DisplayName": "李四",
                "Email": "",
                "Mobile": "13500001234",
                "OpenId": "",
                "QuiteJob": 0,
                "ReceiveOpenId": "",
                "ReceiveUserId": "",
                "Roles": [
                    {
                        "RoleId": "4fcbf3******************ea6c63",
                        "RoleName": "超级管理员"
                    }
                ],
                "UserId": "yDwJ******************BGQyov",
                "Verified": true,
                "VerifiedOn": 1658114066,
                "WeworkOpenId": ""
            }
        ],
        "Limit": 20,
        "Offset": 0,
        "RequestId": "s1663******************195",
        "TotalCount": 2
    }
}
```

