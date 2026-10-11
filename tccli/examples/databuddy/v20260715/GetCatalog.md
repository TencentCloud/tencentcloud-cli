**Example 1: 获取数据目录详情**

获取数据目录详情

Input: 

```
tccli databuddy GetCatalog --cli-unfold-argument  \
    --CatalogName capi_no_delete_table \
    --WorkspaceId 17697667906247629
```

Output: 
```
{
    "Response": {
        "Data": {
            "Catalog": {
                "AssetGuid": "tccatalog.v1.uid3425580874683096126@251436191_ap-guangzhou_CATALOG",
                "Audit": {
                    "CreatedAt": "1778825232449",
                    "Creator": "wedata30-dev@tencent.com",
                    "CreatorName": "wedata30-dev@tencent.com",
                    "LastModifiedAt": "1778825232449",
                    "LastModifier": "wedata30-dev@tencent.com",
                    "LastModifierName": "wedata30-dev@tencent.com"
                },
                "Comment": "",
                "CurrentWorkspacePermissionLevel": 0,
                "Id": "0c4b0b0f-522c-4039-9d7a-63473f85b779",
                "Identifier": "tccatalog.v1.uid3425580874683096126",
                "IsExternal": false,
                "MetaOwner": {
                    "FullName": "capi_no_delete_table",
                    "Owner": "700002164618",
                    "OwnerName": "wedata30-dev@tencent.com",
                    "OwnerType": "user"
                },
                "Name": "capi_no_delete_table",
                "Operator": "wedata30-dev@tencent.com",
                "Properties": [
                    {
                        "Key": "spark.bypass.hive.metastore.jars",
                        "Value": "/opt/spark/hive312/*"
                    }
                ],
                "Status": "2",
                "Tags": [],
                "Type": "TABLE"
            }
        },
        "RequestId": "81b00993-d97c-4dc7-a6f6-c44055b39b1b"
    }
}
```

