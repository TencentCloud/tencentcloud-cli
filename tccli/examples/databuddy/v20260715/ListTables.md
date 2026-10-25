**Example 1: 获取table列表**

获取table列表

Input: 

```
tccli databuddy ListTables --cli-unfold-argument  \
    --MaxResults 20 \
    --CatalogName DataLakeCatalog \
    --SchemaName ericpuwang_test \
    --WorkspaceId 17678671667189298 \
    --FetchOption.FetchOwners False \
    --FetchOption.FetchUserInfo False \
    --FetchOption.FetchFeatureTableDetail True \
    --FetchOption.FetchPermissions True
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "Name": "lyw_wine_0203_v1",
                    "Comment": "",
                    "Columns": [
                        {
                            "Name": "wine_id",
                            "Type": "integer",
                            "Comment": "红酒样本ID",
                            "FieldSetting": "",
                            "IsPrimaryKey": false,
                            "Tags": []
                        }
                    ],
                    "Properties": [
                        {
                            "Key": "feature_engine_name",
                            "Value": ""
                        }
                    ],
                    "Partitioning": [],
                    "Indexes": [],
                    "Audit": {
                        "Creator": "700002164619",
                        "LastModifier": "700002164619",
                        "CreatedAt": "1770090803564",
                        "LastModifiedAt": "1770090804293",
                        "CreatorName": "700002164619",
                        "LastModifierName": "700002164619"
                    },
                    "TableFormat": "TCIceberg",
                    "AssetGuid": "tccatalog.v1.uid2130426800038882810@260073493_ap-guangzhou_TABLE",
                    "TableType": "Managed",
                    "FilesSize": "",
                    "FilesCount": "",
                    "FeatureTableType": "Offline",
                    "FeatureTableDetail": {
                        "PrimaryKeys": [
                            "wine_id"
                        ],
                        "TimestampField": "event_timestamp",
                        "SourceTableName": "",
                        "WorkflowId": "",
                        "OnlineTableName": ""
                    },
                    "PermissionDetail": {
                        "Permissions": [
                            "ALL_PRIVILEGES"
                        ],
                        "CatalogWorkspacePrivilege": "WORKSPACE_READWRITE",
                        "DenyPrivilegeList": []
                    },
                    "Tags": []
                }
            ],
            "NextPageToken": "eyJvZmZzZXQiOjIwfQ=="
        },
        "RequestId": "c7839865-7824-4b29-986f-176470dc22d8"
    }
}
```

