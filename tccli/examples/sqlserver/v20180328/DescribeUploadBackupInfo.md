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
        "TmpSecretId": "AKID44fDXXXXXXXXXXXXXXXXXXXXXXXXX",
        "TmpSecretKey": "2jWOoltcvf21JIsNUaXXXXXXXXXXXXXXXXXXXXXXXXX",
        "XCosSecurityToken": "J6nJk8Q30PaQwyvn4OF4oOezabX61kra1cf794342ff14c39705aa17584f81650YmAxWf4vkrV2ZK2Gcr_-kzjJ7a_fRRCeQtXd547VoWnmbJ2txpX6Kj_SywpVdS4c4sMrIn2aFir1nmTu--k_a9NDyykODaR2O3n-PP_k84qacwjb-XXXXXXXXXXXXXXXXXXXXXXXXX"
    }
}
```

