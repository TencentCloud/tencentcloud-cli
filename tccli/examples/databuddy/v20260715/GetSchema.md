**Example 1: 查询schema详情**

查询schema详情

Input: 

```
tccli databuddy GetSchema --cli-unfold-argument  \
    --CatalogName capi_no_delete_table \
    --SchemaName capi_no_delete_schema \
    --WorkspaceId 17697667906247629 \
    --FetchOption.FetchPermissions True \
    --FetchOption.FetchFeatureTableDetail True \
    --FetchOption.FilterPermissions ["USE_CATALOG"] \
    --FetchOption.FetchOwners True \
    --FetchOption.FetchUserInfo True \
    --FetchOption.FetchMask True \
    --FetchOption.FetchTags True
```

Output: 
```
{
    "Response": {
        "Data": {
            "Schema": {
                "AssetGuid": "tccatalog.v1.uid1482527818963963288@251436191_ap-guangzhou_SCHEMA",
                "Audit": {
                    "CreatedAt": "1778825400056",
                    "Creator": "700002164618",
                    "CreatorName": "wedata30-dev@tencent.com",
                    "LastModifiedAt": "1778825400056",
                    "LastModifier": "700002164618",
                    "LastModifierName": "wedata30-dev@tencent.com"
                },
                "Comment": "",
                "MetaOwner": {
                    "FullName": "capi_no_delete_table.capi_no_delete_schema",
                    "Owner": "700002164618",
                    "OwnerName": "wedata30-dev@tencent.com",
                    "OwnerType": "user"
                },
                "Name": "capi_no_delete_schema",
                "PermissionDetail": {
                    "CatalogWorkspacePrivilege": "WORKSPACE_READWRITE",
                    "DenyPrivilegeList": [],
                    "Permissions": [
                        "ALL_PRIVILEGES"
                    ]
                },
                "Properties": [
                    {
                        "Key": "hive.metastore.database.owner",
                        "Value": "root"
                    }
                ],
                "Tags": []
            }
        },
        "RequestId": "eb8f4015-04e1-4b9b-8aee-633cc1e7a52a"
    }
}
```

