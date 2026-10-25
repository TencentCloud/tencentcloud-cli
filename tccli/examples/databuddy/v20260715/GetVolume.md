**Example 1: 获取数据卷详情**



Input: 

```
tccli databuddy GetVolume --cli-unfold-argument  \
    --CatalogName my_catalog \
    --SchemaName my_schema \
    --VolumeName my_volume \
    --WorkspaceId 17697667906247629
```

Output: 
```
{
    "Response": {
        "RequestId": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        "Data": {
            "Volume": {
                "Name": "my_volume",
                "StorageLocation": "cos://my-bucket/path/"
            }
        }
    }
}
```

