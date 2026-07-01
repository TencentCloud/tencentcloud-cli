**Example 1: ListGrantablePermissions**

权限点列表

Input: 

```
tccli wedata ListGrantablePermissions --cli-unfold-argument  \
    --ResourceTypes SCHEMA \
    --CatalogType TABLE \
    --Recursive True \
    --WorkspaceID 17623497097012366
```

Output: 
```
{
    "Response": {
        "Data": {
            "Configs": [
                {
                    "CurrentPermissions": {
                        "DependencyPermissions": [
                            {
                                "CatalogID": "",
                                "CatalogName": "",
                                "Condition": "",
                                "Description": "授予使用数据目录权限",
                                "DisplayName": "use catalog",
                                "Granted": false,
                                "Inherited": false,
                                "InheritedObject": null,
                                "IsEdit": true,
                                "IsManage": false,
                                "IsMetaDataPermission": false,
                                "IsRead": true,
                                "Name": "USE_CATALOG",
                                "WorkSpaceID": "",
                                "WorkSpaceName": ""
                            }
                        ],
                        "DisplayName": "",
                        "Permissions": [
                            {
                                "CatalogID": "",
                                "CatalogName": "",
                                "Condition": "",
                                "Description": "授予使用函数权限",
                                "DisplayName": "use function",
                                "Granted": false,
                                "Inherited": false,
                                "InheritedObject": null,
                                "IsEdit": true,
                                "IsManage": false,
                                "IsMetaDataPermission": false,
                                "IsRead": true,
                                "Name": "USE_FUNCTION",
                                "WorkSpaceID": "",
                                "WorkSpaceName": ""
                            }
                        ],
                        "ResourceType": "FUNCTION"
                    },
                    "ManagementPermissions": [
                        {
                            "CatalogID": "",
                            "CatalogName": "",
                            "Condition": "",
                            "Description": "授予当前对象所有权限",
                            "DisplayName": "all privileges",
                            "Granted": false,
                            "Inherited": false,
                            "InheritedObject": null,
                            "IsEdit": false,
                            "IsManage": false,
                            "IsMetaDataPermission": false,
                            "IsRead": false,
                            "Name": "ALL_PRIVILEGES",
                            "WorkSpaceID": "",
                            "WorkSpaceName": ""
                        }
                    ],
                    "PermissionTypes": [
                        "READ"
                    ],
                    "ResourceType": "FUNCTION",
                    "SubPermissions": []
                }
            ]
        },
        "RequestId": "62f0168f-4b93-47ed-9b2e-689b0dc97dd4"
    }
}
```

