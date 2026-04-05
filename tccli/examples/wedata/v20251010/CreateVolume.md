**Example 1: 创建volume**

创建volume

Input: 

```
tccli wedata CreateVolume --cli-unfold-argument  \
    --CatalogName easechen_catalog_volume_test \
    --SchemaName easechen_schema_volume_test1 \
    --VolumeName randyrren \
    --StorageLocation cosn://easechen-zd-251409079/tmp/easechen_catalog_volume_test/easechen_schema_volume_test1/randyrren \
    --Type EXTERNAL
```

Output: 
```
{
    "Response": {
        "Data": {
            "Volume": {
                "Audit": {
                    "CreatedAt": "1761907484350",
                    "Creator": "1290245077@qq.com",
                    "LastModifiedAt": "0",
                    "LastModifier": ""
                },
                "CatalogName": "",
                "Comment": "",
                "Name": "randyrren",
                "Properties": [
                    {
                        "Key": "default-location-name",
                        "Value": "unknown"
                    },
                    {
                        "Key": "tccatalog.identifier",
                        "Value": "tccatalog.v1.uid936586501839923178"
                    }
                ],
                "SchemaName": "",
                "StorageLocation": "cosn://easechen-zd-251409079/tmp/easechen_catalog_volume_test/easechen_schema_volume_test1/randyrren",
                "Type": "external"
            }
        },
        "RequestId": "7ed38d37-b539-42b0-b54a-47012d39a29a"
    }
}
```

