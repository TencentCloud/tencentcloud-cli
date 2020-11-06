**Example 1: 查询迁移任务列表**



Input: 

```
tccli sqlserver DescribeMigrations --cli-unfold-argument  \
    --MigrateName 测试 \
    --Limit 10 \
    --Offset 0 \
    --OrderBy name \
    --OrderByType desc \
    --StatusSet 1 4
```

Output: 
```
{
    "Response": {
        "RequestId": "728ba95f-0443-41ec-82c9-44bc8bfc0802",
        "TotalCount": 2,
        "MigrateTaskSet": [
            {
                "MigrateId": 2734,
                "MigrateName": "测试迁移",
                "AppId": 1251006373,
                "Region": "ap-guangzhou",
                "SourceType": 5,
                "CreateTime": "2018-08-09 11:46:15",
                "StartTime": "0000-00-00 00:00:00",
                "EndTime": "0000-00-00 00:00:00",
                "Status": 1,
                "Message": "",
                "CheckFlag": 0,
                "Progress": 0,
                "MigrateDetail": {
                    "StepName": "",
                    "Progress": 0
                }
            },
            {
                "MigrateId": 2732,
                "MigrateName": "测试接口",
                "AppId": 1251006373,
                "Region": "ap-guangzhou",
                "SourceType": 5,
                "CreateTime": "2018-08-08 21:03:09",
                "StartTime": "0000-00-00 00:00:00",
                "EndTime": "0000-00-00 00:00:00",
                "Status": 1,
                "Message": "",
                "CheckFlag": 0,
                "Progress": 0,
                "MigrateDetail": {
                    "StepName": "",
                    "Progress": 0
                }
            }
        ]
    }
}
```

