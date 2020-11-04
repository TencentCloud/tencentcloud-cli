**Example 1: 查询备份配置信息**



Input: 

```
tccli cynosdb DescribeBackupConfig --cli-unfold-argument  \
    --ClusterId cynosdbpg-45knmnra
```

Output: 
```
{
    "Response": {
        "BackupTimeBeg": 7200,
        "BackupTimeEnd": 21600,
        "ReserveDuration": 604800
    }
}
```

