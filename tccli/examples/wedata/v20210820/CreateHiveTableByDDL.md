**Example 1: CreateHiveTableByDDL**

创建表

Input: 

```
tccli wedata CreateHiveTableByDDL --cli-unfold-argument  \
    --DatasourceId 12342313 \
    --Database hive \
    --DDLSql select * from database; \
    --Incharge 231232 \
    --Privilege 0 \
    --ProjectId 124537 \
    --Type HIVE \
    --Async True
```

Output: 
```
{
    "Response": {
        "Data": "tablename",
        "TaskId": "25",
        "RequestId": "as1cs2c123asyi23bh213cc"
    }
}
```

