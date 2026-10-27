**Example 1: pg数据库空间分析**

pg数据库空间分析

Input: 

```
tccli dbbrain DescribeTopSpaceSchemasV2 --cli-unfold-argument  \
    --InstanceId postgres-gq5k0y66 \
    --Product postgres \
    --Date 2026-08-25 \
    --SortBy TotalRelationSize \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "PostgresObjects": [
            {
                "IndexSize": 11.8,
                "RelationSize": 74.2,
                "TableBloat": 1,
                "TableCatalog": "postgres",
                "TableRows": 200002,
                "TableSize": 74.6,
                "TotalRelationSize": 86.5
            }
        ],
        "Timestamp": 1787587210,
        "RequestId": "4b914074-1f96-4d8d-8177-aa103d1b7754"
    }
}
```

