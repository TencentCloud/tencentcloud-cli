**Example 1: 查询基础备份列表**

查询最新一条备份集记录

Input: 

```
tccli postgres DescribeBaseBackups --cli-unfold-argument  \
    --Limit 1 \
    --Offset 0 \
    --OrderBy FinishTime \
    --OrderByType desc
```

Output: 
```
{
    "Response": {
        "BaseBackupSet": [
            {
                "BackupMethod": "physical",
                "BackupMode": "manual",
                "DBInstanceId": "postgres-9n26zs6n",
                "ExpireTime": "2023-02-18 23:59:59",
                "FinishTime": "2023-02-15 19:09:36",
                "Id": "88d3a71e-b822-5728-9d41-d8cfc0d0556e",
                "Name": "manual-20230215190924.tar.gz",
                "Size": 39845888,
                "StartTime": "2023-02-15 19:09:24",
                "State": "finished"
            }
        ],
        "RequestId": "3f164712-8746-464f-a490-3084a470000e",
        "TotalCount": 10
    }
}
```

