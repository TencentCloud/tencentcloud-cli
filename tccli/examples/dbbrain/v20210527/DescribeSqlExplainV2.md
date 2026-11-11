**Example 1: 查询执行计划V2**



Input: 

```
tccli dbbrain DescribeSqlExplainV2 --cli-unfold-argument  \
    --Product mysql \
    --SqlText select * from tao_test.example_table LIMIT 1; \
    --InstanceId cdb-30p95ond \
    --Visual True
```

Output: 
```
{
    "Response": {
        "Explain": {
            "Data": [
                {}
            ],
            "Names": [
                "id"
            ]
        },
        "FieldDesc": [
            {
                "Desc": "表名",
                "Field": "table_name"
            }
        ],
        "Schema": "",
        "SqlText": "select * from tao_test.example_table LIMIT 1;",
        "Tables": [
            {
                "TableName": "example_table",
                "TableSchema": "tao_test"
            }
        ],
        "VisualExplain": "",
        "RequestId": "eeb978d7-7a58-4a1c-a22e-2a018c05424c"
    }
}
```

