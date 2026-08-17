**Example 1: 浏览备份目录文件信息**



Input: 

```
tccli bdrc DescribeFileBackupObjects --cli-unfold-argument  \
    --BackupId fb-p7xd1l0k \
    --Path /data/backup \
    --Offset 0 \
    --Limit 20 \
    --OrderField name \
    --Order desc
```

Output: 
```
{
    "Response": {
        "DirList": [],
        "FileList": [
            "/data/backup/test_file.txt"
        ],
        "RequestId": "1ab4775a-68fc-4194-aecf-f4d920eb17b1"
    }
}
```

