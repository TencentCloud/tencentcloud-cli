**Example 1: 拉取SQL日志起始偏移及日志数量**



Input: 

```
tccli mariadb DescribeSqlLogs --cli-unfold-argument  \
    --InstanceId tdsql-6a0lwzzj \
    --Limit 0
```

Output: 
```
{
    "Response": {
        "RequestId": "f2ede2fd-34b9-4e44-95d5-3198c137b73b",
        "TotalCount": 2205945,
        "StartOffset": 53560502,
        "EndOffset": 55766447,
        "Offset": 53560502,
        "Count": 0,
        "SqlItems": []
    }
}
```

**Example 2: 拉取SQL日志**



Input: 

```
tccli mariadb DescribeSqlLogs --cli-unfold-argument  \
    --InstanceId tdsql-6a0lwzzj \
    --Offset 53560502 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "RequestId": "211bbabb-ffde-467f-b949-e4c61c64c6a6",
        "TotalCount": 2206280,
        "StartOffset": 53560502,
        "EndOffset": 55766782,
        "Offset": 53560502,
        "Count": 1,
        "SqlItems": [
            {
                "Offset": 53560502,
                "User": "jkx_rsd",
                "Client": "10.10.10.32:34812",
                "DbName": "test",
                "Sql": "select * from t",
                "SelectRowNum": 1,
                "AffectRowNum": 0,
                "Timestamp": 1537542271,
                "TimeCostMs": 0,
                "ResultCode": 0
            }
        ]
    }
}
```

