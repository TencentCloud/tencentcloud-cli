**Example 1: 查询volume名称列表**

查询volume名称列表

Input: 

```
tccli wedata ListVolumeNames --cli-unfold-argument  \
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
                    "Name": "volume1",
                    "Namespace": [
                        "easechen_catalog_volume_test",
                        "easechen_schema_volume_test1"
                    ]
                }
            ],
            "NextPageToken": "eyJsaW1pdCI6MSwib2Zmc2V0IjoxfQ==",
            "TotalCount": "2"
        },
        "RequestId": "5cd613b2-bfa3-426f-b2e9-7800cfdcb8ed"
    }
}
```

