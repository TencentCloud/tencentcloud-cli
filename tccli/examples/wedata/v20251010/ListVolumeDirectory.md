**Example 1: 查询Volume文件夹**



Input: 

```
tccli wedata ListVolumeDirectory --cli-unfold-argument  \
    --CatalogName newvolume \
    --SchemaName schema_01 \
    --VolumeName data2 \
    --Path / \
    --PageNumber 0 \
    --PageSize 10 \
    --Keywords yy
```

Output: 
```
{
    "Response": {
        "Data": {
            "Files": [
                {
                    "CreatedTime": "0",
                    "FileType": 2,
                    "IsDirectory": true,
                    "ModifiedTime": "0",
                    "Name": "yy0408",
                    "Path": "gvfs://fileset/newvolume/schema_01/data2/yy0408",
                    "Size": "0"
                }
            ],
            "TotalCount": "1"
        },
        "RequestId": "b0c6aa30-0d14-423f-9120-426ad94c5ccc"
    }
}
```

