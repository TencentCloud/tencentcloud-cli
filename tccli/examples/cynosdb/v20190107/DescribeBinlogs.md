**Example 1: 查询集群 Binlog 日志列表**



Input: 

```
tccli cynosdb DescribeBinlogs --cli-unfold-argument  \
    --ClusterId cynosdbmysql-mwg7122d \
    --StartTime 2024-10-18 11:03:02 \
    --EndTime 2024-10-25 17:24:50 \
    --Limit 2 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Binlogs": [
            {
                "BinlogId": 3364561,
                "FileName": "1_mysql-bin.00**02",
                "FileSize": 815,
                "FinishTime": "2024-10-25 17:24:50",
                "StartTime": "2024-10-18 11:03:02"
            }
        ],
        "RequestId": "9052ff42-8a95-4095-8457-9346eb09dc1a",
        "TotalCount": 1
    }
}
```

