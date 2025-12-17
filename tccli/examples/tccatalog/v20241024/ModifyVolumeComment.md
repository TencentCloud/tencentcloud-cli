**Example 1: 修改数据卷描述**



Input: 

```
tccli tccatalog ModifyVolumeComment --cli-unfold-argument  \
    --CatalogName testcatalog \
    --SchemaName testschema \
    --VolumeName testVolume \
    --NewComment comment
```

Output: 
```
{
    "Response": {
        "RequestId": "b8sd7dd7-ekd4-4e5e-993e-e5db64fa21c1",
        "Volume": {
            "Type": "",
            "Name": "",
            "StorageLocation": "cosn://test/location"
        }
    }
}
```

