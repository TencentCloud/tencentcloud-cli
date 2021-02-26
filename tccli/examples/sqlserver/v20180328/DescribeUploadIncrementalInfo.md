**Example 1: 查询上传增量备份信息**



Input: 

```
tccli sqlserver DescribeUploadIncrementalInfo --cli-unfold-argument  \
    --InstanceId mssql-rdc0gajn \
    --BackupMigrationId mssql-backup-migration-cg0ffgqt \
    --IncrementalMigrationId mssql-incremental-migration-kp7bgv8p
```

Output: 
```
{
    "Response": {
        "BucketName": "cosbacktest-1254065710",
        "ExpiredTime": "1601211711",
        "Path": "251006279/sqlserver/mssql-rdc0gajn/migration/backup/mssql-backup-migration-cg0ffgqt/increment/mssql-incremental-migration-kp7bgv8p/",
        "Region": "ap-guangzhou",
        "RequestId": "8498f427-5b9b-42c8-b587-74fad369f27c",
        "StartTime": "1601211211",
        "TmpSecretId": "AKIDOxJelHkinofTdXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
        "TmpSecretKey": "gzfh3Olpe5HKiviXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
        "XCosSecurityToken": "S0niafv9wK40qvkDv2OjmEc2J7DAJRRa7b8c49fac8faf31d51469d4c639c866eKiE4vy8Y1d36neOhi1yg4RD4q9J4MeUyVSNsdiEt1z8X5zVFLGvGayDCfuA2uNuA5aoUSytd3CZzviKkGN-_Nq4OrIdSMzfeM-SrY3OEkV9TRItcig0PtpUYocSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    }
}
```

