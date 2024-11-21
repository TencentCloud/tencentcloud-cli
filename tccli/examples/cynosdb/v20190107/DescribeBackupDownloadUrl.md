**Example 1: 查询集群备份文件下载地址**



Input: 

```
tccli cynosdb DescribeBackupDownloadUrl --cli-unfold-argument  \
    --ClusterId cynosdbmysql-dnofdr2d \
    --BackupId 1879681
```

Output: 
```
{
    "Response": {
        "DownloadUrl": "https://ncdb-bj-pitr-1258***699.cos.ap-beijing.myqcloud.com/cynosdb/data/mysqldump/****9fd2-691a-11ef-b99a-b02628437590/2024-10-28/1879681/data_backup_1879681_20241028022147.xb?q-sign-algorithm=sha1&q-ak=************&q-sign-time=1730079993%3B1730123193&q-key-time=1730079993%3B1730123193&q-header-list=host&q-url-param-list=&q-signature=*****************",
        "RequestId": "9e56617c-c7cc-44e1-a967-6beb418ad5e7"
    }
}
```

