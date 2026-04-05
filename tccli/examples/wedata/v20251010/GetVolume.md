**Example 1: 1**



Input: 

```
tccli wedata GetVolume --cli-unfold-argument  \
    --CatalogName volume_catalog \
    --SchemaName vol1 \
    --VolumeName 12121
```

Output: 
```
{
    "Response": {
        "Data": {
            "Volume": {
                "Audit": {
                    "CreatedAt": "1764745786265",
                    "Creator": "700002164619",
                    "CreatorName": "",
                    "LastModifiedAt": "1764745786265",
                    "LastModifier": "700002164619",
                    "LastModifierName": ""
                },
                "CatalogName": "",
                "Comment": "ada",
                "MetaOwner": {
                    "FullName": "volume_catalog.vol1.12121",
                    "Owner": "700002164619",
                    "OwnerName": "",
                    "OwnerType": "user"
                },
                "Name": "12121",
                "Properties": [
                    {
                        "Key": "storage-type",
                        "Value": "tclake-standard"
                    },
                    {
                        "Key": "default-location-name",
                        "Value": "unknown"
                    },
                    {
                        "Key": "tccatalog.identifier",
                        "Value": "tccatalog.v1.uid3073858068247592413"
                    }
                ],
                "SchemaName": "",
                "StorageLocation": "cosn://251409079/tmp/volume_catalog/vol1/12121",
                "Type": "external"
            }
        },
        "RequestId": "82c24c3a-7a65-444a-825e-6836132775e5"
    }
}
```

