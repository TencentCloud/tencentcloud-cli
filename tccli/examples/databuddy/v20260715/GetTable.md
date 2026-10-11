**Example 1: 获取table详情**

获取table详情

Input: 

```
tccli databuddy GetTable --cli-unfold-argument  \
    --CatalogName capi_no_delete_table \
    --SchemaName capi_no_delete_schema \
    --TableName user_info_data \
    --WorkspaceId 17697667906247629
```

Output: 
```
{
    "Response": {
        "Data": {
            "Table": {
                "AssetGuid": "tccatalog.v1.uid3977620717726560546@251436191_ap-guangzhou_TABLE",
                "Audit": {
                    "CreatedAt": "1778828835347",
                    "Creator": "700002164618",
                    "CreatorName": "wedata30-dev@tencent.com",
                    "LastModifiedAt": "1778828835347",
                    "LastModifier": "700002164618",
                    "LastModifierName": "wedata30-dev@tencent.com"
                },
                "Columns": [
                    {
                        "Comment": "",
                        "FieldSetting": "",
                        "IsPrimaryKey": false,
                        "Name": "user_id",
                        "Tags": [],
                        "Type": "long"
                    }
                ],
                "Comment": "",
                "FeatureTableType": "",
                "FilesCount": "",
                "FilesSize": "",
                "Indexes": [],
                "MetaOwner": {
                    "FullName": "capi_no_delete_table.capi_no_delete_schema.user_info_data",
                    "Owner": "700002164618",
                    "OwnerName": "wedata30-dev@tencent.com",
                    "OwnerType": "user"
                },
                "Name": "user_info_data",
                "Partitioning": [],
                "Properties": [
                    {
                        "Key": "write.upsert.enabled",
                        "Value": "false"
                    }
                ],
                "TableFormat": "TCIceberg",
                "TableType": "Managed",
                "Tags": []
            }
        },
        "RequestId": "3e1b2e0c-d4a8-482c-96bf-773a4ce1877d"
    }
}
```

