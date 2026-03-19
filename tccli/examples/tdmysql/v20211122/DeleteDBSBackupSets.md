**Example 1: 删除备份集**

删除一个手工备份集

Input: 

```
tccli tdmysql DeleteDBSBackupSets --cli-unfold-argument  \
    --InstanceId tdstore-dfasfa \
    --BackupSetIdList 0
```

Output: 
```
{
    "Response": {
        "IsSuccess": true,
        "Total": 0,
        "Deleted": 0,
        "RequestId": "f234c20b-d71a-4abe-af8c-a8ef15df73d8"
    }
}
```

