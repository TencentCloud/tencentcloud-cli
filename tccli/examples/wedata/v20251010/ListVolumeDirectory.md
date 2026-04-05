**Example 1: 查看文件夹**



Input: 

```
tccli wedata ListVolumeDirectory --cli-unfold-argument  \
    --CatalogName newvolume \
    --SchemaName schema_01 \
    --VolumeName legendlu \
    --Path / \
    --PageNumber 0 \
    --PageSize 10
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
                    "Name": "legendlu_00",
                    "Path": "gvfs://fileset/newvolume/schema_01/legendlu/legendlu_00",
                    "Size": "0"
                }
            ],
            "TotalCount": "1"
        },
        "RequestId": "6a05f37c-afe8-460b-992f-95778e4808b8"
    }
}
```

