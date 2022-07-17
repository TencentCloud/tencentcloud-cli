**Example 1: 查询备份列表**



Input: 

```
tccli sqlserver DescribeBackups --cli-unfold-argument  \
    --InstanceId mssql-njj2mtpl \
    --EndTime 2018-04-20 00:00:00 \
    --Limit 20 \
    --StartTime 2018-03-28 00:00:00 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "863b2797-858b-49f3-88e9-50159e564cbc",
        "TotalCount": 1,
        "Backups": [
            {
                "BackupFormat": "single",
                "BackupName": "mssql-xxx_20220619114124",
                "BackupWay": 0,
                "DBs": [
                    "test_db"
                ],
                "CrossBackupAddr": [
                    {
                        "CrossExternalAddr": "http",
                        "CrossInternalAddr": "http",
                        "CrossRegion": "ap-beijing"
                    }
                ],
                "CrossBackupStatus": [
                    {
                        "CrossRegion": "ap-beijing",
                        "CrossStatus": 1
                    }
                ],
                "EndTime": "2022-06-19 11:54:53",
                "ExternalAddr": "",
                "FileName": "",
                "GroupId": "16556099469691",
                "Id": 0,
                "InternalAddr": "",
                "Size": 20887196,
                "StartTime": "2022-06-19 11:41:24",
                "Status": 1,
                "Strategy": 0,
                "Region": "ap-guangzhou"
            }
        ]
    }
}
```

