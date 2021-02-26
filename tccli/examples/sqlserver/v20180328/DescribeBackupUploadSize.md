**Example 1: 查询已上传的全量备份文件列表**



Input: 

```
tccli sqlserver DescribeBackupUploadSize --cli-unfold-argument  \
    --InstanceId mssql-rdc0gajn \
    --BackupMigrationId mssql-backup-migration-kpl74n9l
```

Output: 
```
{
    "Response": {
        "CosUploadBackupFileSet": [
            {
                "FileName": "db1.bak",
                "Size": 172032
            }
        ],
        "RequestId": "15455085-fe18-4c19-a463-5494451fb0f0"
    }
}
```

**Example 2: 查询已上传的增量备份文件列表**



Input: 

```
tccli sqlserver DescribeBackupUploadSize --cli-unfold-argument  \
    --InstanceId mssql-rdc0gajn \
    --BackupMigrationId mssql-backup-migration-cg0ffgqt \
    --IncrementalMigrationId mssql-incremental-migration-kp7bgv8p
```

Output: 
```
{
    "Response": {
        "CosUploadBackupFileSet": [
            {
                "FileName": "db_cvm_1_20200927204209_2log2_2noreconvery2.bak",
                "Size": 28672
            },
            {
                "FileName": "db_cvm_3_20200927204219_2log2_2noreconvery2.bak",
                "Size": 40960
            }
        ],
        "RequestId": "08218621-158d-49df-8366-dfa7958a1ffd"
    }
}
```

