**Example 1: 获取实例备份列表**

该接口用于获取实例的备份列表

Input: 

```
tccli mariadb DescribeBackupFiles --cli-unfold-argument  \
    --InstanceId tdsql-02badqa3 \
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
                "FilePath": "cos_backup/tdsql/set_1734680376_202786203/xtrabackup/2024-12-20/cos_xtrabackup+1734683337+20241220+162857+1507806831+xbstream.lz4",
                "FileSize": 13930740,
                "InstanceId": "tdsql-02badqa3",
                "InstanceName": "QT4syxfv8.0",
                "InstanceStatus": 2,
                "ManualBackup": 0,
                "ShardId": "",
                "StartTime": "2024-12-20 16:28:57",
                "StorageClass": "STANDARD"
            }
        ],
        "RequestId": "549454bd-65ac-4507-8f75-65609c357328",
        "TotalCount": 1,
        "UrlPrefix": "http://newdtsdev-1301792469.cos.ap-guangzhou.myqcloud.com"
    }
}
```

