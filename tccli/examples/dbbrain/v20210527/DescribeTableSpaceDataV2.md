**Example 1: 查询postgres表空间数据**

查询postgres表空间数据

Input: 

```
tccli dbbrain DescribeTableSpaceDataV2 --cli-unfold-argument  \
    --InstanceId postgres-40b08oij \
    --Product postgres \
    --TableSchema public \
    --TableName tencentdb_tbl_dial_test_long_1q9b045f8w1 \
    --TableCatalog postgres \
    --Date 2026-10-22
```

Output: 
```
{
    "Response": {
        "PostgresTableSpaceData": {
            "IndexSize": 0,
            "RelationSize": 0,
            "TableBloat": 1,
            "TableCatalog": "postgres",
            "TableName": "tencentdb_tbl_dial_test_long_1q9b045f8w1",
            "TableRows": 1,
            "TableSchema": "public",
            "TableSize": 0,
            "TableStatus": 0,
            "TotalRelationSize": 0
        },
        "Timestamp": 1792598400,
        "RequestId": "04d5a126-4883-4978-aabe-72eff28132cb"
    }
}
```

