**Example 1: 查询慢查询日志列表**



Input: 

```
tccli mariadb DescribeDBSlowLogs --cli-unfold-argument  \
    --InstanceId tdsql-ige1a5k3 \
    --Offset 0 \
    --Limit 20 \
    --StartTime '2017-08-06 00:00:00' \
    --EndTime '2017-08-07 23:59:59' \
    --Slave 1
```

Output: 
```
{
    "Response": {
        "LockTimeSum": 0.0,
        "QueryCount": 1,
        "QueryTimeSum": 1.13,
        "RequestId": "1e74e824-6d2b-495d-b347-5250cdf8e964",
        "Total": 1,
        "Data": [
            {
                "CheckSum": "14090621765287179955",
                "Db": "",
                "FingerPrint": "replace into sysdb.statustable set ts = from_unixtime(?),ip=?,port=?",
                "LockTimeAvg": "0.00",
                "LockTimeMax": "0.00",
                "LockTimeMin": "0.00",
                "LockTimeSum": "0.00",
                "QueryCount": "1",
                "QueryTimeAvg": "1.13",
                "QueryTimeMax": "1.13",
                "QueryTimeMin": "1.13",
                "QueryTimeSum": "1.13",
                "RowsExaminedSum": "0.00",
                "RowsSentSum": "0.00",
                "TsMax": "2016-08-06 11:32:10",
                "TsMin": "2016-08-06 11:32:10",
                "User": "agent",
                "Host": "10.1.1.1",
                "ExampleSql": ""
            }
        ]
    }
}
```

