**Example 1: 修改模型名称**

修改模型名称

Input: 

```
tccli wedata UpdateVolumeName --cli-unfold-argument  \
    --CatalogName easechen_volume_catalog \
    --SchemaName easechen_volume_schema \
    --VolumeName easechen_volume1 \
    --NewName easechen_volume2
```

Output: 
```
{
    "Response": {
        "Data": {
            "Volume": {
                "Audit": {
                    "CreatedAt": "1762313563576",
                    "Creator": "700002164618",
                    "LastModifiedAt": "1762502748828",
                    "LastModifier": "700002164618"
                },
                "CatalogName": "",
                "Comment": "",
                "MetaOwner": {
                    "FullName": "easechen_volume_catalog.easechen_volume_schema.easechen_volume2",
                    "Owner": "700002164618",
                    "OwnerType": "user"
                },
                "Name": "easechen_volume2",
                "Properties": [
                    {
                        "Key": "default-location-name",
                        "Value": "unknown"
                    },
                    {
                        "Key": "tccatalog.identifier",
                        "Value": "tccatalog.v1.uid2308882229446420174"
                    }
                ],
                "SchemaName": "",
                "StorageLocation": "cosn://easechen-zd-251409079/tmp/easechen_volume_catalog/easechen_volume_schema/easechen_volume",
                "Type": "managed"
            }
        },
        "RequestId": "4c583977-e17f-437e-a64d-375eea29a418"
    }
}
```

