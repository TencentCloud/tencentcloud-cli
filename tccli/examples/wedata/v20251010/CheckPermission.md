**Example 1: CheckPermission**

权限校验

Input: 

```
tccli wedata CheckPermission --cli-unfold-argument  \
    --Resources.0.ResourceType METALAKE \
    --Resources.0.ResourceUri default \
    --Permissions.0.Name GRANT_PRIVILEGES
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
                            "CatalogID": "",
                            "CatalogName": "",
                            "Condition": "",
                            "Description": "",
                            "DisplayName": "",
                            "Granted": true,
                            "Inherited": false,
                            "InheritedObject": null,
                            "IsEdit": false,
                            "IsManage": false,
                            "IsMetaDataPermission": false,
                            "IsRead": false,
                            "Name": "GRANT_PRIVILEGES",
                            "WorkSpaceID": "",
                            "WorkSpaceName": ""
                        }
                    ],
                    "Resource": {
                        "ResourceType": "METALAKE",
                        "ResourceUri": "default"
                    }
                }
            ]
        },
        "RequestId": "8396b742-54ee-49b3-b709-6d0155e53427"
    }
}
```

