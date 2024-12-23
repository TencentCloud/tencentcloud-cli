**Example 1: 修改实例的备份模式**

修改实例的备份模式

Input: 

```
tccli redis ModifyInstanceBackupMode --cli-unfold-argument  \
    --InstanceId crs-asdasdas \
    --BackupMode SecondLevelBackup
```

Output: 
```
{
    "Response": {
        "RequestId": "fa6ec05f-d469-41cd-862f-da6771c4554d",
        "TaskId": 1719562435
    }
}
```

