**Example 1: ListWorkspaceRoles**

查询工作空间角色列表

Input: 

```
tccli databuddy ListWorkspaceRoles --cli-unfold-argument  \
    --WorkspaceId 17623497097012366 \
    --NameKeyword 工作空间 \
    --PageNumber 1 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "BasicInfo": {
                        "Description": "对工作空间内的所有功能模块都有全读写访问权限",
                        "DisplayName": "工作空间管理员",
                        "GroupNames": [],
                        "Id": "3001",
                        "Name": "Workspace Manager",
                        "RoleType": "workspace",
                        "Source": 0
                    },
                    "Permissions": []
                }
            ],
            "PageNumber": 1,
            "PageSize": 10,
            "TotalCount": 2,
            "TotalPageNumber": 1
        },
        "RequestId": "591bb402-7a93-4aae-99ae-adf7c2efef48"
    }
}
```

