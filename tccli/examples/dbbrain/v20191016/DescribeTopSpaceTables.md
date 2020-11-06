**Example 1: 获取Top表的空间统计信息**



Input: 

```
tccli dbbrain DescribeTopSpaceTables --cli-unfold-argument  \
    --InstanceId cdb-test \
    --Limit 2 \
    --SortBy TableRows
```

Output: 
```
{
    "Response": {
        "RequestId": "ed279d8b-a9d9-48d6-9429-e0fde000994a",
        "Timestamp": 1603819881,
        "TopSpaceTables": [
            {
                "DataFree": 0,
                "TableName": "test",
                "TotalLength": 0.1,
                "TableSchema": "test_bak",
                "FragRatio": 0,
                "DataLength": 0.1,
                "PhysicalFileSize": 0.1,
                "TableRows": 9,
                "Engine": "InnoDB",
                "IndexLength": 0
            },
            {
                "DataFree": 0,
                "TableName": "test",
                "TotalLength": 0.1,
                "TableSchema": "test_bak",
                "FragRatio": 0,
                "DataLength": 0.1,
                "PhysicalFileSize": 0.1,
                "TableRows": 9,
                "Engine": "InnoDB",
                "IndexLength": 0
            }
        ]
    }
}
```

