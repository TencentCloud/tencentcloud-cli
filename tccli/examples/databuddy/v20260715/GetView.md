**Example 1: 查询view详情**



Input: 

```
tccli databuddy GetView --cli-unfold-argument  \
    --CatalogName svmgao0710 \
    --SchemaName information_schema \
    --ViewName users \
    --WorkspaceId 17836526087487468 \
    --FetchOption.FetchPermissions True \
    --FetchOption.FetchFeatureTableDetail True
```

Output: 
```
{
    "Response": {
        "Data": {
            "View": {
                "AssetGuid": "tccatalog.v1.uid2710499687237408551@260073493_ap-guangzhou_VIEW",
                "Audit": {
                    "CreatedAt": "1783652631760",
                    "Creator": "700002164619",
                    "CreatorName": "*e*a*a30*t*s****encent.com",
                    "LastModifiedAt": "1783652638078",
                    "LastModifier": "700002164619",
                    "LastModifierName": "we*a***0***s*1***********m"
                },
                "Columns": [
                    {
                        "Comment": "metalake name",
                        "FieldSetting": "",
                        "IsPrimaryKey": false,
                        "Name": "metalake_name",
                        "Tags": [],
                        "Type": "string"
                    }
                ],
                "Comment": "users",
                "MetaOwner": {
                    "FullName": "svmgao0710.information_schema.users",
                    "Owner": "700002164619",
                    "OwnerName": "we*a****-*e******ncent.com",
                    "OwnerType": "user"
                },
                "Name": "users",
                "PermissionDetail": {
                    "CatalogWorkspacePrivilege": "WORKSPACE_READWRITE",
                    "DenyPrivilegeList": [],
                    "Permissions": [
                        "ALL_PRIVILEGES"
                    ]
                },
                "Properties": [
                    {
                        "Key": "tccatalog.identifier",
                        "Value": "tccatalog.v1.uid2710499687237408551"
                    }
                ],
                "Tags": []
            }
        },
        "RequestId": "d2bb3f89-e227-4be9-b528-836883f6f100"
    }
}
```

