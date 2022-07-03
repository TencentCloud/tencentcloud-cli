**Example 1: 查询集群备份文件下载地址**



Input: 

```
tccli cynosdb DescribeBackupDownloadUrl --cli-unfold-argument  \
    --ClusterId cynosdbmysql-xxxxxxxx \
    --BackupId 1000
```

Output: 
```
{
    "Response": {
        "DownloadUrl": "xxxx",
        "RequestId": "9e56617c-c7cc-44e1-a967-6beb418ad5e7"
    }
}
```

