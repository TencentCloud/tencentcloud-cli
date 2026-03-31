**Example 1: 创建手工备份**

手工创建一个备份集

Input: 

```
tccli tdmysql CreateDBSBackup --cli-unfold-argument  \
    --BackupMethod physical \
    --BackupType full \
    --InstanceId tdsql3-3f17e49d \
    --BackupName myback
```

Output: 
```
{
    "Response": {
        "BackupSetId": 73165397733012,
        "IsSuccess": true,
        "RequestId": "048bd43c-279c-4d32-97a4-c65b378bf550"
    }
}
```

