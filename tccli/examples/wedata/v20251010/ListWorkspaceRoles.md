**Example 1: demo**



Input: 

```
tccli wedata ListWorkspaceRoles --cli-unfold-argument  \
    --WorkspaceId 1 \
    --PageRequest.PageNumber 1 \
    --PageRequest.PageSize 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "PageResponse": {
                "PageNumber": 0,
                "PageSize": 0,
                "TotalCount": 3,
                "TotalPageNumber": 3
            },
            "Roles": [
                {
                    "BasicInfo": {
                        "Description": "对工作空间内的所有功能模块都有全读写访问权限",
                        "DisplayName": "工作空间管理员",
                        "Id": "3001",
                        "Name": "Workspace Manager",
                        "RoleType": "workspace"
                    },
                    "MetaData": {
                        "CreateTime": "",
                        "Creator": "",
                        "UpdateTime": "",
                        "Updater": ""
                    },
                    "Permissions": []
                }
            ]
        },
        "RequestId": "4da32a05-31f2-471d-a2c6-4ae85c228f3d"
    }
}
```

