**Example 1: CreateHiveTable**

建hive表

Input: 

```
tccli wedata CreateHiveTable --cli-unfold-argument  \
    --Database testDB \
    --ProjectId 1 \
    --Incharge 1 \
    --DatasourceId 1 \
    --Privilege 0 \
    --DDLSql create table if not exist test_table(id int)
```

Output: 
```
{
    "Response": {
        "IsSuccess": true,
        "RequestId": "123"
    }
}
```

