**Example 1: 查询全量备份上传密钥**



Input: 

```
tccli sqlserver DescribeUploadBackupInfo --cli-unfold-argument  \
    --InstanceId mssql-rdc0gajn \
    --BackupMigrationId mssql-backup-migration-kpl74n9l
```

Output: 
```
{
    "Response": {
        "BucketName": "cosbacktest-1254065710",
        "ExpiredTime": "1601205149",
        "Path": "251006279/sqlserver/mssql-rdc0gajn/migration/backup/mssql-backup-migration-kpl74n9l/",
        "Region": "ap-guangzhou",
        "RequestId": "6ce2010c-a9c2-474d-860e-f2c8581304eb",
        "StartTime": "1601204649",
        "TmpSecretId": "****************************",
        "TmpSecretKey": "*****************************",
        "CosSecurityToken": "**********************************"
    }
}
```

