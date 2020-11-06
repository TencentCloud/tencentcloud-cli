**Example 1: 拉取SQL日志起始偏移及日志数量**



Input: 

```
tccli dcdb DescribeSqlLogs --cli-unfold-argument  \
    --InstanceId dcdbt-ovulpcjf \
    --Limit 0
```

Output: 
```
{
    "Response": {
        "RequestId": "9ce0cbb4-3863-4214-b7b2-d060a3f530d8",
        "TotalCount": 63,
        "StartOffset": 0,
        "EndOffset": 63,
        "Offset": 0,
        "Count": 0,
        "SqlItems": []
    }
}
```

**Example 2: 拉取SQL日志**



Input: 

```
tccli dcdb DescribeSqlLogs --cli-unfold-argument  \
    --InstanceId tdsql-6a0lwzzj \
    --Offset 53560502 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "RequestId": "c08964d6-e5c2-4a50-9936-2c4a6e0bb640",
        "TotalCount": 63,
        "StartOffset": 0,
        "EndOffset": 63,
        "Offset": 1,
        "Count": 1,
        "SqlItems": [
            {
                "Offset": 1,
                "User": "testaccount",
                "Client": "172.16.0.5:47503",
                "DbName": "",
                "Sql": "select @@version_comment limit 1",
                "SelectRowNum": 1,
                "AffectRowNum": 0,
                "Timestamp": 1537932957,
                "TimeCostMs": 0,
                "ResultCode": 0
            }
        ]
    }
}
```

