**Example 1: 删除备份集**

删除一个手工备份集

Input: 

```
tccli tdmysql DeleteDBSBackupSets --cli-unfold-argument  \
    --InstanceId tdsql3-3f17e49d \
    --BackupSetIdList 73165397733012
```

Output: 
```
{
    "Response": {
        "Deleted": 1,
        "IsSuccess": true,
        "Total": 1,
        "RequestId": "bb46e0a1-2e6f-4483-9317-78197c170bdc"
    }
}
```

