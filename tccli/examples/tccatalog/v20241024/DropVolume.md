**Example 1: 删除数据卷**



Input: 

```
tccli tccatalog DropVolume --cli-unfold-argument  \
    --CatalogName testcatalog \
    --SchemaName testschema \
    --VolumeName testVolume
```

Output: 
```
{
    "Response": {
        "RequestId": "b8sd7dd7-ekd4-4e5e-993e-e5db64fa21c1",
        "Dropped": true
    }
}
```

