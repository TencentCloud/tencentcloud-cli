**Example 1: 获取数据卷详情**



Input: 

```
tccli tccatalog DescribeVolume --cli-unfold-argument  \
    --CatalogName test_catalog_001 \
    --SchemaName test_schema_001 \
    --VolumeName test_volume_001
```

Output: 
```
{
    "Response": {
        "RequestId": "27b2fbff-3345-40a6-9477-add21f717575",
        "Volume": {
            "Audit": {
                "CreatedTime": "2024-11-27 14:25:49",
                "Creator": "600000559549",
                "LastModifiedTime": "2024-11-27T08:15:47.006817181Z",
                "LastModifier": "600000559549"
            },
            "Comment": "aaaab",
            "Name": "test_volume_001",
            "Properties": [
                {
                    "Key": "aaabc",
                    "Value": "ccc"
                }
            ],
            "StorageLocation": "cos://test-a-001-1305424723/test001",
            "Type": "external"
        }
    }
}
```

