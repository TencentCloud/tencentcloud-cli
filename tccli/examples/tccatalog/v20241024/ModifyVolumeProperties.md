**Example 1: 修改数据卷属性**



Input: 

```
tccli tccatalog ModifyVolumeProperties --cli-unfold-argument  \
    --CatalogName testcatalog \
    --SchemaName testschema \
    --VolumeName testVolume
```

Output: 
```
{
    "Response": {
        "RequestId": "b8sd7dd7-ekd4-4e5e-993e-e5db64fa21c1",
        "Volume": {
            "Name": "testname",
            "Type": "",
            "StorageLocation": ""
        }
    }
}
```

