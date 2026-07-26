**Example 1: 修改备份集备注**

修改备份集备注

Input: 

```
tccli tdmysql ModifyDBSBackupSetComment --cli-unfold-argument  \
    --InstanceId tdsql3-3f17e49d \
    --BackupSetId 73094409561375 \
    --NewBackupName newBackName
```

Output: 
```
{
    "Response": {
        "IsSuccess": true,
        "Msg": "Modify backup set successfully",
        "RequestId": "570461d1-4936-4f07-8a5f-952c9161544f"
    }
}
```

