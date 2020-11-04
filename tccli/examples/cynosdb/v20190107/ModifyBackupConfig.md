**Example 1: 修改集群备份配置**



Input: 

```
tccli cynosdb ModifyBackupConfig --cli-unfold-argument  \
    --ClusterId cynosdbpg-45knmnra\
    --BackupTimeBeg 7200\
    --BackupTimeEnd 21600\
    --ReserveDuration 604800
```

Output: 
```
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7"
    }
}
```

