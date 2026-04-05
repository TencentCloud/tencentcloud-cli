**Example 1: Catalog权限点**



Input: 

```
tccli wedata ListGrantablePermissions --cli-unfold-argument  \
    --ResourceTypes Catalog \
    --CatalogType LAKEHOUSE
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
                                "Description": "使用数据目录",
                                "DisplayName": "use catalog",
                                "Granted": false,
                                "Inherited": false,
                                "InheritedObject": null,
                                "IsEdit": true,
                                "IsManage": false,
                                "IsRead": true,
                                "Name": "USE_CATALOG"
                            }
                        ],
                        "DisplayName": "",
                        "Permissions": [
                            {
                                "Description": "使用数据目录",
                                "DisplayName": "use catalog",
                                "Granted": false,
                                "Inherited": false,
                                "InheritedObject": null,
                                "IsEdit": true,
                                "IsManage": false,
                                "IsRead": true,
                                "Name": "USE_CATALOG"
                            },
                            {
                                "Description": "修改数据目录",
                                "DisplayName": "alter catalog",
                                "Granted": false,
                                "Inherited": false,
                                "InheritedObject": null,
                                "IsEdit": true,
                                "IsManage": false,
                                "IsRead": false,
                                "Name": "ALTER_CATALOG"
                            },
                            {
                                "Description": "删除数据目录",
                                "DisplayName": "drop catalog",
                                "Granted": false,
                                "Inherited": false,
                                "InheritedObject": null,
                                "IsEdit": true,
                                "IsManage": false,
                                "IsRead": false,
                                "Name": "DROP_CATALOG"
                            },
                            {
                                "Description": "创建Schema",
                                "DisplayName": "create schema",
                                "Granted": false,
                                "Inherited": false,
                                "InheritedObject": null,
                                "IsEdit": true,
                                "IsManage": false,
                                "IsRead": false,
                                "Name": "CREATE_SCHEMA"
                            }
                        ],
                        "ResourceType": "CATALOG"
                    },
                    "ManagementPermissions": [
                        {
                            "Description": "所有权限（不包含用户和角色管理）",
                            "DisplayName": "all privileges",
                            "Granted": false,
                            "Inherited": false,
                            "InheritedObject": null,
                            "IsEdit": false,
                            "IsManage": false,
                            "IsRead": false,
                            "Name": "ALL_PRIVILEGES"
                        },
                        {
                            "Description": "授予权限给他人",
                            "DisplayName": "grant",
                            "Granted": false,
                            "Inherited": false,
                            "InheritedObject": null,
                            "IsEdit": true,
                            "IsManage": false,
                            "IsRead": false,
                            "Name": "GRANT_PRIVILEGES"
                        }
                    ],
                    "PermissionTypes": [
                        "READ",
                        "EDIT"
                    ],
                    "ResourceType": "CATALOG",
                    "SubPermissions": [
                        {
                            "DependencyPermissions": [
                                {
                                    "Description": "使用数据目录",
                                    "DisplayName": "use catalog",
                                    "Granted": false,
                                    "Inherited": false,
                                    "InheritedObject": null,
                                    "IsEdit": true,
                                    "IsManage": false,
                                    "IsRead": true,
                                    "Name": "USE_CATALOG"
                                },
                                {
                                    "Description": "使用Schema",
                                    "DisplayName": "use schema",
                                    "Granted": false,
                                    "Inherited": false,
                                    "InheritedObject": null,
                                    "IsEdit": true,
                                    "IsManage": false,
                                    "IsRead": true,
                                    "Name": "USE_SCHEMA"
                                }
                            ],
                            "DisplayName": "",
                            "Permissions": [
                                {
                                    "Description": "使用Schema",
                                    "DisplayName": "use schema",
                                    "Granted": false,
                                    "Inherited": false,
                                    "InheritedObject": null,
                                    "IsEdit": true,
                                    "IsManage": false,
                                    "IsRead": true,
                                    "Name": "USE_SCHEMA"
                                },
                                {
                                    "Description": "修改schema",
                                    "DisplayName": "alter schema",
                                    "Granted": false,
                                    "Inherited": false,
                                    "InheritedObject": null,
                                    "IsEdit": true,
                                    "IsManage": false,
                                    "IsRead": false,
                                    "Name": "ALTER_SCHEMA"
                                },
                                {
                                    "Description": "删除Schema",
                                    "DisplayName": "drop schema",
                                    "Granted": false,
                                    "Inherited": false,
                                    "InheritedObject": null,
                                    "IsEdit": true,
                                    "IsManage": false,
                                    "IsRead": false,
                                    "Name": "DROP_SCHEMA"
                                },
                                {
                                    "Description": "创建表",
                                    "DisplayName": "create table",
                                    "Granted": false,
                                    "Inherited": false,
                                    "InheritedObject": null,
                                    "IsEdit": true,
                                    "IsManage": false,
                                    "IsRead": false,
                                    "Name": "CREATE_TABLE"
                                },
                                {
                                    "Description": "创建视图",
                                    "DisplayName": "create view",
                                    "Granted": false,
                                    "Inherited": false,
                                    "InheritedObject": null,
                                    "IsEdit": true,
                                    "IsManage": false,
                                    "IsRead": false,
                                    "Name": "CREATE_VIEW"
                                },
                                {
                                    "Description": "创建函数",
                                    "DisplayName": "create function",
                                    "Granted": false,
                                    "Inherited": false,
                                    "InheritedObject": null,
                                    "IsEdit": true,
                                    "IsManage": false,
                                    "IsRead": false,
                                    "Name": "CREATE_FUNCTION"
                                }
                            ],
                            "ResourceType": "SCHEMA"
                        },
                        {
                            "DependencyPermissions": [
                                {
                                    "Description": "使用数据目录",
                                    "DisplayName": "use catalog",
                                    "Granted": false,
                                    "Inherited": false,
                                    "InheritedObject": null,
                                    "IsEdit": true,
                                    "IsManage": false,
                                    "IsRead": true,
                                    "Name": "USE_CATALOG"
                                },
                                {
                                    "Description": "使用Schema",
                                    "DisplayName": "use schema",
                                    "Granted": false,
                                    "Inherited": false,
                                    "InheritedObject": null,
                                    "IsEdit": true,
                                    "IsManage": false,
                                    "IsRead": true,
                                    "Name": "USE_SCHEMA"
                                }
                            ],
                            "DisplayName": "",
                            "Permissions": [
                                {
                                    "Description": "修改表数据或表结构",
                                    "DisplayName": "modify table",
                                    "Granted": false,
                                    "Inherited": false,
                                    "InheritedObject": null,
                                    "IsEdit": true,
                                    "IsManage": false,
                                    "IsRead": false,
                                    "Name": "MODIFY_TABLE"
                                },
                                {
                                    "Description": "查询表数据",
                                    "DisplayName": "select table",
                                    "Granted": false,
                                    "Inherited": false,
                                    "InheritedObject": null,
                                    "IsEdit": true,
                                    "IsManage": false,
                                    "IsRead": true,
                                    "Name": "SELECT_TABLE"
                                },
                                {
                                    "Description": "插入表数据",
                                    "DisplayName": "insert table",
                                    "Granted": false,
                                    "Inherited": false,
                                    "InheritedObject": null,
                                    "IsEdit": true,
                                    "IsManage": false,
                                    "IsRead": false,
                                    "Name": "INSERT_TABLE"
                                },
                                {
                                    "Description": "删除表数据",
                                    "DisplayName": "delete table",
                                    "Granted": false,
                                    "Inherited": false,
                                    "InheritedObject": null,
                                    "IsEdit": true,
                                    "IsManage": false,
                                    "IsRead": false,
                                    "Name": "DELETE_TABLE"
                                },
                                {
                                    "Description": "修改表结构",
                                    "DisplayName": "alter table",
                                    "Granted": false,
                                    "Inherited": false,
                                    "InheritedObject": null,
                                    "IsEdit": true,
                                    "IsManage": false,
                                    "IsRead": false,
                                    "Name": "ALTER_TABLE"
                                },
                                {
                                    "Description": "删除表",
                                    "DisplayName": "drop table",
                                    "Granted": false,
                                    "Inherited": false,
                                    "InheritedObject": null,
                                    "IsEdit": true,
                                    "IsManage": false,
                                    "IsRead": false,
                                    "Name": "DROP_TABLE"
                                }
                            ],
                            "ResourceType": "TABLE"
                        },
                        {
                            "DependencyPermissions": [
                                {
                                    "Description": "使用数据目录",
                                    "DisplayName": "use catalog",
                                    "Granted": false,
                                    "Inherited": false,
                                    "InheritedObject": null,
                                    "IsEdit": true,
                                    "IsManage": false,
                                    "IsRead": true,
                                    "Name": "USE_CATALOG"
                                },
                                {
                                    "Description": "使用Schema",
                                    "DisplayName": "use schema",
                                    "Granted": false,
                                    "Inherited": false,
                                    "InheritedObject": null,
                                    "IsEdit": true,
                                    "IsManage": false,
                                    "IsRead": true,
                                    "Name": "USE_SCHEMA"
                                }
                            ],
                            "DisplayName": "",
                            "Permissions": [
                                {
                                    "Description": "使用函数",
                                    "DisplayName": "use function",
                                    "Granted": false,
                                    "Inherited": false,
                                    "InheritedObject": null,
                                    "IsEdit": true,
                                    "IsManage": false,
                                    "IsRead": true,
                                    "Name": "USE_FUNCTION"
                                },
                                {
                                    "Description": "删除函数",
                                    "DisplayName": "drop function",
                                    "Granted": false,
                                    "Inherited": false,
                                    "InheritedObject": null,
                                    "IsEdit": true,
                                    "IsManage": false,
                                    "IsRead": false,
                                    "Name": "DROP_FUNCTION"
                                },
                                {
                                    "Description": "修改函数",
                                    "DisplayName": "alter function",
                                    "Granted": false,
                                    "Inherited": false,
                                    "InheritedObject": null,
                                    "IsEdit": true,
                                    "IsManage": false,
                                    "IsRead": false,
                                    "Name": "ALTER_FUNCTION"
                                }
                            ],
                            "ResourceType": "FUNCTION"
                        },
                        {
                            "DependencyPermissions": [
                                {
                                    "Description": "使用数据目录",
                                    "DisplayName": "use catalog",
                                    "Granted": false,
                                    "Inherited": false,
                                    "InheritedObject": null,
                                    "IsEdit": true,
                                    "IsManage": false,
                                    "IsRead": true,
                                    "Name": "USE_CATALOG"
                                },
                                {
                                    "Description": "使用Schema",
                                    "DisplayName": "use schema",
                                    "Granted": false,
                                    "Inherited": false,
                                    "InheritedObject": null,
                                    "IsEdit": true,
                                    "IsManage": false,
                                    "IsRead": true,
                                    "Name": "USE_SCHEMA"
                                }
                            ],
                            "DisplayName": "",
                            "Permissions": [
                                {
                                    "Description": "修改视图",
                                    "DisplayName": "alter view",
                                    "Granted": false,
                                    "Inherited": false,
                                    "InheritedObject": null,
                                    "IsEdit": true,
                                    "IsManage": false,
                                    "IsRead": false,
                                    "Name": "ALTER_VIEW"
                                },
                                {
                                    "Description": "删除视图",
                                    "DisplayName": "drop view",
                                    "Granted": false,
                                    "Inherited": false,
                                    "InheritedObject": null,
                                    "IsEdit": true,
                                    "IsManage": false,
                                    "IsRead": false,
                                    "Name": "DROP_VIEW"
                                },
                                {
                                    "Description": "查询视图",
                                    "DisplayName": "select view",
                                    "Granted": false,
                                    "Inherited": false,
                                    "InheritedObject": null,
                                    "IsEdit": true,
                                    "IsManage": false,
                                    "IsRead": true,
                                    "Name": "SELECT_VIEW"
                                }
                            ],
                            "ResourceType": "VIEW"
                        }
                    ]
                }
            ]
        },
        "RequestId": "93f82ddc-f846-4690-a184-3e1a45c29b79"
    }
}
```

