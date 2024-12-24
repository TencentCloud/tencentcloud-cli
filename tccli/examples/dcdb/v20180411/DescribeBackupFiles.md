**Example 1: 查询冷备文件**

查询冷备文件示例

Input: 

```
tccli dcdb DescribeBackupFiles --cli-unfold-argument  \
    --InstanceId tdsqlshard-02badqa3 \
    --ShardId shard-fqj08u7f \
    --BackupType Data \
    --Limit 20 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Files": [
            {
                "BackupType": "Data",
                "EndTime": "2024-12-20 16:29:07",
                "FileName": "cos_xtrabackup+1734683337+20241220+162857+1507806831+xbstream.lz4",
                "FilePath": "cos_backup/tdsql/group_1734680376_202786203/set_1734681147_5/xtrabackup/2024-12-20/cos_xtrabackup+1734683337+20241220+162857+1507806831+xbstream.lz4",
                "FileSize": 13930740,
                "InstanceId": "tdsqlshard-02badqa3",
                "InstanceName": "QT4syxfv8.0",
                "InstanceStatus": 2,
                "ManualBackup": 0,
                "ShardId": "shard-fqj08u7f",
                "StartTime": "2024-12-20 16:28:57",
                "StorageClass": "STANDARD"
            }
        ],
        "RequestId": "549454bd-65ac-4507-8f75-65609c357328",
        "TotalCount": 1
    }
}
```

