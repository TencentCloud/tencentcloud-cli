**Example 1: 修改数据卷名**



Input: 

```
tccli tccatalog ModifyVolumeName --cli-unfold-argument  \
    --CatalogName testcatalog \
    --SchemaName testschema \
    --VolumeName testVolume \
    --NewName newname
```

Output: 
```
{
    "Response": {
        "RequestId": "b8sd7dd7-ekd4-4e5e-993e-e5db64fa21c1",
        "Volume": {
            "Name": "",
            "Type": "",
            "StorageLocation": "cos://test1/volume"
        }
    }
}
```

