**Example 1: 查询备份配置信息**



Input: 

```
tccli cynosdb DescribeBackupConfig --cli-unfold-argument  \
    --ClusterId cynosdbmysql-45knmnra
```

Output: 
```
{
    "Response": {
        "BackupFreq": [
            "full",
            "increment",
            "increment",
            "increment",
            "increment",
            "increment",
            "increment"
        ],
        "BackupType": "",
        "BackupTimeEnd": 21600,
        "BackupTimeBeg": 7200,
        "RequestId": "180877",
        "ReserveDuration": 604800
    }
}
```

