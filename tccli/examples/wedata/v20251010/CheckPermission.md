**Example 1: 检查权限**



Input: 

```
tccli wedata CheckPermission --cli-unfold-argument  \
    --Resources.0.ResourceType Catalog \
    --Resources.0.ResourceUri DataLakeCatalog \
    --Permissions.0.Name USE_CATALOG \
    --Permissions.0.DisplayName None \
    --Permissions.0.Description None \
    --Permissions.0.IsRead None \
    --Permissions.0.IsManage None \
    --Permissions.0.Granted None \
    --Permissions.0.InheritedObject.ResourceType None \
    --Permissions.0.InheritedObject.ResourceUri None \
    --Permissions.0.Inherited None \
    --Permissions.0.IsEdit None
```

Output: 
```
{
    "Response": {
        "Data": {
            "Results": [
                {
                    "PermissionResults": [
                        {
                            "Description": "",
                            "DisplayName": "",
                            "Granted": true,
                            "Inherited": false,
                            "InheritedObject": null,
                            "IsEdit": false,
                            "IsManage": false,
                            "IsRead": false,
                            "Name": "USE_CATALOG"
                        }
                    ],
                    "Resource": {
                        "ResourceType": "Catalog",
                        "ResourceUri": "DataLakeCatalog"
                    }
                }
            ]
        },
        "RequestId": "922e97ba-8209-4cc2-b7c8-e03ccd2bce35"
    }
}
```

