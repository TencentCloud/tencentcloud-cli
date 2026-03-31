**Example 1: wedata3.0资产统一检索**

wedata3.0资产统一检索

Input: 

```
tccli wedata SearchAsset --cli-unfold-argument  \
    --WorkspaceId 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "AssetGuid": "tccatalog.v1.uid4251621611903313274@1300055887_ap-guangzhou_TABLE",
                    "AssetId": "tccatalog.v1.uid4251621611903313274",
                    "AssetName": "xzp_tb2",
                    "AssetType": "TABLE",
                    "Comment": "",
                    "FullName": "xzp_catalog.xzp_schema.xzp_tb2",
                    "Highlighting": [],
                    "ModifiedTime": "1765850565098",
                    "Popularity": "0",
                    "Properties": [],
                    "Tags": [],
                    "WorkspaceFolderPath": "",
                    "WorkspaceId": ""
                },
                {
                    "AssetGuid": "tccatalog.v1.uid1272939539879410265@1300055887_ap-guangzhou_TABLE",
                    "AssetId": "tccatalog.v1.uid1272939539879410265",
                    "AssetName": "xzp_tb1",
                    "AssetType": "TABLE",
                    "Comment": "",
                    "FullName": "xzp_catalog.xzp_schema.xzp_tb1",
                    "Highlighting": [],
                    "ModifiedTime": "1765806822843",
                    "Popularity": "0",
                    "Properties": [],
                    "Tags": [],
                    "WorkspaceFolderPath": "",
                    "WorkspaceId": ""
                },
                {
                    "AssetGuid": "tccatalog.v1.uid1886792928627642738@1300055887_ap-guangzhou_VOLUME",
                    "AssetId": "tccatalog.v1.uid1886792928627642738",
                    "AssetName": "test1",
                    "AssetType": "VOLUME",
                    "Comment": "",
                    "FullName": "micofywang_volume.schema_1.test1",
                    "Highlighting": [],
                    "ModifiedTime": "1763517614039",
                    "Popularity": "0",
                    "Properties": [],
                    "Tags": [],
                    "WorkspaceFolderPath": "",
                    "WorkspaceId": ""
                }
            ],
            "NextPageToken": ""
        },
        "RequestId": "d2df3169-687d-407e-be9e-106c08ff6f29"
    }
}
```

