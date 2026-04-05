**Example 1: 授权catalog**



Input: 

```
tccli wedata GrantPermission --cli-unfold-argument  \
    --Resources.0.ResourceType CATALOG \
    --Resources.0.ResourceUri DataLakeCatalog \
    --Subjects.0.SubjectType User \
    --Subjects.0.SubjectValues 700002164618 \
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
            "OverallSuccess": true,
            "Results": [
                {
                    "Reason": "",
                    "Resource": {
                        "ResourceType": "CATALOG",
                        "ResourceUri": "DataLakeCatalog"
                    },
                    "Result": true
                }
            ]
        },
        "RequestId": "afcbfe75-c2f5-4bd8-9dfd-403294d0e74b"
    }
}
```

