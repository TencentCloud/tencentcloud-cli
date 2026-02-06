**Example 1: 创建备份集**

手工创建一个备份集

Input: 

```
tccli tdmysql CreateDBSBackup --cli-unfold-argument  \
    --InstanceId tdsql3-xxx \
    --BackupMethod physical \
    --BackupType full \
    --BackupName test-backup
```

Output: 
```
{
    "Response": {
        "IsSuccess": true,
        "BackupSetId": 0,
        "RequestId": "fsafdsfasdfasdfsd"
    }
}
```

