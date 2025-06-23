**Example 1: test1**

test1

Input: 

```
tccli wedata DescribeRoleList --cli-unfold-argument  \
    --ProjectId 1554879954290339840
```

Output: 
```
{
    "Response": {
        "Data": {
            "PageNumber": 1,
            "PageSize": 10,
            "Rows": [
                {
                    "CreateTime": null,
                    "CreateTimeStr": "1600938213660",
                    "Creator": null,
                    "Description": "负责项目日常管理，包括成员添加，角色分配等",
                    "DisplayName": "项目管理员",
                    "MemberCount": null,
                    "OperateTime": null,
                    "Operator": null,
                    "Parameters": null,
                    "Privileges": null,
                    "ProjectId": null,
                    "RoleId": "308335260274237440",
                    "RoleName": "ProjectManager",
                    "RoleType": null,
                    "SystemDefault": null,
                    "UpdateTime": null,
                    "UpdateTimeStr": "1629985314500"
                },
                {
                    "CreateTime": null,
                    "CreateTimeStr": "1600938213684",
                    "Creator": null,
                    "Description": "负责数据集成、数据开发和服务开发",
                    "DisplayName": "数据工程师",
                    "MemberCount": null,
                    "OperateTime": null,
                    "Operator": null,
                    "Parameters": null,
                    "Privileges": null,
                    "ProjectId": null,
                    "RoleId": "308335260676890624",
                    "RoleName": "DataEngineer",
                    "RoleType": null,
                    "SystemDefault": null,
                    "UpdateTime": null,
                    "UpdateTimeStr": "1629985314533"
                },
                {
                    "CreateTime": null,
                    "CreateTimeStr": "1600938213690",
                    "Creator": null,
                    "Description": "运维中心，负责平台和业务运维工作，平台运维主要指在私有云环境",
                    "DisplayName": "运维工程师",
                    "MemberCount": null,
                    "OperateTime": null,
                    "Operator": null,
                    "Parameters": null,
                    "Privileges": null,
                    "ProjectId": null,
                    "RoleId": "308335260844662784",
                    "RoleName": "OperationEngineer",
                    "RoleType": null,
                    "SystemDefault": null,
                    "UpdateTime": null,
                    "UpdateTimeStr": "1629985314558"
                },
                {
                    "CreateTime": null,
                    "CreateTimeStr": "1600938213696",
                    "Creator": null,
                    "Description": "只读账号",
                    "DisplayName": "访客",
                    "MemberCount": null,
                    "OperateTime": null,
                    "Operator": null,
                    "Parameters": null,
                    "Privileges": null,
                    "ProjectId": null,
                    "RoleId": "308335260945326080",
                    "RoleName": "Visitor",
                    "RoleType": null,
                    "SystemDefault": null,
                    "UpdateTime": null,
                    "UpdateTimeStr": "1629985314587"
                }
            ],
            "TotalCount": 4,
            "TotalPageNumber": 0
        },
        "RequestId": "8de3d3ad-978c-426b-83bb-f1af8b534ff1"
    }
}
```

