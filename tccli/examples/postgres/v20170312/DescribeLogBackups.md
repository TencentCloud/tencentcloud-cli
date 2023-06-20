**Example 1: 查询日志备份列表**

查询最新一条日志备份记录

Input: 

```
tccli postgres DescribeLogBackups --cli-unfold-argument  \
    --Limit 1 \
    --Offset 0 \
    --OrderBy FinishTime \
    --OrderByType desc
```

Output: 
```
{
    "Response": {
        "LogBackupSet": [
            {
                "BackupMethod": "physical",
                "BackupMode": "automatic",
                "DBInstanceId": "postgres-jdlmoll9",
                "ExpireTime": "2023-02-22 21:10:52",
                "FinishTime": "2023-02-15 21:10:52",
                "Id": "2628bcde-ce13-554a-b47d-2b15187a02ec",
                "Name": "******.tar.gz",
                "Size": 16783360,
                "StartTime": "2023-02-15 21:10:52",
                "State": "finished"
            }
        ],
        "RequestId": "c716c175-6037-4bdd-a35b-2c05399489f3",
        "TotalCount": 10
    }
}
```

