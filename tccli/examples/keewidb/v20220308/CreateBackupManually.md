**Example 1: 示例1**



Input: 

```
tccli keewidb CreateBackupManually --cli-unfold-argument  \
    --InstanceId kee-lagg27el \
    --StorageDays 14 \
    --Remark 备份test
```

Output: 
```
{
    "Response": {
        "RequestId": "9275a3b1-565a-4a0d-90c4-4cd39421160f",
        "TaskId": 1655902385
    }
}
```

