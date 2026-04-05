**Example 1: 批量回收**



Input: 

```
tccli wedata BatchRevokePermission --cli-unfold-argument  \
    --WorkspaceId 17635505654938513 \
    --Items.0.Resource.ResourceType None \
    --Items.0.Resource.ResourceUri None \
    --Items.0.Subject.SubjectType None \
    --Items.0.Subject.SubjectValues None \
    --Items.0.Permissions.0.Name USE_CATALOG \
    --Items.0.Permissions.0.DisplayName None \
    --Items.0.Permissions.0.Description None \
    --Items.0.Permissions.0.IsRead None \
    --Items.0.Permissions.0.IsManage None \
    --Items.0.Permissions.0.Granted None \
    --Items.0.Permissions.0.InheritedObject.ResourceType None \
    --Items.0.Permissions.0.InheritedObject.ResourceUri None \
    --Items.0.Permissions.0.Inherited None \
    --Items.0.Permissions.0.IsEdit None
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
                    "Resource": null,
                    "Result": false,
                    "Subject": null
                }
            ]
        },
        "RequestId": "a0aebbcd-cb86-4e99-a7a6-98b0cd8d11da"
    }
}
```

