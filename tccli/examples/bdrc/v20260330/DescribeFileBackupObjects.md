**Example 1: 浏览备份目录文件信息**



Input: 

```
tccli bdrc DescribeFileBackupObjects --cli-unfold-argument  \
    --BackupId cosbk-kh0666nx \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "DirList": [
            {
                "ChangeTime": 28800,
                "ModifyTime": 1789491427,
                "Path": "/ali",
                "Size": 29723016,
                "Type": "dir"
            }
        ],
        "FileList": [
            {
                "ChangeTime": 28800,
                "ModifyTime": 1788890030,
                "Path": "/容灾中心AI应用调研.pdf",
                "Size": 476487,
                "Type": "file"
            }
        ],
        "TotalCount": 3,
        "RequestId": "127b9b0a-19ce-4ca0-b0b2-1d5d5a72e27b"
    }
}
```

