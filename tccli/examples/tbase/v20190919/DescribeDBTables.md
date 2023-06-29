**Example 1: 查询Schema下的表名**



Input: 

```
tccli tbase DescribeDBTables --cli-unfold-argument  \
    --InstanceId tdpg-xxx \
    --PageNumber 1 \
    --DBName dbName \
    --PageSize 1 \
    --Schemas schema1 schema2
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RequestId": "xx",
        "Items": [
            {
                "SchemaName": "schema1",
                "TableNames": [
                    "table1",
                    "table2"
                ]
            }
        ]
    }
}
```

