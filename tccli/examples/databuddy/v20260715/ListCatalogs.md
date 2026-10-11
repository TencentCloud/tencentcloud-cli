**Example 1: 根据类型筛选示例**

根据类型筛选示例

Input: 

```
tccli databuddy ListCatalogs --cli-unfold-argument  \
    --WorkspaceId 17697667906247629 \
    --MaxResults 5
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "AssetGuid": "tccatalog.v1.uid1682010588499561186@251436191_ap-guangzhou_CATALOG",
                    "Audit": {
                        "CreatedAt": "1779363594232",
                        "Creator": "zhipengxue2",
                        "CreatorName": "zhipengxue2",
                        "LastModifiedAt": "1779363606061",
                        "LastModifier": "700002657504",
                        "LastModifierName": "zhipengxue2"
                    },
                    "Comment": "",
                    "CurrentWorkspacePermissionLevel": 2,
                    "Id": "1aa25d21-335f-4dad-a7e6-fda752d7804a",
                    "Identifier": "tccatalog.v1.uid1682010588499561186",
                    "IsExternal": false,
                    "MetaOwner": {
                        "FullName": "afa",
                        "Owner": "700002657504",
                        "OwnerName": "zhipengxue2",
                        "OwnerType": "user"
                    },
                    "Name": "afa",
                    "Operator": "zhipengxue2",
                    "Properties": [
                        {
                            "Key": "gravitino.bypass.catalog-impl",
                            "Value": "org.apache.iceberg.hive.TCLakeHiveCatalog"
                        }
                    ],
                    "Status": "2",
                    "Tags": [],
                    "Type": "TABLE"
                }
            ],
            "NextPageToken": "eyJvZmZzZXQiOjV9"
        },
        "RequestId": "9362aef9-3934-4257-9b87-89e3078d281d"
    }
}
```

