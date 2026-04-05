**Example 1: 快捷检索**

快捷检索

Input: 

```
tccli wedata SearchAssetQuickly --cli-unfold-argument  \
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
                    "FullName": "xzp_catalog.xzp_schema.xzp_tb2",
                    "LastViewTime": "",
                    "WorkspaceFolderPath": "",
                    "WorkspaceId": "1"
                },
                {
                    "AssetGuid": "tccatalog.v1.uid1886792928627642738@1300055887_ap-guangzhou_VOLUME",
                    "AssetId": "tccatalog.v1.uid1886792928627642738",
                    "AssetName": "test1",
                    "AssetType": "VOLUME",
                    "FullName": "micofywang_volume.schema_1.test",
                    "LastViewTime": "",
                    "WorkspaceFolderPath": "",
                    "WorkspaceId": "1"
                }
            ],
            "NextPageToken": ""
        },
        "RequestId": "ca2aafbb-117b-410e-a128-ce851b87c4be"
    }
}
```

