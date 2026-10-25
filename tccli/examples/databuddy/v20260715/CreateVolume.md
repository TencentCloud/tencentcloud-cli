**Example 1: 创建数据卷**



Input: 

```
tccli databuddy CreateVolume --cli-unfold-argument  \
    --CatalogName my_catalog \
    --SchemaName my_schema \
    --VolumeName my_volume \
    --StorageLocation cos://my-bucket/path/ \
    --Type MANAGED \
    --WorkspaceId 17697667906247629 \
    --Comment 这是一个数据卷
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

