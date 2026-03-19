**Example 1: 修改备份集备注**

修改备份集备注

Input: 

```
tccli tdmysql ModifyDBSBackupSetComment --cli-unfold-argument  \
    --InstanceId tdsql3-31l2r0yn912rg \
    --BackupSetId 28217173338212 \
    --NewBackupName test-manual
```

Output: 
```
{
    "Response": {
        "IsSuccess": true,
        "Msg": "Modify backup set successfully",
        "RequestId": "fa6a683c-5625-402b-9ab1-7b2a82a85fee"
    }
}
```

