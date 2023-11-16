**Example 1: 开启、关闭跨地域备份策略**



Input: 

```
tccli sqlserver ModifyCrossBackupStrategy --cli-unfold-argument  \
    --InstanceId mssql-7vfv3rk3 \
    --InstanceIdSet mssql-7vfv3rk3 \
    --CrossBackupEnabled enable \
    --CrossBackupSaveDays 7 \
    --CrossBackupRegion ap-guangzhou \
    --CleanUpCrossBackup 1
```

Output: 
```
{
    "Response": {
        "RequestId": "fc765108-efcd-11ec-887f-525400853186"
    }
}
```

