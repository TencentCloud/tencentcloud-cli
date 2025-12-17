**Example 1: 创建数据卷test1**



Input: 

```
tccli tccatalog CreateVolume --cli-unfold-argument  \
    --CatalogName test \
    --SchemaName test \
    --VolumeName test1 \
    --StorageLocation cos://test-a-001-1305424723/test001/ \
    --Comment just test \
    --Type EXTERNAL
```

Output: 
```
{
    "Response": {
        "RequestId": "a83dd4ea-b9fe-4bc5-9fae-18e917ed07bb",
        "Volume": {
            "Name": "test1",
            "Type": "external",
            "StorageLocation": "cos://test-a-001-1305424723/test001",
            "Comment": "just test",
            "Audit": {
                "Creator": "100039364093",
                "CreatedTime": "2024-12-17 17:09:58",
                "LastModifier": "",
                "LastModifiedTime": ""
            }
        }
    }
}
```

