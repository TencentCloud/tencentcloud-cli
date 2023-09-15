**Example 1: 示例-主代子查询**

示例-主代子查询

Input: 

```
tccli ess DescribeIntegrationRoles --cli-unfold-argument  \
    --Filters.0.Key RoleType \
    --Filters.0.Values 1 \
    --Agent.ProxyOrganizationId y**********************J \
    --Operator.UserId y******************5 \
    --Limit 1 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "IntegrateRoles": [
            {
                "IsGroupRole": false,
                "RoleId": "c*************************b",
                "RoleName": "超级管理员",
                "RoleStatus": 1,
                "SubOrgIdList": []
            }
        ],
        "Limit": 1,
        "Offset": 0,
        "RequestId": "s************************1",
        "TotalCount": 8
    }
}
```

**Example 2: 示例-普通企业查询**

示例-普通企业查询

Input: 

```
tccli ess DescribeIntegrationRoles --cli-unfold-argument  \
    --Filters.0.Key RoleType \
    --Filters.0.Values 1 \
    --Operator.UserId y******************5 \
    --Limit 5 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "IntegrateRoles": [
            {
                "IsGroupRole": false,
                "RoleId": "b4******************bf",
                "RoleName": "超级管理员",
                "RoleStatus": 1,
                "SubOrgIdList": []
            },
            {
                "IsGroupRole": false,
                "RoleId": "1**********************1",
                "RoleName": "企业印章管理员",
                "RoleStatus": 1,
                "SubOrgIdList": []
            },
            {
                "IsGroupRole": false,
                "RoleId": "2*********************0",
                "RoleName": "部门业务管理员",
                "RoleStatus": 1,
                "SubOrgIdList": []
            },
            {
                "IsGroupRole": false,
                "RoleId": "3**************************c",
                "RoleName": "业务员",
                "RoleStatus": 1,
                "SubOrgIdList": []
            },
            {
                "IsGroupRole": false,
                "RoleId": "a******************************9",
                "RoleName": "企业合同管理员",
                "RoleStatus": 1,
                "SubOrgIdList": []
            }
        ],
        "Limit": 5,
        "Offset": 0,
        "RequestId": "s*******************",
        "TotalCount": 13
    }
}
```

**Example 3: 示例-查询企业角色列表（返回角色对应的权限树）**

通过添加过滤参数 IsReturnPermissionGroup 可返回角色对应的权限树信息。

Input: 

```
tccli ess DescribeIntegrationRoles --cli-unfold-argument  \
    --Filters.0.Key IsReturnPermissionGroup \
    --Filters.0.Values 1 \
    --Operator.UserId y******************5 \
    --Limit 5 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "IntegrateRoles": [
            {
                "IsGroupRole": false,
                "RoleId": "b4******************bf",
                "RoleName": "超级管理员",
                "RoleStatus": 1,
                "SubOrgIdList": [],
                "PermissionGroups": []
            },
            {
                "IsGroupRole": false,
                "RoleId": "1**********************1",
                "RoleName": "企业印章管理员",
                "RoleStatus": 1,
                "SubOrgIdList": [],
                "PermissionGroups": []
            }
        ],
        "Limit": 5,
        "Offset": 0,
        "RequestId": "s*******************",
        "TotalCount": 2
    }
}
```

