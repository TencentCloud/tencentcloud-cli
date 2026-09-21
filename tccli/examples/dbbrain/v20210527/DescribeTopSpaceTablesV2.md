**Example 1: 查询表空间分析**

查询表空间分析

Input: 

```
tccli dbbrain DescribeTopSpaceTablesV2 --cli-unfold-argument  \
    --InstanceId cdb-lvgh1oyv \
    --Product mysql \
    --Date 2026-08-25 \
    --SortBy PhysicalFileSize \
    --Limit 100
```

Output: 
```
{
    "Response": {
        "MysqlObjects": [
            {
                "DataFree": 4,
                "DataLength": 10.5,
                "Engine": "InnoDB",
                "FragRatio": 21.05,
                "IndexLength": 4.5,
                "PhysicalFileSize": 23,
                "TableName": "txn_order",
                "TableRows": 148161,
                "TableSchema": "txn_test",
                "TotalLength": 19
            }
        ],
        "Timestamp": 1786559643,
        "RequestId": "190b39d8-0329-4901-a211-d7b2d024b5d7"
    }
}
```

