**Example 1: 修改集群备份配置**

修改备份配置

Input: 

```
tccli cynosdb ModifyBackupConfig --cli-unfold-argument  \
    --BackupTimeBeg 7200 \
    --ReserveDuration 604800 \
    --ClusterId cynosdbmysql-45knmnra \
    --BackupTimeEnd 21600
```

Output: 
```
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7"
    }
}
```

