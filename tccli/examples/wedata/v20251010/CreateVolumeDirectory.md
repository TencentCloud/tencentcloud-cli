**Example 1: 创建文件夹**



Input: 

```
tccli wedata CreateVolumeDirectory --cli-unfold-argument  \
    --CatalogName test_catalog \
    --SchemaName test_schema \
    --VolumeName volume \
    --Path /test
```

Output: 
```
{
    "Response": {
        "Data": {
            "Path": "/"
        },
        "RequestId": "2cd7a473-3667-4c92-bd87-1931754a4d51"
    }
}
```

