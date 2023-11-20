**Example 1: 查询可回档的数据库**

查询可回档的数据库

Input: 

```
tccli sqlserver DescribeDBRestoreTime --cli-unfold-argument  \
    --InstanceId mssql-quw892ks \
    --TargetInstanceId mssql-quw892ks \
    --Time 2023-04-11 12:00:00 \
    --BackupId 0 \
    --DBName test_db
```

Output: 
```
{
    "Response": {
        "Details": [
            {
                "NewName": "new_db_test",
                "OldName": "db_test"
            }
        ],
        "RequestId": "424e1df0-9253-11ed-8d88-ffd89b85f329",
        "TotalCount": 1
    }
}
```

