**Example 1: openapi权限列表**

openapi权限列表

Input: 

```
tccli wedata ListPermissions --cli-unfold-argument  \
    --Resource.ResourceType Catalog \
    --Resource.ResourceUri sa_tb
```

Output: 
```
{
    "Response": {
        "Data": {
            "Details": [
                {
                    "PermissionDetails": [
                        {
                            "CatalogID": "",
                            "CatalogName": "",
                            "Description": "",
                            "DisplayName": "use schema",
                            "Granted": false,
                            "Inherited": false,
                            "InheritedObject": {
                                "ResourceType": "Catalog",
                                "ResourceUri": "sa_tb"
                            },
                            "IsEdit": false,
                            "IsManage": false,
                            "IsMetaDataPermission": false,
                            "IsRead": false,
                            "Name": "USE_SCHEMA",
                            "WorkSpaceID": "",
                            "WorkSpaceName": ""
                        }
                    ],
                    "Resource": {
                        "ResourceType": "Catalog",
                        "ResourceUri": "sa_tb"
                    },
                    "SubjectDetails": [
                        {
                            "SubjectType": "User",
                            "SubjectTypeDisplayName": "用户",
                            "SubjectValue": "700002285834",
                            "SubjectValueDisplayName": "linaszzhang"
                        }
                    ]
                }
            ],
            "TotalCount": 4
        },
        "RequestId": "3d9fc7dc-2155-4227-a7ec-456dc39d99f2"
    }
}
```

