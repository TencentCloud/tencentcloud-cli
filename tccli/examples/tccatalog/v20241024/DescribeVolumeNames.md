**Example 1: 查询test_catalog_001 下test_schema_001下面的volume 列表**



Input: 

```
tccli tccatalog DescribeVolumeNames --cli-unfold-argument  \
    --CatalogName test_catalog_001 \
    --SchemaName test_schema_001
```

Output: 
```
{
    "Response": {
        "RequestId": "fe543dd5-38ab-414e-8685-0b73314dd030",
        "VolumeNames": [
            {
                "Name": "fileset1",
                "Namespace": [
                    "default",
                    "test_catalog_001",
                    "test_schema_001"
                ]
            },
            {
                "Name": "test_volume_001",
                "Namespace": [
                    "default",
                    "test_catalog_001",
                    "test_schema_001"
                ]
            }
        ]
    }
}
```

