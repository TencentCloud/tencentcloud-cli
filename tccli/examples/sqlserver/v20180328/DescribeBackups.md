**Example 1: 查询备份列表**



Input: 

```
tccli sqlserver DescribeBackups --cli-unfold-argument  \
    --InstanceId mssql-njj2mtpl \
    --StartTime '2018-03-28 00:00:00' \
    --EndTime '2018-04-20 00:00:00' \
    --Limit 20 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "863b2797-858b-49f3-88e9-50159e564cbc",
        "TotalCount": 2,
        "Backups": [
            {
                "Id": 49760,
                "BackupName": "mssql-3l3fgqn7_202007302200",
                "FileName": "manual_instance_58001_20180702160920.bak.tar",
                "StartTime": "2018-07-02 16:09:20",
                "EndTime": "2018-07-02 16:09:20",
                "Size": 192,
                "Strategy": 0,
                "GroupId": 0,
                "Status": 1,
                "BackupWay": 0,
                "DBs": [
                    "testdbvictornew"
                ],
                "InternalAddr": "http://10.66.0.88:58366/download/backup_49760.tar?YJW3gzNLKt2LCrywP9JslJXZo6TXiqprJ6x+tRJfDqzgJRdDrKF8j2V0XGk/MyyS00h9hexVea0A3GvpPf2aoq80DbnTNfZrLB+Ys00Glvzfv7CfaHRsoM95IpqVGrfNMrxomN6lVfnj6qb8Y3duxg==",
                "ExternalAddr": "https://gz-dl-sqlserver.cloud.tencent.com/download/backup_49760.tar?YJW3gzNLKt2LCrywP9JslJXZo6TXiqprJ6x+tRJfDqzgJRdDrKF8j2V0XGk/MyyS00h9hexVea0A3GvpPf2aoq80DbnTNfZrLB+Ys00Glvzfv7CfaHRsoM95IpqVGrfNMrxomN6lVfnj6qb8Y3duxg=="
            },
            {
                "Id": 49759,
                "BackupName": "mssql-3l3fgqn7_202007302200",
                "FileName": "manual_instance_58001_20180702010430.bak.tar",
                "StartTime": "2018-07-02 01:04:30",
                "EndTime": "2018-07-02 01:04:30",
                "Size": 192,
                "Strategy": 0,
                "GroupId": 0,
                "Status": 1,
                "BackupWay": 0,
                "DBs": [
                    "testdbvictornew"
                ],
                "InternalAddr": "http://10.66.0.88:58366/download/backup_49759.tar?YJW3gzNLKt2LCrywP9JslJXZo6TXiqprJ6x+tRJfDqzgJRdDrKF8j2V0XGk/MyyS00h9hexVea0A3GvpPf2aoq80DbnTNfZrvuFmWRKDML0cICOu7LASU2gWXlUkKcHfj/tspGhVGw8RX0OKecEUIQ==",
                "ExternalAddr": "https://gz-dl-sqlserver.cloud.tencent.com/download/backup_49759.tar?YJW3gzNLKt2LCrywP9JslJXZo6TXiqprJ6x+tRJfDqzgJRdDrKF8j2V0XGk/MyyS00h9hexVea0A3GvpPf2aoq80DbnTNfZrvuFmWRKDML0cICOu7LASU2gWXlUkKcHfj/tspGhVGw8RX0OKecEUIQ=="
            }
        ]
    }
}
```

