**Example 1: 修改数据卷信息**

修改数据卷的名称或注释

Input: 

```
tccli databuddy UpdateVolume --cli-unfold-argument  \
    --CatalogName my_catalog \
    --SchemaName my_schema \
    --VolumeName my_volume \
    --NewComment updated volume comment \
    --WorkspaceId 17697667906247629
```

Output: 
```
{
    "Response": {
        "Data": {
            "Volume": {
                "Name": "my_volume",
                "Comment": "updated volume comment",
                "Type": "EXTERNAL",
                "StorageLocation": "cos://bucket-30-251436191/volume_test"
            }
        },
        "RequestId": "eb32265a-bf2d-4da5-a3e5-683a1abf6197"
    }
}
```

