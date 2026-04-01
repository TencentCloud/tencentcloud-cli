**Example 1: 查询volume列表**

查询volume列表

Input: 

```
tccli wedata ListVolumes --cli-unfold-argument  \
    --CatalogName easechen_catalog_volume_test \
    --SchemaName easechen_schema_volume_test1 \
    --MaxResults 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "Audit": {
                        "CreatedAt": "1761906784518",
                        "Creator": "1290245077@qq.com",
                        "LastModifiedAt": "0",
                        "LastModifier": ""
                    },
                    "CatalogName": "",
                    "Comment": "",
                    "Name": "volume1",
                    "Properties": [
                        {
                            "Key": "default-location-name",
                            "Value": "unknown"
                        },
                        {
                            "Key": "tccatalog.identifier",
                            "Value": "tccatalog.v1.uid4217204172379907294"
                        }
                    ],
                    "SchemaName": "",
                    "StorageLocation": "cosn://easechen-zd-251409079/tmp/easechen_catalog_volume_test/easechen_schema_volume_test1/volume1",
                    "Type": "external"
                }
            ],
            "NextPageToken": "eyJsaW1pdCI6MSwib2Zmc2V0IjoxfQ==",
            "TotalCount": "2"
        },
        "RequestId": "0df7eb2b-f106-4587-8909-7f891e893b4a"
    }
}
```

