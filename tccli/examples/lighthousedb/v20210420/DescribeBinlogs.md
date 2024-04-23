**Example 1: 查询集群Binlog日志列表**



Input: 

```
tccli lighthousedb DescribeBinlogs --cli-unfold-argument  \
    --ClusterId lhdbmysql-12345678 \
    --StartTime 2022-01-01 00:00:00 \
    --EndTime 2022-01-01 23:59:59 \
    --Limit 100 \
    --Offset 100
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RequestId": "9e56617c-c7cc-44e1-a967-6beb418ad5e7",
        "Binlogs": [
            {
                "BinlogId": 10782259,
                "FileName": "00000002_0010782259_mysql-bin.001002",
                "FileSize": 479,
                "FinishTime": "2022-06-16 18:36:14",
                "StartTime": "2022-06-15 17:19:19"
            }
        ]
    }
}
```

