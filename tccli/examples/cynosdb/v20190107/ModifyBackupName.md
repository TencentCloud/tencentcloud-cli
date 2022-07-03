**Example 1: 修改备份文件备注名**



Input: 

```
tccli cynosdb ModifyBackupName --cli-unfold-argument  \
    --ClusterId cynosdbmysql-xxxxxxxx \
    --BackupId 1000 \
    --BackupName backupfile-01
```

Output: 
```
{
    "Response": {
        "RequestId": "9e56617c-c7cc-44e1-a967-6beb418ad5e7"
    }
}
```

